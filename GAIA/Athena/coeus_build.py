#!/usr/bin/env python3
"""
coeus_build.py — Builds quiz.html from Coeus markdown files.

Markdown format Coeus must write:
─────────────────────────────────────────────────────
# Session Name — Quiz
**Source:** `Y - notes.md` | **Session:** Y | **Date:** YYYY-MM-DD

---

### Q1. [MCQ] Question text here?

- A) option one
- B) option two
- C) option three
- D) option four

**Correct:** B
**Explanation:** Explanation text.

---

### Q2. [True/False] Statement to evaluate.

**Correct:** True
**Explanation:** Explanation text.

---

### Q3. [Open] Open question text.

**Answer:** Full answer here. Can span multiple sentences and include $math$.

---
─────────────────────────────────────────────────────

Usage:
    python3 coeus_build.py "session - quiz.md" ...
    python3 coeus_build.py *.md --themes /path/to/themes -o output.html
"""

import sys, re, shutil, html as html_lib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import shared


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text):
    s = re.sub(r'\$[^$]*\$', '', text)
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s).strip('-').lower()
    return s or 'q'


def inline_fmt(s):
    """Basic inline markdown → HTML (bold, italic, code, math passthrough)."""
    s = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', s)
    s = re.sub(r'\*\*(.*?)\*\*',     r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.*?)\*',          r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`',          r'<code>\1</code>', s)
    return s


