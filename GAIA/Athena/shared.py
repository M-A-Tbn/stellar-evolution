"""
shared.py — Shared CSS, JS, and HTML components for all GAIA builders.

Provides:
  • Font picker panel  (settings button + slide-down panel, persisted to localStorage)
  • Sliding window tab system  (3 visible tabs + overflow dropdown + slide animation)

Import in each builder:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    import shared
"""

import json

# ── Font picker ────────────────────────────────────────────────────────────────

FONT_CSS = """
/* ── Settings (font picker) button ── */
.settings-btn {
  display: flex; align-items: center; gap: 5px;
  padding: 5px 11px; border-radius: 6px; cursor: pointer;
  font: inherit; font-size: 12px; font-weight: 600; letter-spacing: .04em;
  text-transform: uppercase; color: var(--mute);
  border: 1px solid var(--line); background: transparent;
  transition: color .15s, border-color .15s, background .15s;
  white-space: nowrap;
}
.settings-btn:hover,
.settings-btn.is-open { color: var(--ink); border-color: var(--bronze-edge); background: var(--bronze-soft); }

/* ── Settings panel (slides down from topbar) ── */
.settings-panel {
  position: fixed;
  top: var(--topbar-h);
  right: 12px;
  width: 256px;
  background: var(--bg-elev);
  border: 1px solid var(--line);
  border-top: none;
  border-radius: 0 0 10px 10px;
  padding: 14px 16px 16px;
  z-index: 500;
  box-shadow: 0 10px 28px rgba(0,0,0,.22);
  transform: translateY(-6px);
  opacity: 0;
  pointer-events: none;
  transition: transform .18s ease, opacity .18s ease;
}
.settings-panel.is-open { transform: translateY(0); opacity: 1; pointer-events: auto; }

.sp-label {
  display: block;
  font-size: 10px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase;
  color: var(--mute); margin-bottom: 10px;
}
.sp-row {
  display: flex; align-items: center; justify-content: space-between;
  gap: 10px; margin-bottom: 9px;
}
.sp-row-label { font-size: 12px; color: var(--body); flex: none; }

.sp-select {
  flex: 1; min-width: 0;
  font: inherit; font-size: 12px; color: var(--ink);
  background: var(--bg-soft); border: 1px solid var(--line);
  border-radius: 5px; padding: 4px 6px; cursor: pointer;
  appearance: none;
}
.sp-select:focus { outline: none; border-color: var(--bronze-edge); }

.sp-divider { border: none; border-top: 1px solid var(--line-soft); margin: 10px 0 11px; }

.sp-size-row { display: flex; align-items: center; gap: 9px; flex: 1; }
.sp-slider {
  flex: 1; -webkit-appearance: none; appearance: none;
  height: 3px; background: var(--line); border-radius: 2px;
  outline: none; cursor: pointer;
}
.sp-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 14px; height: 14px; border-radius: 50%;
  background: var(--bronze); border: 2px solid var(--bg-elev); cursor: pointer;
}
.sp-slider::-moz-range-thumb {
  width: 14px; height: 14px; border-radius: 50%;
  background: var(--bronze); border: 2px solid var(--bg-elev); cursor: pointer; border: none;
}
.sp-size-val {
  font-size: 12px; font-family: var(--mono, monospace);
  color: var(--body); min-width: 34px; text-align: right; flex: none;
}

/* Apply --font-code variable to all code/pre elements */
pre, code { font-family: var(--font-code, monospace); }
"""

_GEAR_SVG = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" '
             'stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">'
             '<circle cx="12" cy="12" r="3"/>'
             '<path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06'
             'a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4'
             'a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15'
             'a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82'
             'l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3'
             'a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83'
             'l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09'
             'a1.65 1.65 0 00-1.51 1z"/></svg>')


