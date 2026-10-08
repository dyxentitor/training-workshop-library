# Readability rework, 8 October 2026

Scope: `dist/workshop.html` and its sources, on branch `clarity-rework`. Baseline: commit `2f5a021` (the 76-slide deck with the visual asset pack integrated). The brief asked for larger, readable text, a clearer hierarchy, fewer competing containers and deliberate splitting of crowded slides, with the story, evidence, questions, answer logic, notes and sources unchanged.

**Slide count: 76 → 87.** Programme: 420 minutes, every module total unchanged. Pause points: 16, unchanged. No new vote, reveal or exercise. No new characters, events or statistics. Design direction (navy, teal, warm white; Arial/Helvetica) unchanged.

The per-slide inventory, the original-to-updated mapping, the wording changes and their reasons, and the note moves are in `docs/READABILITY_INVENTORY_2026-10-08.md`. The design record is `docs/superpowers/specs/2026-10-08-readability-rework-design.md`.

## What was wrong

In the baseline renders, titles were already 52 px canvas, but almost every supporting element (markers, findings, card text, evidence copy, hints, feedback) sat at 21 px canvas, which projects at about 15 px on a 1366-wide screen. Eleven slides stacked three to five containers (cards, a diagram, a question, a hint, a table), and the dark `.card`/`.panel` boxes gave every explanation the same border and fill as the evidence, so nothing led the eye.

## Main readability changes

1. **Type scale** (`src/css/base.css`, canvas px): title 52 → 56, lead 30 → 32, h3 26 → 28, body 26 → 28, supporting copy 21 → 24, small 18 → 20, label 13 → 14. A new step `--t-read` 26 px carries message bodies inside evidence mock-ups (mail, chat, transcript, tabletop card), so the evidence stays dominant without forcing the mock-ups taller than the slide. The narrow-screen scale rose in step.
2. **Slide header.** The kicker and the evidence-kind pill share one row and the title takes the full width, so titles such as “Access can be granted without sharing a password” stay on one line at 56 px. On reveal slides the button is pinned at the right and the title keeps a right padding.
3. **Fewer competing containers.** Explanation cards and panels are now columns with a thin top rule, not filled boxes; the answer box uses the same left-rule style as the callouts; the agenda, takeaways and recap lose their outer box. Boxes remain where they carry meaning: paper evidence mock-ups, choice buttons and feedback, the opener’s outcomes panel (it sits on a photograph), the habit box and the known-evidence chips on the tabletop board.
4. **Evidence first.** The evidence column of the standard grid is wider (1.5 : 1), the phone mock-up on SL33 is larger, and the three tall diagrams (device code, paste-step consequences, copied profile versus takeover) sit beside their explanation rather than squeezed under a question.
5. **Splits.** Eleven crowded slides became two slides each. The continuation keeps the parent’s kicker with “· continued” and the same evidence-kind pill, has a distinct descriptive title for the menu, and carries the notes and sources that apply to its content. Evidence and questions always precede findings and answers.

| Parent | Now shows | Continuation | Now shows |
|---|---|---|---|
| SL09 Impersonation and phishing | three definitions | SL09B One message can do all three | the three-step story |
| SL12 A genuine account, an unusual request | chat and the discussion question | SL12B Two checks before sharing the list | two findings and the copied/taken-over diagram |
| SL15 Someone is using your name | situation and three responses | SL15B Copied profile or taken-over account? | the sorting table |
| SL33 The same request on a phone | the SMS, large, and the question | SL33B The same text message, inspected | sender label, link and saved portal |
| SL41 Module 4 opener | why, cast, outcomes | SL41B Words we will use | the six-term glossary |
| SL45 A real sign-in page, someone else’s code | message, genuine page, question | SL45B Whose device the code would sign in | the device-code diagram and explanation |
| SL47 Linking another device | invitation and what the app shows | SL47B Joining a group or linking a device? | the comparison diagram |
| SL54 The verification page asks too much | the page and the question | SL54B What that step would actually do | the consequence diagram and the response |
| SL61 Your team at Meranti | the four roles | SL61B How the tabletop runs | what to record and how it runs |
| SL66 What stopped the chain? | the observation strip | SL66B What the evidence supports | supported versus not established |
| SL70 Your actual reporting route | the four reporting steps | SL70B Your organisation’s route | the confirmed or placeholder contacts |

Each split divides the parent’s minutes (for example SL45 8 min → 4 + 4; SL70 5 min → 3 + 2); the full table is in the inventory.

## Wording

