#!/usr/bin/env python3
"""
GAIA Dashboard — local web UI for the GAIA study orchestration system.
Usage:  python3 GAIA/dashboard.py
        python3 GAIA/dashboard.py 8080   (custom port)
"""

import http.server
import json
import os
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE        = Path(__file__).parent.parent   # CAS root
GAIA        = BASE / "GAIA"
APOLLO      = GAIA / "Apollo"
COEUS       = GAIA / "Coeus"
METIS       = GAIA / "Metis"
IRIS        = GAIA / "Iris"
STUDY_PATH  = GAIA / "STUDY PATH"
PDFS        = GAIA / "StudyMaterials" / "pdfs"
ATHENA      = GAIA / "Athena"

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 7890

# ── Job registry (for SSE streaming) ──────────────────────────────────────────
_jobs: dict = {}
_job_counter = 0
_job_lock = threading.Lock()

def _new_job() -> str:
    global _job_counter
    with _job_lock:
        _job_counter += 1
        jid = str(_job_counter)
        _jobs[jid] = {"lines": [], "done": False, "rc": None, "lock": threading.Lock()}
        return jid

def _run_job(jid: str, cmd: list, cwd=None):
    job = _jobs[jid]
    try:
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, cwd=str(cwd or BASE), bufsize=1
        )
        for line in proc.stdout:
            with job["lock"]:
                job["lines"].append(line.rstrip())
        proc.wait()
        with job["lock"]:
            job["rc"] = proc.returncode
            job["lines"].append(f"{'✓ Done' if proc.returncode == 0 else f'✗ Exit {proc.returncode}'}")
    except Exception as e:
        with job["lock"]:
            job["lines"].append(f"[error] {e}")
    finally:
        with job["lock"]:
            job["done"] = True

# ── Data helpers ───────────────────────────────────────────────────────────────
def get_sessions() -> list:
    sessions = {}
    for f in sorted(APOLLO.glob("* - notes.md")):
        stem = f.stem                              # "Y - notes"
        name = stem[: -len(" - notes")]            # "Y"
        if name.startswith("."):
            continue
        sessions[name] = {
            "name":            name,
            "notes_md":        True,
            "notes_parts":     len(list(APOLLO.glob(f"{name} - notes*.md"))),
            "quiz_md":         (COEUS / f"{name} - quiz.md").exists(),
            "flashcards_txt":  (METIS / f"{name} - flashcards.txt").exists(),
            "summary_md":      (IRIS  / f"{name} - summary.md").exists(),
            "pdf":             (APOLLO / f"{name} - notes.pdf").exists(),
            "notes_html":      (STUDY_PATH / "notes.html").exists(),
            "quiz_html":       (STUDY_PATH / "quiz.html").exists(),
            "flashcards_html": (STUDY_PATH / "flashcards.html").exists(),
            "summary_html":    (STUDY_PATH / "summary.html").exists(),
        }
    return list(sessions.values())

def get_categorised_sessions() -> dict:
    """Return sessions from sessions.json with notes status. Returns dict with
    'sessions' list and 'configured' bool (False if sessions.json missing)."""
    sessions_json = PDFS / "sessions.json"
    if not sessions_json.exists():
        return {"configured": False, "sessions": []}
    try:
        data = json.loads(sessions_json.read_text())
    except Exception:
        return {"configured": False, "sessions": []}
    result = []
    for s in data:
        name = s.get("name", "")
        has_notes = (APOLLO / f"{name} - notes.md").exists()
        result.append({
            "name":      name,
            "pdfs":      s.get("pdfs", []),
            "fortran":   s.get("fortran", []),
            "has_notes": has_notes,
        })
    return {"configured": True, "sessions": result}