def md_block_to_html(text):
    """Convert a multi-line markdown block (answer/explanation) to HTML."""
    placeholders = {}
    ph = [0]

    def protect(v):
        k = f'\x00PH{ph[0]}\x00'; ph[0] += 1; placeholders[k] = v; return k

    def rep_display(m):
        return protect('<p class="display-math">$$' + m.group(1).replace('<','&lt;').replace('>','&gt;') + '$$</p>')
    text = re.sub(r'\$\$(.*?)\$\$', rep_display, text, flags=re.DOTALL)

    def rep_inline(m):
        return protect(m.group(0).replace('<','&lt;').replace('>','&gt;'))
    text = re.sub(r'\$[^$\n]+?\$', rep_inline, text)

    lines = text.strip().split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if '\x00PH' in line and line.strip().startswith('\x00PH') and line.strip().endswith('\x00'):
            out.append(line.strip()); i += 1; continue
        if not line.strip():
            i += 1; continue
        if re.match(r'^[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                items.append(f'<li>{inline_fmt(lines[i][2:].strip())}</li>'); i += 1
            out.append('<ul>' + ''.join(items) + '</ul>'); continue
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                stripped = re.sub(r'^\d+\.\s', '', lines[i])
                items.append(f'<li>{inline_fmt(stripped)}</li>'); i += 1
            out.append('<ol>' + ''.join(items) + '</ol>'); continue
        para = []
        i_para_start = i
        while i < len(lines) and lines[i].strip() and not re.match(r'^[-*] |\d+\. ', lines[i]):
            if '\x00PH' in lines[i] and lines[i].strip().startswith('\x00PH'): break
            para.append(inline_fmt(lines[i])); i += 1
        if para:
            out.append('<p>' + ' '.join(para) + '</p>')
        elif i == i_para_start and i < len(lines):
            # Line starts with a placeholder mixed with text — output as-is and advance
            out.append('<p>' + lines[i] + '</p>'); i += 1
    result = '\n'.join(out)
    for k, v in placeholders.items():
        result = result.replace(k, v)
    return result


# ── Coeus markdown parser ─────────────────────────────────────────────────────

TYPE_RE  = re.compile(r'\[(?P<type>MCQ|True/False|Open)\]', re.IGNORECASE)
OPT_RE   = re.compile(r'^-\s+([A-Da-d])[.)]\s+(.+)$')
FIELD_RE = re.compile(r'^\*\*(?P<key>Correct|Answer|Explanation):\*\*\s*(?P<val>.+)$', re.IGNORECASE)


def parse_coeus_md(path, prefix):
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    doc = {'title': '', 'source': '', 'session': '', 'date': '', 'questions': []}
    cur_q = None
    extra_buf = []   # lines that might be additional explanation

    def flush_extra():
        if cur_q and extra_buf:
            block = '\n'.join(extra_buf).strip()
            if block:
                key = 'answer_html' if cur_q['type'] == 'open' else 'explanation_html'
                cur_q[key] = (cur_q.get(key, '') + '\n' + md_block_to_html(block)).strip()
            extra_buf.clear()

    for line in lines:
        # Document title
        if line.startswith('# ') and not doc['title']:
            doc['title'] = line[2:].strip(); continue

        # Metadata line: **Source:** ... | **Session:** ... | **Date:** ...
        if re.match(r'\*\*Source', line):
            for key, pat in [('source', r'\*\*Sources?:\*\*\s*`?([^`|]+)`?'),
                             ('session', r'\*\*Session:\*\*\s*([^|]+)'),
                             ('date',    r'\*\*Date:\*\*\s*(\S+)')]:
                m = re.search(pat, line)
                if m: doc[key] = m.group(1).strip()
            continue

        # Separator
        if re.match(r'^---+$', line.strip()):
            flush_extra(); continue

        # Question heading: ### Q{n}. [TYPE] text
        if line.startswith('### '):
            flush_extra()
            heading = line[4:].strip()
            tm = TYPE_RE.search(heading)
            qtype = tm.group('type').lower().replace('/', '') if tm else 'open'
            if qtype == 'truefals': qtype = 'truefalse'
            # Strip Q{n}. and [TYPE] from heading text
            text = TYPE_RE.sub('', heading)
            text = re.sub(r'^Q\d+\.\s*', '', text).strip()
            n = len(doc['questions']) + 1
            cur_q = {
                'n': n,
                'id': f'{prefix}-q{n}',
                'type': qtype,   # 'mcq' | 'truefalse' | 'open'
                'text': text,
                'options': [],   # list of (letter, text) for MCQ
                'correct': '',   # 'A'/'B'/'C'/'D' or 'true'/'false'
                'explanation_html': '',
                'answer_html': '',
            }
            doc['questions'].append(cur_q)
            continue

        if cur_q is None:
            continue

        # MCQ option: - A) text
        om = OPT_RE.match(line)
        if om:
            flush_extra()
            cur_q['options'].append((om.group(1).upper(), om.group(2).strip()))
            continue

        # Field: **Correct:** / **Answer:** / **Explanation:**
        fm = FIELD_RE.match(line)
        if fm:
            flush_extra()
            key, val = fm.group('key').lower(), fm.group('val').strip()
            if key == 'correct':
                cur_q['correct'] = val.strip().upper() if cur_q['type'] == 'mcq' else val.strip().lower()
            elif key == 'answer':
                cur_q['answer_html'] = md_block_to_html(val)
            elif key == 'explanation':
                cur_q['explanation_html'] = md_block_to_html(val)
            continue

        # Everything else in a question block — could be continuation of explanation/answer
        if line.strip():
            extra_buf.append(line)
        else:
            flush_extra()

    flush_extra()
    return doc


# ── Tab label / key ───────────────────────────────────────────────────────────

def tab_label(path):
    stem = Path(path).stem
    name = re.sub(r'\s*-\s*quiz.*$', '', stem, flags=re.IGNORECASE).strip()
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
/* ── Progress bar (below topbar) ── */
.progress-wrap {
  position: sticky; top: var(--topbar-h); z-index: 9;
  height: 3px; background: var(--line-soft);
}
.progress-fill {
  height: 100%; width: 0%; background: var(--teal);
  transition: width .3s ease;
}

/* ── New Test button ── */
.new-test-btn {
  display: flex; align-items: center; gap: 6px;
  font-size: 12px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase;
  padding: 5px 14px; border-radius: 999px; cursor: pointer;
  border: 1px solid var(--bronze-edge); background: var(--bronze-soft); color: var(--bronze);
  transition: opacity .15s, background .15s;
  white-space: nowrap; flex: none;
}
.new-test-btn:hover { opacity: .8; }
.new-test-btn svg { flex: none; }

/* ── Score chip in topbar ── */
.score-chip {
  font-size: 13px; font-weight: 600; color: var(--ink);
  background: var(--bg-soft); border: 1px solid var(--line);
  border-radius: 999px; padding: 4px 14px;
  white-space: nowrap; flex: none;
}

/* ── Sidebar Q list ── */
.q-list { padding: 0.75rem 0; }
.q-link {
  display: flex; align-items: center; gap: 10px;
  padding: 6px 20px; font-size: 13px; color: var(--body);
  cursor: pointer; transition: background .12s, color .12s;
  text-decoration: none;
}
.q-link:hover { background: var(--bg-soft); color: var(--ink); }
.q-link.is-current { color: var(--ink); background: var(--bronze-soft); }
.q-status {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--line); flex: none; transition: background .2s;
}
.q-link.answered-correct .q-status { background: var(--teal); }
.q-link.answered-wrong   .q-status { background: #e05c5c; }
.q-link.revealed         .q-status { background: var(--bronze); }
.q-type-tag {
  font-size: 10px; font-weight: 600; letter-spacing: .04em;
  text-transform: uppercase; color: var(--mute); margin-left: auto;
}

/* ── Quiz page ── */
.quiz-page { display: none; padding: 2.5rem 2.5rem 1.5rem; max-width: 760px; }
.quiz-page.is-active { display: block; }

.q-meta {
  display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem;
}
.q-num { font-size: 12px; font-weight: 600; color: var(--mute); letter-spacing: .06em; text-transform: uppercase; }
.q-badge {
  font-size: 10px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase;
  padding: 2px 9px; border-radius: 4px;
}
.badge-mcq       { background: var(--teal-soft);   color: var(--teal);   border: 1px solid var(--teal-edge); }
.badge-truefalse { background: var(--bronze-soft);  color: var(--bronze); border: 1px solid var(--bronze-edge); }
.badge-open      { background: var(--bg-soft);      color: var(--mute);   border: 1px solid var(--line); }

.q-text {
  font-size: 1.1rem; font-weight: 500; color: var(--ink);
  line-height: 1.6; margin-bottom: 2rem;
}

/* ── MCQ options ── */
.q-options { display: flex; flex-direction: column; gap: 10px; margin-bottom: 1.5rem; }
.q-opt {
  display: flex; align-items: flex-start; gap: 14px;
  padding: 12px 16px; border-radius: 8px; cursor: pointer;
  border: 1px solid var(--line); background: var(--bg-elev);
  font: inherit; font-size: 0.93rem; color: var(--body);
  text-align: left; transition: border-color .15s, background .15s;
}
.q-opt:hover:not(:disabled) { border-color: var(--bronze-edge); background: var(--bronze-soft); color: var(--ink); }
.q-opt .opt-letter {
  flex: none; width: 24px; height: 24px; border-radius: 50%;
  display: grid; place-items: center;
  font-size: 11px; font-weight: 700; letter-spacing: .04em;
  background: var(--bg-soft); color: var(--mute);
  border: 1px solid var(--line);
}
.q-opt.correct  { border-color: var(--teal);  background: var(--teal-soft);   color: var(--ink); }
.q-opt.correct  .opt-letter { background: var(--teal);  color: #fff; border-color: var(--teal); }
.q-opt.wrong    { border-color: #e05c5c; background: rgba(224,92,92,.1); color: var(--ink); }
.q-opt.wrong    .opt-letter { background: #e05c5c; color: #fff; border-color: #e05c5c; }
.q-opt.revealed { border-color: var(--teal); background: var(--teal-soft); }
.q-opt:disabled { cursor: default; }

/* ── True/False buttons ── */
.tf-buttons { display: flex; gap: 12px; margin-bottom: 1.5rem; }
.tf-btn {
  flex: 1; padding: 16px; border-radius: 10px; cursor: pointer;
  font: inherit; font-size: 1rem; font-weight: 600;
  border: 1px solid var(--line); background: var(--bg-elev); color: var(--body);
  transition: border-color .15s, background .15s;
}
.tf-btn:hover:not(:disabled) { border-color: var(--bronze-edge); background: var(--bronze-soft); color: var(--ink); }
.tf-btn.correct  { border-color: var(--teal);  background: var(--teal-soft);         color: var(--ink); }
.tf-btn.wrong    { border-color: #e05c5c;       background: rgba(224,92,92,.1);       color: var(--ink); }
.tf-btn.revealed { border-color: var(--teal);  background: var(--teal-soft); }
.tf-btn:disabled { cursor: default; }

/* ── Open reveal ── */
.reveal-btn {
  padding: 10px 22px; border-radius: 8px; cursor: pointer;
  font: inherit; font-size: 0.9rem; font-weight: 600;
  border: 1px solid var(--bronze-edge); background: var(--bronze-soft); color: var(--bronze);
  transition: opacity .15s;
  margin-bottom: 1rem;
}
.reveal-btn:hover { opacity: .8; }
.reveal-btn:disabled { opacity: .4; cursor: default; }

/* ── Feedback / explanation ── */
.q-feedback {
  margin-top: 1rem; padding: 14px 16px; border-radius: 8px;
  border-left: 3px solid var(--teal); background: var(--teal-soft);
  font-size: 0.88rem; line-height: 1.6; color: var(--body);
  display: none;
}
.q-feedback.show { display: block; }
.q-feedback.wrong-fb { border-color: #e05c5c; background: rgba(224,92,92,.08); }
.q-feedback .result-line {
  font-weight: 700; color: var(--teal); margin-bottom: 6px; font-size: 0.85rem;
}
.q-feedback.wrong-fb .result-line { color: #e05c5c; }
.q-feedback .result-line.open-line { color: var(--bronze); }
.q-feedback p  { margin: 4px 0; }
.q-feedback ul, .q-feedback ol { padding-left: 1.4rem; margin: 4px 0; }
.q-feedback li { margin-bottom: 3px; }
.q-feedback pre { background: var(--bg-code, #111); color: var(--code-ink, #ddd);
                  padding: .7rem 1rem; border-radius: 6px; font-size: .8rem;
                  overflow-x: auto; margin: .5rem 0; }
.q-feedback code { font-family: var(--mono, monospace); font-size: .85em; }
.display-math { text-align: center; margin: .6rem 0; }

/* ── Pager ── */
.q-pager {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 2rem; padding-top: 1rem;
  border-top: 1px solid var(--line-soft);
}
.q-pager a, .q-pager button {
  display: flex; flex-direction: column; padding: 8px 14px;
  border-radius: 8px; border: 1px solid var(--line);
  background: var(--bg-elev); color: var(--body);
  font: inherit; cursor: pointer; text-decoration: none;
  transition: border-color .15s, background .15s;
  min-width: 110px;
}
.q-pager a:hover, .q-pager button:hover { border-color: var(--bronze-edge); background: var(--bronze-soft); color: var(--ink); }
.q-pager .dir  { font-size: 11px; color: var(--mute); margin-bottom: 2px; }
.q-pager .prev { align-items: flex-start; }
.q-pager .next { align-items: flex-end; }
.q-pager .spacer { flex: 1; }
"""

SCRIPT = r"""
/* ── Per-project state (must be declared before IIFEs run) ── */
const STATE = {};  // { projectKey: { answers: {qId: 'correct'|'wrong'|'revealed'}, current: idx } }
let ACTIVE_PROJECT = null;

/*THEME_PICKER_JS*/

/*FONT_JS*/

/*TAB_JS*/

function getState(key) {
  if (!STATE[key]) STATE[key] = { answers: {}, current: 0 };
  return STATE[key];
}

/* ── Score + progress update ── */
function updateHUD(key) {
  const pages = Array.from(document.querySelectorAll(`.quiz-page[data-project="${key}"]`));
  const s = getState(key);
  const total    = pages.length;
  const answered = Object.keys(s.answers).length;
  const correct  = Object.values(s.answers).filter(v => v === 'correct').length;

  const chip = document.querySelector(`.score-chip[data-project="${key}"]`);
  if (chip) chip.textContent = `${correct} / ${total}`;

  const fill = document.querySelector(`.progress-fill[data-project="${key}"]`);
  if (fill) fill.style.width = total ? (answered / total * 100) + '%' : '0%';
}

/* ── Per-project activation (called by shared tab system) ── */
function onProjectActivated(key) {
  document.querySelectorAll('.article[data-project]').forEach(a => { a.hidden = a.dataset.project !== key; });
  document.querySelectorAll('.sidebar .q-list[data-project]').forEach(n => { n.hidden = n.dataset.project !== key; });
  document.querySelectorAll('.score-chip[data-project]').forEach(c => { c.hidden = c.dataset.project !== key; });
  document.querySelectorAll('.progress-fill[data-project]').forEach(f => { f.hidden = f.dataset.project !== key; });
  ACTIVE_PROJECT = key;
  updateHUD(key);
}

/* ── Navigate to question ── */
function goToQuestion(key, idx) {
  const pages = Array.from(document.querySelectorAll(`.quiz-page[data-project="${key}"]`));
  if (!pages[idx]) return;
  pages.forEach((p, i) => p.classList.toggle('is-active', i === idx));
  getState(key).current = idx;

  // Update sidebar highlight
  document.querySelectorAll(`.q-link[data-project="${key}"]`).forEach(l => {
    l.classList.toggle('is-current', parseInt(l.dataset.idx, 10) === idx);
  });

  // Show/hide pager buttons based on position
  const active = pages[idx];
  if (active) {
    const prevBtn = active.querySelector('.pager-btn[data-dir="prev"]');
    const nextBtn = active.querySelector('.pager-btn[data-dir="next"]');
    if (prevBtn) prevBtn.style.visibility = idx === 0 ? 'hidden' : '';
    if (nextBtn) nextBtn.style.visibility = idx === pages.length - 1 ? 'hidden' : '';
  }

  window.scrollTo(0, 0);
}

/* ── New Test: shuffle questions + reset state ── */
function newTest(key) {
  const s = getState(key);
  s.answers = {};
  s.current = 0;

  // Collect pages and shuffle (Fisher-Yates)
  const article = document.querySelector(`.article[data-project="${key}"]`);
  const pages = Array.from(article.querySelectorAll('.quiz-page'));
  for (let i = pages.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [pages[i], pages[j]] = [pages[j], pages[i]];
  }
  // Re-append in shuffled order, reset active state
  pages.forEach(p => {
    p.classList.remove('is-active');
    article.appendChild(p);
  });

  // Re-order sidebar links to match, reset status classes, update data-idx
  const qlist = document.querySelector(`.q-list[data-project="${key}"]`);
  pages.forEach((p, newPos) => {
    const qid = p.dataset.qid;
    const link = qlist.querySelector(`.q-link[data-qid="${qid}"]`);
    if (link) {
      link.dataset.idx = newPos;
      link.className = 'q-link';
      link.setAttribute('data-project', key);
      link.setAttribute('data-qid', qid);
      qlist.appendChild(link);
    }
  });

  updateHUD(key);
  goToQuestion(key, 0);
}

/* ── Sidebar clicks ── */
document.querySelectorAll('.q-link[data-project]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    goToQuestion(a.dataset.project, parseInt(a.dataset.idx, 10));
  });
});

/* ── Pager buttons ── */
document.querySelectorAll('.pager-btn[data-dir]').forEach(btn => {
  btn.addEventListener('click', e => {
    e.preventDefault();
    const key = btn.dataset.project;
    const pages = Array.from(document.querySelectorAll(`.quiz-page[data-project="${key}"]`));
    const cur = getState(key).current;
    if (btn.dataset.dir === 'prev' && cur > 0) goToQuestion(key, cur - 1);
    if (btn.dataset.dir === 'next' && cur < pages.length - 1) goToQuestion(key, cur + 1);
  });
});

/* ── New Test button ── */
document.getElementById('newTestBtn').addEventListener('click', () => {
  if (ACTIVE_PROJECT) newTest(ACTIVE_PROJECT);
});

/* ── Keyboard nav ── */
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  const article = document.querySelector('.article:not([hidden])');
  if (!article) return;
  const key = article.dataset.project;
  const pages = Array.from(article.querySelectorAll('.quiz-page'));
  const cur = pages.findIndex(p => p.classList.contains('is-active'));
  if (e.key === 'ArrowRight' && cur < pages.length - 1) { e.preventDefault(); goToQuestion(key, cur + 1); }
  if (e.key === 'ArrowLeft'  && cur > 0)                { e.preventDefault(); goToQuestion(key, cur - 1); }
});

/* ── MCQ answer ── */
document.querySelectorAll('.q-opt').forEach(btn => {
  btn.addEventListener('click', () => {
    const page    = btn.closest('.quiz-page');
    const key     = page.dataset.project;
    const qId     = page.dataset.qid;
    if (getState(key).answers[qId]) return;   // already answered

    const correct = page.dataset.correct;
    const chosen  = btn.dataset.opt;
    const isRight = chosen === correct;

    // Disable all options
    page.querySelectorAll('.q-opt').forEach(b => {
      b.disabled = true;
      if (b.dataset.opt === correct) b.classList.add('correct');
      else if (b.dataset.opt === chosen && !isRight) b.classList.add('wrong');
    });

    // Show feedback
    const fb = page.querySelector('.q-feedback');
    if (fb) {
      fb.classList.add('show');
      if (!isRight) fb.classList.add('wrong-fb');
    }

    getState(key).answers[qId] = isRight ? 'correct' : 'wrong';
    markSidebarQ(key, qId, getState(key).answers[qId]);
    updateHUD(key);
  });
});

/* ── True/False answer ── */
document.querySelectorAll('.tf-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const page    = btn.closest('.quiz-page');
    const key     = page.dataset.project;
    const qId     = page.dataset.qid;
    if (getState(key).answers[qId]) return;

    const correct = page.dataset.correct;  // 'true' or 'false'
    const chosen  = btn.dataset.ans;
    const isRight = chosen === correct;

    page.querySelectorAll('.tf-btn').forEach(b => {
      b.disabled = true;
      if (b.dataset.ans === correct) b.classList.add('correct');
      else if (b.dataset.ans === chosen && !isRight) b.classList.add('wrong');
    });

    const fb = page.querySelector('.q-feedback');
    if (fb) { fb.classList.add('show'); if (!isRight) fb.classList.add('wrong-fb'); }

    getState(key).answers[qId] = isRight ? 'correct' : 'wrong';
    markSidebarQ(key, qId, getState(key).answers[qId]);
    updateHUD(key);
  });
});

