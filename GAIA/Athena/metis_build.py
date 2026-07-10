#!/usr/bin/env python3
"""
metis_build.py — Builds flashcards.html from Metis .txt files.

Input format (tab-separated, one card per line):
    {number}\\t{front}\\t{back}    (three columns — leading number from Anki export)
    {front}\\t{back}               (two columns)

Usage:
    python3 metis_build.py "session - flashcards.txt" ...
    python3 metis_build.py *.txt --themes /path/to/themes -o output.html
"""

import sys, re, json, shutil, html as html_lib
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import shared


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text):
    s = re.sub(r'[^\w\s-]', '', text)
    s = re.sub(r'[\s_]+', '-', s).strip('-').lower()
    return s or 'deck'


def tab_label(path):
    stem = Path(path).stem
    name = re.sub(r'\s*-\s*flashcards?.*$', '', stem, flags=re.IGNORECASE).strip()
    return name.title() if name else stem


def session_key(path):
    return slugify(tab_label(path)) or 'session'


# ── Parser ────────────────────────────────────────────────────────────────────

def parse_metis_txt(path, prefix):
    """Parse a tab-separated Metis flashcard file. Returns list of card dicts."""
    cards = []
    for raw_line in Path(path).read_text(encoding='utf-8').splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) >= 3:
            # {number}\t{front}\t{back}
            front = parts[1].strip()
            back  = '\t'.join(parts[2:]).strip()
        elif len(parts) == 2:
            front = parts[0].strip()
            back  = parts[1].strip()
        else:
            continue
        if not front or not back:
            continue
        n = len(cards) + 1
        cards.append({'n': n, 'id': f'{prefix}-c{n}', 'front': front, 'back': back})
    return cards


# ── Static assets ─────────────────────────────────────────────────────────────

BRAND_SVG = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="3" y="4" width="26" height="17" rx="2.5" stroke="currentColor" stroke-width="1.7" fill="none"/>
  <line x1="3" y1="11.5" x2="29" y2="11.5" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.45"/>
  <line x1="11" y1="4" x2="11" y2="11.5" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.45"/>
  <line x1="13" y1="16" x2="23" y2="16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="13" y1="19.5" x2="20" y2="19.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M10 25 L16 28 L22 25" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-opacity="0.6"/>