def build_cmd(action: str, session: str, pdf: str, session_name: str, extra: dict) -> list | None:
    if action == "gen_quiz_all":
        return ["claude", "--dangerously-skip-permissions", "-p",
                "Run Coeus on all available session notes to generate quizzes"]
    if action == "gen_flashcards_all":
        return ["claude", "--dangerously-skip-permissions", "-p",
                "Run Metis on all available session notes to generate flashcards"]
    if action == "gen_summary_all":
        return ["claude", "--dangerously-skip-permissions", "-p",
                "Run Iris on all available sessions to generate summaries"]
    if action == "pdf":
        md  = APOLLO / f"{session} - notes.md"
        out = APOLLO / f"{session} - notes.pdf"
        return ["pandoc", str(md), "--pdf-engine=xelatex",
                "-V", "geometry:margin=2.5cm", "-V", "fontsize=11pt",
                "-V", "mainfont=Georgia", "-V", "monofont=Menlo",
                "-o", str(out)]
    if action == "notes":
        return ["claude", "--dangerously-skip-permissions", "-p",
                f"GAIA, work on the session '{session_name}'"]
    if action == "rebuild_notes":
        mds = sorted(APOLLO.glob("* - notes*.md"), key=lambda f: f.name)
        if not mds:
            return None
        return (["python3", str(ATHENA / "build.py")] +
                [str(f) for f in mds] +
                ["-o", str(STUDY_PATH / "notes.html"),
                 "--themes", str(ATHENA / "themes")])
    if action == "rebuild_quiz":
        mds = sorted(COEUS.glob("* - quiz.md"), key=lambda f: f.name)
        if not mds:
            return None
        return (["python3", str(ATHENA / "coeus_build.py")] +
                [str(f) for f in mds] +
                ["-o", str(STUDY_PATH / "quiz.html"),
                 "--themes", str(ATHENA / "themes")])
    if action == "rebuild_flashcards":
        txts = sorted(METIS.glob("* - flashcards.txt"), key=lambda f: f.name)
        if not txts:
            return None
        return (["python3", str(ATHENA / "metis_build.py")] +
                [str(f) for f in txts] +
                ["-o", str(STUDY_PATH / "flashcards.html"),
                 "--themes", str(ATHENA / "themes")])
    if action == "rebuild_summary":
        mds = sorted(IRIS.glob("* - summary.md"), key=lambda f: f.name)
        if not mds:
            return None
        return (["python3", str(ATHENA / "iris_build.py")] +
                [str(f) for f in mds] +
                ["-o", str(STUDY_PATH / "summary.html"),
                 "--themes", str(ATHENA / "themes")])
    return None