def font_picker_html():
    """Returns the ⚙ Aa button + settings panel HTML, to be placed in topbar-actions."""
    return f'''\
<button class="settings-btn" id="settingsBtn" title="Font settings">
      {_GEAR_SVG} <span>Aa</span>
    </button>
    <div class="settings-panel" id="settingsPanel" role="dialog" aria-label="Font settings">
      <span class="sp-label">Body font</span>
      <div class="sp-row">
        <select class="sp-select" id="spBodyFont">
          <option value="theme">Theme default</option>
          <option value="system">System UI</option>
          <option value="georgia">Georgia</option>
          <option value="palatino">Palatino</option>
          <option value="inter">Inter</option>
        </select>
      </div>
      <hr class="sp-divider">
      <span class="sp-label">Code font</span>
      <div class="sp-row">
        <select class="sp-select" id="spCodeFont">
          <option value="theme">Theme default</option>
          <option value="mono">Monospace</option>
          <option value="jetbrains">JetBrains Mono</option>
          <option value="fira">Fira Code</option>
        </select>
      </div>
      <hr class="sp-divider">
      <span class="sp-label">Font size</span>
      <div class="sp-row">
        <div class="sp-size-row">
          <input type="range" class="sp-slider" id="spFontSize" min="12" max="22" step="1" value="15">
          <span class="sp-size-val" id="spFontSizeVal">15px</span>
        </div>
      </div>
    </div>'''


FONT_JS = r"""
/* ── Font / typography settings ── */
(function () {
  const BODY_FONTS = {
    theme:    null,
    system:   'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    georgia:  'Georgia, "Times New Roman", serif',
    palatino: '"Palatino Linotype", Palatino, "Book Antiqua", serif',
    inter:    '"Inter", system-ui, sans-serif',
  };
  const CODE_FONTS = {
    theme:     null,
    mono:      'ui-monospace, "Cascadia Code", "Fira Code", "Courier New", monospace',
    jetbrains: '"JetBrains Mono", ui-monospace, monospace',
    fira:      '"Fira Code", "Fira Mono", ui-monospace, monospace',
  };
  const DEF = { bodyFont: 'theme', codeFont: 'theme', fontSize: 15 };

  function apply(s) {
    const r = document.documentElement;
    const bf = BODY_FONTS[s.bodyFont];
    const cf = CODE_FONTS[s.codeFont];
    if (bf) { r.style.setProperty('--font-body',    bf); r.style.setProperty('--font-heading', bf); }
    else     { r.style.removeProperty('--font-body');      r.style.removeProperty('--font-heading'); }
    if (cf) r.style.setProperty('--font-code', cf);
    else    r.style.removeProperty('--font-code');
    r.style.setProperty('--size-base', s.fontSize + 'px');
    r.style.fontSize = s.fontSize + 'px';  /* makes 1rem = chosen size */
  }

  let s;
  try { s = { ...DEF, ...JSON.parse(localStorage.getItem('gaia-font') || '{}') }; }
  catch (e) { s = { ...DEF }; }
  apply(s);

  const panel = document.getElementById('settingsPanel');
  const btn   = document.getElementById('settingsBtn');
  if (!panel || !btn) return;

  const bodyFSel = document.getElementById('spBodyFont');
  const codeFSel = document.getElementById('spCodeFont');
  const slider   = document.getElementById('spFontSize');
  const sizeVal  = document.getElementById('spFontSizeVal');

  if (bodyFSel) bodyFSel.value = s.bodyFont;
  if (codeFSel) codeFSel.value = s.codeFont;
  if (slider)   slider.value   = s.fontSize;
  if (sizeVal)  sizeVal.textContent = s.fontSize + 'px';

  function save() { localStorage.setItem('gaia-font', JSON.stringify(s)); }

  btn.addEventListener('click', e => {
    e.stopPropagation();
    const open = panel.classList.toggle('is-open');
    btn.classList.toggle('is-open', open);
  });
  document.addEventListener('click', e => {
    if (!panel.contains(e.target) && !btn.contains(e.target)) {
      panel.classList.remove('is-open'); btn.classList.remove('is-open');
    }
  });

  if (bodyFSel) bodyFSel.addEventListener('change', e => { s.bodyFont = e.target.value; apply(s); save(); });
  if (codeFSel) codeFSel.addEventListener('change', e => { s.codeFont = e.target.value; apply(s); save(); });
  if (slider)   slider.addEventListener('input', e => {
    s.fontSize = parseInt(e.target.value, 10);
    if (sizeVal) sizeVal.textContent = s.fontSize + 'px';
    apply(s); save();
  });
})();
"""


