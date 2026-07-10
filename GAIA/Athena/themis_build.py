#!/usr/bin/env python3
"""
themis_build.py — Builds question_bank.html from Themis question_bank.md.

Input format (CLAUDE.md spec):
    ## Q{n}. [Question text verbatim]

    **Answer:**

    [Comprehensive answer — rich markdown, LaTeX, sub-headings, lists, ---]

    **Source:** [file(s)]

    ---

Usage:
    python3 themis_build.py "GAIA/Themis/question_bank.md"
    python3 themis_build.py question_bank.md -o output.html --themes /path/to/themes
"""

import sys, re, json, shutil, html as html_lib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import shared


# ── Helpers ───────────────────────────────────────────────────────────────────

def inline_fmt(s):
    """Inline markdown → HTML: bold, italic, code. Math already protected."""
    s = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', s)
    s = re.sub(r'\*\*(.*?)\*\*',     r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.*?)\*',          r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`',          r'<code>\1</code>', s)
    return s


def md_to_html(text):
    """Convert a Themis answer markdown block to HTML.

    Handles: display/inline LaTeX (protected), horizontal rules, unordered
    and ordered lists, paragraphs with inline formatting.
    """
    if not text or not text.strip():
        return '<p><em>No answer recorded.</em></p>'

    placeholders = {}
    ph = [0]

    def protect(v):
        k = f'\x00PH{ph[0]}\x00'; ph[0] += 1; placeholders[k] = v; return k

    # Protect display math ($$...$$) first — may span multiple lines
    def rep_display(m):
        inner = m.group(1).replace('<', '&lt;').replace('>', '&gt;')
        return protect(f'<p class="display-math">$${inner}$$</p>')
    text = re.sub(r'\$\$(.*?)\$\$', rep_display, text, flags=re.DOTALL)

    # Protect inline math ($...$)
    def rep_inline(m):
        return protect(m.group(0).replace('<', '&lt;').replace('>', '&gt;'))
    text = re.sub(r'\$[^$\n]+?\$', rep_inline, text)

    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Protected placeholder on its own line
        if '\x00PH' in stripped and stripped.startswith('\x00PH') and stripped.endswith('\x00'):
            out.append(stripped); i += 1; continue

        # Empty
        if not stripped:
            i += 1; continue

        # Horizontal rule
        if re.match(r'^---+$', stripped):
            out.append('<hr>'); i += 1; continue

        # Unordered list
        if re.match(r'^[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                items.append(f'<li>{inline_fmt(lines[i][2:].strip())}</li>'); i += 1
            out.append('<ul>' + ''.join(items) + '</ul>'); continue

        # Ordered list
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                item_text = re.sub(r'^\d+\.\s+', '', lines[i])
                items.append(f'<li>{inline_fmt(item_text)}</li>'); i += 1
            out.append('<ol>' + ''.join(items) + '</ol>'); continue

        # Paragraph (accumulate until blank, list, hr, or standalone placeholder)
        para = []
        i_start = i
        while i < len(lines):
            l = lines[i]
            ls = l.strip()
            if not ls:
                break
            if re.match(r'^[-*] |\d+\. |^---+$', l):
                break
            if '\x00PH' in ls and ls.startswith('\x00PH') and ls.endswith('\x00'):
                break
            para.append(inline_fmt(l)); i += 1
        if para:
            out.append('<p>' + ' '.join(para) + '</p>')
        elif i == i_start and i < len(lines):
            out.append('<p>' + inline_fmt(lines[i]) + '</p>'); i += 1

    result = '\n'.join(out)
    for k, v in placeholders.items():
        result = result.replace(k, v)
    return result


# ── Parser ────────────────────────────────────────────────────────────────────

def parse_themis_md(path):
    """Parse question_bank.md. Returns (meta dict, list of question dicts)."""
    text = Path(path).read_text(encoding='utf-8')

    # Header metadata (first ~8 lines)
    meta = {'title': '', 'generated': '', 'course': '', 'sources': ''}
    for line in text.splitlines()[:8]:
        if line.startswith('# ') and not meta['title']:
            meta['title'] = line[2:].strip()
        elif m := re.match(r'\*\*Generated:\*\*\s*(.+)', line):
            meta['generated'] = m.group(1).strip()
        elif m := re.match(r'\*\*Course:\*\*\s*(.+)', line):
            meta['course'] = m.group(1).strip()
        elif m := re.match(r'\*\*Sources?:\*\*\s*(.+)', line):
            meta['sources'] = m.group(1).strip().replace('`', '')

    # Split into blocks on ## Q{n}.
    blocks = re.split(r'(?=^## Q\d+\.)', text, flags=re.MULTILINE)

    questions = []
    for block in blocks:
        block = block.strip()
        if not block.startswith('## Q'):
            continue

        block_lines = block.splitlines()
        heading = block_lines[0]
        m = re.match(r'^## Q(\d+)\.\s*(.+)$', heading)
        if not m:
            continue
        n     = int(m.group(1))
        title = m.group(2).strip()

        rest_lines = block_lines[1:]

        # Find **Answer:** start and **Source:** line (last occurrence wins)
        ans_start = None
        src_idx   = None
        for li, l in enumerate(rest_lines):
            if ans_start is None and re.match(r'^\*\*Answer:\*\*', l):
                ans_start = li + 1   # body starts on next line
            if re.match(r'^\*\*Source:\*\*', l):
                src_idx = li

        # Extract source
        source = ''
        if src_idx is not None:
            src_raw = rest_lines[src_idx]
            source = re.sub(r'^\*\*Source:\*\*\s*', '', src_raw).replace('`', '').strip()

        # Extract answer body
        if ans_start is not None:
            end = src_idx if (src_idx is not None and src_idx > ans_start) else len(rest_lines)
            answer_md = '\n'.join(rest_lines[ans_start:end]).strip()
        else:
            answer_md = ''

        answer_html = md_to_html(answer_md)

        questions.append({
            'n':           n,
            'title':       title,
            'answer_html': answer_html,
            'source':      source,
        })

    # Sort by question number in case file order differs
    questions.sort(key=lambda q: q['n'])
    return meta, questions


# ── Static assets ─────────────────────────────────────────────────────────────

BRAND_SVG = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <line x1="16" y1="5" x2="16" y2="27" stroke="currentColor" stroke-width="1.5" stroke-opacity="0.55"/>
  <line x1="8" y1="9" x2="24" y2="9" stroke="currentColor" stroke-width="1.6"/>
  <line x1="8" y1="9" x2="6" y2="16" stroke="currentColor" stroke-width="1.4"/>
  <line x1="6" y1="16" x2="10" y2="16" stroke="currentColor" stroke-width="1.4"/>
  <line x1="24" y1="9" x2="26" y2="16" stroke="currentColor" stroke-width="1.4"/>
  <line x1="22" y1="16" x2="26" y2="16" stroke="currentColor" stroke-width="1.4"/>
  <line x1="8" y1="9" x2="8.5" y2="7" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.5"/>
  <line x1="24" y1="9" x2="23.5" y2="7" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.5"/>
  <line x1="13" y1="27" x2="19" y2="27" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

INLINE_CSS = """
/* ── Progress bar ── */
.progress-wrap {
  position: sticky; top: var(--topbar-h); z-index: 9;
  height: 3px; background: var(--line-soft);
}
.progress-fill { height: 100%; width: 0%; background: var(--teal); transition: width .35s ease; }

/* ── Progress chip ── */
.progress-chip {
  font-size: 13px; font-weight: 600; color: var(--ink);
  background: var(--bg-soft); border: 1px solid var(--line);
  border-radius: 999px; padding: 4px 14px;
  white-space: nowrap; flex: none;
}

/* ── Theme picker ── */
.theme-picker { display: flex; align-items: center; gap: 8px; }
.theme-label  { font-size: 11px; color: var(--mute); text-transform: uppercase; letter-spacing: .08em; }
.theme-picker button {
  width: 20px; height: 20px; border-radius: 50%; cursor: pointer;
  border: 2px solid transparent; padding: 0;
  transition: border-color .15s, transform .12s;
}
.theme-picker button:hover { transform: scale(1.15); }
.theme-picker button[aria-pressed="true"]  { border-color: var(--bronze); }
.theme-picker button[data-theme="folio"]    { background: #ECE6D4; }
.theme-picker button[data-theme="deepdive"] { background: #2B2D31; border-color: var(--line); }

/* ── Sidebar Q list ── */
.q-list { padding: .5rem 0; }
.q-link {
  display: flex; align-items: center; gap: 9px;
  padding: 5px 16px 5px 20px; font-size: 12.5px; color: var(--body);
  cursor: pointer; border: none; background: none; width: 100%;
  text-align: left; font-family: inherit;
  transition: background .12s, color .12s;
}
.q-link:hover    { background: var(--bg-soft);    color: var(--ink); }
.q-link.is-current  { background: var(--bronze-soft); color: var(--ink); }
.q-status {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--line); flex: none; transition: background .2s;
}
.q-link.is-reviewed .q-status { background: var(--teal); }
.q-num-tag {
  font-size: 10.5px; color: var(--mute);
  font-family: var(--mono, monospace); flex: none; min-width: 28px;
}
.q-title-short {
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  flex: 1; min-width: 0;
}

/* ── Q panel ── */
.q-panel { padding: 2.5rem 2.5rem 2rem; max-width: 820px; }

.q-header {
  display: flex; align-items: flex-start; justify-content: space-between;
  gap: 1rem; margin-bottom: 1.75rem; flex-wrap: wrap;
}
.q-header-left { flex: 1; min-width: 0; }
.q-num-label {
  font-size: 11px; font-weight: 700; letter-spacing: .1em;
  text-transform: uppercase; color: var(--mute); margin-bottom: 8px;
}
.q-title-text {
  font-size: 1.2rem; font-weight: 700; color: var(--ink); line-height: 1.45;
  margin: 0;
}

/* ── Reviewed button ── */
.review-btn {
  flex: none; display: flex; align-items: center; gap: 6px;
  font-size: 12px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase;
  padding: 6px 16px; border-radius: 999px; cursor: pointer;
  border: 1px solid var(--line); background: transparent; color: var(--mute);
  transition: border-color .15s, background .15s, color .15s; font-family: inherit;
  white-space: nowrap;
}
.review-btn:hover           { border-color: var(--teal-edge); color: var(--teal); background: var(--teal-soft); }
.review-btn.is-reviewed     { border-color: var(--teal-edge); color: var(--teal); background: var(--teal-soft); }

/* ── Answer body ── */
.q-answer {
  font-size: .95rem; line-height: 1.85; color: var(--body);
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--line-soft);
  margin-bottom: 1.25rem;
}
.q-answer p          { margin: 0 0 .9em; }
.q-answer ul,
.q-answer ol         { padding-left: 1.6em; margin: 0 0 .9em; }
.q-answer li         { margin-bottom: .35em; }
.q-answer hr         { border: none; border-top: 1px solid var(--line-soft); margin: 1.2em 0; }
.q-answer code       {
  font-family: var(--mono, monospace); font-size: .875em;
  background: var(--bg-soft); padding: 1px 5px; border-radius: 3px;
}
.display-math        { text-align: center; margin: .75rem 0; overflow-x: auto; }

/* ── Source chip ── */
.q-source {
  font-size: 11.5px; color: var(--mute); font-style: italic;
  padding: 6px 12px; background: var(--bg-soft);
  border-radius: 6px; border: 1px solid var(--line-soft);
  display: inline-block; margin-bottom: 1.5rem;
}
.q-source strong { color: var(--body); font-style: normal; }

/* ── Nav bar ── */
.q-nav {
  display: flex; align-items: center; justify-content: space-between; gap: 12px;
  margin-bottom: 1.5rem;
}
.nav-btn {
  display: flex; align-items: center; gap: 6px;
  padding: 9px 20px; border-radius: 8px; cursor: pointer;
  font: inherit; font-size: .85rem; font-weight: 600; color: var(--body);
  border: 1px solid var(--line); background: var(--bg-elev);
  transition: border-color .15s, background .15s, color .15s;
}
.nav-btn:hover:not(:disabled) { border-color: var(--bronze-edge); background: var(--bronze-soft); color: var(--ink); }
.nav-btn:disabled              { opacity: .32; cursor: default; }
.q-pos {
  font-size: 13px; color: var(--mute); text-align: center;
  min-width: 60px; font-family: var(--mono, monospace);
}

/* ── Keyboard hints ── */
.kbd-hint {
  margin-top: 1.5rem; padding-top: 1rem;
  border-top: 1px solid var(--line-soft);
  display: flex; flex-wrap: wrap; gap: 10px 22px;
}
.kbd-item      { display: flex; align-items: center; gap: 8px; font-size: 11.5px; color: var(--mute); }
.kbd-item .kbd {
  font-family: var(--mono, monospace); font-size: 10px;
  padding: 2px 7px; border-radius: 4px;
  border: 1px solid var(--line); background: var(--bg-soft); color: var(--mute);
}

/* ── Responsive ── */
@media (max-width: 660px) {
  .q-panel       { padding: 1.5rem 1.25rem 1.5rem; }
  .q-title-text  { font-size: 1.05rem; }
  .q-header      { flex-direction: column; }
}
"""

# ── JavaScript ────────────────────────────────────────────────────────────────

SCRIPT = r"""
/*THEME_PICKER_JS*/

/*FONT_JS*/

/* ── Question data (injected by Python) ── */
/*QUESTIONS_PLACEHOLDER*/

/* ── MathJax typeset helper ── */
function typesetEl(el) {
  if (!window.MathJax || !MathJax.typesetPromise) return;
  MathJax.typesetClear([el]);
  MathJax.typesetPromise([el]).catch(() => {});
}

/* ── Reviewed state (persisted) ── */
let reviewed;
try { reviewed = new Set(JSON.parse(localStorage.getItem('themis-reviewed') || '[]')); }
catch (e) { reviewed = new Set(); }

function saveReviewed() {
  localStorage.setItem('themis-reviewed', JSON.stringify([...reviewed]));
}

/* ── Progress bar + chip ── */
function updateProgress() {
  const fill = document.querySelector('.progress-fill');
  if (fill) fill.style.width = QUESTIONS.length
    ? (reviewed.size / QUESTIONS.length * 100) + '%' : '0%';
  const chip = document.getElementById('progressChip');
  if (chip) chip.textContent = reviewed.size + ' / ' + QUESTIONS.length + ' reviewed';
}

/* ── Sidebar ── */
function updateSidebar(idx) {
  document.querySelectorAll('.q-link').forEach((link, i) => {
    const n = parseInt(link.dataset.n, 10);
    link.classList.toggle('is-current',  i === idx);
    link.classList.toggle('is-reviewed', reviewed.has(n));
  });
  const cur = document.querySelector('.q-link.is-current');
  if (cur) cur.scrollIntoView({ block: 'nearest' });
}

/* ── Review button ── */
function updateReviewBtn(n) {
  const btn = document.getElementById('reviewBtn');
  if (!btn) return;
  const isRev = reviewed.has(n);
  btn.classList.toggle('is-reviewed', isRev);
  btn.textContent = isRev ? '✓ Reviewed' : 'Mark Reviewed';
}

/* ── Current question index ── */
let currentIdx = 0;

/* ── Select question by index ── */
function selectQuestion(idx) {
  if (idx < 0 || idx >= QUESTIONS.length) return;
  currentIdx = idx;
  const q = QUESTIONS[idx];

  document.getElementById('qNumLabel').textContent = 'Q' + q.n;
  document.getElementById('qTitle').textContent = q.title;

  const answerEl = document.getElementById('qAnswer');
  answerEl.innerHTML = q.answer_html;
  typesetEl(answerEl);
  if (typeof hljs !== 'undefined') answerEl.querySelectorAll('pre code').forEach(el => hljs.highlightElement(el));

  const srcEl = document.getElementById('qSource');
  if (q.source) {
    srcEl.innerHTML = '<strong>Source:</strong> ' + escHtml(q.source);
    srcEl.style.display = '';
  } else {
    srcEl.style.display = 'none';
  }

  document.getElementById('qPos').textContent = (idx + 1) + ' / ' + QUESTIONS.length;

  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  if (prevBtn) prevBtn.disabled = idx === 0;
  if (nextBtn) nextBtn.disabled = idx === QUESTIONS.length - 1;

  updateSidebar(idx);
  updateReviewBtn(q.n);
  localStorage.setItem('themis-current', String(idx));
}

function escHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/* ── Toggle reviewed ── */
function toggleReviewed() {
  if (!QUESTIONS.length) return;
  const n = QUESTIONS[currentIdx].n;
  if (reviewed.has(n)) reviewed.delete(n);
  else reviewed.add(n);
  saveReviewed();
  updateProgress();
  updateSidebar(currentIdx);
  updateReviewBtn(n);
}

/* ── Init ── */
(function () {
  let startIdx = 0;
  try { startIdx = parseInt(localStorage.getItem('themis-current') || '0', 10) || 0; } catch (e) {}
  if (startIdx < 0 || startIdx >= QUESTIONS.length) startIdx = 0;
  updateProgress();
  selectQuestion(startIdx);
})();

/* ── Nav buttons ── */
document.getElementById('prevBtn').addEventListener('click', () => selectQuestion(currentIdx - 1));
document.getElementById('nextBtn').addEventListener('click', () => selectQuestion(currentIdx + 1));
document.getElementById('reviewBtn').addEventListener('click', toggleReviewed);

/* ── Sidebar links ── */
document.querySelectorAll('.q-link').forEach((link, i) => {
  link.addEventListener('click', () => selectQuestion(i));
});

/* ── Keyboard ── */
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  switch (e.key) {
    case 'ArrowRight': case 'l':
      e.preventDefault(); selectQuestion(currentIdx + 1); break;
    case 'ArrowLeft': case 'h':
      e.preventDefault(); selectQuestion(currentIdx - 1); break;
    case 'r': case 'R':
      e.preventDefault(); toggleReviewed(); break;
  }
});

/* ── Mobile sidebar toggle ── */
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
"""


# ── HTML rendering ────────────────────────────────────────────────────────────

def render_sidebar_qlist(questions):
    lines = ['<div class="q-list">']
    for q in questions:
        short = q['title'][:58] + '…' if len(q['title']) > 58 else q['title']
        short_esc = html_lib.escape(short)
        lines.append(
            f'  <button class="q-link" data-n="{q["n"]}">'
            f'<span class="q-status"></span>'
            f'<span class="q-num-tag">Q{q["n"]}</span>'
            f'<span class="q-title-short">{short_esc}</span>'
            f'</button>'
        )
    lines.append('</div>')
    return '\n'.join(lines)


def render_html(meta, questions, themes_dir=None):
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

    total = len(questions)

    sidebar_html = render_sidebar_qlist(questions)

    # QUESTIONS JS array (embed answer_html as raw HTML string in JSON)
    qs_data = [
        {'n': q['n'], 'title': q['title'], 'answer_html': q['answer_html'], 'source': q['source']}
        for q in questions
    ]
    questions_js = 'const QUESTIONS = ' + json.dumps(qs_data, ensure_ascii=False) + ';'
    script = (SCRIPT
              .replace('/*THEME_PICKER_JS*/', shared.theme_picker_js())
              .replace('/*FONT_JS*/',         shared.FONT_JS)
              .replace('/*QUESTIONS_PLACEHOLDER*/', questions_js))

    title_str  = meta.get('title') or 'Hermes Question Bank'
    course_str = meta.get('course') or ''
    font_html  = shared.font_picker_html()

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Themis — {html_lib.escape(title_str)}</title>
<script>
MathJax = {{
  tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']], processEscapes: true }},
  options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre'] }},
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
    <span class="brand-mark" aria-hidden="true">{BRAND_SVG}</span>
    <span class="brand-name">THEMIS</span>
    <span class="brand-issue">{html_lib.escape(course_str) if course_str else 'Question Bank'}</span>
  </a>
  <div class="topbar-actions">
    <span class="progress-chip" id="progressChip">0 / {total} reviewed</span>
    <button class="icon-btn menu-btn" id="menuBtn" aria-label="Open menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="6" x2="21" y2="6"/>
        <line x1="3" y1="12" x2="21" y2="12"/>
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

<div class="progress-wrap">
  <div class="progress-fill"></div>
</div>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="side-label">THEMIS · {total} Questions</div>
{sidebar_html}
  </aside>

  <div class="main" style="padding: 0; align-items: start;">
    <div class="q-panel">

      <div class="q-header">
        <div class="q-header-left">
          <div class="q-num-label" id="qNumLabel">Q1</div>
          <h2 class="q-title-text" id="qTitle"></h2>
        </div>
        <button class="review-btn" id="reviewBtn">Mark Reviewed</button>
      </div>

      <div class="q-answer" id="qAnswer"></div>

      <div class="q-source" id="qSource"></div>

      <div class="q-nav">
        <button class="nav-btn" id="prevBtn" disabled>&#8592; Prev</button>
        <span class="q-pos" id="qPos">1 / {total}</span>
        <button class="nav-btn" id="nextBtn"{' disabled' if total <= 1 else ''}>Next &#8594;</button>
      </div>

      <div class="kbd-hint">
        <span class="kbd-item"><span class="kbd">&#8594;</span> Next</span>
        <span class="kbd-item"><span class="kbd">&#8592;</span> Prev</span>
        <span class="kbd-item"><span class="kbd">R</span> Toggle reviewed</span>
      </div>

    </div>
  </div>
</div>

<script>{script}</script>
</body>
</html>
'''


# ── Main ──────────────────────────────────────────────────────────────────────

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
        print('Error: no input file specified.'); sys.exit(1)

    # Use the first file (question_bank.md is a single file)
    md_path = Path(md_files[0])
    if not md_path.exists():
        print(f'Error: file not found: {md_path}'); sys.exit(1)

    script_dir = Path(__file__).parent
    if not output_file:
        output_file = script_dir.parent / 'STUDY PATH' / 'question_bank.html'
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Copy themes folder if not already present beside output
    themes_dst = output_file.parent / 'themes'
    if not themes_dst.exists():
        candidates = ([Path(themes_src)] if themes_src else []) + [script_dir / 'themes']
        src = next((c for c in candidates if c.exists()), None)
        if src:
            shutil.copytree(src, themes_dst)
            print(f'Copied themes → {themes_dst}')
        else:
            print('Warning: themes folder not found — HTML will load without theme CSS.')

    print(f'Parsing {md_path.name}…')
    meta, questions = parse_themis_md(md_path)
    if not questions:
        print('Error: no questions parsed from input file.'); sys.exit(1)
    print(f'  {len(questions)} questions')

    print('Rendering HTML…')
    html_out = render_html(meta, questions, themes_dst)
    output_file.write_text(html_out, encoding='utf-8')
    print(f'✓  Written → {output_file}')
    print(f'   {len(questions)} questions, {meta.get("course") or "unknown course"}.')


if __name__ == '__main__':
    main()
