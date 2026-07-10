#!/usr/bin/env python3
"""
build.py — Converts Markdown study notes into the paged Study Notes HTML.

Usage:
    # Generate notes.html from one or more markdown files (one file = one project tab):
    python3 build.py "project1 - notes.md"
    python3 build.py "project1 - notes.md" "project 2 - notes.md" "Numerical Methods - notes.md"

    # Custom output file:
    python3 build.py "project1 - notes.md" -o my_notes.html

    # Specify where the themes folder is (defaults to ./themes):
    python3 build.py "project1 - notes.md" --themes /path/to/themes

Each run fully regenerates the HTML — no manual editing needed.

The parser handles any combination of heading levels (H2, H3, H4, …) and
mixed structures (some H2s with sub-headings, some without).
"""

import sys, os, re, json, shutil, html as html_lib
from pathlib import Path
import mistune

sys.path.insert(0, str(Path(__file__).parent))
import shared

# ── Helpers ────────────────────────────────────────────────────────────────

def slugify(text):
    """Make an HTML-safe ID from a heading string."""
    s = re.sub(r'`[^`]*`', '', text)        # strip inline code
    s = re.sub(r'\$[^$]*\$', '', s)         # strip inline math
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s).strip('-').lower()
    return s or 'section'


# ── Markdown → HTML ────────────────────────────────────────────────────────

_md_renderer = None

def _get_md_renderer():
    global _md_renderer
    if _md_renderer is None:
        plugins = ['table', 'strikethrough']
        try:
            mistune.create_markdown(plugins=['task_lists'])
            plugins.append('task_lists')
        except Exception:
            pass
        _md_renderer = mistune.create_markdown(plugins=plugins)
    return _md_renderer


def md_to_html(text):
    """Convert a markdown body block to HTML via mistune.
    Math and fenced code blocks are extracted before rendering so mistune
    doesn't touch their contents, then restored afterward.
    """
    placeholders = {}
    ph_idx = [0]

    def protect_block(content):
        key = f'XBLOCK{ph_idx[0]}XEND'
        ph_idx[0] += 1
        placeholders[key] = ('block', content)
        return f'\n{key}\n'

    def protect_inline(content):
        key = f'XINLINE{ph_idx[0]}XEND'
        ph_idx[0] += 1
        placeholders[key] = ('inline', content)
        return key

    # Protect fenced code blocks first (before math, so $ inside code is safe)
    def replace_code(m):
        lang = m.group(1).strip()
        code = html_lib.escape(m.group(2).rstrip('\n'))
        cls = f' class="language-{lang}"' if lang else ''
        return protect_block(f'<pre><code{cls}>{code}</code></pre>')
    text = re.sub(r'```(\w*)\n(.*?)```', replace_code, text, flags=re.DOTALL)

    # Protect display math $$...$$
    def replace_display_math(m):
        inner = m.group(1).replace('<', '&lt;').replace('>', '&gt;')
        return protect_block(f'<p class="math-display">$${inner}$$</p>')
    text = re.sub(r'\$\$(.*?)\$\$', replace_display_math, text, flags=re.DOTALL)

    # Protect inline math $...$
    def replace_inline_math(m):
        escaped = m.group(0).replace('<', '&lt;').replace('>', '&gt;')
        return protect_inline(escaped)
    text = re.sub(r'\$[^$\n]+?\$', replace_inline_math, text)

    result = _get_md_renderer()(text)

    # Restore placeholders (block ones are wrapped in <p> by mistune)
    for key, (kind, val) in placeholders.items():
        if kind == 'block':
            result = result.replace(f'<p>{key}</p>', val)
            result = result.replace(f'<p>{key}\n</p>', val)
        result = result.replace(key, val)

    return result


# ── Markdown file parser ────────────────────────────────────────────────────

_HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)')


def _build_section_tree(flat):
    """
    Build a heading tree from a flat list of {level, title, lines} dicts.
    Returns a list of root nodes (level 2 for standard docs).

    Each node: {level, title, id, html, children}
    IDs are slugified and deduplicated globally across the whole tree.
    """
    seen_ids: dict = {}
    nodes = []
    for item in flat:
        base_id = slugify(item['title'])
        count = seen_ids.get(base_id, 0) + 1
        seen_ids[base_id] = count
        node_id = base_id if count == 1 else f'{base_id}-{count}'
        nodes.append({
            'level': item['level'],
            'title': item['title'],
            'id':    node_id,
            'html':  md_to_html('\n'.join(item['lines'])),
            'children': [],
        })

    root: list = []
    stack: list = []   # active ancestor nodes, shallowest first
    for node in nodes:
        # Pop ancestors that are at the same or deeper level
        while stack and stack[-1]['level'] >= node['level']:
            stack.pop()
        if stack:
            stack[-1]['children'].append(node)
        else:
            root.append(node)
        stack.append(node)
    return root