# ── Sliding window tab system ──────────────────────────────────────────────────

TAB_CSS = """
/* ── Session nav ── */
.session-nav   {
  display: flex; align-items: stretch; gap: 0; flex: 1; justify-content: center;
  min-width: 0; overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none;
}
.session-nav::-webkit-scrollbar { display: none; }
.tab-window    { display: flex; align-items: stretch; flex: none; }
/* Push all topbar controls to the far right regardless of theme's flex-basis */
.topbar-actions { flex: none; margin-left: auto; }

/* ── Mobile: the theme's own responsive rules target a legacy `.topnav` class that
   this sliding-window tab bar replaced, so `.session-nav` was never constrained and
   forced the whole page wider than the viewport. Keep it scrollable-in-place instead,
   with a guaranteed minimum width so it can't be squeezed out entirely by sibling
   flex items (brand / search / actions) that carry their own content-based floors. ── */
@media (max-width: 880px) {
  .session-nav { justify-content: flex-start; min-width: 130px; }
  .brand-name, .brand-issue { display: none; }
  .session-tab {
    max-width: 130px; padding: 0 12px; font-size: 12.5px;
    overflow: hidden; text-overflow: ellipsis;
  }
  /* `build.py` hides these in its own <style> block on mobile, but iris_build.py /
     coeus_build.py / metis_build.py never picked up that rule, so their theme-picker
     (a full row of theme-swatch buttons) and settings-btn were left at full width —
     the actual cause of most of the page-wide overflow on those pages. Centralize
     the hide here so all four builders get it uniformly. */
  .theme-picker, .settings-btn, .zen-btn { display: none !important; }
  .topbar-actions { gap: 8px; }
  /* With `.brand-name` hidden, `.brand` has nothing left to show but the icon —
     but the theme's own `.brand { flex: 1; }` mobile override still gives it equal
     grow priority against `.session-nav`, so it keeps claiming ~100px+ it doesn't
     need. Let it size to content and hand that space to the tab bar instead. */
  .brand { flex: 0 0 auto; }
}
@media (max-width: 480px) {
  /* Themes set a fixed 28px/24px topbar padding+gap regardless of viewport; on a
     phone that alone eats ~100px before any actual controls are laid out. */
  .topbar { padding: 0 12px; gap: 10px; }
  .session-nav { min-width: 110px; }
  .session-tab { max-width: 96px; padding: 0 9px; font-size: 12px; }
  .session-dropdown .drop-trigger { padding: 0 8px; }
  /* Coeus quiz page: "New Test" button's un-wrapped text node can't be hidden by
     itself, so collapse it via font-size and keep just the (fixed-px, unaffected) icon. */
  .new-test-btn { font-size: 0; padding: 7px; gap: 0; }
  .new-test-btn svg { width: 15px; height: 15px; }
  /* Metis flashcards page: the progress "N / total" chip is visible by default
     (unlike Coeus's score-chip, which starts `hidden`), so it must be compact
     enough to coexist with the menu button in the remaining topbar space. */
  .score-chip { padding: 3px 8px; font-size: 11.5px; }
}

/* ── MathJax overflow guard ──────────────────────────────────────────────────
   `.display-math` paragraphs already scroll via their own overflow-x: auto, but
   that only helps content the build scripts wrapped in that class. Any inline
   formula living in ordinary flowing text (a `<p>`, list item, table cell, or an
   Iris `.def-body` one-liner) renders its `mjx-container` as `display: inline`,
   which browsers won't clip/scroll — a sufficiently wide equation just pushes the
   whole page wider. Giving the block-level ancestor its own overflow-x: auto is a
   no-op when nothing overflows, so it's safe to apply everywhere as a blanket
   guard rather than track down every place math can appear. ── */
.prose p, .intro-content p, .def-body, .prose li, .prose td {
  max-width: 100%; overflow-x: auto;
}


@keyframes tabsExitLeft   { to   { opacity: 0; transform: translateX(-14px); } }
@keyframes tabsExitRight  { to   { opacity: 0; transform: translateX(14px);  } }
@keyframes tabsEnterLeft  { from { opacity: 0; transform: translateX(-14px); } }
@keyframes tabsEnterRight { from { opacity: 0; transform: translateX(14px);  } }

.tab-window.exit-left   { animation: tabsExitLeft   .13s ease forwards; pointer-events: none; }
.tab-window.exit-right  { animation: tabsExitRight  .13s ease forwards; pointer-events: none; }
.tab-window.enter-left  { animation: tabsEnterLeft  .15s ease; }
.tab-window.enter-right { animation: tabsEnterRight .15s ease; }

/* ── Individual tab ── */
.session-tab {
  padding: 0 16px; font-size: 13px; font-weight: 500;
  color: var(--body); text-decoration: none;
  display: flex; align-items: center;
  border-bottom: 2px solid transparent;
  transition: color .15s, border-color .15s, background .15s;
  white-space: nowrap; cursor: pointer;
}
.session-tab:hover    { color: var(--ink); background: rgba(0,0,0,.04); }
.session-tab.is-active { color: var(--ink); border-bottom-color: var(--bronze); font-weight: 600; }

/* ── Dropdown ── */
.session-dropdown { position: relative; display: flex; align-items: center; margin-left: 4px; }

.drop-trigger {
  display: flex; align-items: center; gap: 4px;
  height: 28px; padding: 0 10px; cursor: pointer;
  font: inherit; font-size: 12px; color: var(--mute);
  border: 1px solid var(--line); border-radius: 6px; background: transparent;
  transition: color .15s, border-color .15s, background .15s;
}
.drop-trigger:hover,
.drop-trigger.is-open { color: var(--ink); border-color: var(--bronze-edge); background: var(--bronze-soft); }
.drop-trigger svg { transition: transform .15s; flex: none; }
.drop-trigger.is-open svg { transform: rotate(180deg); }

.drop-list {
  position: absolute; top: calc(100% + 6px); left: 0;
  min-width: 200px; max-height: 280px; overflow-y: auto;
  background: var(--bg-elev); border: 1px solid var(--line);
  border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,.2);
  padding: 4px 0; z-index: 300; list-style: none; margin: 0;
}
.drop-list[hidden] { display: none; }
.drop-item-btn {
  display: flex; align-items: center; gap: 10px; width: 100%;
  padding: 8px 14px; font: inherit; font-size: 13px; color: var(--body);
  background: none; border: none; cursor: pointer; text-align: left;
  transition: background .1s, color .1s;
}
.drop-item-btn:hover  { background: var(--bg-soft); color: var(--ink); }
.drop-item-btn.is-active { color: var(--ink); font-weight: 600; }
.drop-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--bronze); flex: none; opacity: 0; transition: opacity .15s;
}
.drop-item-btn.is-active .drop-dot { opacity: 1; }
"""