No teaching point was removed. Where a key point covered both halves of a split, each slide now carries the half that applies, in the original words (for example SL09’s “One message can do all three” moved to SL09B). Three continuation slides needed a key point of their own; each is composed from existing notes or screen text (SL54B from the SL54 answer, SL61B from the recording instructions, SL66B from the SL66 answer). The two new one-line hints on SL12 (“The account is genuinely Siti’s. That does not show who is typing today.”) and SL45 (“The address is the real service. Ask who started this sign-in.”) restate the facilitator’s existing question so participants see it; the SL33 hint restores the desktop-versus-phone point from the presenter notes. The inventory lists every changed field with the original text.

Presenter notes moved with the content they describe (diagram, table, panel) and every original note sentence is still present; the inventory script checks this. Facilitator timings and the facilitator guide are regenerated from the plan.

## Bookkeeping

- IDs: original IDs unchanged; continuation slides carry the parent ID plus `B`. `build/build.py`, `src/js/deck.js` (`#SL45B` deep links), the unit tests and `10-validation/validate_package.py` accept the suffix. Displayed numbers are positions (SL45B is screen 50) and are generated, never hard-coded; the drawer index numbers by position and lists the continuation directly after its parent.
- Resume and deep links: the deck stores nothing, so the only resume mechanism is the URL hash. ID links (`#SL41`) land on the same content as before. The legacy position link (`#slide-9`) still works but counts positions and therefore shifts after an insertion; the user guide says so.
- Reveal states, votes, exercise destinations and the reset tool are untouched; no pause-point ID changed.
- `04-content/slides.json` `slide_count` is 87; the facilitator guide’s timetable reads the screen count from the data (it said “61 screens” before).
- Docs updated: `CHANGELOG.md`, `07-implementation/ARCHITECTURE.md`, `05-design/LAYOUT_AND_ASSET_RULES.md`, `10-validation/PROGRESS_LEDGER.md`, `10-validation/COVERAGE_MATRIX.md`, `validation/QA_REPORT.md`, `dist/README.md`, `MANIFEST.json`.

## Validation (8 October 2026, headless Chromium 1234 via playwright-core 1.55; system Firefox for static renders)

- `python3 -m unittest discover -s build/tests`: 44 tests passed (one added for the glossary layout).
- `python3 build/build.py`: strict build passed, 87 slides, 420 minutes.
- `build/qa/render.cjs`, every slide, default plus every choice and the revealed state, at 1920×1080, 1366×768, 1280×720 and 390×844: **524 states, 0 failures, 0 page or console errors, 0 non-local requests.** Screenshots refreshed in `validation/screenshots/1366x768/` and `390x844/`; the 35 changed or inserted slides also captured at `1920x1080/` and `1280x720/`.
- `build/qa/interact.cjs`: **92 of 92 checks passed** (three checks were made position-aware: End and the last-slide hash use the last slide’s ID; the index-highlight check derives SL13’s position; two checks added for `#SL09B` entry, a rejected `#SL09Z`, and the continuation’s place and number in the index). Text contrast: 0 pairs below 4.5:1 (3:1 large) on any slide in the expanded state.
- Firefox 1366×768 static renders of SL09B, SL33B, SL41B, SL45B, SL66 and SL70 (`validation/screenshots/firefox/`) match the Chromium layout.
- Baseline failures: none. The baseline run on `2f5a021` reported 480 states with 0 failures and 89/89 checks; every failure seen during this work was introduced by the larger type and fixed before delivery (26 slide-states overflowed after the first scale change; the fixes are the header restructure, the evidence-copy step, tighter mock-up padding, and placing the tall diagrams beside their text).
- Content checks (scripted in the inventory): every participant-facing text fragment of the baseline is present in the new fragments (five labels became titles or what-lines of the continuation slide); every presenter-note sentence is present; module order, pause-point IDs, option labels, preferred answers and source IDs unchanged.
- Manual inspection at 1366×768 of every changed or inserted slide in default and expanded states, plus SL43, SL15B, SL45B and SL54B at 1280×720 and SL03, SL11, SL37, SL42 at 1920×1080: titles on one line, diagram labels unchanged or larger, no text or arrow collisions, footers and counter clear, continuation slides consistent with their parents.

## Remaining limitations

- The tabletop observation strip (SL66, INFO-003) is authored at 1440×270 and cannot be drawn wider than the canvas, so its second-level labels stay at about 13–15 px canvas. SL66B carries the same conclusions at full size; the strip is the visual summary. Redrawing the asset was outside this brief.
- The relayed sign-in diagram (SL43, FLOW-001) is shown at 1360 px wide (94% of its authored size) so the MFA line below it fits; its labels are about 15 px canvas.
- At 390 px the wide diagrams still scroll sideways inside the slide, and the fixed counter can overlap body text while scrolling (both pre-existing).
- Firefox was checked with static renders only; Safari, Edge and a physical projector were not tested. No screen-reader session.
- The `#slide-N` position link shifts after insertions (documented); ID links are stable.
- Customer date, venue, reporting route and support details remain placeholders.
