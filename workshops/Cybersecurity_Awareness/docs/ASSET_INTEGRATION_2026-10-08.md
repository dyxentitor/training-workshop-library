# Visual asset integration, 8 October 2026

Scope: the complete production pack in `Workshop_Visuals_Complete/` (13 asset groups; CHART-001 blocked and not produced) applied to the 76-slide v3 deck. Slide count, timing, module order, pause points, portraits, menu/drawer/counter shell, keyboard shortcuts, exercise state and offline behaviour are unchanged. No slide was split; no reveal or continuation was needed.

## Where each asset went

| Asset | Slide | Replaced | How |
|---|---|---|---|
| FLOW-001 relayed sign-in (1440×420) | SL43 | the three mock screens (`.seq.aitm`); their wording moved to presenter notes | `{{asset:flow-001-relayed-signin\|wide}}`; the MFA lede stays below |
| FLOW-002 device code (698×340) | SL45 | the two findings | `{{asset:flow-002-device-code}}` under the question; aside uses `.side.tight` |
| FLOW-003 join vs link (698×210) | SL47 | the two comparison cards | between the “what the app shows” card and the hint |
| FLOW-004 paste-step consequences (594×360) | SL54 | the hint (kept in notes) | directly under the question |
| INFO-001 copied profile vs takeover (594×210) | SL12 | the cloning/compromise hint (kept in notes) | under the two findings |
| INFO-002 same-SMS inspection (HTML) | SL33 | the “on a desktop you would also see” card and the mobile hint (kept in notes) | component markup from the pack; eyebrow “Inspect the request, not just the screen”, question “Where would Aina check this?” |
| INFO-003 tabletop strip (1440×270) | SL66 | the three debrief cards | full width above the two facts panels |
| ICON-001 (14 symbols) | SL38, SL42, SL69, SL71 | nothing; added beside labels | sprite inlined once; `{{icon:…}}`; 56 px on dark cards, 48 px on white cards; `verify` reuses `route-contact` |
| IMG-001 Aina takes the call | SL23 | nothing | 594×270 under the hint; caller not shown |
| IMG-002 Farid at his desk (optional) | SL04, SL20 | nothing | 594×220 crop under the hint (`short`); face kept by `object-position` |
| BG-001 dusk office | SL01 | nothing | painted on the viewport (`.viewport::before`, 15 % opacity) so it fills the whole window, not just the 16:9 canvas; headline and email stay above |
| BG-002 opener pattern + BG-001 office photograph | SL08, 19, 28, 41, 51, 60, 68 | nothing | the dusk-office photograph is painted on the viewport at 70 % opacity (raised from 22 % at the user’s request) and fills the whole window, letterbox included; the pattern overlays it as a transparent variant (base rect removed) on `[data-layout="opener"]`, SL41 keeping the y 74–100 band only. `deck.js` mirrors the active slide’s layout on `<body data-layout>`, which switches the backdrop on for cover and openers and off elsewhere. No module gets a character scene photograph: none of the three scenes fits every module, so the shared office backdrop is used throughout. |
| BG-003 break pattern (optional) | SL18, 40, 59 | nothing | CSS background on `[data-layout="intermission"]` |

Dense evidence slides, votes, exercises, the signals table, the sources panel and the close stay plain. ICON-001 was not added to SL37 or SL49 (listed as optional in the audit).

## Content corrections made

- **Device code (SL45):** diagram step 3 is “Enters the code and authorises. May need to sign in first.” Key point: “Only enter and authorise a code for a sign-in you started yourself. Here, authorising the code would sign in the sender’s device as Aina.” Notes cite Microsoft, 6 April 2026 (S12, already on the slide).
- **Session replay (SL43):** the diagram and notes say the session can be reused “while that session is valid”; the answer now reads “while that session remains valid and the service’s controls allow it, often without the password or another prompt” (S11, S13 unchanged).
- **ClickFix (SL54):** the diagram says “can execute”, “can download or run”, “possible harm”; notes say outcomes depend on what ran and what was blocked (S16 unchanged).
- **SL33:** stays a same-SMS comparison (sender label, message link, saved portal). The slide no longer claims the link is hidden, since `mrnt-review.example/a1` is visible; key point and what-line adjusted. `it.meranti.example` is a fictional scenario detail, flagged in notes for reconciliation with customer configuration.
- **Tabletop debrief (SL66):** the card saying known routes “stopped” a sign-in, a payment and a remote session was removed. The strip marks T2 and T3 as confirmed observations and T1/T4 as recommended responses; key point and answer updated; dotted links mean no established relationship.
- Not done, by instruction: CHART-001; no customer routes, statistics, attribution or QR data were invented.