/* ── Open reveal ── */
document.querySelectorAll('.reveal-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const page = btn.closest('.quiz-page');
    const key  = page.dataset.project;
    const qId  = page.dataset.qid;
    if (getState(key).answers[qId]) return;

    btn.disabled = true;
    const fb = page.querySelector('.q-feedback');
    if (fb) fb.classList.add('show');

    getState(key).answers[qId] = 'revealed';
    markSidebarQ(key, qId, 'revealed');
    updateHUD(key);
  });
});

/* ── Sidebar status update ── */
function markSidebarQ(key, qId, status) {
  const link = document.querySelector(`.q-link[data-project="${key}"][data-qid="${qId}"]`);
  if (!link) return;
  link.classList.remove('answered-correct','answered-wrong','revealed');
  if (status === 'correct')  link.classList.add('answered-correct');
  if (status === 'wrong')    link.classList.add('answered-wrong');
  if (status === 'revealed') link.classList.add('revealed');
}

/* ── Init pager visibility on first load ── */
(function () {
  document.querySelectorAll('.article[data-project]').forEach(article => {
    const key = article.dataset.project;
    const pages = Array.from(article.querySelectorAll('.quiz-page'));
    const cur = getState(key).current;
    const active = pages[cur];
    if (active) {
      const prevBtn = active.querySelector('.pager-btn[data-dir="prev"]');
      const nextBtn = active.querySelector('.pager-btn[data-dir="next"]');
      if (prevBtn) prevBtn.style.visibility = cur === 0 ? 'hidden' : '';
      if (nextBtn) nextBtn.style.visibility = cur === pages.length - 1 ? 'hidden' : '';
    }
  });
})();

