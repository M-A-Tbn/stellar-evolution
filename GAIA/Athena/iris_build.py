#!/usr/bin/env python3
"""
iris_build.py — Builds summary.html from Iris markdown files.

Usage:
    python3 iris_build.py "session - summary.md" "other - summary.md"
    python3 iris_build.py exam_summary.md -o "GAIA/STUDY PATH/exam_summary.html"
    python3 iris_build.py *.md --themes /path/to/themes -o output.html

Each file = one tab. ## sections = collapsible sidebar categories.
### sub-headings = sidebar leaf links. Sections are fully open (no paging).
Two themes: folio and deepdive.
"""

import sys, re, shutil, html as html_lib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import shared


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text):
    s = re.sub(r'`[^`]*`', '', text)
    s = re.sub(r'\$[^$]*\$', '', s)
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s).strip('-').lower()
    return s or 'section'


# ── Markdown body → HTML ──────────────────────────────────────────────────────

def md_to_html(text):
    """Convert Iris markdown body to HTML (no ## / ### — those are pre-parsed)."""
    placeholders = {}
    ph_idx = [0]

    def protect(content):
        key = f'\x00PH{ph_idx[0]}\x00'
        ph_idx[0] += 1
        placeholders[key] = content
        return key

    def replace_code(m):
        lang = m.group(1).strip()
        code = html_lib.escape(m.group(2).rstrip('\n'))
        cls = f' class="language-{lang}"' if lang else ''
        return protect(f'<pre><code{cls}>{code}</code></pre>')
    text = re.sub(r'```(\w*)\n(.*?)```', replace_code, text, flags=re.DOTALL)

    def replace_display(m):
        inner = m.group(1).replace('<', '&lt;').replace('>', '&gt;')
        return protect(f'<p class="display-math">$${inner}$$</p>')
    text = re.sub(r'\$\$(.*?)\$\$', replace_display, text, flags=re.DOTALL)

    def replace_inline(m):
        return protect(m.group(0).replace('<', '&lt;').replace('>', '&gt;'))
    text = re.sub(r'\$[^$\n]+?\$', replace_inline, text)

    def inline_fmt(s):
        s = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', s)
        s = re.sub(r'\*\*(.*?)\*\*',     r'<strong>\1</strong>', s)
        s = re.sub(r'\*(.*?)\*',          r'<em>\1</em>', s)
        s = re.sub(r'`([^`]+)`',          r'<code>\1</code>', s)
        return s

    lines = text.split('\n')
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Placeholder passthrough
        if '\x00PH' in line and line.strip().startswith('\x00PH') and line.strip().endswith('\x00'):
            out.append(line.strip()); i += 1; continue

        # Horizontal rule
        if re.match(r'^---+$', line.strip()):
            i += 1; continue

        # h4 ####
        if line.startswith('#### '):
            title = line[5:].strip()
            out.append(f'<h4 id="{slugify(title)}">{inline_fmt(title)}</h4>')
            i += 1; continue

        # Blockquote → exam callout or generic
        if line.startswith('> '):
            bq = []
            while i < len(lines) and lines[i].startswith('> '):
                bq.append(lines[i][2:]); i += 1
            content = inline_fmt(' '.join(bq))
            if 'EXAM QUESTION' in content:
                out.append(f'<div class="exam-callout">{content}</div>')
            else:
                out.append(f'<blockquote>{content}</blockquote>')
            continue

        # Markdown table
        if '|' in line and i + 1 < len(lines):
            sep = lines[i + 1].replace('|', '').strip()
            if sep and re.match(r'^[\s:-]+$', sep):
                rows = []
                while i < len(lines) and '|' in lines[i]:
                    cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                    rows.append(cells); i += 1
                if len(rows) >= 2:
                    thead = '<tr>' + ''.join(f'<th>{inline_fmt(c)}</th>' for c in rows[0]) + '</tr>'
                    tbody = ''.join(
                        '<tr>' + ''.join(f'<td>{inline_fmt(c)}</td>' for c in row) + '</tr>\n'
                        for row in rows[2:]
                    )
                    out.append(f'<div class="table-wrap"><table><thead>{thead}</thead><tbody>{tbody}</tbody></table></div>')
                continue

        # Unordered list
        if re.match(r'^[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^([-*]|\s{2,}[-*]) ', lines[i]):
                raw = re.sub(r'^[-*]\s', '', lines[i])
                items.append(f'<li>{inline_fmt(raw.strip())}</li>'); i += 1
            out.append('<ul>\n' + '\n'.join(items) + '\n</ul>'); continue

        # Ordered list
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                raw = re.sub(r'^\d+\.\s', '', lines[i])
                items.append(f'<li>{inline_fmt(raw.strip())}</li>'); i += 1
            out.append('<ol>\n' + '\n'.join(items) + '\n</ol>'); continue

        # Empty line
        if not line.strip():
            i += 1; continue

        # Paragraph
        para = []
        while i < len(lines):
            l = lines[i]
            if not l.strip(): break
            if re.match(r'^[-*] |\d+\. |---+$|^> |^#### ', l): break
            if '|' in l and i + 1 < len(lines) and re.match(r'^[\s:-]+$', lines[i+1].replace('|','').strip() or '-'): break
            if '\x00PH' in l and l.strip().startswith('\x00PH'): break
            para.append(inline_fmt(l)); i += 1

        if para:
            p = ' '.join(para)
            # Definition entry: **term** — definition
            if p.startswith('<strong>') and '</strong>' in p and ' — ' in p:
                end = p.index('</strong>')
                term = p[8:end]
                rest = re.sub(r'^\s*—\s*', '', p[end + 9:])
                out.append(
                    f'<div class="def-entry">'
                    f'<span class="def-term">{term}</span>'
                    f'<span class="def-body">{rest}</span>'
                    f'</div>'
                )
            else:
                out.append(f'<p>{p}</p>')
        else:
            i += 1

    result = '\n'.join(out)
    for key, val in placeholders.items():
        result = result.replace(key, val)
    return result


