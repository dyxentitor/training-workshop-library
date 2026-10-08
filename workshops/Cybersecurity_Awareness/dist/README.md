# Impersonation and phishing workshop: user guide

A full-day (10:00–17:00 MYT) interactive workshop deck, built from the package in this folder. It has 89 screens: an agenda, seven module openers (one with a separate glossary slide) and seven takeaway slides, the learning and activity screens, thirteen continuation slides that spread the densest material over two screens or give a scene’s lesson its own screen, and 3 breaks (short break, lunch break, tea break). Break slides show no clock times; timings are in the presenter notes and facilitator guide.

## What is in `dist/`

| File | Purpose |
|---|---|
| `workshop.html` | The presentation. One self-contained file: styles, script, notes and slide data are embedded. |
| `facilitator-guide.md` | Complete runbook: timetable, slide-by-slide notes, expected answers, answer keys, tabletop rubric and response table. Print it for private reference. |
| `participant-quick-reference.html` | One-page printable response card (A4). |
| `SOURCE_INDEX.md` | Cited primary sources, what each supports, its limits, the 2 October 2026 recheck result and the slides that cite it. |

## Opening and presenting

1. Double-click `workshop.html`, or open it from your browser’s File menu. No installation, server, account or internet connection is needed. Tested in Chromium; use a current Chrome, Edge or Firefox.
2. The deck is a 1600×900 presentation canvas that scales to the window, so projected text is the same size relative to the screen at 1280×720, 1366×768 and 1920×1080. Press **F** or choose **Enter fullscreen** in the menu. If the browser refuses, the menu says so; use the browser’s own full-screen mode (often F11).
3. Move with **→ / Page Down** and **← / Page Up** (presentation clickers send these), or a horizontal swipe on empty slide space (touch screens). **Home** and **End** jump to the first and last slide. Only a slide counter (for example `03 / 89`) stays on screen, bottom-right.
4. The **menu button** (top-right, or **M**) opens a side drawer with the slide index grouped by module (current module open, current slide highlighted), presenter notes, sources, fullscreen, keyboard help, workshop information and, on slides with a vote or reveal, **Reset this interaction**. Selecting a slide closes the drawer. **Escape**, the Close button or a click outside closes any panel.
5. Most slides show everything at once: the evidence, numbered amber markers explaining it, a one-line “what this slide shows”, and the slide’s **takeaway** beside or beneath the evidence (a teal-ruled statement with its supporting actions). 16 slides are **pause points** (marked in the facilitator guide): the room votes or discusses first, then you click once to reveal the answer and its takeaway. The cover opens its email in place with **Open the first message**.
6. **Sources** in the menu lists the sources cited on the current slide first, then the full reference index. External links open the publisher’s website in a new tab, and only when you select one.

| Shortcut | Action |
|---|---|
| → or Page Down | Next slide |
| ← or Page Up | Previous slide |
| Home / End | First or last slide |
| M | Open or close the menu |
| F | Enter or exit fullscreen |
| ? | Keyboard help |
| Escape | Close the open menu or panel |

Shortcuts pause while a panel is open or while a control on a slide has focus; Enter and Space operate buttons as usual, and Ctrl/Alt/Cmd combinations are left to the browser. Choices and reveals persist while you move around the deck and are cleared when you reload the page. Nothing is saved, collected or sent.

> **Presenter notes are shown on the presentation screen, not privately.** Menu › **Presenter notes** opens the notes for the current slide as a panel over the slide, on the same screen. If you are projecting, the audience will see them. There is no separate presenter window. For private notes, print `facilitator-guide.md` or open it on another device.

A direct link to a slide works by adding its ID to the address, for example `workshop.html#SL41` or, for a continuation slide, `workshop.html#SL45B`. Since the readability rework the on-screen number is the slide’s position in the deck and no longer matches the ID (SL45B is screen 50); IDs are stable, so use them in links and notes. The older `#slide-7` form counts positions and shifts when slides are inserted. On phones and small tablets the deck switches to a single-column reading layout that scrolls.

Character portraits and the three desk-scene photographs (SL04, SL20, SL23) are AI-generated; no real person is depicted. Source portraits are in `dist/Image_ref/profile-pictures/`; the build embeds small copies from `src/img/avatars/` (regenerate them with `python3 build/tools/make_avatars.py`, which needs Pillow). Diagrams, icons, scene photographs and backdrops come from `src/img/assets/` (see `docs/ASSET_INTEGRATION_2026-10-08.md`). The fictional-scenario and portrait disclosures are on the cover and in Menu › **About this workshop**, which also shows the session date and venue once they are confirmed in the configuration (until then they appear there as bracketed placeholders and stay off the cover).

## Safety of the practice material

All Meranti people, organisations, messages, links, files, codes and QR tiles are fictional and inert. Addresses use reserved `.example` and `.test` names and are shown as text, never as links. QR tiles are decorative and cannot be scanned. There are no input fields, credential forms, commands, clipboard actions, device linking or remote sessions. Documented incidents (Hong Kong 2024, Cloudflare 2022, and the Microsoft-documented techniques) are labelled and cited.