/* ── Mobile menu ── */
(function () {
  const btn     = document.getElementById('menuBtn');
  const sidebar = document.getElementById('sidebar');
  if (!btn || !sidebar) return;
  btn.addEventListener('click', () => sidebar.classList.toggle('is-open'));
  document.addEventListener('click', e => {
    if (!sidebar.contains(e.target) && !btn.contains(e.target)) sidebar.classList.remove('is-open');
  });
})();
window.addEventListener('load', () => { if (typeof hljs !== 'undefined') hljs.highlightAll(); });
"""


# ── HTML rendering ────────────────────────────────────────────────────────────

BADGE_CLASS = {'mcq': 'badge-mcq', 'truefalse': 'badge-truefalse', 'open': 'badge-open'}
BADGE_LABEL = {'mcq': 'MCQ', 'truefalse': 'True / False', 'open': 'Open'}


def render_question_page(q, key, total):
    qtype = q['type']
    badge_cls = BADGE_CLASS.get(qtype, 'badge-open')
    badge_lbl = BADGE_LABEL.get(qtype, 'Open')
    correct    = html_lib.escape(q['correct'])

    lines = [
        f'<div class="quiz-page" data-project="{key}" data-idx="{q["n"]-1}" '
        f'data-qid="{q["id"]}" data-correct="{correct}">',
        f'  <div class="q-meta">',
        f'    <span class="q-num">Q{q["n"]} / {total}</span>',
        f'    <span class="q-badge {badge_cls}">{badge_lbl}</span>',
        f'  </div>',
        f'  <div class="q-text">{inline_fmt(q["text"])}</div>',
    ]

    # Interaction area
    if qtype == 'mcq':
        lines.append('  <div class="q-options">')
        for letter, text in q['options']:
            lines.append(
                f'    <button class="q-opt" data-opt="{letter}">'
                f'<span class="opt-letter">{letter}</span>'
                f'<span>{inline_fmt(text)}</span></button>'
            )
        lines.append('  </div>')

    elif qtype == 'truefalse':
        lines.append('  <div class="tf-buttons">')
        lines.append('    <button class="tf-btn" data-ans="true">True</button>')
        lines.append('    <button class="tf-btn" data-ans="false">False</button>')
        lines.append('  </div>')

    elif qtype == 'open':
        lines.append('  <button class="reveal-btn">Reveal Answer</button>')

    # Feedback / explanation block
    fb_class = 'q-feedback'
    if qtype in ('mcq', 'truefalse'):
        result_line = ''
        if q['correct']:
            correct_display = q['correct']
            if qtype == 'truefalse':
                correct_display = correct_display.capitalize()
            result_line = f'<div class="result-line">✓ Correct: {html_lib.escape(correct_display)}</div>'
        explanation = q.get('explanation_html', '')
        if result_line or explanation:
            lines.append(f'  <div class="{fb_class}">{result_line}{explanation}</div>')
    else:
        answer = q.get('answer_html', '')
        if answer:
            lines.append(f'  <div class="{fb_class}"><div class="result-line open-line">Answer</div>{answer}</div>')

    # Pager
    lines.append('  <nav class="q-pager">')
    lines.append(f'    <button class="prev pager-btn" data-project="{key}" data-dir="prev">'
                 f'<span class="dir">← Previous</span></button>')
    lines.append('    <span class="spacer"></span>')
    lines.append(f'    <button class="next pager-btn" data-project="{key}" data-dir="next">'
                 f'<span class="dir">Next →</span></button>')
    lines.append('  </nav>')
    lines.append('</div>')
    return '\n'.join(lines)


def render_sidebar_qlist(doc, key):
    lines = [f'<div class="q-list" data-project="{key}" hidden>']
    for q in doc['questions']:
        type_tag = BADGE_LABEL.get(q['type'], '')
        lines.append(
            f'  <a class="q-link" data-project="{key}" data-idx="{q["n"]-1}" '
            f'data-qid="{q["id"]}" href="#">'
            f'<span class="q-status"></span>'
            f'Q{q["n"]}'
            f'<span class="q-type-tag">{type_tag}</span>'
            f'</a>'
        )
    lines.append('</div>')
    return '\n'.join(lines)


def render_article(doc, key):
    total  = len(doc['questions'])
    lines  = [f'<article class="article" data-project="{key}" hidden>']
    for q in doc['questions']:
        page = render_question_page(q, key, total)
        if q['n'] == 1:
            page = page.replace('class="quiz-page"', 'class="quiz-page is-active"', 1)
        lines.append(page)
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

    score_chips = ''.join(
        f'<span class="score-chip" data-project="{key}" hidden>0 / {len(doc["questions"])}</span>'
        for key, doc in projects
    )
    progress_fills = ''.join(
        f'<div class="progress-fill" data-project="{key}" hidden></div>'
        for key, doc in projects
    )
    sidebar_html  = '\n'.join(render_sidebar_qlist(doc, key) for key, doc in projects)
    articles_html = '\n'.join(render_article(doc, key)       for key, doc in projects)

    nav_html  = shared.session_nav_html(len(projects))
    font_html = shared.font_picker_html()

    script = (SCRIPT
              .replace('/*THEME_PICKER_JS*/', shared.theme_picker_js())
              .replace('/*FONT_JS*/',         shared.FONT_JS)
              .replace('/*TAB_JS*/',          shared.tab_js(proj_keys, proj_labels,
                                                            'gaia-coeus-tab', 'COEUS')))

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coeus — Quiz</title>
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
    <span class="brand-name">COEUS</span>
    <span class="brand-issue">Quiz</span>
  </a>
  {nav_html}
  <div class="topbar-actions">
    {score_chips}
    <button class="new-test-btn" id="newTestBtn" title="Shuffle questions and reset score">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/>
        <polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>
      </svg>
      New Test
    </button>
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

<div class="progress-wrap">
  {progress_fills}
</div>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="side-label" id="sideLabel">COEUS · Quiz</div>
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

    output_file = None; themes_src = None; md_files = []
    i = 0
    while i < len(args):
        if args[i] in ('-o','--output') and i+1 < len(args):
            output_file = args[i+1]; i += 2
        elif args[i] == '--themes' and i+1 < len(args):
            themes_src = args[i+1]; i += 2
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
        output_file = script_dir.parent / 'STUDY PATH' / 'quiz.html'
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
            print('Warning: themes not found.')

    projects = []; tab_labels = {}; seen = {}
    for path in md_paths:
        print(f'Parsing {path.name}…')
        key = session_key(path)
        if key in seen: seen[key] += 1; key = f'{key}-{seen[key]}'
        else: seen[key] = 1
        doc = parse_coeus_md(path, prefix=key)
        tab_labels[key] = tab_label(path)
        projects.append((key, doc))

    print('Rendering HTML…')
    html_out = render_html(projects, tab_labels, themes_dst)
    output_file.write_text(html_out, encoding='utf-8')
    q_total = sum(len(d['questions']) for _, d in projects)
    print(f'✓  Written → {output_file}')
    print(f'   {len(projects)} session(s), {q_total} questions.')


if __name__ == '__main__':
    main()