_CHEV_SVG = ('<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
             '<polyline points="6 9 12 15 18 9"/></svg>')


def session_nav_html(total):
    """Returns the session nav HTML: tab-window + optional dropdown.

    The dropdown is omitted entirely when total <= 3 (never needed).
    JS populates and manages the tab-window contents.
    """
    if total <= 3:
        return (
            '<div class="session-nav" id="sessionNav">\n'
            '    <div class="tab-window" id="tabWindow"></div>\n'
            '  </div>'
        )
    return (
        '<div class="session-nav" id="sessionNav">\n'
        '    <div class="tab-window" id="tabWindow"></div>\n'
        '    <div class="session-dropdown" id="sessionDropdown">\n'
        '      <button class="drop-trigger" id="dropTrigger"\n'
        '              aria-haspopup="listbox" aria-expanded="false">\n'
        f'        {_CHEV_SVG}\n'
        '      </button>\n'
        '      <ul class="drop-list" id="dropList" hidden role="listbox"></ul>\n'
        '    </div>\n'
        '  </div>'
    )


# ── Tab JS (template — call tab_js() to get the filled version) ───────────────

_TAB_JS_TEMPLATE = r"""
/* ── Session nav: sliding window tabs + dropdown ── */
(function () {
/*PROJ_DATA*/

  const total = PROJ_KEYS.length;
  let currentIdx = 0;

  function _esc(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function winStart(idx) {
    return Math.max(0, Math.min(idx - 1, total - 3));
  }

  /* ── Render tab window ── */
  function renderTabs(idx, direction) {
    const tw = document.getElementById('tabWindow');
    if (!tw) return;
    const doRender = () => {
      const ws    = winStart(idx);
      const count = Math.min(3, total);
      tw.innerHTML = Array.from({ length: count }, (_, i) => {
        const pi    = ws + i;
        const key   = PROJ_KEYS[pi];
        const act   = pi === idx ? ' is-active' : '';
        return `<a class="session-tab${act}" data-idx="${pi}" data-project="${_esc(key)}" href="#" role="tab" aria-selected="${pi === idx}">${_esc(PROJ_LABELS[key] || key)}</a>`;
      }).join('');
      tw.querySelectorAll('.session-tab').forEach(t =>
        t.addEventListener('click', e => { e.preventDefault(); activateSession(parseInt(t.dataset.idx, 10)); })
      );
    };
    if (!direction) { doRender(); return; }
    const exitCls  = direction === 'right' ? 'exit-left'   : 'exit-right';
    const enterCls = direction === 'right' ? 'enter-right' : 'enter-left';
    tw.classList.remove('exit-left','exit-right','enter-left','enter-right');
    tw.classList.add(exitCls);
    tw.addEventListener('animationend', function onEnd() {
      tw.removeEventListener('animationend', onEnd);
      tw.classList.remove(exitCls);
      doRender();
      void tw.offsetWidth;
      tw.classList.add(enterCls);
      tw.addEventListener('animationend', () => tw.classList.remove(enterCls), { once: true });
    }, { once: true });
  }

  /* ── Render dropdown ── */
  function renderDropdown(idx) {
    const list = document.getElementById('dropList');
    if (!list) return;
    list.innerHTML = PROJ_KEYS.map((key, i) =>
      `<li><button class="drop-item-btn${i === idx ? ' is-active' : ''}" data-idx="${i}">`+
      `<span class="drop-dot"></span>${_esc(PROJ_LABELS[key] || key)}</button></li>`
    ).join('');
    list.querySelectorAll('.drop-item-btn').forEach(b =>
      b.addEventListener('click', () => { closeDropdown(); activateSession(parseInt(b.dataset.idx, 10)); })
    );
  }

  function openDropdown() {
    const t = document.getElementById('dropTrigger');
    const l = document.getElementById('dropList');
    if (t) { t.classList.add('is-open'); t.setAttribute('aria-expanded','true'); }
    if (l) l.hidden = false;
  }
  function closeDropdown() {
    const t = document.getElementById('dropTrigger');
    const l = document.getElementById('dropList');
    if (t) { t.classList.remove('is-open'); t.setAttribute('aria-expanded','false'); }
    if (l) l.hidden = true;
  }

  /* ── Main activate ── */
  function activateSession(newIdx) {
    if (newIdx < 0 || newIdx >= total) return;
    const prevWs = winStart(currentIdx);
    const newWs  = winStart(newIdx);
    const dir    = newWs > prevWs ? 'right' : newWs < prevWs ? 'left' : null;
    currentIdx   = newIdx;
    const key    = PROJ_KEYS[newIdx];

    /* Side label */
    const lbl = document.getElementById('sideLabel');
    if (lbl) lbl.textContent = SIDE_PREFIX + ' · ' + (PROJ_LABELS[key] || key);

    renderTabs(newIdx, dir);
    renderDropdown(newIdx);
    try { localStorage.setItem(STORAGE_KEY, key); } catch(e) {}
    if (typeof onProjectActivated === 'function') onProjectActivated(key);
  }

  /* Dropdown toggle */
  const dropTrigger = document.getElementById('dropTrigger');
  if (dropTrigger) {
    dropTrigger.addEventListener('click', e => {
      e.stopPropagation();
      const l = document.getElementById('dropList');
      if (l && !l.hidden) closeDropdown(); else openDropdown();
    });
  }
  document.addEventListener('click', e => {
    const dd = document.getElementById('sessionDropdown');
    if (dd && !dd.contains(e.target)) closeDropdown();
  });

  /* Init */
  let savedKey = null;
  try { savedKey = localStorage.getItem(STORAGE_KEY); } catch(e) {}
  const startIdx = savedKey && PROJ_KEYS.includes(savedKey) ? PROJ_KEYS.indexOf(savedKey) : 0;
  renderDropdown(startIdx);
  activateSession(startIdx);

  /* Expose for search / external callers */
  window._gaiaActivateSession = activateSession;
  window._gaiaProjKeys = PROJ_KEYS;
})();
"""