</svg>'''

SHUFFLE_SVG = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/></svg>'
FILTER_SVG  = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="6" x2="2" y2="6"/><line x1="17" y1="12" x2="7" y2="12"/><line x1="12" y1="18" x2="12" y2="18"/></svg>'
RESET_SVG   = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 .49-3.5"/></svg>'

INLINE_CSS = """
/* ── Progress bar ── */
.progress-wrap {
  position: sticky; top: var(--topbar-h); z-index: 9;
  height: 3px; background: var(--line-soft);
}
.progress-fill { height: 100%; width: 0%; background: var(--teal); transition: width .3s ease; }

/* ── Score chip ── */
.score-chip {
  font-size: 13px; font-weight: 600; color: var(--ink);
  background: var(--bg-soft); border: 1px solid var(--line);
  border-radius: 999px; padding: 4px 14px;
  white-space: nowrap; flex: none;
}

/* ── Theme picker ── */
.theme-picker { display: flex; align-items: center; gap: 8px; }
.theme-label { font-size: 11px; color: var(--mute); text-transform: uppercase; letter-spacing: .08em; }
.theme-picker button {
  width: 20px; height: 20px; border-radius: 50%; cursor: pointer;
  border: 2px solid transparent; padding: 0;
  transition: border-color .15s, transform .12s;
}
.theme-picker button:hover { transform: scale(1.15); }
.theme-picker button[aria-pressed="true"] { border-color: var(--bronze); }
.theme-picker button[data-theme="folio"]    { background: #ECE6D4; }
.theme-picker button[data-theme="deepdive"] { background: #2B2D31; border-color: var(--line); }

/* ── Sidebar card list ── */
.c-list { padding: .5rem 0; }
.c-link {
  display: flex; align-items: center; gap: 9px;
  padding: 5px 16px 5px 20px; font-size: 12.5px; color: var(--body);
  cursor: pointer; transition: background .12s, color .12s;
  border: none; background: none; width: 100%; text-align: left; font-family: inherit;
}
.c-link:hover { background: var(--bg-soft); color: var(--ink); }
.c-link.is-current { color: var(--ink); background: var(--bronze-soft); }
.c-status {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--line); flex: none; transition: background .2s;
}
.c-link.is-known  .c-status { background: var(--teal); }
.c-link.is-missed .c-status { background: #e05c5c; }
.c-num { font-size: 10.5px; color: var(--mute); font-family: var(--mono, monospace); flex: none; min-width: 26px; }
.c-front { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; min-width: 0; }

/* ── Deck layout ── */
.deck-wrap { display: none; padding: 2.5rem 2.5rem 3rem; max-width: 800px; }
.deck-wrap.is-active { display: block; }

/* ── 3D Card ── */
.card-scene {
  width: 100%;
  height: 300px;
  perspective: 1200px;
  cursor: pointer;
  margin-bottom: 1.25rem;
  user-select: none;
}
.card-inner {
  width: 100%; height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .48s cubic-bezier(.4, 0, .2, 1);
}
.card-scene.is-flipped .card-inner { transform: rotateY(180deg); }

.card-face {
  position: absolute; inset: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border-radius: 14px;
  border: 1.5px solid var(--line);
  background: var(--bg-elev);
  display: flex; flex-direction: column;
  overflow: hidden;
  transition: border-color .2s, box-shadow .2s;
}
.card-scene:hover:not(.is-flipped) .card-face.card-front-face {
  border-color: var(--bronze-edge);
  box-shadow: 0 4px 24px rgba(0,0,0,.08);
}
.card-scene.is-flipped:hover .card-face.card-back-face {
  border-color: var(--teal-edge);
  box-shadow: 0 4px 24px rgba(0,0,0,.08);
}

.card-back-face { transform: rotateY(180deg); }

/* Front: vertically centred */
.card-front-face { justify-content: center; align-items: center; padding: 32px 44px; }
/* Back: top-aligned, scrollable */
.card-back-face { justify-content: flex-start; align-items: flex-start; padding: 28px 36px; overflow-y: auto; }

.card-label {
  font-size: 9.5px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase;
  color: var(--mute); margin-bottom: 14px; flex: none;
}
.card-front-face .card-label { align-self: flex-start; }

.card-text {
  font-size: 1.08rem; color: var(--ink); line-height: 1.7; width: 100%;
}
.card-front-face .card-text { text-align: center; }
.card-back-face  .card-text { text-align: left; font-size: .95rem; }

.card-tap-hint {
  margin-top: auto; padding-top: 12px; align-self: flex-end;
  font-size: 10.5px; color: var(--faint, var(--mute)); flex: none;
}

/* ── Flip hint ── */
.flip-hint {
  font-size: 12px; color: var(--mute); text-align: center;
  margin-bottom: 1.2rem;
}
.flip-hint .kbd { font-family: var(--mono, monospace); font-size: 10.5px; padding: 1px 6px; border-radius: 4px; border: 1px solid var(--line); background: var(--bg-soft); color: var(--mute); }

/* ── Feedback buttons ── */
.feedback-btns {
  display: none;
  flex-direction: row; gap: 12px; justify-content: center;
  margin-bottom: 1.2rem;
}
.feedback-btns.show { display: flex; }
.fb-btn {
  flex: 1; max-width: 220px; padding: 12px 20px; border-radius: 10px; cursor: pointer;
  font: inherit; font-size: .92rem; font-weight: 700;
  transition: opacity .15s, transform .1s; border: 1.5px solid;
}
.fb-btn:active { transform: scale(.97); }
.fb-btn.know { border-color: var(--teal);  background: var(--teal-soft);        color: var(--teal); }
.fb-btn.know:hover { opacity: .8; }
.fb-btn.miss { border-color: #e05c5c; background: rgba(224,92,92,.1);  color: #e05c5c; }
.fb-btn.miss:hover { opacity: .8; }

/* ── Card nav bar ── */
.card-nav {
  display: flex; align-items: center; justify-content: space-between; gap: 12px;
}
.nav-btn {
  display: flex; align-items: center; gap: 6px;
  padding: 9px 20px; border-radius: 8px; cursor: pointer;
  font: inherit; font-size: .85rem; font-weight: 600; color: var(--body);
  border: 1px solid var(--line); background: var(--bg-elev);
  transition: border-color .15s, background .15s, color .15s;
}
.nav-btn:hover:not(:disabled) { border-color: var(--bronze-edge); background: var(--bronze-soft); color: var(--ink); }
.nav-btn:disabled { opacity: .32; cursor: default; }
.card-pos { font-size: 13px; color: var(--mute); text-align: center; min-width: 72px; font-family: var(--mono, monospace); }

/* ── Deck controls ── */
.deck-controls { display: flex; gap: 8px; margin-top: 1.6rem; flex-wrap: wrap; }
.ctrl-btn {
  display: flex; align-items: center; gap: 6px;
  padding: 6px 14px; border-radius: 999px; cursor: pointer;
  font: inherit; font-size: 11.5px; font-weight: 600; letter-spacing: .04em; text-transform: uppercase;
  border: 1px solid var(--line); background: transparent; color: var(--mute);
  transition: border-color .15s, color .15s, background .15s;
}
.ctrl-btn:hover { border-color: var(--bronze-edge); color: var(--body); background: var(--bronze-soft); }
.ctrl-btn.is-active { border-color: var(--teal-edge); color: var(--teal); background: var(--teal-soft); }

/* ── Keyboard hints ── */
.kbd-hint {
  margin-top: 2rem; padding-top: 1rem;
  border-top: 1px solid var(--line-soft);
  display: flex; flex-wrap: wrap; gap: 10px 22px;
}
.kbd-item { display: flex; align-items: center; gap: 8px; font-size: 11.5px; color: var(--mute); }
.kbd-item .kbd { font-family: var(--mono, monospace); font-size: 10px; padding: 2px 7px; border-radius: 4px; border: 1px solid var(--line); background: var(--bg-soft); color: var(--mute); }

/* ── All-done banner ── */
.all-done {
  margin-top: 1.8rem; padding: 18px 22px; border-radius: 10px;
  border: 1.5px solid var(--teal-edge); background: var(--teal-soft);
  display: none;
}
.all-done.show { display: block; }
.all-done-title { font-size: 1rem; font-weight: 700; color: var(--ink); margin-bottom: 3px; }
.all-done-sub { font-size: .875rem; color: var(--body); }

/* ── Math display ── */
.display-math { text-align: center; margin: .5rem 0; }

/* ── Responsive ── */
@media (max-width: 660px) {
  .deck-wrap { padding: 1.5rem 1.25rem 2rem; }
  .card-scene { height: 260px; }
  .card-front-face { padding: 24px 28px; }
  .card-back-face  { padding: 20px 24px; }
  .card-text { font-size: 1rem; }
  .card-back-face .card-text { font-size: .9rem; }
}
"""

# ── JavaScript ────────────────────────────────────────────────────────────────

SCRIPT = r"""
/*THEME_PICKER_JS*/

/*FONT_JS*/

/* ── Card data ── */
/*DECKS_PLACEHOLDER*/

/* ── MathJax typeset helper ── */
function typesetEl(el) {
  if (!window.MathJax || !MathJax.typesetPromise) return;
  MathJax.typesetClear([el]);
  MathJax.typesetPromise([el]).catch(() => {});
}

/* ── State ── */
const STATE = {};
function getState(key) {
  if (!STATE[key]) {
    const deck = DECKS[key] || [];
    STATE[key] = {
      order:      deck.map((_, i) => i),
      currentIdx: 0,
      known:      new Set(),
      missed:     new Set(),
      filterMode: 'all',
      isFlipped:  false,
    };
  }
  return STATE[key];
}

/* ── HUD (progress bar + score chip) ── */
function updateHUD(key) {
  const s    = getState(key);
  const deck = DECKS[key] || [];
  const seen = s.known.size + s.missed.size;
  const chip = document.querySelector(`.score-chip[data-project="${key}"]`);
  if (chip) chip.textContent = `${s.known.size} / ${deck.length} known`;
  const fill = document.querySelector(`.progress-fill[data-project="${key}"]`);
  if (fill) fill.style.width = deck.length ? (seen / deck.length * 100) + '%' : '0%';
}

/* ── Render current card ── */
function renderCard(key) {
  const s    = getState(key);
  const deck = DECKS[key] || [];
  if (!deck.length || !s.order.length) return;

  const cardIdx = s.order[s.currentIdx];
  const card    = deck[cardIdx];
  if (!card) return;

  // Reset flip
  const scene = document.getElementById('scene-' + key);
  if (scene) { scene.classList.remove('is-flipped'); s.isFlipped = false; }

  // Update text
  const frontEl = document.getElementById('front-text-' + key);
  const backEl  = document.getElementById('back-text-' + key);
  if (frontEl) { frontEl.textContent = card.front; typesetEl(frontEl); }
  if (backEl)  { backEl.textContent  = card.back;  typesetEl(backEl);  }

  // Show hint, hide feedback
  const hintEl = document.getElementById('flip-hint-' + key);
  const feedEl = document.getElementById('feedback-' + key);
  if (hintEl) hintEl.style.display = '';
  if (feedEl) feedEl.classList.remove('show');

  // Nav buttons
  const wrap = document.querySelector('.deck-wrap[data-project="' + key + '"]');
  if (wrap) {
    const pb = wrap.querySelector('.prev-btn');
    const nb = wrap.querySelector('.next-btn');
    if (pb) pb.disabled = s.currentIdx === 0;
    if (nb) nb.disabled = s.currentIdx >= s.order.length - 1;
  }

  // Position counter
  const posEl = document.getElementById('card-pos-' + key);
  if (posEl) posEl.textContent = (s.currentIdx + 1) + ' / ' + s.order.length;

  // Sidebar highlight
  document.querySelectorAll('.c-link[data-project="' + key + '"]').forEach(l => {
    l.classList.toggle('is-current', parseInt(l.dataset.cardIdx, 10) === cardIdx);
  });
  // Scroll current card into sidebar view
  const curLink = document.querySelector('.c-link[data-project="' + key + '"].is-current');
  if (curLink) curLink.scrollIntoView({ block: 'nearest' });

  // All-done banner
  const allDone = document.getElementById('all-done-' + key);
  if (allDone) {
    const complete = deck.every((_, i) => s.known.has(i) || s.missed.has(i));
    allDone.classList.toggle('show', complete && s.currentIdx === s.order.length - 1);
  }
}

/* ── Flip card ── */
function flipCard(key) {
  const s    = getState(key);
  const scene = document.getElementById('scene-' + key);
  if (!scene) return;
  s.isFlipped = !s.isFlipped;
  scene.classList.toggle('is-flipped', s.isFlipped);
  if (s.isFlipped) {
    const hintEl = document.getElementById('flip-hint-' + key);
    const feedEl = document.getElementById('feedback-' + key);
    if (hintEl) hintEl.style.display = 'none';
    if (feedEl) feedEl.classList.add('show');
  }
}

/* ── Mark known / missed ── */
function markCard(key, verdict) {
  const s       = getState(key);
  const cardIdx = s.order[s.currentIdx];
  if (verdict === 'know') { s.known.add(cardIdx);  s.missed.delete(cardIdx); }
  else                    { s.missed.add(cardIdx);  s.known.delete(cardIdx);  }
  const link = document.querySelector('.c-link[data-project="' + key + '"][data-card-idx="' + cardIdx + '"]');
  if (link) {
    link.classList.remove('is-known', 'is-missed');
    link.classList.add(verdict === 'know' ? 'is-known' : 'is-missed');
  }
  updateHUD(key);
  if (s.currentIdx < s.order.length - 1) { s.currentIdx++; renderCard(key); }
  else renderCard(key);
}

/* ── Navigation ── */
function goIdx(key, idx) {
  const s = getState(key);
  if (idx < 0 || idx >= s.order.length) return;
  s.currentIdx = idx;
  renderCard(key);
}

/* ── Shuffle (Fisher-Yates) ── */
function shuffleDeck(key) {
  const s = getState(key);
  const a = s.order;
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  s.currentIdx = 0;
  renderCard(key);
}

/* ── Filter: Review Misses ── */
function toggleFilter(key) {
  const s    = getState(key);
  const deck = DECKS[key] || [];
  const btn  = document.querySelector('.filter-btn[data-project="' + key + '"]');
  if (s.filterMode === 'all') {
    if (!s.missed.size) return;
    s.filterMode = 'missed';
    s.order      = Array.from(s.missed);
    if (btn) btn.classList.add('is-active');
  } else {
    s.filterMode = 'all';
    s.order      = deck.map((_, i) => i);
    if (btn) btn.classList.remove('is-active');
  }
  s.currentIdx = 0;
  renderCard(key);
}

/* ── Reset ── */
function resetDeck(key) {
  const deck = DECKS[key] || [];
  STATE[key] = {
    order: deck.map((_, i) => i), currentIdx: 0,
    known: new Set(), missed: new Set(),
    filterMode: 'all', isFlipped: false,
  };
  document.querySelectorAll('.c-link[data-project="' + key + '"]').forEach(l => {
    l.classList.remove('is-known', 'is-missed');
  });
  const btn = document.querySelector('.filter-btn[data-project="' + key + '"]');
  if (btn) btn.classList.remove('is-active');
  updateHUD(key);
  renderCard(key);
}

/* ── Active project ── */
let ACTIVE_PROJECT = null;

/* ── Project activated callback (called by shared tab system) ── */
function onProjectActivated(key) {
  ACTIVE_PROJECT = key;
  document.querySelectorAll('.deck-wrap[data-project]').forEach(w =>
    w.classList.toggle('is-active', w.dataset.project === key));
  document.querySelectorAll('.c-list[data-project]').forEach(n =>
    { n.hidden = n.dataset.project !== key; });
  document.querySelectorAll('.score-chip[data-project]').forEach(c =>
    { c.hidden = c.dataset.project !== key; });
  document.querySelectorAll('.progress-fill[data-project]').forEach(f =>
    { f.hidden = f.dataset.project !== key; });
  updateHUD(key);
  renderCard(key);
}

/* ── Card scene click ── */
document.querySelectorAll('.card-scene').forEach(scene => {
  scene.addEventListener('click', () => flipCard(scene.dataset.project));
});

/* ── Know / Miss buttons ── */
document.querySelectorAll('.fb-btn.know').forEach(b => b.addEventListener('click', () => markCard(b.dataset.project, 'know')));
document.querySelectorAll('.fb-btn.miss').forEach(b => b.addEventListener('click', () => markCard(b.dataset.project, 'miss')));

/* ── Nav buttons ── */
document.querySelectorAll('.prev-btn').forEach(b => b.addEventListener('click', () => {
  const s = getState(b.dataset.project); if (s.currentIdx > 0) { s.currentIdx--; renderCard(b.dataset.project); }
}));
document.querySelectorAll('.next-btn').forEach(b => b.addEventListener('click', () => {
  const s = getState(b.dataset.project); if (s.currentIdx < s.order.length - 1) { s.currentIdx++; renderCard(b.dataset.project); }
}));

/* ── Deck control buttons ── */
document.querySelectorAll('.shuffle-btn').forEach(b => b.addEventListener('click', () => shuffleDeck(b.dataset.project)));
document.querySelectorAll('.filter-btn').forEach(b  => b.addEventListener('click', () => toggleFilter(b.dataset.project)));
document.querySelectorAll('.reset-btn').forEach(b   => b.addEventListener('click', () => resetDeck(b.dataset.project)));

/* ── Sidebar card links ── */
document.querySelectorAll('.c-link[data-project]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    const key = a.dataset.project;
    const cidx = parseInt(a.dataset.cardIdx, 10);
    const s = getState(key);
    let pos = s.order.indexOf(cidx);
    if (pos < 0 && s.filterMode !== 'all') {
      toggleFilter(key);
      pos = getState(key).order.indexOf(cidx);
    }
    if (pos >= 0) goIdx(key, pos);
  });
});

/* ── Keyboard shortcuts ── */
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  const key = ACTIVE_PROJECT;
  if (!key) return;
  const s = getState(key);
  switch (e.key) {
    case ' ': case 'Enter':
      e.preventDefault(); flipCard(key); break;
    case 'ArrowRight': case 'l':
      e.preventDefault();
      if (s.currentIdx < s.order.length - 1) { s.currentIdx++; renderCard(key); } break;
    case 'ArrowLeft': case 'h':
      e.preventDefault();
      if (s.currentIdx > 0) { s.currentIdx--; renderCard(key); } break;
    case 'k': case 'K':
      if (s.isFlipped) { e.preventDefault(); markCard(key, 'know'); } break;
    case 'm': case 'M':
      if (s.isFlipped) { e.preventDefault(); markCard(key, 'miss'); } break;
    case 's': case 'S':
      e.preventDefault(); shuffleDeck(key); break;
    case 'r': case 'R':
      e.preventDefault(); resetDeck(key); break;
  }
});

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

/*TAB_JS*/
"""


# ── HTML rendering ────────────────────────────────────────────────────────────

def render_sidebar_clist(cards, key, first=False):
    hidden = '' if first else ' hidden'
    lines  = [f'<div class="c-list" data-project="{key}"{hidden}>']
    for c in cards:
        front_short = c['front'][:55]
        if len(c['front']) > 55:
            front_short += '…'
        front_esc = html_lib.escape(front_short)
        lines.append(
            f'  <button class="c-link" data-project="{key}" data-card-idx="{c["n"]-1}">'
            f'<span class="c-status"></span>'
            f'<span class="c-num">#{c["n"]}</span>'
            f'<span class="c-front">{front_esc}</span>'
            f'</button>'
        )
    lines.append('</div>')
    return '\n'.join(lines)


def render_deck(cards, key, first=False):
    active = ' is-active' if first else ''
    n      = len(cards)
    # First card shown before JS takes over
    first_front = html_lib.escape(cards[0]['front']) if cards else ''
    first_back  = html_lib.escape(cards[0]['back'])  if cards else ''

    return f'''<div class="deck-wrap{active}" data-project="{key}">
  <div class="card-scene" id="scene-{key}" data-project="{key}">
    <div class="card-inner">
      <div class="card-face card-front-face">
        <span class="card-label">Question</span>
        <div class="card-text" id="front-text-{key}">{first_front}</div>
        <span class="card-tap-hint">tap to flip</span>
      </div>
      <div class="card-face card-back-face">
        <span class="card-label">Answer</span>
        <div class="card-text" id="back-text-{key}">{first_back}</div>
      </div>
    </div>
  </div>
  <div class="flip-hint" id="flip-hint-{key}">
    Click card &nbsp;·&nbsp; <kbd class="kbd">Space</kbd> to flip
  </div>
  <div class="feedback-btns" id="feedback-{key}">
    <button class="fb-btn know" data-project="{key}">✓ Know it</button>
    <button class="fb-btn miss" data-project="{key}">✗ Miss</button>
  </div>
  <div class="card-nav">
    <button class="nav-btn prev-btn" data-project="{key}" disabled>← Prev</button>
    <span class="card-pos" id="card-pos-{key}">1 / {n}</span>
    <button class="nav-btn next-btn" data-project="{key}"{' disabled' if n <= 1 else ''}>Next →</button>
  </div>
  <div class="deck-controls">
    <button class="ctrl-btn shuffle-btn" data-project="{key}">{SHUFFLE_SVG} Shuffle</button>
    <button class="ctrl-btn filter-btn"  data-project="{key}">{FILTER_SVG} Review Misses</button>
    <button class="ctrl-btn reset-btn"   data-project="{key}">{RESET_SVG} Reset</button>
  </div>
  <div id="all-done-{key}" class="all-done">
    <div class="all-done-title">Deck complete!</div>
    <div class="all-done-sub">You've reviewed all {n} cards. Shuffle or reset to go again.</div>
  </div>
  <div class="kbd-hint">
    <span class="kbd-item"><span class="kbd">Space</span> Flip</span>
    <span class="kbd-item"><span class="kbd">→</span> Next</span>
    <span class="kbd-item"><span class="kbd">←</span> Prev</span>
    <span class="kbd-item"><span class="kbd">K</span> Know it</span>
    <span class="kbd-item"><span class="kbd">M</span> Miss</span>
    <span class="kbd-item"><span class="kbd">S</span> Shuffle</span>
    <span class="kbd-item"><span class="kbd">R</span> Reset</span>
  </div>