def parse_markdown(path):
    """
    General-purpose markdown parser.

    Handles any combination of heading levels — H2 sections with or without
    H3/H4 sub-sections, or any other mixed structure.

    Returns a doc dict:
        title, subtitle, intro_html, sources, date, course, sections

    sections is a list of tree nodes: {level, title, id, html, children}
    where children are deeper headings nested under their parent.
    """
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    doc = {
        'title': '', 'subtitle': '', 'intro_html': '',
        'sources': [], 'date': '', 'course': '',
        'sections': [],
    }

    flat: list = []          # [{level, title, lines}]
    intro_lines: list = []   # content before the first section heading
    title_set = False
    in_fence = False

    for line in lines:
        stripped = line.rstrip()

        # ── Code fence markers: flip state and route to content ──────────────
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
            (flat[-1]['lines'] if flat else intro_lines).append(line)
            continue

        # ── Inside a fence: pass through unchanged ───────────────────────────
        if in_fence:
            (flat[-1]['lines'] if flat else intro_lines).append(line)
            continue

        # ── Outside a fence: metadata, separators, headings ─────────────────

        if line.strip() == '---':
            continue  # visual section divider — skip

        if line.startswith('**Sources:**'):
            raw = re.sub(r'\*\*Sources:\*\*\s*', '', line)
            doc['sources'] = [
                s.strip().strip('`·').strip()
                for s in re.split(r'[·,]', raw) if s.strip()
            ]
            continue
        if re.match(r'\*\*(Generated|Date):\*\*', line):
            doc['date'] = re.sub(r'\*\*(?:Generated|Date):\*\*\s*', '', line).strip()
            continue
        if line.startswith('**Course:**'):
            doc['course'] = re.sub(r'\*\*Course:\*\*\s*', '', line).strip()
            continue

        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()

            if level == 1 and not title_set:
                doc['title'] = title
                title_set = True
                continue

            # A lone H3 before any H2 is treated as a subtitle
            if level == 3 and not flat and not doc['subtitle']:
                doc['subtitle'] = title
                continue

            flat.append({'level': level, 'title': title, 'lines': []})
            continue

        # ── Regular content line ─────────────────────────────────────────────
        (flat[-1]['lines'] if flat else intro_lines).append(line)

    if intro_lines:
        doc['intro_html'] = md_to_html('\n'.join(intro_lines))

    doc['sections'] = _build_section_tree(flat)
    return doc


# ── Project prefix from filename ────────────────────────────────────────────

def session_key(path):
    """Derive a unique HTML-safe key from the filename stem.

    GAIA filenames follow the pattern: '{session_name} - notes.md',
    '{session_name} - notes 2.md', '{session_name} - notes 3.md'.
    The key is the full slugified session name so collisions are impossible.
    """
    stem = Path(path).stem
    part_match = re.search(r'\s*-\s*notes\s+([23])\s*$', stem, flags=re.IGNORECASE)
    part_num = part_match.group(1) if part_match else None
    name = re.sub(r'\s*-\s*notes(\s+[23])?\s*$', '', stem, flags=re.IGNORECASE).strip()
    slug = re.sub(r'[^\w\s-]', '', name.lower())
    slug = re.sub(r'[\s_]+', '-', slug).strip('-')
    if part_num:
        slug = f'{slug}-pt{part_num}'
    return slug or 'session'


def project_label(path, doc):
    """Display label for the topnav tab — derived from the session name in the filename."""
    stem = Path(path).stem
    part_match = re.search(r'\s*-\s*notes\s+([23])\s*$', stem, flags=re.IGNORECASE)
    part_num = part_match.group(1) if part_match else None
    name = re.sub(r'\s*-\s*notes(\s+[23])?\s*$', '', stem, flags=re.IGNORECASE).strip()
    label = name if name else (doc['title'][:40] if doc['title'] else 'Notes')
    if part_num:
        label = f'{label} (Part {part_num})'
    return label


# ── HTML rendering ─────────────────────────────────────────────────────────

_CHEV_SVG = (
    '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<polyline points="9 6 15 12 9 18"></polyline></svg>'
)


def _render_nav_node(node, prefix, out, active='', collapsed='true', depth=0):
    """Recursively render one sidebar tree node into the `out` list.

    depth=0 nodes (H2) always get a .cat wrapper for layout and active-state tracking.
    depth>0 leaf nodes are plain <a class="leaf"> — no extra wrapper.
    depth>0 nodes with children get a nested collapsible .cat.
    """
    ind = '  ' * (depth + 1)
    node_id = f'{prefix}-{node["id"]}'

    if depth == 0:
        # Top-level section: always a .cat wrapper (leaf or collapsible)
        if node['children']:
            out.append(f'{ind}<div class="cat{active}" data-collapsed="{collapsed}">')
            out.append(
                f'{ind}  <button class="cat-row" data-toggle="cat">'
                f'{_CHEV_SVG}'
                f'<span>{html_lib.escape(node["title"])}</span></button>'
            )
            out.append(f'{ind}  <div class="cat-body">')
            for child in node['children']:
                _render_nav_node(child, prefix, out, depth=depth + 1)
            out.append(f'{ind}  </div>')
            out.append(f'{ind}</div>')
        else:
            out.append(f'{ind}<div class="cat{active}" data-collapsed="false">')
            out.append(f'{ind}  <div class="cat-body">')
            out.append(f'{ind}    <a class="leaf" href="#{node_id}">{html_lib.escape(node["title"])}</a>')
            out.append(f'{ind}  </div>')
            out.append(f'{ind}</div>')
    else:
        # Sub-level: leaf → plain link; has children → nested collapsible
        if node['children']:
            out.append(f'{ind}<div class="cat" data-collapsed="false">')
            out.append(
                f'{ind}  <button class="cat-row" data-toggle="cat">'
                f'{_CHEV_SVG}'
                f'<span>{html_lib.escape(node["title"])}</span></button>'
            )
            out.append(f'{ind}  <div class="cat-body">')
            for child in node['children']:
                _render_nav_node(child, prefix, out, depth=depth + 1)
            out.append(f'{ind}  </div>')
            out.append(f'{ind}</div>')
        else:
            out.append(f'{ind}<a class="leaf" href="#{node_id}">{html_lib.escape(node["title"])}</a>')


