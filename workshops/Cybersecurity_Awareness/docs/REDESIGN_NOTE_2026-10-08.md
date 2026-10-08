# Presentation redesign note, 8 October 2026

Scope: `dist/workshop.html` and its sources. Educational content, factual explanations, source references, module order, character identities and the 16 pause-point exercises are unchanged. No workshop dates, venues, company facts or security claims were added.

## What changed

### Navigation
- The persistent bottom toolbar (Notes, Index, Sources, Reset slide, Fullscreen, Help, previous/next) and the segmented module progress bar are gone, including their layout space. Only a slide counter (`01 / 76`) remains at the bottom-right. It is generated from the slide sequence, never hardcoded.
- A single menu button sits top-right beside an understated module label (truncated with an ellipsis, so the two never overlap). It opens a right-hand drawer, closed by default, as a native modal `<dialog>`: the slide does not move or resize, the backdrop dims, focus is contained, hidden controls are not focusable, and focus returns to the menu button on close. Close button, backdrop click and Escape all close it.
- The drawer lists every slide grouped by module with descriptive titles and numbers, built from the embedded slide data (no second list to drift). Groups expand and collapse; the current module opens automatically and the current slide is highlighted (`aria-current="page"`) and scrolled into view. Selecting a slide navigates and closes the drawer.
- The drawer also holds Presenter notes, Sources, Enter/Exit fullscreen (label follows the Fullscreen API; disabled with an explanation where the API is unavailable; a refusal is reported in place), Keyboard shortcuts, About this workshop (fictional-scenario and AI-portrait disclosures; date, venue and organisation placeholders) and Reset this interaction, which appears only on slides with a vote or reveal and is enabled only once that slide has state.
- Notes, Sources, Help and About are side panels with a fixed header (title and Close) and an independently scrolling body, so long notes never cover their own close control. Notes are labelled as shown on this screen; nothing calls them private.

### Keyboard
| Shortcut | Action |
|---|---|
| → / Page Down | Next slide |
| ← / Page Up | Previous slide |
| Home / End | First / last slide |
| M | Open or close the menu |
| F | Enter or exit fullscreen |
| ? | Keyboard help |
| Escape | Close the open menu or panel (otherwise left to the browser) |

Shortcuts are ignored while typing (input, textarea, select, contenteditable) or inside slider, radio, listbox, combobox, menu or tab controls; while any overlay is open; and with Ctrl, Alt or Cmd held. Browser defaults are prevented only for keys the deck handles. Auto-repeat never advances more than one slide, and a short debounce absorbs clicker double-fires. First and last slides clamp. Space and Enter are not global shortcuts, so slide buttons behave natively. The shortcut list lives in the Help panel and the menu; nothing is printed permanently on the canvas.

### Layout and typography
- The deck is now a 1600×900 presentation canvas scaled by `deck.js` to fit the window on landscape screens. Every slide fits the canvas without page scrolling, and the proportions are identical at 1280×720, 1366×768, 1600×900 and 1920×1080. Below 900px wide the CSS switches to an unscaled, single-column reading layout that scrolls.
- `src/css/base.css` holds the design tokens: navy background, two navy surfaces, warm-white text with a readable secondary tone, teal reserved for emphasis and primary actions, amber for markers and warnings, and a light paper palette for email, documents and screens. The type scale has eight steps (display 76, title 52, lead 30, heading 26, body 26, copy 21, small 18, label 13 canvas pixels). `src/css/deck.css` holds the components and uses only those tokens; the old per-viewport override blocks are gone.
- Every slide shares the same structure: label, title and one-line explanation at the top; evidence and explanation in the middle; the Key point and source line in a footer. Decorative shadows, gradients and glow effects were removed; borders are used once per surface.
- SL15 was restructured (situation line above, three actions beside the comparison table) so it fits at the larger type size without dropping content. No slide was split.