# ── Iris markdown parser ──────────────────────────────────────────────────────

def parse_iris_md(path, prefix):
    """
    Parse an Iris summary markdown.
    Returns doc dict with sections; each section has subsections (from ###).
    prefix: unique string used to build element IDs (e.g. 'nm' for Numerical Methods).
    """
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    doc = {'title': '', 'source': '', 'course': '', 'date': '', 'sections': []}
    cur_sec = None
    cur_sub = None
    buf = []
    preamble = []

    def flush_sub():
        if cur_sub is not None:
            cur_sub['html'] = md_to_html('\n'.join(buf))
            buf.clear()

    def flush_sec_preamble():
        if cur_sec is not None and preamble:
            cur_sec['preamble_html'] = md_to_html('\n'.join(preamble))
            preamble.clear()

    for line in lines:
        if line.startswith('# ') and not doc['title']:
            doc['title'] = line[2:].strip()
        elif re.match(r'\*\*Sources?:\*\*', line):
            doc['source'] = re.sub(r'\*\*Sources?:\*\*\s*', '', line).strip()
        elif line.startswith('**Course:**'):
            doc['course'] = re.sub(r'\*\*Course:\*\*\s*', '', line).strip()
        elif re.match(r'\*\*(Generated|Date):\*\*', line):
            doc['date'] = re.sub(r'\*\*(?:Generated|Date):\*\*\s*', '', line).strip()
        elif line.strip() == '---':
            continue
        elif line.startswith('## '):
            flush_sub()
            flush_sec_preamble()
            cur_sub = None
            title = line[3:].strip()
            sid = f'{prefix}-{slugify(title)}'
            cur_sec = {'title': title, 'id': sid, 'preamble_html': '', 'subsections': []}
            doc['sections'].append(cur_sec)
            buf.clear()
            preamble.clear()
        elif line.startswith('### '):
            flush_sub()
            if cur_sec and not cur_sec['preamble_html']:
                flush_sec_preamble()
            elif cur_sec:
                # dump buf to preamble if no subsection started yet
                if not cur_sec['subsections'] and buf:
                    preamble.extend(buf)
                    buf.clear()
                    flush_sec_preamble()
            title = line[4:].strip()
            sub_id = f'{prefix}-{slugify(title)}'
            cur_sub = {'title': title, 'id': sub_id, 'html': ''}
            buf.clear()
            if cur_sec:
                cur_sec['subsections'].append(cur_sub)
        elif cur_sub is not None:
            buf.append(line)
        elif cur_sec is not None:
            preamble.append(line)

    flush_sub()
    if cur_sec and not cur_sec['preamble_html'] and preamble:
        cur_sec['preamble_html'] = md_to_html('\n'.join(preamble))
    return doc