def render_sidebar_nav(doc, prefix, project_key):
    out = [
        f'<nav class="nav" data-project="{project_key}" '
        f'aria-label="{html_lib.escape(project_label_from_key(project_key))}" hidden>'
    ]
    for si, section in enumerate(doc['sections']):
        active    = ' is-active' if si == 0 else ''
        collapsed = 'false'      if si == 0 else 'true'
        _render_nav_node(section, prefix, out, active=active, collapsed=collapsed, depth=0)
    out.append('</nav>')
    return '\n'.join(out)


def _render_article_node(node, prefix, out):
    """Recursively render a section node into the article HTML."""
    node_id = f'{prefix}-{node["id"]}'
    level   = node['level']
    tag     = f'h{level}'

    # H3 and deeper get anchor links; H2 does not (matches existing CSS/JS expectations)
    if level >= 3:
        out.append(
            f'<{tag} id="{node_id}">'
            f'<a href="#{node_id}">{html_lib.escape(node["title"])}</a>'
            f'</{tag}>'
        )
    else:
        out.append(f'<{tag} id="{node_id}">{html_lib.escape(node["title"])}</{tag}>')

    if node['html'].strip():
        out.append(node['html'])

    for child in node['children']:
        _render_article_node(child, prefix, out)


def render_article(doc, prefix, project_key):
    out = []
    out.append(f'<article class="article" data-project="{project_key}" hidden>')
    out.append(f'  <h1 class="title">{html_lib.escape(doc["title"])}</h1>')
    if doc.get('subtitle'):
        out.append(f'  <p class="doc-subtitle">{html_lib.escape(doc["subtitle"])}</p>')

    byline_parts = []
    if doc['sources']:
        srcs = ' · '.join(f'<code>{html_lib.escape(s)}</code>' for s in doc['sources'] if s)
        byline_parts.append(f'Source: <span class="by-em">{srcs}</span>')
    if doc['date']:
        byline_parts.append(html_lib.escape(doc['date']))
    if byline_parts:
        out.append(f'  <p class="byline">{" · ".join(byline_parts)}</p>')

    if doc.get('intro_html'):
        out.append(f'  <div class="intro-content">{doc["intro_html"]}</div>')

    out.append('  <section class="prose">')
    for section in doc['sections']:
        _render_article_node(section, prefix, out)
    out.append('  </section>')
    out.append('</article>')
    return '\n'.join(out)


_key_to_label: dict = {}

def project_label_from_key(key):
    return _key_to_label.get(key, key)


def _build_prebaked_index(projects):
    """Build a search index matching buildPagedView's H2/H3 page grouping."""
    def strip_html(h):
        t = re.sub(r'<[^>]+>', ' ', h or '')
        t = (t.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
               .replace('&quot;', '"').replace('&#39;', "'"))
        return re.sub(r'\s+', ' ', t).strip()

    def subtree_text(node):
        parts = [node['title'], strip_html(node['html'])]
        for ch in node['children']:
            parts.append(subtree_text(ch))
        return ' '.join(p for p in parts if p)

    index = []
    for key, doc in projects:
        page_idx = 0
        for h2 in doc['sections']:
            h3s = [c for c in h2['children'] if c['level'] == 3]
            if not h3s:
                # H2-only page (no H3 children)
                index.append({
                    'key': key, 'pageIdx': page_idx,
                    'title': '', 'section': h2['title'],
                    'text': subtree_text(h2).lower(),
                    'titleLow': '',
                })
                page_idx += 1
            else:
                h2_prefix = h2['title'] + ' ' + strip_html(h2['html'])
                for ci, h3 in enumerate(h3s):
                    page_text = (h2_prefix + ' ' if ci == 0 else '') + subtree_text(h3)
                    page_text = re.sub(r'\s+', ' ', page_text).strip()
                    index.append({
                        'key': key, 'pageIdx': page_idx,
                        'title': h3['title'],
                        'section': h2['title'] if ci == 0 else '',
                        'text': page_text.lower(),
                        'titleLow': h3['title'].lower(),
                    })
                    page_idx += 1
    return index


# ── Full HTML template ──────────────────────────────────────────────────────

TOPNAV_SVG = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M3 7.5 L15 10.2 L15 25 L3 22.3 Z" fill="currentColor" fill-opacity="0.95"/>
  <path d="M29 7.5 L17 10.2 L17 25 L29 22.3 Z" fill="currentColor" fill-opacity="0.7"/>
  <path d="M16 10 L16 25" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.5"/>
