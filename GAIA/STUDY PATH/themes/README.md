# Note themes

Four drop-in stylesheets that share the same HTML structure. Swap one `<link>`
to change the entire look — class names and DOM stay the same.

```html
<link rel="stylesheet" href="themes/quarto.css" />
```

## Files

| File              | Vibe                                                          |
|-------------------|---------------------------------------------------------------|
| `mutegold.css`    | Warm dark amber. Newsreader + Manrope.                        |
| `deepdive.css`     | Charcoal / bronze / teal. Lora + Inter. Discord-tinted chrome.|
| `folio.css`       | Cream paper editorial. Cormorant + Spectral + Plex Mono.      |
| `quarto.css`      | Long-read tuned. Literata + Atkinson Hyperlegible.            |

Each file `@import`s its own Google Fonts at the top — no extra `<link>` tags needed.

---

## HTML contract

The structure these themes expect, top to bottom:

```html
<header class="topbar">
  <a class="brand" href="#">
    <span class="brand-mark">…SVG mark…</span>
    <span class="brand-name">QUARTO</span>
    <span class="brand-issue">Reading<br/>Edition</span>   <!-- optional -->
  </a>

  <nav class="topnav" id="projTabs">
    <a href="#" class="is-active" data-project="reading" aria-current="page">Slow Reading</a>
    <a href="#" data-project="notes">Note-taking</a>
    <!-- one <a> per project / top-level folder -->
  </nav>

  <div class="topbar-actions">
    <button class="icon-btn menu-btn" id="menuBtn">…hamburger…</button>
    <label class="top-search">
      <svg>…search glyph…</svg>
      <input type="text" placeholder="Search notes…" />
      <span class="kbd">⌘K</span>
    </label>
    <button class="zen-btn" id="zenBtn" aria-pressed="false">
      <svg>…corners…</svg><span>Zen</span>
    </button>
  </div>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="side-label" id="sideLabel">Slow Reading</div>

    <!-- one <nav> per project; show the active one, hide the rest -->
    <nav class="nav" data-project="reading">

      <!-- Level 1: category (collapsible) -->
      <div class="cat is-active" data-collapsed="false">
        <button class="cat-row" data-toggle="cat">
          <svg class="chev">…chevron…</svg>
          Articles
        </button>
        <div class="cat-body">

          <!-- Level 2: sub-category (collapsible) -->
          <div class="sub" data-collapsed="false">
            <button class="sub-row" data-toggle="sub">
              <svg class="chev">…chevron…</svg>
              Focus &amp; Depth
            </button>
            <div class="sub-body">
              <!-- Level 3: leaf note -->
              <a class="leaf is-current" aria-current="page" href="#">Slow Reading</a>
              <a class="leaf" href="#">Digital Fatigue</a>
            </div>
          </div>

        </div>
      </div>
    </nav>
  </aside>

  <div class="main">
    <article class="article">
      <span class="section-mark">§ Quarto · Reading Edition</span>   <!-- optional -->
      <h1 class="title">The Art of Slow Reading in a Digital Age</h1>
      <p class="byline">Finding focus and depth — By <span class="by-em">Eleanor Vance</span></p>

      <section class="prose">
        <!-- Markdown output goes here: p, h2, h3, ul, ol, blockquote, a, strong, em -->
      </section>

      <nav class="pager">
        <a class="prev" href="#"><div class="dir">← Previous</div><div class="ttl">…</div></a>
        <a class="next" href="#"><div class="dir">Next →</div><div class="ttl">…</div></a>
      </nav>
    </article>

    <aside class="meta-rail">
      <div class="meta-label">Related Articles</div>
      <ul class="meta-list">
        <li><a href="#">Title<span class="meta-sub">By · 8 min</span></a></li>
      </ul>

      <div class="meta-label">Popular Tags</div>
      <div class="tag-cloud">
        <a class="tag" href="#">Focus</a>
      </div>
    </aside>
  </div>
</div>

<button class="zen-exit" id="zenExit">Exit Zen <span class="kbd">Esc</span></button>
```

## Behaviour the JS owns (theme-agnostic)

These are all in the prototype HTML files; reuse them as-is in your app shell:

- `[data-toggle="cat"]` / `[data-toggle="sub"]` — toggle `data-collapsed` on the
  parent `.cat` / `.sub`.
- `#projTabs a[data-project]` — set `.is-active`, then show the matching
  `.sidebar nav[data-project="X"]` and `hidden` the rest. Update `#sideLabel`.
- `#zenBtn` — toggle `body.zen`. The theme handles the rest (hides chrome,
  centers the article, shows `.zen-exit`). `Esc` and `Z` shortcuts wired up.

## Class reference (what each theme styles)

| Class                | Role                                                  |
|----------------------|-------------------------------------------------------|
| `.topbar`            | Sticky top bar (brand, project tabs, search, zen)     |
| `.brand-mark` / `.brand-name` / `.brand-issue` | Masthead bits                |
| `.topnav` / `.is-active`                       | Project tabs                  |
| `.top-search` / `.kbd` / `.zen-btn`            | Top-bar controls              |
| `.layout` / `.sidebar` / `.main` / `.meta-rail`| Page grid                     |
| `.side-label`        | "DOCUMENTATION" / project name above the tree         |
| `.cat` / `.cat-row` / `.cat-body` / `.chev`    | Level-1 chapter               |
| `.sub` / `.sub-row` / `.sub-body`              | Level-2 chapter               |
| `.leaf` / `.is-current`                        | Level-3 note link             |
| `.article` / `.section-mark` / `.title` / `.byline` | Article header           |
| `.prose`             | Wrapper for rendered Markdown output                  |
| `.pager`             | Prev / Next                                           |
| `.meta-rail` / `.meta-label` / `.meta-list` / `.tag-cloud` / `.tag` | Right rail |
| `.zen-exit`          | Floating exit-zen pill                                |

## Notes on rendering Markdown into `.prose`

The prose styles cover: `p`, `h2`, `h3`, `a`, `strong`, `em`, `ul`, `ol`,
`li`, `blockquote`. The first `<p>` in `.prose` gets a drop cap in editorial
themes (Folio, Quarto). `<h2>`s in Folio/Quarto auto-number with `§ 01`, `§ 02`
via `counter-increment` — so render output in order, don't manually number.