# ── HTTP handler ───────────────────────────────────────────────────────────────
class Handler(http.server.BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        pass   # silence access log

    # ── helpers ────────────────────────────────────────────────────────────────
    def _json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _html(self, html: str):
        body = html.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # ── GET ────────────────────────────────────────────────────────────────────
    def do_GET(self):
        parsed = urlparse(self.path)
        p  = parsed.path
        qs = parse_qs(parsed.query)

        if p == "/":
            self._html(DASHBOARD_HTML)

        elif p == "/api/sessions":
            self._json(get_sessions())

        elif p == "/api/categorised":
            self._json(get_categorised_sessions())

        elif p == "/api/open":
            fname  = qs.get("file", [""])[0]
            target = STUDY_PATH / fname
            if target.exists():
                webbrowser.open(target.as_uri())
                self._json({"ok": True})
            else:
                self._json({"ok": False, "error": "not found"}, 404)

        elif p == "/api/stream":
            jid = qs.get("job", [""])[0]
            if jid not in _jobs:
                self._json({"error": "no such job"}, 404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            sent = 0
            job  = _jobs[jid]
            while True:
                with job["lock"]:
                    new_lines = job["lines"][sent:]
                    done      = job["done"]
                for line in new_lines:
                    msg = json.dumps(line)
                    try:
                        self.wfile.write(f"data: {msg}\n\n".encode())
                    except (BrokenPipeError, ConnectionResetError):
                        return
                    sent += 1
                if new_lines:
                    try:
                        self.wfile.flush()
                    except (BrokenPipeError, ConnectionResetError):
                        return
                if done and sent >= len(_jobs[jid]["lines"]):
                    try:
                        self.wfile.write(b'data: "__done__"\n\n')
                        self.wfile.flush()
                    except (BrokenPipeError, ConnectionResetError):
                        pass
                    return
                if not new_lines:
                    time.sleep(0.1)

        else:
            self.send_response(404)
            self.end_headers()

    # ── POST ───────────────────────────────────────────────────────────────────
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body   = json.loads(self.rfile.read(length)) if length else {}
        p      = self.path

        if p == "/api/run":
            action       = body.get("action", "")
            session      = body.get("session", "")
            pdf          = body.get("pdf", "")
            session_name = body.get("session_name", "")

            cmd = build_cmd(action, session, pdf, session_name, body)
            if cmd is None:
                self._json({"error": "nothing to run (no source files?)"}, 400)
                return

            jid = _new_job()
            threading.Thread(target=_run_job, args=(jid, cmd), daemon=True).start()
            self._json({"job_id": jid})

        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


# ── Dashboard HTML ─────────────────────────────────────────────────────────────
DASHBOARD_HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GAIA Dashboard</title>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:       #1e1f22;
  --bg-soft:  #27292d;
  --bg-card:  #2b2d31;
  --line:     #3a3c42;
  --ink:      #e0e0e0;
  --body:     #b0b3ba;
  --mute:     #6b6f7a;
  --bronze:   #c9a96e;
  --teal:     #5ba4a4;
  --green:    #5cb85c;
  --red:      #d9534f;
  --amber:    #e0a030;
  --radius:   8px;
  --font:     -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --mono:     "Menlo", "Fira Mono", monospace;
}

body {
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font);
  font-size: 14px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* ── Topbar ── */
.topbar {
  background: var(--bg-soft);
  border-bottom: 1px solid var(--line);
  padding: 0 24px;
  height: 52px;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
  position: sticky;
  top: 0;
  z-index: 100;
}
.topbar-logo {
  font-size: 17px;
  font-weight: 700;
  letter-spacing: .12em;
  color: var(--bronze);
}
.topbar-sub {
  font-size: 12px;
  color: var(--mute);
  letter-spacing: .06em;
  text-transform: uppercase;
}
.topbar-spacer { flex: 1; }
.topbar-btn {
  background: none;
  border: 1px solid var(--line);
  color: var(--body);
  font-size: 12px;
  padding: 5px 14px;
  border-radius: 6px;
  cursor: pointer;
  transition: border-color .15s, color .15s;
}
.topbar-btn:hover { border-color: var(--bronze); color: var(--bronze); }

/* ── Layout ── */
.layout {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 0;
  flex: 1;
  min-height: 0;
}

/* ── Left panel (PDFs) ── */
.left-panel {
  background: var(--bg-soft);
  border-right: 1px solid var(--line);
  padding: 20px 16px;
  overflow-y: auto;
}
.panel-title {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mute);
  margin-bottom: 14px;
}

.pdf-item {
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 12px;
  margin-bottom: 10px;
}
.pdf-name {
  font-size: 12.5px;
  color: var(--ink);
  font-weight: 500;
  word-break: break-all;
  margin-bottom: 8px;
}
.pdf-done { color: var(--mute); font-style: italic; }
.pdf-form { display: flex; gap: 6px; flex-direction: column; }
.pdf-input {
  background: var(--bg-soft);
  border: 1px solid var(--line);
  border-radius: 5px;
  color: var(--ink);
  font-size: 12px;
  padding: 5px 8px;
  width: 100%;
}
.pdf-input:focus { outline: none; border-color: var(--bronze); }
.pdf-input::placeholder { color: var(--mute); }