</svg>'''

INLINE_SCRIPT = r"""
/*THEME_PICKER_JS*/

/*FONT_JS*/

/*TAB_JS*/

/* ── Per-project activation (called by shared tab system) ── */
function onProjectActivated(key) {
  document.querySelectorAll('.article[data-project]').forEach(a => { a.hidden = a.dataset.project !== key; });
  document.querySelectorAll('.sidebar .nav[data-project]').forEach(n => { n.hidden = n.dataset.project !== key; });
}

/* ── Sidebar cat toggle ── */
document.querySelectorAll('[data-toggle="cat"]').forEach(btn => {
  btn.addEventListener('click', () => {
    const cat = btn.closest('.cat');
    const collapsed = cat.dataset.collapsed === 'true';
    cat.dataset.collapsed = collapsed ? 'false' : 'true';
  });
});

/* ── Search ── */
(function () {
  const input = document.getElementById('searchInput');
  const dropdown = document.getElementById('searchDropdown');
  if (!input || !dropdown) return;

  const searchIndex = window.SEARCH_INDEX || [];

  function navigateTo(key, pageIdx) {
    if (window._gaiaActivateSession) {
      const idx = (window._gaiaProjKeys || []).indexOf(key);
      if (idx >= 0) window._gaiaActivateSession(idx);
    }
    requestAnimationFrame(() => {
      const article = document.querySelector(`.article[data-project="${key}"]`);
      if (!article) return;
      const pages = Array.from(article.querySelectorAll('.prose-page'));
      if (!pages[pageIdx]) return;
      pages.forEach((p, i) => p.classList.toggle('is-active', i === pageIdx));
      window.scrollTo(0, 0);
      const h3 = pages[pageIdx].querySelector('h3');
      if (!h3) return;
      history.replaceState(null, '', '#' + h3.id);
      document.querySelectorAll('.sidebar a.leaf.is-current').forEach(el => { el.classList.remove('is-current'); el.removeAttribute('aria-current'); });
      const leaf = document.querySelector('.sidebar a.leaf[href="#' + CSS.escape(h3.id) + '"]');
      if (leaf) { leaf.classList.add('is-current'); leaf.setAttribute('aria-current', 'page'); leaf.scrollIntoView({ block: 'nearest' }); }
    });
  }

  function showDropdown(q) {
    if (!q) { dropdown.hidden = true; dropdown.innerHTML = ''; return; }
    const matches = searchIndex.filter(e => e.titleLow.includes(q) || e.text.includes(q)).slice(0, 14);
    if (!matches.length) {
      dropdown.innerHTML = '<div class="search-empty">No results</div>';
      dropdown.hidden = false;
      return;
    }
    dropdown.innerHTML = matches.map((m, i) => {
      const snippetStart = m.text.indexOf(q);
      const snippet = snippetStart >= 0 ? '…' + m.text.slice(Math.max(0, snippetStart - 20), snippetStart + 60).trim() + '…' : '';
      return `<a class="search-result" data-key="${m.key}" data-idx="${m.pageIdx}" href="#">` +
        (m.section ? `<span class="sr-sec">${m.section}</span>` : '') +
        `<span class="sr-title">${hlText(m.title || '(untitled)', q)}</span>` +
        (snippet && !m.titleLow.includes(q) ? `<span class="sr-snippet">${hlText(snippet, q)}</span>` : '') +
        '</a>';
    }).join('');
    dropdown.hidden = false;
  }

  function closeDropdown() {
    dropdown.hidden = true;
    dropdown.innerHTML = '';
  }

  function hlText(text, q) {
    const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    if (!q || !text) return esc(text || '');
    const idx = text.toLowerCase().indexOf(q);
    if (idx < 0) return esc(text);
    return esc(text.slice(0, idx)) + '<mark>' + esc(text.slice(idx, idx + q.length)) + '</mark>' + esc(text.slice(idx + q.length));
  }

  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); input.focus(); input.select(); }
    if (e.key === 'Escape' && !dropdown.hidden) { closeDropdown(); input.value = ''; input.blur(); }
  });

  input.addEventListener('input', () => {
    const q = input.value.toLowerCase().trim();
    showDropdown(q);
  });

  input.addEventListener('focus', () => {
    const q = input.value.toLowerCase().trim();
    if (q) showDropdown(q);
  });

  dropdown.addEventListener('click', e => {
    const r = e.target.closest('.search-result');
    if (!r) return;
    e.preventDefault();
    navigateTo(r.dataset.key, parseInt(r.dataset.idx, 10));
    closeDropdown();
    input.value = '';
  });

  document.addEventListener('click', e => {
    if (!input.closest('.search-wrap').contains(e.target)) closeDropdown();
  });
})();

/* ── Zen mode ── */
(function () {
  const btn = document.getElementById('zenBtn');
  const exitBtn = document.getElementById('zenExit');
  if (!btn) return;
  function toggle() {
    const on = document.body.classList.toggle('zen');
    btn.setAttribute('aria-pressed', on);
    localStorage.setItem('sn-zen', on);
  }
  btn.addEventListener('click', toggle);
  if (exitBtn) exitBtn.addEventListener('click', toggle);
  document.addEventListener('keydown', e => { if (e.key === 'z' && !e.metaKey && !e.ctrlKey && document.activeElement.tagName !== 'INPUT') toggle(); });
  if (localStorage.getItem('sn-zen') === 'true') toggle();
})();

/* ── Menu button (mobile) ── */
(function () {
  const btn = document.getElementById('menuBtn');
  const sidebar = document.getElementById('sidebar');
  if (!btn || !sidebar) return;
  btn.addEventListener('click', () => sidebar.classList.toggle('is-open'));
  document.addEventListener('click', e => {
    if (!sidebar.contains(e.target) && !btn.contains(e.target)) sidebar.classList.remove('is-open');
  });
})();

/* ── Copy buttons on code blocks ── */
window.addEventListener('load', () => {
  document.querySelectorAll('pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = 'Copy';
    btn.addEventListener('click', () => {
      const code = pre.querySelector('code');
      navigator.clipboard.writeText(code ? code.innerText : pre.innerText).then(() => {
        btn.textContent = 'Copied ✓';
        btn.classList.add('copied');
        setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1800);
      });
    });
    pre.appendChild(btn);
  });
});

/* ── Paged subsection view ── */
function buildPagedView() {
  const baseTitle = document.title;
  /* Return the first H3 or H2 (fallback) anchor element in a group. */
  function groupAnchor(nodes) {
    return nodes.find(n => n.nodeType === Node.ELEMENT_NODE && n.tagName === 'H3') ||
           nodes.find(n => n.nodeType === Node.ELEMENT_NODE && n.tagName === 'H2') || null;
  }
  document.querySelectorAll('.article').forEach(article => {
    const prose = article.querySelector('.prose');
    if (!prose) return;
    const groups = [];
    let pendingH2 = null;
    let pendingContent = [];
    Array.from(prose.childNodes).forEach(node => {
      if (node.nodeType !== Node.ELEMENT_NODE) {
        if (pendingH2) pendingContent.push(node);
        else if (groups.length) groups[groups.length - 1].push(node);
        return;
      }
      const tag = node.tagName;
      if (tag === 'H3' && node.id) {
        /* H3 always starts a new page; attach any pending H2 at the top */
        const g = pendingH2 ? [pendingH2, ...pendingContent, node] : [node];
        pendingH2 = null; pendingContent = [];
        groups.push(g);
      } else if (tag === 'H2') {
        /* Flush any previous H2-only section before starting a new one */
        if (pendingH2) { groups.push([pendingH2, ...pendingContent]); pendingContent = []; }
        pendingH2 = node;
      } else if (tag === 'HR' || (node.classList && node.classList.contains('pager'))) {
        /* drop */
      } else if (pendingH2) {
        pendingContent.push(node);
      } else if (groups.length) {
        groups[groups.length - 1].push(node);
      }
    });
    /* Flush a trailing H2-only section */
    if (pendingH2) groups.push([pendingH2, ...pendingContent]);
    if (groups.length === 0) return;
    const pages = groups.map((nodes, i) => {
      const div = document.createElement('div');
      div.className = 'prose-page' + (i === 0 ? ' is-active' : '');
      nodes.forEach(n => div.appendChild(n));
      return div;
    });
    pages.forEach((page, i) => {
      const nav = document.createElement('nav');
      nav.className = 'pager subsection-pager';
      nav.setAttribute('aria-label', 'Subsection navigation');
      const prevAnchor = i > 0 ? groupAnchor(groups[i-1]) : null;
      const nextAnchor = i < groups.length-1 ? groupAnchor(groups[i+1]) : null;
      if (prevAnchor) {
        const a = document.createElement('a');
        a.href = '#' + prevAnchor.id; a.className = 'prev'; a.dataset.pageTarget = i-1;
        a.innerHTML = '<div class="dir">← Previous</div><div class="ttl">' + prevAnchor.textContent + '</div>';
        nav.appendChild(a);
      } else { nav.appendChild(document.createElement('span')); }
      if (nextAnchor) {
        const a = document.createElement('a');
        a.href = '#' + nextAnchor.id; a.className = 'next'; a.dataset.pageTarget = i+1;
        a.innerHTML = '<div class="dir">Next →</div><div class="ttl">' + nextAnchor.textContent + '</div>';
        nav.appendChild(a);
      }
      page.appendChild(nav);
      const counter = document.createElement('div');
      counter.className = 'page-counter';
      counter.textContent = (i + 1) + ' / ' + pages.length;
      page.appendChild(counter);
    });
    /* Build id→page map for both H3 and H2 anchors */
    const idToPage = {};
    groups.forEach((nodes, i) => {
      nodes.forEach(n => {
        if (n.nodeType === Node.ELEMENT_NODE && (n.tagName === 'H3' || n.tagName === 'H2') && n.id)
          idToPage[n.id] = i;
      });
    });
    while (prose.firstChild) prose.removeChild(prose.firstChild);
    pages.forEach(p => prose.appendChild(p));
    function showPage(idx) {
      idx = Math.max(0, Math.min(idx, pages.length-1));
      pages.forEach((p, i) => p.classList.toggle('is-active', i === idx));
      article.classList.toggle('past-cover', idx > 0);
      window.scrollTo(0, 0);
      const anchor = groupAnchor(groups[idx]);
      if (!anchor) return;
      document.title = anchor.textContent.trim() + ' — ' + baseTitle;
      history.replaceState(null, '', '#' + anchor.id);
      document.querySelectorAll('.sidebar a.leaf.is-current').forEach(el => { el.classList.remove('is-current'); el.removeAttribute('aria-current'); });
      const leaf = document.querySelector('.sidebar a.leaf[href="#' + CSS.escape(anchor.id) + '"]');
      if (leaf) {
        leaf.classList.add('is-current'); leaf.setAttribute('aria-current', 'page');
        leaf.scrollIntoView({ block: 'nearest' });
        const cat = leaf.closest('.cat');
        if (cat && cat.dataset.collapsed === 'true') cat.querySelector('[data-toggle="cat"]')?.click();
      }
    }
    prose.addEventListener('click', e => {
      const a = e.target.closest('a[data-page-target]');
      if (!a) return; e.preventDefault(); showPage(parseInt(a.dataset.pageTarget, 10));
    });
    document.querySelectorAll('.sidebar a.leaf[href]').forEach(leaf => {
      const id = leaf.getAttribute('href').slice(1);
      if (!(id in idToPage)) return;
      leaf.addEventListener('click', e => { e.preventDefault(); showPage(idToPage[id]); });
    });
    window.addEventListener('hashchange', () => { const id = location.hash.slice(1); if (id in idToPage) showPage(idToPage[id]); });
    document.addEventListener('keydown', e => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (document.querySelector('.article:not([hidden])') !== article) return;
      const cur = pages.findIndex(p => p.classList.contains('is-active'));
      if (e.key === 'ArrowRight') { e.preventDefault(); showPage(cur+1); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); showPage(cur-1); }
    });
    const initId = location.hash.slice(1);
    showPage(initId in idToPage ? idToPage[initId] : 0);
  });
}
window.addEventListener('load', buildPagedView);

window.addEventListener('load', () => { if (typeof hljs !== 'undefined') hljs.highlightAll(); });
"""


_HLJS_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles'
_THEME_HLJS = {
    'deepdive': 'atom-one-dark',
    'slate':    'nord',
    'forest':   'monokai-sublime',
    'paper':    'monokai',
    'graphite': 'github-dark',
}
_HLJS_DEFAULT = 'github-dark-dimmed'


def render_html(projects, tab_labels, themes_dir=None):
    """
    projects: list of (project_key, doc) tuples, first is default active.
    tab_labels: dict {project_key: display_label}
    themes_dir: Path to themes folder (auto-discovered if None)
    """
    proj_keys   = [key for key, _ in projects]
    proj_labels = {key: tab_labels[key] for key, _ in projects}

    # Discover themes dynamically from the themes folder
    script_dir = Path(__file__).parent
    if themes_dir is None:
        themes_dir = script_dir / 'themes'
    theme_names = []
    if themes_dir.exists():
        theme_names = sorted(
            p.stem for p in themes_dir.glob('*.css')
            if p.stem != 'overrides'
        )
    if not theme_names:
        theme_names = ['default']
    default_theme = theme_names[0]

    theme_buttons = '\n'.join(
        f'      <button data-theme="{name}" aria-pressed="{str(name == default_theme).lower()}" title="{name.capitalize()}"></button>'
        for name in theme_names
    )

    sidebar_html = ''
    for key, doc in projects:
        sidebar_html += render_sidebar_nav(doc, key, key) + '\n'

    articles_html = ''
    for key, doc in projects:
        articles_html += render_article(doc, key, key) + '\n'

    nav_html  = shared.session_nav_html(len(projects))
    font_html = shared.font_picker_html()

    inline_script = (INLINE_SCRIPT
                     .replace('/*THEME_PICKER_JS*/', shared.theme_picker_js())
                     .replace('/*FONT_JS*/',         shared.FONT_JS)
                     .replace('/*TAB_JS*/',          shared.tab_js(proj_keys, proj_labels,
                                                                   'gaia-notes-tab', 'GAIA')))

    search_index_json = json.dumps(
        _build_prebaked_index(projects), ensure_ascii=False, separators=(',', ':')
    )

    default_hljs = _THEME_HLJS.get(default_theme, _HLJS_DEFAULT)
    hljs_css_url = f'{_HLJS_CDN}/{default_hljs}.min.css'

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Study Notes</title>
<script>
window.addEventListener('error', (e) => {{
  if (e.message && /ResizeObserver loop/.test(e.message)) {{ e.stopImmediatePropagation(); e.preventDefault(); }}
}}, true);
</script>
<script>
MathJax = {{
  tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']], processEscapes: true }},
  options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre'] }},
  chtml: {{ scale: 1.0 }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script" async></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,500;1,400&family=Fira+Code:wght@400;500&display=swap">
<link rel="stylesheet" id="themeCSS" href="themes/{default_theme}.css">
<link id="hljsCSS" rel="stylesheet" href="{hljs_css_url}">
<link rel="stylesheet" href="themes/overrides.css">
<style>
  .prose-page {{ display: none; }}
  .prose-page.is-active {{ display: block; }}

  /* ── Zen mode (all themes) ── */
  body.zen .title {{ display: none; }}
  body.zen .byline {{ display: none; }}

  /* Zen exit button */
  .zen-exit-btn {{
    display: none;
    position: fixed;
    top: 14px;
    right: 16px;
    z-index: 9999;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border: 1px solid rgba(128,128,128,0.35);
    border-radius: 6px;
    background: rgba(20,20,20,0.72);
    color: #eee;
    font-size: 12px;
    font-family: inherit;
    cursor: pointer;
    backdrop-filter: blur(6px);
    transition: background .15s;
  }}
  .zen-exit-btn:hover {{ background: rgba(40,40,40,0.9); }}
  body.zen .zen-exit-btn {{ display: flex; }}

  /* Search dropdown */
  .search-wrap {{ position: relative; }}
  .search-drop {{
    position: absolute;
    top: calc(100% + 8px);
    left: 0;
    min-width: 320px;
    background: var(--surface, #fff);
    border: 1px solid var(--border, #ddd);
    border-radius: 8px;
    box-shadow: 0 8px 28px rgba(0,0,0,0.18);
    max-height: 380px;
    overflow-y: auto;
    z-index: 999;
  }}
  .search-drop[hidden] {{ display: none; }}
  .search-result {{
    display: block;
    padding: 9px 14px;
    cursor: pointer;
    border-bottom: 1px solid var(--border, #eee);
    text-decoration: none;
    color: inherit;
  }}
  .search-result:last-child {{ border-bottom: none; }}
  .search-result:hover {{ background: rgba(0,0,0,0.045); }}
  .sr-sec {{ display: block; font-size: 10px; opacity: .5; margin-bottom: 2px; text-transform: uppercase; letter-spacing: .04em; }}
  .sr-title {{ display: block; font-size: 13px; font-weight: 500; }}
  .sr-snippet {{ display: block; font-size: 11px; opacity: .55; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .search-empty {{ padding: 12px 14px; font-size: 13px; opacity: .5; }}

  /* ── Tables ── */
  .prose table, .intro-content table {{ border-collapse: collapse; width: 100%; margin: 1em 0; font-size: .92em; }}
  .prose th, .prose td, .intro-content th, .intro-content td {{
    border: 1px solid var(--line, #ccc); padding: 7px 11px; text-align: left; vertical-align: top;
  }}
  .prose thead th, .intro-content thead th {{
    background: var(--bg-soft, #f5f5f5); font-weight: 600;
  }}
  .prose tbody tr:nth-child(even), .intro-content tbody tr:nth-child(even) {{
    background: var(--bg-soft, #f9f9f9);
  }}

  /* ── Blockquotes ── */
  .prose blockquote, .intro-content blockquote {{
    margin: 1em 0; padding: .6em 1em;
    border-left: 3px solid var(--bronze, #b8860b);
    background: var(--bg-soft, #f9f9f9);
    color: var(--body, #333);
  }}
  .prose blockquote p, .intro-content blockquote p {{ margin: .25em 0; }}

  /* ── H3 heading anchors ── */
  .prose h3 > a {{ color: inherit; text-decoration: none; }}
  .prose h3 > a:hover::after {{ content: ' #'; opacity: .4; font-weight: 400; }}

  /* ── H4 headings ── */
  .prose h4 {{ font-size: .9em; font-weight: 700; margin: 1.1em 0 .4em; text-transform: uppercase; letter-spacing: .04em; opacity: .8; }}

  /* ── Task-list checkboxes ── */
  .prose li input[type="checkbox"] {{ margin-right: .4em; vertical-align: middle; }}

  /* ── Doc subtitle ── */
  .doc-subtitle {{ font-size: .95em; opacity: .7; margin: -.3em 0 .6em; font-style: italic; }}

  /* ── Intro content (pre-section) ── */
  .intro-content {{ margin-bottom: 1.4em; }}

  /* ── Hide article header (title/byline/intro) on pages after the first ── */
  .article.past-cover .title,
  .article.past-cover .doc-subtitle,
  .article.past-cover .byline,
  .article.past-cover .intro-content {{ display: none; }}

  /* ── Copy button on code blocks ── */
  pre {{ position: relative; }}
  .copy-btn {{
    position: absolute; top: 7px; right: 8px;
    padding: 2px 8px; font-size: 11px; font-family: var(--font-code, monospace);
    background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.16);
    border-radius: 4px; color: var(--code-ink, #ccc); cursor: pointer;
    opacity: 0; transition: opacity .15s, background .15s; line-height: 1.6;
  }}
  pre:hover .copy-btn {{ opacity: 1; }}
  .copy-btn.copied {{ background: rgba(80,200,120,0.2); border-color: rgba(80,200,120,0.45); }}

  /* ── Page counter ── */
  .page-counter {{
    text-align: center; font-size: 11px; opacity: 0.5;
    margin-top: 10px; font-variant-numeric: tabular-nums; pointer-events: none;
  }}

  /* ── Search match highlight ── */
  .search-drop mark {{ background: rgba(255,200,0,0.3); color: inherit; border-radius: 2px; padding: 0 1px; }}

  /* ── Print ── */
  @media print {{
    .topbar, .sidebar, .pager, .zen-exit-btn, .settings-panel {{ display: none !important; }}
    .layout {{ display: block; }}
    .prose-page {{ display: block !important; page-break-inside: avoid; }}
    .article[hidden] {{ display: none !important; }}
  }}

  /* ── Responsive: phones ── */
  @media (max-width: 640px) {{
    .theme-picker, .settings-btn, .zen-btn {{ display: none !important; }}
    .top-search {{ width: auto; flex: 1 1 0; min-width: 0; }}
    .kbd {{ display: none; }}
    .topbar-actions {{ gap: 8px; }}
  }}
  @media (max-width: 480px) {{
    .brand-name {{ font-size: 17px; letter-spacing: 0; }}
    .brand-issue {{ display: none; }}
    .top-search {{ max-width: 96px; }}
  }}

  /* Touch: copy button always visible (no hover on touchscreen) */
  @media (hover: none) {{
    .copy-btn {{ opacity: 0.85 !important; }}
  }}

  /* Wide tables scroll horizontally instead of breaking layout */
  .prose table, .intro-content table {{ display: block; overflow-x: auto; }}

{shared.FONT_CSS}{shared.TAB_CSS}</style>
</head>
<body data-theme="{default_theme}">

<header class="topbar">
  <a class="brand" href="#">
    <span class="brand-mark" aria-hidden="true">{TOPNAV_SVG}</span>
    <span class="brand-name">STUDY</span>
    <span class="brand-issue">Notes<br>2025–26</span>
  </a>
  {nav_html}
  <div class="topbar-actions">
    <button class="icon-btn menu-btn" id="menuBtn" aria-label="Open menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
    <div class="search-wrap">
      <label class="top-search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input type="text" placeholder="Search notes…" id="searchInput">
        <span class="kbd">⌘K</span>
      </label>
      <div id="searchDropdown" class="search-drop" hidden></div>
    </div>
    {font_html}
    <div class="theme-picker" role="group" aria-label="Theme">
      <span class="theme-label">Theme</span>
{theme_buttons}
    </div>
    <button class="zen-btn" id="zenBtn" aria-pressed="false" title="Zen mode (Z)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9V5H8"/><path d="M20 9V5H16"/><path d="M4 15v4h4"/><path d="M20 15v4h-4"/></svg>
      <span>Zen</span>
    </button>
  </div>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="side-label" id="sideLabel">GAIA · Project 1</div>
{sidebar_html}
  </aside>

  <div class="main">
{articles_html}
  </div>
</div>

<button class="zen-exit-btn" id="zenExit" title="Exit Zen mode (Z)">
  <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>
  Exit Zen
</button>

<script>window.SEARCH_INDEX = {search_index_json};</script>
<script>
{inline_script}
</script>
</body>
</html>
'''


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help'):
        print(__doc__)
        sys.exit(0)

    # Parse flags
    output_file = None
    themes_src = None
    md_files = []
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

    # Resolve paths relative to script location
    script_dir = Path(__file__).parent
    md_paths = [Path(f) if Path(f).is_absolute() else script_dir / f for f in md_files]

    for p in md_paths:
        if not p.exists():
            print(f'Error: file not found: {p}'); sys.exit(1)

    # Default output
    if not output_file:
        output_file = script_dir / 'notes.html'
    else:
        output_file = Path(output_file)

    # Copy themes
    if themes_src:
        themes_dst = output_file.parent / 'themes'
        if not themes_dst.exists():
            shutil.copytree(themes_src, themes_dst)
            print(f'Copied themes → {themes_dst}')
    else:
        candidates = [
            script_dir / 'themes',
            output_file.parent / 'themes',
        ]
        themes_dst = output_file.parent / 'themes'
        if not themes_dst.exists():
            src = next((c for c in candidates if c.exists() and c != themes_dst), None)
            if src:
                shutil.copytree(src, themes_dst)
                print(f'Copied themes → {themes_dst}')
            else:
                print('Warning: themes folder not found. HTML will be unstyled.')
                print('Re-run with --themes /path/to/themes to fix this.')

    # Parse all markdown files
    projects = []
    tab_labels = {}
    seen_keys: dict = {}
    global _key_to_label
    for path in md_paths:
        print(f'Parsing {path.name}…')
        doc = parse_markdown(path)
        key = session_key(path)
        if key in seen_keys:
            seen_keys[key] += 1
            key = f'{key}-{seen_keys[key]}'
        else:
            seen_keys[key] = 1
        label = project_label(path, doc)
        tab_labels[key] = label
        _key_to_label[key] = label
        projects.append((key, doc))

    # Count total nodes in tree (for stats)
    def count_nodes(sections):
        return sum(1 + count_nodes(s['children']) for s in sections)

    print('Rendering HTML…')
    html_out = render_html(projects, tab_labels, themes_dst)

    output_file.write_text(html_out, encoding='utf-8')
    print(f'✓ Written → {output_file}')
    print(f'  {len(projects)} project(s), '
          f'{sum(len(d["sections"]) for _, d in projects)} top-level sections, '
          f'{sum(count_nodes(d["sections"]) for _, d in projects)} total nodes.')


if __name__ == '__main__':
    main()