def tab_js(proj_keys, proj_labels, storage_key, side_prefix):
    """Return the complete tab system JS with project data embedded.

    proj_keys:   list of project key strings (in display order)
    proj_labels: dict mapping key → display label
    storage_key: localStorage key for persisting active tab (e.g. 'gaia-notes-tab')
    side_prefix: prefix for the sidebar label (e.g. 'METIS', 'IRIS')
    """
    data_block = (
        f'const PROJ_KEYS   = {json.dumps(proj_keys)};\n'
        f'  const PROJ_LABELS = {json.dumps(proj_labels, ensure_ascii=False)};\n'
        f'  const STORAGE_KEY = {json.dumps(storage_key)};\n'
        f'  const SIDE_PREFIX = {json.dumps(side_prefix)};'
    )
    return _TAB_JS_TEMPLATE.replace('/*PROJ_DATA*/', data_block)


# ── Shared theme picker JS ─────────────────────────────────────────────────────
# All builders use the same gaia-theme key so the choice persists across pages.

def theme_picker_js():
    """Returns the theme picker IIFE (uses shared gaia-theme storage key)."""
    return r"""
/* ── Theme picker ── */
(function () {
  const btns = document.querySelectorAll('.theme-picker button[data-theme]');
  const css  = document.getElementById('themeCSS');
  const hljsLink = document.getElementById('hljsCSS');
  const HLJS_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/';
  const HLJS_MAP = {
    deepdive: 'atom-one-dark',
    slate:    'nord',
    forest:   'monokai-sublime',
    paper:    'monokai',
    graphite: 'github-dark',
  };
  function setTheme(t) {
    if (css) css.href = 'themes/' + t + '.css';
    if (hljsLink) hljsLink.href = HLJS_CDN + (HLJS_MAP[t] || 'github-dark-dimmed') + '.min.css';
    btns.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.theme === t)));
    try { localStorage.setItem('gaia-theme', t); } catch(e) {}
  }
  btns.forEach(b => b.addEventListener('click', () => setTheme(b.dataset.theme)));
  let saved = null;
  try { saved = localStorage.getItem('gaia-theme'); } catch(e) {}
  const valid = saved && document.querySelector('[data-theme="' + saved + '"]');
  if (valid) setTheme(saved);
})();
"""