.btn {
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 500;
  padding: 6px 12px;
  transition: opacity .15s, filter .15s;
  white-space: nowrap;
}
.btn:hover { filter: brightness(1.1); }
.btn:active { filter: brightness(.9); }
.btn:disabled { opacity: .4; cursor: not-allowed; filter: none; }
.btn-primary   { background: var(--bronze); color: #1a1a1a; }
.btn-secondary { background: var(--bg-soft); border: 1px solid var(--line); color: var(--body); }
.btn-teal      { background: var(--teal);   color: #1a1a1a; }
.btn-sm        { font-size: 11px; padding: 4px 10px; }

.empty-state {
  color: var(--mute);
  font-size: 12px;
  text-align: center;
  padding: 24px 0;
}

/* ── Right panel (sessions) ── */
.right-panel {
  padding: 24px;
  overflow-y: auto;
}

.sessions-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  gap: 12px;
}

.session-card {
  background: var(--bg-card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  margin-bottom: 14px;
  overflow: hidden;
  transition: border-color .15s;
}
.session-card:hover { border-color: #4a4d55; }

.session-head {
  padding: 14px 16px 10px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.session-name {
  font-size: 15px;
  font-weight: 600;
  color: var(--ink);
  flex: 1;
}
.session-meta {
  font-size: 11px;
  color: var(--mute);
}

.badges {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  padding: 0 16px 12px;
}
.badge {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .04em;
  padding: 2px 8px;
  border-radius: 4px;
  text-transform: uppercase;
}
.badge-on  { background: #1e3a2a; color: #5cb85c; border: 1px solid #2d5a3e; }
.badge-off { background: #2d2a1e; color: #888; border: 1px solid #44400a; opacity: .6; }

.session-actions {
  padding: 10px 16px 14px;
  display: flex;
  gap: 7px;
  flex-wrap: wrap;
  border-top: 1px solid var(--line);
}

/* ── Rebuild bar ── */
.rebuild-bar {
  background: var(--bg-soft);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 12px 16px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.rebuild-label {
  font-size: 11px;
  color: var(--mute);
  text-transform: uppercase;
  letter-spacing: .08em;
  flex: 1;
}

/* ── Terminal drawer ── */
.terminal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.5);
  z-index: 200;
  display: none;
  align-items: flex-end;
}
.terminal-overlay.open { display: flex; }

.terminal-drawer {
  width: 100%;
  height: 45vh;
  background: #0d0f12;
  border-top: 2px solid var(--bronze);
  display: flex;
  flex-direction: column;
}
.terminal-header {
  display: flex;
  align-items: center;
  padding: 8px 16px;
  border-bottom: 1px solid #1e2025;
  gap: 10px;
  flex-shrink: 0;
}
.terminal-title {
  font-size: 12px;
  font-weight: 600;
  color: var(--bronze);
  letter-spacing: .06em;
  flex: 1;
}
.terminal-status {
  font-size: 11px;
  color: var(--mute);
}
.terminal-close {
  background: none;
  border: none;
  color: var(--mute);
  font-size: 18px;
  cursor: pointer;
  line-height: 1;
  padding: 0 4px;
}
.terminal-close:hover { color: var(--ink); }
.terminal-body {
  flex: 1;
  overflow-y: auto;
  padding: 12px 16px;
  font-family: var(--mono);
  font-size: 12px;
  line-height: 1.6;
}
.t-line { color: #c8cdd6; }
.t-line.done  { color: var(--green); }
.t-line.error { color: var(--red); }
.t-line.warn  { color: var(--amber); }
.t-cursor {
  display: inline-block;
  width: 7px; height: 13px;
  background: var(--bronze);
  vertical-align: text-bottom;
  animation: blink .9s step-start infinite;
}
@keyframes blink { 50% { opacity: 0; } }

/* ── Spinner ── */
.spinner {
  display: inline-block;
  width: 12px; height: 12px;
  border: 2px solid var(--line);
  border-top-color: var(--bronze);
  border-radius: 50%;
  animation: spin .6s linear infinite;
  vertical-align: middle;
  margin-right: 4px;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--line); border-radius: 3px; }
</style>
</head>
<body>

<!-- Topbar -->
<header class="topbar">
  <span class="topbar-logo">GAIA</span>
  <span class="topbar-sub">Dashboard</span>
  <div class="topbar-spacer"></div>
  <button class="topbar-btn" onclick="refresh()">↺ Refresh</button>
</header>

<!-- Layout -->
<div class="layout">

  <!-- Left: PDFs -->
  <aside class="left-panel">
    <div class="panel-title">Sessions — Generate Notes</div>
    <div id="pdf-list"><div class="empty-state">Loading…</div></div>
  </aside>

  <!-- Right: Sessions -->
  <main class="right-panel">
    <div class="panel-title">Sessions</div>

    <!-- Generate Content bar -->
    <div class="rebuild-bar" style="margin-bottom:10px">
      <span class="rebuild-label">Generate</span>
      <button class="btn btn-primary btn-sm" onclick="genAll('gen_quiz_all')">Quiz — all sessions</button>
      <button class="btn btn-primary btn-sm" onclick="genAll('gen_flashcards_all')">Flashcards — all sessions</button>
      <button class="btn btn-primary btn-sm" onclick="genAll('gen_summary_all')">Summary — all sessions</button>
    </div>

    <!-- Open HTML bar -->
    <div class="rebuild-bar" style="margin-bottom:10px">
      <span class="rebuild-label">Open</span>
      <span id="open-btns" style="display:flex;gap:7px;flex-wrap:wrap"></span>
    </div>

    <!-- Rebuild HTML bar -->
    <div class="rebuild-bar">
      <span class="rebuild-label">Rebuild HTML</span>
      <button class="btn btn-secondary btn-sm" onclick="rebuildHTML('rebuild_notes')">Notes</button>
      <button class="btn btn-secondary btn-sm" onclick="rebuildHTML('rebuild_quiz')">Quiz</button>
      <button class="btn btn-secondary btn-sm" onclick="rebuildHTML('rebuild_flashcards')">Flashcards</button>
      <button class="btn btn-secondary btn-sm" onclick="rebuildHTML('rebuild_summary')">Summary</button>
    </div>

    <div id="sessions-list"><div class="empty-state">Loading…</div></div>
  </main>
</div>

<!-- Terminal drawer -->
<div class="terminal-overlay" id="terminal-overlay" onclick="maybeCloseTerminal(event)">
  <div class="terminal-drawer">
    <div class="terminal-header">
      <span class="terminal-title" id="terminal-title">Running…</span>
      <span class="terminal-status" id="terminal-status"></span>
      <button class="terminal-close" onclick="closeTerminal()">×</button>
    </div>
    <div class="terminal-body" id="terminal-body"></div>
  </div>
</div>

<script>
const API = '';
let _running = false;

// ── Fetch helpers ──────────────────────────────────────────────────────────
async function api(path, opts) {
  const r = await fetch(API + path, opts);
  return r.json();
}

// ── Render categorised sessions (left panel) ───────────────────────────────
function renderCategorised(data) {
  const el = document.getElementById('pdf-list');
  if (!data.configured) {
    el.innerHTML = '<div class="empty-state">No sessions defined.<br>Type <b>categories</b> in Claude Code<br>to set them up first.</div>';
    return;
  }
  if (!data.sessions.length) {
    el.innerHTML = '<div class="empty-state">No sessions found in<br>sessions.json</div>';
    return;
  }
  el.innerHTML = data.sessions.map(s => {
    if (s.has_notes) {
      return `<div class="pdf-item">
        <div class="pdf-name" style="margin-bottom:4px">${esc(s.name)}</div>
        <div style="font-size:11px;color:var(--green)">✓ Notes exist</div>
      </div>`;
    }
    const pdfList = s.pdfs.map(p => `<span style="color:var(--mute)">${esc(p)}</span>`).join('<br>');
    return `<div class="pdf-item">
      <div class="pdf-name" style="margin-bottom:6px">${esc(s.name)}</div>
      <div style="font-size:11px;line-height:1.7;margin-bottom:8px">${pdfList}</div>
      <button class="btn btn-primary btn-sm" style="width:100%"
        onclick="generateNotes('${esc(s.name)}')">
        Generate Notes
      </button>
    </div>`;
  }).join('');
}

// ── Render sessions ────────────────────────────────────────────────────────
function badge(label, on) {
  return `<span class="badge ${on ? 'badge-on' : 'badge-off'}">${label}</span>`;
}

function renderSessions(sessions) {
  const el = document.getElementById('sessions-list');
  if (!sessions.length) {
    el.innerHTML = '<div class="empty-state">No sessions yet.<br>Generate notes from a PDF to start.</div>';
    renderOpenBar({});
    return;
  }

  const any = sessions[0];
  renderOpenBar({
    notes_html:      any.notes_html,
    quiz_html:       any.quiz_html,
    flashcards_html: any.flashcards_html,
    summary_html:    any.summary_html,
  });

  el.innerHTML = sessions.map(s => {
    const actions = [];
    if (!s.pdf)
      actions.push(`<button class="btn btn-secondary btn-sm" onclick="runAgent('pdf','${esc(s.name)}')">Export PDF</button>`);

    const opens = [];
    if (s.pdf)
      opens.push(`<button class="btn btn-teal btn-sm" onclick="openPdf('${esc(s.name)}')">Open PDF</button>`);

    const allActions = [...opens, ...actions];

    return `<div class="session-card">
      <div class="session-head">
        <div class="session-name">${esc(s.name)}</div>
        <div class="session-meta">${s.notes_parts > 1 ? s.notes_parts + ' parts' : ''}</div>
      </div>
      <div class="badges">
        ${badge('Notes', s.notes_md)}
        ${badge('Quiz', s.quiz_md)}
        ${badge('Flashcards', s.flashcards_txt)}
        ${badge('Summary', s.summary_md)}
        ${badge('PDF', s.pdf)}
      </div>
      ${allActions.length ? `<div class="session-actions">${allActions.join('')}</div>` : ''}
    </div>`;
  }).join('');
}

function renderOpenBar(flags) {
  const btns = [];
  if (flags.notes_html)      btns.push(`<button class="btn btn-teal btn-sm" onclick="openFile('notes.html')">Notes</button>`);
  if (flags.quiz_html)       btns.push(`<button class="btn btn-teal btn-sm" onclick="openFile('quiz.html')">Quiz</button>`);
  if (flags.flashcards_html) btns.push(`<button class="btn btn-teal btn-sm" onclick="openFile('flashcards.html')">Flashcards</button>`);
  if (flags.summary_html)    btns.push(`<button class="btn btn-teal btn-sm" onclick="openFile('summary.html')">Summary</button>`);
  document.getElementById('open-btns').innerHTML =
    btns.length ? btns.join('') : '<span style="color:var(--mute);font-size:12px">Generate content first</span>';
}

// ── Actions ────────────────────────────────────────────────────────────────
async function generateNotes(sessionName) {
  await runRaw('Generate Notes — ' + sessionName, {action: 'notes', session_name: sessionName});
}

async function genAll(action) {
  const labels = {
    gen_quiz_all:       'Generate Quiz — all sessions',
    gen_flashcards_all: 'Generate Flashcards — all sessions',
    gen_summary_all:    'Generate Summary — all sessions',
  };
  await runRaw(labels[action] || action, {action});
}

async function runAgent(action, session) {
  const labels = {pdf: 'Export PDF'};
  await runRaw((labels[action] || action) + ' — ' + session, {action, session});
}

async function rebuildHTML(action) {
  const labels = {rebuild_notes:'Rebuild Notes HTML', rebuild_quiz:'Rebuild Quiz HTML',
                  rebuild_flashcards:'Rebuild Flashcards HTML', rebuild_summary:'Rebuild Summary HTML'};
  await runRaw(labels[action] || action, {action});
}

async function openFile(file) {
  await api('/api/open?file=' + encodeURIComponent(file));
}

async function openPdf(session) {
  // PDFs are in Apollo/ — open via system
  const path = encodeURIComponent(session + ' - notes.pdf');
  await fetch(`/api/open?file=..%2FApollo%2F${path}`).catch(() => {});
  // Fallback: just open via OS
  const res = await api('/api/open?file=' + encodeURIComponent('../Apollo/' + session + ' - notes.pdf'));
  if (!res.ok) alert('PDF not found — try Export PDF first.');
}

// ── Core run + stream ──────────────────────────────────────────────────────
async function runRaw(title, body) {
  if (_running) { alert('A task is already running. Please wait.'); return; }
  _running = true;
  openTerminal(title);

  let res;
  try {
    res = await api('/api/run', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body),
    });
  } catch (e) {
    appendLine('[error] Could not start task: ' + e.message, 'error');
    _running = false;
    return;
  }

  if (res.error) {
    appendLine('[error] ' + res.error, 'error');
    setTerminalStatus('Error');
    _running = false;
    return;
  }

  streamJob(res.job_id);
}

function streamJob(jid) {
  const es = new EventSource('/api/stream?job=' + jid);
  const cursor = document.getElementById('t-cursor');
  es.onmessage = e => {
    const line = JSON.parse(e.data);
    if (line === '__done__') {
      es.close();
      if (cursor) cursor.remove();
      setTerminalStatus('Done');
      _running = false;
      // Auto-refresh data
      setTimeout(refresh, 800);
      return;
    }
    const cls = line.startsWith('✓') ? 'done'
              : line.startsWith('✗') || line.startsWith('[error]') ? 'error'
              : line.startsWith('[warning]') || line.startsWith('WARNING') ? 'warn'
              : '';
    appendLine(line, cls);
  };
  es.onerror = () => {
    es.close();
    if (cursor) cursor.remove();
    setTerminalStatus('Disconnected');
    _running = false;
  };
}

// ── Terminal UI ────────────────────────────────────────────────────────────
function openTerminal(title) {
  document.getElementById('terminal-title').textContent = title;
  document.getElementById('terminal-status').textContent = '';
  document.getElementById('terminal-body').innerHTML =
    '<span id="t-cursor" class="t-cursor"></span>';
  document.getElementById('terminal-overlay').classList.add('open');
}

function closeTerminal() {
  if (_running) return;
  document.getElementById('terminal-overlay').classList.remove('open');
}

function maybeCloseTerminal(e) {
  if (e.target === document.getElementById('terminal-overlay')) closeTerminal();
}

function appendLine(text, cls = '') {
  const body   = document.getElementById('terminal-body');
  const cursor = document.getElementById('t-cursor');
  const div    = document.createElement('div');
  div.className = 't-line' + (cls ? ' ' + cls : '');
  div.textContent = text;
  body.insertBefore(div, cursor || null);
  body.scrollTop = body.scrollHeight;
}

function setTerminalStatus(text) {
  document.getElementById('terminal-status').textContent = text;
  document.getElementById('terminal-title').innerHTML =
    document.getElementById('terminal-title').textContent +
    (text === 'Done' ? ' <span style="color:var(--green)">✓</span>' : '');
}

// ── Refresh ────────────────────────────────────────────────────────────────
async function refresh() {
  const [sessions, categorised] = await Promise.all([
    api('/api/sessions'),
    api('/api/categorised'),
  ]);
  renderSessions(sessions);
  renderCategorised(categorised);
}

function esc(s) {
  return String(s)
    .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

refresh();
</script>
</body>
</html>
"""

# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    os.chdir(BASE)   # ensure cwd is the project root for claude commands
    server = http.server.ThreadingHTTPServer(("localhost", PORT), Handler)
    url    = f"http://localhost:{PORT}"
    print(f"GAIA Dashboard  →  {url}")
    print("Press Ctrl+C to stop.\n")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