## Disclosure

The cover credit and Menu › About now read that portraits **and scene photographs** are AI-generated and no real person is depicted. `dist/README.md` and the facilitator notes for SL04, SL20 and SL23 say the same.

## Build and files

- `src/img/assets/`: the nine SVGs and three JPEGs copied unchanged from the pack.
- `build/assets.py` (new) and `build/tests/test_assets.py` (10 tests): id namespacing, inline SVG, sprite, icon references, JPEG/SVG data URIs, SL41 band variant.
- `build/build.py`: `{{asset}}`, `{{icon}}`, `{{image}}` tokens; `{{asset-uri:…}}` substitution in CSS; sprite placeholder.
- `src/shell.html`: `<!--SPRITE-->`; About wording. `src/css/deck.css`: asset, icon, SMS-component and backdrop rules, narrow-screen diagram scrolling. `src/js/deck.js`: swipe ignores touches that start on a diagram; `go()` mirrors the active layout on `<body>` for the full-window backdrop.
- Slides: `src/slides/M0–M7.html`. Content: `04-content/slides.json` (SL33, SL45, SL66 key points; SL33 what-line and run-it), `src/content/notes.json` (SL01, 04, 12, 20, 23, 33, 43, 45, 54, 66).
- Docs: `CHANGELOG.md`, `07-implementation/ARCHITECTURE.md`, `05-design/LAYOUT_AND_ASSET_RULES.md`, `10-validation/PROGRESS_LEDGER.md`, `validation/QA_REPORT.md`, `dist/README.md`, `MANIFEST.json` hashes.
- Deck size: 644 KB → 1,406 KB (two copies of IMG-002 and two of BG-001 as data URIs are the bulk).

## Validation run (8 October 2026, headless Chromium 1234 via playwright-core 1.55; system Firefox for static renders)

- `python3 -m unittest discover -s build/tests`: 41 tests passed.
- `python3 build/build.py`: strict build passed.
- `build/qa/render.cjs`, all 76 slides, default plus every choice and revealed state: **480 states at 1920×1080, 1366×768, 1280×720 and 390×844, 0 failures**, 0 page or console errors, 0 non-local requests (re-run on the final build after the opener backdrops were added). Screenshots refreshed in `validation/screenshots/1366x768/` and `390x844/`; the 18 slides touched by this work also captured at `1920x1080/` and `1280x720/`, and the seven openers at all three landscape sizes.
- `build/qa/interact.cjs`: 89/89 checks passed on the final build (navigation, drawer focus, reset, state persistence and isolation, safety, contrast at 4.5:1 on every slide including the photographic openers, narrow layout, reduced motion).
- Backdrop at a 16:10 window (1440×900): cover and openers rendered with the photograph filling the letterbox; a content slide (SL09) and a break (SL18) stay plain; the backdrop opacity follows navigation (0.7 on SL08, 0 on SL09, 0.15 on SL01, 0 on SL18).
- Extra checks in Chromium: at 390 px the wide diagrams scroll inside their wrapper (document width stays 390); a swipe that starts on a diagram does not change slide, a swipe on the heading does; 342 element ids, all unique; all 15 `<use>` references resolve.
- Firefox 1366×768 static renders of SL23, SL33, SL43 and SL66 (`validation/screenshots/firefox/`) match the Chromium layout.
- `10-validation/validate_package.py`: passes after the manifest hash refresh.
- Manual inspection of SL01 (both states), SL04, SL08, SL12, SL18, SL20, SL23, SL33, SL38, SL41, SL42, SL43, SL45, SL47, SL54, SL60, SL66, SL69 and SL71 at 1366×768, plus SL43/SL54 at 1280×720 and SL19/SL45 at 1920×1080: no text or arrow collisions, diagram labels readable, photo crops keep the faces and show no readable screen content, backdrops do not reduce text contrast, footers and counter unobstructed.

## Remaining limitations

- Projector, Safari and Edge not tested; Firefox checked with static renders only, no Firefox interaction run.
- On narrow screens the wide diagrams (SL43, SL66) need a sideways scroll inside the slide; text in the 594–698 px diagrams renders at roughly 15 px there. The fixed slide counter can overlap body text while scrolling on narrow screens (pre-existing).
- The same Farid photograph appears on SL04 and SL20; drop one if the repeat feels heavy in rehearsal.
- The SL33 saved-portal address and the Route 3 ticket process remain placeholders until the customer confirms them.
- The pack’s PNG masters and fallback renders are not embedded (SVG and JPEG only) and stay in `Workshop_Visuals_Complete/` for reference.