</div>'''


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

    # Score chips (all hidden; onProjectActivated shows the right one)
    score_chips = ''.join(
        f'<span class="score-chip" data-project="{key}" hidden>'
        f'0 / {len(cards)} known</span>'
        for key, cards in projects
    )

    # Progress fills (all hidden)
    progress_fills = ''.join(
        f'<div class="progress-fill" data-project="{key}" hidden></div>'
        for key, _ in projects
    )

    # Sidebar card lists (all hidden; onProjectActivated reveals correct one)
    sidebar_html = '\n'.join(
        render_sidebar_clist(cards, key, first=False)
        for key, cards in projects
    )

    # Decks (none active; onProjectActivated sets is-active)
    decks_html = '\n'.join(
        render_deck(cards, key, first=False)
        for key, cards in projects
    )

    # DECKS JS object
    decks_js_parts = []
    for key, cards in projects:
        cards_data = [{'front': c['front'], 'back': c['back']} for c in cards]
        decks_js_parts.append(f'  {json.dumps(key)}: {json.dumps(cards_data, ensure_ascii=False)}')
    decks_js = 'const DECKS = {\n' + ',\n'.join(decks_js_parts) + '\n};'

    tab_js_code   = shared.tab_js(proj_keys, proj_labels, 'gaia-metis-tab', 'METIS')
    theme_js_code = shared.theme_picker_js()
    script = (SCRIPT
              .replace('/*DECKS_PLACEHOLDER*/', decks_js)
              .replace('/*THEME_PICKER_JS*/', theme_js_code)
              .replace('/*FONT_JS*/', shared.FONT_JS)
              .replace('/*TAB_JS*/', tab_js_code))

    font_picker = shared.font_picker_html()
    session_nav = shared.session_nav_html(len(projects))
    inline_css  = INLINE_CSS + shared.FONT_CSS + shared.TAB_CSS

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Metis — Flashcards</title>
<script>
MathJax = {{
  tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']], processEscapes: true }},
  options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre'] }},
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script" async></script>
<link rel="stylesheet" id="themeCSS" href="themes/{default_theme}.css">
<link rel="stylesheet" href="themes/overrides.css">
<style>{inline_css}</style>
</head>
<body>

<header class="topbar">
  <a class="brand" href="#">
    <span class="brand-mark" aria-hidden="true">{BRAND_SVG}</span>
    <span class="brand-name">METIS</span>
    <span class="brand-issue">Flashcards</span>
  </a>
  {session_nav}
  <div class="topbar-actions">
    {score_chips}
    <button class="icon-btn menu-btn" id="menuBtn" aria-label="Open menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
           stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/>
        <line x1="3" y1="18" x2="21" y2="18"/>
      </svg>
    </button>
    {font_picker}
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
    <div class="side-label" id="sideLabel">METIS · Cards</div>
{sidebar_html}
  </aside>
  <div class="main" style="padding: 0; align-items: start;">
{decks_html}
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

    output_file = None; themes_src = None; txt_files = []
    i = 0
    while i < len(args):
        if args[i] in ('-o', '--output') and i + 1 < len(args):
            output_file = args[i + 1]; i += 2
        elif args[i] == '--themes' and i + 1 < len(args):
            themes_src = args[i + 1]; i += 2
        else:
            txt_files.append(args[i]); i += 1

    if not txt_files:
        print('Error: no .txt files specified.'); sys.exit(1)

    script_dir = Path(__file__).parent
    txt_paths  = [Path(f) for f in txt_files]
    for p in txt_paths:
        if not p.exists():
            print(f'Error: file not found: {p}'); sys.exit(1)

    if not output_file:
        output_file = script_dir.parent / 'STUDY PATH' / 'flashcards.html'
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Copy themes
    themes_dst = output_file.parent / 'themes'
    if not themes_dst.exists():
        candidates = ([Path(themes_src)] if themes_src else []) + [script_dir / 'themes']
        src = next((c for c in candidates if c.exists()), None)
        if src:
            shutil.copytree(src, themes_dst)
            print(f'Copied themes → {themes_dst}')
        else:
            print('Warning: themes folder not found — HTML will load without theme CSS.')

    # Parse
    projects = []; tab_labels_map = {}; seen = {}
    for path in txt_paths:
        print(f'Parsing {path.name}…')
        key = session_key(path)
        if key in seen: seen[key] += 1; key = f'{key}-{seen[key]}'
        else: seen[key] = 1
        cards = parse_metis_txt(path, prefix=key)
        if not cards:
            print(f'  Warning: no cards found in {path.name}'); continue
        tab_labels_map[key] = tab_label(path)
        projects.append((key, cards))
        print(f'  {len(cards)} cards')

    if not projects:
        print('Error: no cards parsed from any input file.'); sys.exit(1)

    print('Rendering HTML…')
    html_out = render_html(projects, tab_labels_map, themes_dst)
    output_file.write_text(html_out, encoding='utf-8')
    total = sum(len(c) for _, c in projects)
    print(f'✓  Written → {output_file}')
    print(f'   {len(projects)} session(s), {total} cards.')


if __name__ == '__main__':
    main()