# ── Tab label / key from filename ────────────────────────────────────────────

def tab_label(path):
    stem = Path(path).stem
    if re.match(r'^exam[_\s]?summary$', stem, flags=re.IGNORECASE):
        return 'Exam Summary'
    name = re.sub(r'\s*-\s*summary.*$', '', stem, flags=re.IGNORECASE).strip()
    return name.title() if name else stem


def session_key(path):
    return slugify(tab_label(path)) or 'session'


# ── Static assets ─────────────────────────────────────────────────────────────

TOPNAV_SVG = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3 7.5 L15 10.2 L15 25 L3 22.3 Z" fill="currentColor" fill-opacity="0.95"/>
  <path d="M29 7.5 L17 10.2 L17 25 L29 22.3 Z" fill="currentColor" fill-opacity="0.7"/>
  <path d="M16 10 L16 25" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.5"/>
</svg>'''

INLINE_CSS = """
/* ── Definition entries ── */
.def-entry {
  display: grid;
  grid-template-columns: 210px minmax(0, 1fr);
  gap: 0.4rem 1.4rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--line-soft);
  align-items: baseline;
}
@media (max-width: 640px) {
  /* Plain `1fr` still respects the body column's content-based minimum width, so an
     unbroken inline formula could force the grid wider than its container and blow
     out the page. `minmax(0, 1fr)` above fixes that; stacking the columns here also
     makes the fixed 210px term column usable on a ~330px-wide mobile content area. */
  .def-entry { grid-template-columns: 1fr; gap: 0.15rem; }
}
.def-term { font-weight: 600; color: var(--ink); font-size: 0.88rem; }
.def-body { color: var(--body); font-size: 0.88rem; line-height: 1.6; }

/* ── Exam callout ── */
.exam-callout {
  margin: 0.15rem 0 1rem;
  padding: 0.55rem 1rem;
  border-left: 3px solid var(--bronze);
  background: var(--bronze-soft);
  border-radius: 0 6px 6px 0;
  font-size: 0.78rem; line-height: 1.55; color: var(--body);
}
.exam-callout strong { color: var(--bronze); }
.exam-callout em     { font-style: normal; opacity: 0.85; }

/* ── Tables (Coverage Map etc.) ── */
.table-wrap { overflow-x: auto; margin: 1.2rem 0; }
table { border-collapse: collapse; width: 100%; font-size: 0.84rem; }
th, td { text-align: left; padding: 0.5rem 0.85rem; border-bottom: 1px solid var(--line); }
th { font-weight: 600; color: var(--ink); background: var(--bg-elev);
     font-size: 0.75rem; letter-spacing: 0.04em; text-transform: uppercase; }
tr:hover td { background: var(--bg-soft); }

/* ── General prose ── */
.prose h2 { margin: 2rem 0 0.6rem; font-size: 1.05rem; color: var(--ink); }
.prose h3 { margin: 1.4rem 0 0.5rem; font-size: 0.95rem; color: var(--ink);
            font-weight: 600; border-bottom: 1px solid var(--line-soft); padding-bottom: 0.25rem; }
.prose h4 { margin: 1rem 0 0.4rem; font-size: 0.88rem; color: var(--mute);
            font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; }
p  { margin: 0.5rem 0; font-size: 0.88rem; line-height: 1.65; }
ul, ol { padding-left: 1.5rem; margin: 0.4rem 0; font-size: 0.88rem; }
li { margin-bottom: 0.3rem; line-height: 1.6; }
pre { background: var(--bg-code, #111); color: var(--code-ink, #ddd);
      padding: 1rem 1.2rem; border-radius: 6px; overflow-x: auto;
      font-size: 0.82rem; margin: 0.8rem 0; }
code { font-family: var(--mono, monospace); font-size: 0.85em; }
.display-math { text-align: center; margin: 0.9rem 0; overflow-x: auto; }
blockquote { border-left: 3px solid var(--teal-edge); padding: 0.4rem 0.9rem;
             margin: 0.6rem 0; color: var(--mute); font-size: 0.86rem; }
"""

SCRIPT = r"""
/*THEME_PICKER_JS*/

/*FONT_JS*/

/*TAB_JS*/

/* ── Per-project activation (called by shared tab system) ── */
function onProjectActivated(key) {
  document.querySelectorAll('.article[data-project]').forEach(a => { a.hidden = a.dataset.project !== key; });
  document.querySelectorAll('.sidebar .nav[data-project]').forEach(n => { n.hidden = n.dataset.project !== key; });
}

/* ── Sidebar category collapse ── */
document.querySelectorAll('[data-toggle="cat"]').forEach(btn => {
  btn.addEventListener('click', () => {
    const cat = btn.closest('.cat');
    cat.dataset.collapsed = cat.dataset.collapsed === 'true' ? 'false' : 'true';
  });
});

/* ── Sidebar anchor scroll ── */
document.querySelectorAll('.sidebar a.leaf[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    const target = document.getElementById(a.getAttribute('href').slice(1));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      document.querySelectorAll('.sidebar a.leaf.is-current').forEach(el => el.classList.remove('is-current'));
      a.classList.add('is-current');
    }
  });
});

/* ── Mobile menu ── */
(function () {
  const btn     = document.getElementById('menuBtn');
  const sidebar = document.getElementById('sidebar');
  if (!btn || !sidebar) return;
  btn.addEventListener('click', () => sidebar.classList.toggle('is-open'));
  document.addEventListener('click', e => {
    if (!sidebar.contains(e.target) && !btn.contains(e.target))
      sidebar.classList.remove('is-open');
  });
})();
window.addEventListener('load', () => { if (typeof hljs !== 'undefined') hljs.highlightAll(); });
"""

CHEV_SVG = ('<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '<polyline points="9 6 15 12 9 18"></polyline></svg>')


# ── HTML renderers ────────────────────────────────────────────────────────────

def render_sidebar_nav(doc, key):
    lines = [f'<nav class="nav" data-project="{key}" aria-label="{html_lib.escape(doc["title"])}" hidden>']
    for si, sec in enumerate(doc['sections']):
        collapsed = 'false' if si == 0 else 'true'
        active = ' is-active' if si == 0 else ''
        lines.append(f'  <div class="cat{active}" data-collapsed="{collapsed}">')
        lines.append(f'    <button class="cat-row" data-toggle="cat">'
                     f'{CHEV_SVG}<span>{html_lib.escape(sec["title"])}</span></button>')
        lines.append('    <div class="cat-body">')
        if sec['subsections']:
            for sub in sec['subsections']:
                lines.append(f'      <a class="leaf" href="#{sub["id"]}">{html_lib.escape(sub["title"])}</a>')
        else:
            lines.append(f'      <a class="leaf" href="#{sec["id"]}">{html_lib.escape(sec["title"])}</a>')
        lines.append('    </div>')
        lines.append('  </div>')
    lines.append('</nav>')
    return '\n'.join(lines)


def render_article(doc, key):
    byline_parts = []
    if doc['source']:
        byline_parts.append(f'Source: <code>{html_lib.escape(doc["source"])}</code>')
    if doc['course']:
        byline_parts.append(html_lib.escape(doc['course']))
    if doc['date']:
        byline_parts.append(html_lib.escape(doc['date']))
    byline = ' · '.join(byline_parts)

    lines = [f'<article class="article" data-project="{key}" hidden>']
    lines.append(f'  <h1 class="title">{html_lib.escape(doc["title"])}</h1>')
    if byline:
        lines.append(f'  <p class="byline">{byline}</p>')
    lines.append('  <section class="prose">')

    for sec in doc['sections']:
        lines.append(f'<h2 id="{sec["id"]}">{html_lib.escape(sec["title"])}</h2>')
        if sec['preamble_html']:
            lines.append(sec['preamble_html'])
        for sub in sec['subsections']:
            lines.append(f'<h3 id="{sub["id"]}">{html_lib.escape(sub["title"])}</h3>')
            lines.append(sub['html'])

    lines.append('  </section>')
    lines.append('</article>')
    return '\n'.join(lines)


def render_html(projects, tab_labels, themes_dir=None):
    script_dir = Path(__file__).parent
    if themes_dir is None:
        themes_dir = script_dir / 'themes'
    theme_names = []
    if themes_dir.exists():
        theme_names = sorted(p.stem for p in themes_dir.glob('*.css') if p.stem != 'overrides')
    if not theme_names:
        theme_names = ['default']
    default_theme = theme_names[0]
    theme_buttons = '\n'.join(
        f'      <button data-theme="{n}" aria-pressed="{str(n == default_theme).lower()}" title="{n.capitalize()}"></button>'
        for n in theme_names
    )

    proj_keys   = [key for key, _ in projects]
    proj_labels = {key: tab_labels[key] for key, _ in projects}

    sidebar_html  = '\n'.join(render_sidebar_nav(doc, key) for key, doc in projects)
    articles_html = '\n'.join(render_article(doc, key)     for key, doc in projects)

    nav_html  = shared.session_nav_html(len(projects))
    font_html = shared.font_picker_html()

    script = (SCRIPT
              .replace('/*THEME_PICKER_JS*/', shared.theme_picker_js())
              .replace('/*FONT_JS*/',         shared.FONT_JS)
              .replace('/*TAB_JS*/',          shared.tab_js(proj_keys, proj_labels,
                                                            'gaia-iris-tab', 'IRIS')))

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Iris — Exam Summary</title>
<script>
MathJax = {{
  tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']], processEscapes: true }},
  options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre'] }},
  chtml: {{ scale: 1.0 }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script" async></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<link rel="stylesheet" id="themeCSS" href="themes/{default_theme}.css">
<link rel="stylesheet" href="themes/overrides.css">
<style>{INLINE_CSS}{shared.FONT_CSS}{shared.TAB_CSS}</style>
</head>
<body>

<header class="topbar">
  <a class="brand" href="#">
    <span class="brand-mark" aria-hidden="true">{TOPNAV_SVG}</span>
    <span class="brand-name">IRIS</span>
    <span class="brand-issue">Exam<br>Summary</span>
  </a>
  {nav_html}
  <div class="topbar-actions">
    <button class="icon-btn menu-btn" id="menuBtn" aria-label="Open menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/>
        <line x1="3" y1="18" x2="21" y2="18"/>
      </svg>
    </button>
    {font_html}
    <div class="theme-picker" role="group" aria-label="Theme">
      <span class="theme-label">Theme</span>
{theme_buttons}
    </div>
  </div>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="side-label" id="sideLabel">IRIS · Summary</div>
{sidebar_html}
  </aside>
  <div class="main">
{articles_html}
  </div>
</div>

<script>{script}</script>
</body>
</html>
'''


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help'):
        print(__doc__); sys.exit(0)

    output_file = None
    themes_src  = None
    md_files    = []
    i = 0
    while i < len(args):
        if args[i] in ('-o', '--output') and i + 1 < len(args):
            output_file = args[i + 1]; i += 2
        elif args[i] == '--themes' and i + 1 < len(args):
            themes_src = args[i + 1]; i += 2
        else:
            md_files.append(args[i]); i += 1

    if not md_files:
        print('Error: no markdown files specified.'); sys.exit(1)

    script_dir = Path(__file__).parent
    md_paths   = [Path(f) for f in md_files]
    for p in md_paths:
        if not p.exists():
            print(f'Error: file not found: {p}'); sys.exit(1)

    if not output_file:
        output_file = script_dir.parent / 'STUDY PATH' / 'summary.html'
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    themes_dst = output_file.parent / 'themes'
    if not themes_dst.exists():
        candidates = ([Path(themes_src)] if themes_src else []) + [script_dir / 'themes']
        src = next((c for c in candidates if c.exists()), None)
        if src:
            shutil.copytree(src, themes_dst)
            print(f'Copied themes → {themes_dst}')
        else:
            print('Warning: themes not found — HTML will be unstyled.')

    projects   = {}  # key → (label, doc) ordered
    seen       = {}
    result     = []
    for path in md_paths:
        print(f'Parsing {path.name}…')
        key = session_key(path)
        if key in seen:
            seen[key] += 1; key = f'{key}-{seen[key]}'
        else:
            seen[key] = 1
        doc = parse_iris_md(path, prefix=key)
        label = tab_label(path)
        result.append((key, doc))
        projects[key] = label

    print('Rendering HTML…')
    html_out = render_html(result, projects, themes_dst)
    output_file.write_text(html_out, encoding='utf-8')
    print(f'✓  Written → {output_file}')
    print(f'   {len(result)} session(s), '
          f'{sum(len(d["sections"]) for _, d in result)} sections, '
          f'{sum(sum(len(s["subsections"]) for s in d["sections"]) for _, d in result)} subsections.')


if __name__ == '__main__':
    main()