## Before live delivery: customer inputs still needed

These are shown in the deck as bracketed placeholders until supplied and confirmed:

- **Reporting route:** report button or menu name, reporting mailbox, urgent phone route and step-by-step instructions (optionally a safe screenshot). SL70 shows a labelled **demo workflow** until confirmed.
- **IT support contact and ticket process** (SL38, SL70, response card).
- **Session date and venue** (shown on the cover and in About this workshop once confirmed), and break arrangements for the day. If a longer break is needed, revise the whole timetable rather than shortening the reporting segment.
- **Customer name and any approved logo.** The deck uses fictional Meranti branding and does not imply it is the customer’s brand.
- Audience size and departments, room and projector, and confirmation that English is the delivery language.
- A facilitator rehearsal on the actual projector.

## Adding customer details

1. Edit `config/customer-config.json`. For reporting details to appear, set `"reporting": {"verified": true, ...}` and fill in the fields. Do the same for `support`.
2. Only enter details the customer’s owner has confirmed. While `verified` is `false`, the build ignores the values and shows placeholders.
3. Rebuild (see below). Contacts appear as plain text. No email or phone link is created, so nothing on screen can send a report.

## Building from source

Requirements: Python 3.8+ (standard library only).

```
python3 build/build.py
```

The build reads `04-content/slides.json` (canonical titles, order, timing, notes, decision options and source IDs), `02-research/sources.json`, `config/customer-config.json`, the slide bodies in `src/slides/M0–M7.html`, the data in `src/content/` (choice feedback, extended notes, modules, source groups), `src/css/` and `src/js/deck.js`. It writes all four files in `dist/`.

The build stops with an error if a planned slide is missing, a heading differs from `slides.json`, the timing is not 420 minutes, a module total changes, an element ID is duplicated or not prefixed with its slide ID, a decision lacks exactly one recommended option, a source ID is unknown, or a fragment contains a form control, an embedded frame, a remote asset, a `mailto:`/`tel:` link or a link to a mock domain. It also stops if a content slide lacks its `what_this_shows` line or `key_point`, if any slide outside the 16 pause points hides content or has a click control, if a break, opener, takeaway or agenda slide shows a clock time, or if the word “prayer” appears anywhere in the deck.

`python3 build/build.py --draft` writes the deck even when checks fail and lists every error. Use it only while editing; never deliver a draft build.

Optional environment variables: `CUSTOMER_CONFIG=/path/to/config.json` and `DIST_DIR=/path/to/output` (useful for testing a customer configuration without touching `dist/`).

## Editing content

- Change a title, timing, objective, notes, decision option or source list in `04-content/slides.json`. Keep the total at 420 minutes and the module totals in `src/content/modules.json` unchanged unless the agenda changes.
- Each slide in `slides.json` has `what_this_shows` (the line under the title), `key_point` (the summary used in presenter notes and the facilitator guide; on screen the point is authored in the slide body as a `.takeaway` block, see `docs/TAKEAWAY_REWORK_2026-10-08.md`) and `pause_point`. Module openers, takeaways, the agenda (SL02) and the day recap (SL75) are generated from their `slides.json` fields (`why`, `outcomes`, `cast`, `glossary`, `takeaways`, `habit`, `rules`); they have no HTML fragment.
- Change what a slide shows in `src/slides/M*.html`. Each `<section data-slide="SLxx">` holds one slide body (`SLxxB` is a continuation slide placed directly after SLxx; its order comes from `slides.json`). Element IDs must start with the slide ID.
- Change decision explanations in `src/content/choices.json`, and expected answers or extra notes in `src/content/notes.json`.
- Styles: `src/css/base.css` holds the design tokens (palette, 8-step type scale, spacing), the 1600×900 canvas, the shell and the overlays; `src/css/deck.css` holds the slide components and uses only those tokens. Change a token rather than adding per-slide overrides. The shell markup (header, menu drawer, panels) is `src/shell.html`; the runtime is `src/js/deck.js`.

## Validation (optional, for maintainers)

`build/qa/render.cjs` (fit at 1920×1080, 1366×768, 1280×720 and 390×844, measured in canvas pixels) and `build/qa/interact.cjs` (navigation, menu, keyboard, focus, state, safety, contrast) re-run the browser checks recorded in `validation/QA_REPORT.md`. They need Node.js, the `playwright-core` package and a Chromium build, which are not part of the deck:

```
PW=/path/to/node_modules/playwright-core CHROME=/path/to/chrome node build/qa/render.cjs
PW=/path/to/node_modules/playwright-core CHROME=/path/to/chrome node build/qa/interact.cjs
```

## Printing

The deck has a convenience print stylesheet (one slide per landscape page), but printed or PDF output of the deck has not been validated. The response card is designed for A4 printing and was checked to fit one page in Chromium’s PDF output.