### Opening slide
- Headline and the email are the two focal points. The email uses From, To, Subject and Message, with a small inbox bar. “Open the first message” opens the full message and attachment in place (and relabels to “Close the message”); it no longer jumps to the agenda.
- The large 16:42 clock is gone. Time and deadline appear as one supporting line under the button and in the inbox bar.
- The cast strip was removed; characters are introduced on the module openers where they become relevant. The SL01 facilitator note was reworded to match.
- Date and venue appear on the cover only once confirmed in `config/customer-config.json`; until then they stay in About this workshop as placeholders. The fictional-scenario and AI-portrait disclosures remain on the cover (one small line) and in About.
- SL03, SL30, SL34 and SL56 use the same From / To / Subject structure.

### Interactions
Unchanged in substance: 16 pause points (9 votes, 6 reveals, 1 exercise), feedback with text verdicts (“Recommended” / “Reconsider”, now also with a glyph) that explain why and what to do next, state kept while navigating and cleared on reload, reset limited to the current slide. The former cover “next” button was the only navigation-only button and was replaced by the in-place reveal.

## Launching
Open `dist/workshop.html` in a current Chrome, Edge or Firefox (double-click; no server or network). Press F for fullscreen, → / Page Down to advance, M for the menu. Deep links keep working: `workshop.html#SL41`. Rebuild from source with `python3 build/build.py`.

## Validation performed (8 October 2026, headless Chromium 151 via Playwright; system Firefox for static renders)
- `python3 -m unittest discover -s build/tests`: 31 tests passed.
- `python3 build/build.py`: strict build passed (all existing content rules, plus the cover reveal allowance).
- `build/qa/render.cjs`: 480 states (76 slides, default plus every choice and the revealed state) at 1920×1080, 1366×768, 1280×720 and 390×844: 0 failures. Fit is measured in canvas pixels: nothing spills past the canvas, under the header, over the counter or under the Key point footer; no horizontal overflow at any size. A further 32 states for nine representative slides captured at 1920×1080 and 1280×720.
- `build/qa/interact.cjs`: 89 of 89 checks passed, covering counter generation, absence of toolbar/progress elements, inert hidden slides, keyboard set and guards (modifiers, auto-repeat, typing, Escape with nothing open), hash entry, drawer structure and behaviour (grouping, highlight, expansion, hidden groups not focusable, focus containment, focus restoration, backdrop and Escape close, navigate-and-close), notes/sources/help/about contents, reset visibility and scope, cover reveal, vote and reveal state persistence and isolation, fullscreen label, SL76 sources button, swipe, native Enter/Space, safety (no forms, https-only noopener links, no storage, no network), text contrast on every slide and in the shell, 390px reading layout and drawer, reduced motion.
- Screenshots: `validation/screenshots/1366x768/` (all slides, default and expanded), `390x844/` (all slides, full page), `1920x1080/` and `1280x720/` (representative slides), `firefox/` (static Firefox renders of SL01, SL13 and SL37 from a copy of the deck with the 160 ms arrival fade removed, because Firefox’s headless screenshot captures the first frame; layout matched Chromium).

Problems found during the review and fixed: first key press swallowed by the debounce; focus bouncing back to the menu button after drawer navigation; one 390px overflow (header label); SL11 profile labels hidden behind the avatar; truncated header labels on SL29 and SL69; SL15 content running under the Key point (also closed a measurement gap so the fit check now detects footer overlap); SL02, SL03, SL14, SL20, SL26 running long after the type scale was raised.

## Remaining limitations
- Real fullscreen was exercised in headless Chromium only; the visible fallback path was tested, but not on a physical projector.
- Firefox was checked with static headless renders; Firefox interactions, Safari and Edge were not driven.
- No screen-reader session and no formal WCAG audit; contrast is measured from rendered colours, focus order and ARIA states are checked structurally.
- Printing the deck remains a convenience stylesheet and is unvalidated.
- The drawer's slide list starts scrolled to the current slide, so on later modules the tool buttons sit above the fold; scroll up to reach them.
- Customer date, venue, reporting route and support details are still unconfirmed placeholders.
