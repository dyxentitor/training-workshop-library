# Progress ledger

Package v1.0. Full 61-screen build delivered by Claude, 2 October 2026 MYT; clarity rework v2 (76 screens) delivered the same day. Keep 'specified', 'implemented', 'tested' and 'customer confirmed' distinct.

| Stage | Status | Evidence |
|---|---|---|
| Research baseline | Complete with documented source limits | 02-research |
| Source recheck | Done 2 Oct 2026 06:23–06:35 UTC: 17/21 supported; S7, S11 partial (wording adjusted); S4 claim not found (not cited on slides); S8 retrieval failed | validation/source_recheck_2026-10-02.json, dist/SOURCE_INDEX.md |
| Six-slide reference | Unchanged | 06-prototype |
| Full content/storyboard | Implemented, 61 screens, 420 min; SL21 also cites S5 | 04-content/slides.json |
| Full HTML deck | Implemented | dist/workshop.html (`python3 build/build.py`) |
| Facilitator guide, response card, source index, user guide | Implemented | dist/facilitator-guide.md, dist/participant-quick-reference.html, dist/SOURCE_INDEX.md, dist/README.md |
| Render/fit checks | Tested: 378 states at 1440×900, 1366×768, 390×844; 0 failures | validation/qa-results.json, validation/screenshots/ |
| Interaction/a11y-structure/safety/contrast | Tested: 60/60 checks | validation/interaction-results.json |
| QA report | Complete | validation/QA_REPORT.md |
| Customer reporting, support, date/venue, break arrangements | **Unconfirmed**: placeholders and labelled demo shown | config/customer-config.json |
| Facilitator rehearsal, projector test | Not done | — |
| Aesthetic approval / customer review | Not recorded | — |
| **v3 presentation redesign (8 Oct 2026)** | Implemented and tested: toolbar and progress bar removed; menu drawer with module-grouped index, notes, sources, fullscreen, help, about, reset; shortcut set →/←, Page Up/Down, Home/End, M, F, ?, Esc; 1600×900 scaled canvas with design tokens; redesigned cover; 480 render states at 1920×1080, 1366×768, 1280×720 and 390×844 (0 failures); 89/89 interaction checks; 31 unit tests | validation/QA_REPORT.md (v3 section), docs/REDESIGN_NOTE_2026-10-08.md |
| **Visual asset pack integrated (8 Oct 2026)** | Implemented and tested: 6 inline SVG diagrams (SL12, 43, 45, 47, 54, 66), same-SMS inspection component (SL33), 14-icon sprite (SL38, 42, 69, 71), 3 AI scene photographs (SL04, 20, 23), dusk-office backdrop on the cover and all seven module openers under the opener pattern, break pattern; narrow corrections on device-code authorisation, session validity, ClickFix outcomes, SL33 comparison and tabletop debrief; CHART-001 not produced; 480 render states 0 failures; 89/89 interaction checks; 41 unit tests | docs/ASSET_INTEGRATION_2026-10-08.md, validation/QA_REPORT.md (asset section) |
| **Layout fix (8 Oct 2026, 89 slides)** | Implemented and tested: three-row slide grid (header, body, footer) with the body wrapped by the build; one takeaway spacing rule; SL03/SL04 question-only with new explanation slide SL04B; SL42, SL61B, SL66B recomposed; SL11, SL43, SL57 fit corrections; render check now fails body content below the footer row; 532 render states 0 failures; 100/100 interaction checks; 48 unit tests | docs/LAYOUT_FIX_2026-10-08.md, validation/QA_REPORT.md |
| **Takeaway presentation rework (8 Oct 2026, 88 slides)** | Implemented and tested: bottom “Key point” banner removed from every slide; each point placed inside its content as a `.takeaway` block (aside, under diagram/table/cards, or with the vote/reveal), consolidated where the slide already said it, openers’ lessons moved to the next teaching slide; SL23B dedicated takeaway slide; 528 render states 0 failures (none below the padding line); 96/96 interaction checks; 50 unit tests | docs/TAKEAWAY_REWORK_2026-10-08.md, validation/QA_REPORT.md |
| **Readability rework (8 Oct 2026, 87 slides)** | Implemented and tested: type scale raised (title 56, body 28, evidence copy 26, supporting copy 24); kicker-and-pill header row with full-width titles; explanation cards as top-rule columns; eleven crowded slides split into continuation slides (`SLxxB`) that divide the parent’s minutes; 524 render states 0 failures; 92/92 interaction checks; 43 unit tests; all original participant text and notes retained | docs/READABILITY_REWORK_2026-10-08.md, docs/READABILITY_INVENTORY_2026-10-08.md, validation/QA_REPORT.md (readability section) |
| **v2 clarity rework (76 slides)** | Implemented and tested: 16 pause points; what-line and Key point on every content slide; openers and takeaways; photos; no on-screen times or prayer wording; 303 render states 0 failures; 61/61 interaction checks; 31 unit tests | validation/QA_REPORT.md (v2 section), branch `clarity-rework` |

## Files
- Editable sources: `src/slides/M0–M7.html`, `src/content/{choices,notes,modules,source-groups}.json`, `src/css/{base,deck}.css`, `src/js/deck.js`, `src/shell.html`, `src/img/assets/` (diagrams, icons, photographs), `config/customer-config.json`.
- Build: `build/build.py` + `build/make_docs.py` (stdlib only). QA: `build/qa/render.cjs`, `build/qa/interact.cjs` (need playwright-core + Chromium).

## Decisions recorded
- v1: no slide split; count 61. v2: 76 slides. Readability rework (8 Oct 2026): 87 slides, eleven continuation slides (`SLxxB`) that divide their parent’s minutes; timing stays 420 (310 + 110).
- Takeaway rework (8 Oct 2026): 88 slides (SL23B added, 4 + 2 min); the `key_point` field is the notes summary, the on-screen point is authored per slide; no slide carries a bottom banner.
- Layout fix (8 Oct 2026): 89 slides (SL04B added, 2 + 2 + 2 min for SL03/SL04/SL04B); SL04 carries no source line by plan (fictional evidence, no external claim) and none was invented; the footer is a grid row sized to the source line, body content must end above it.
- SL30 card set follows slides.json; HR card from EXERCISES key kept for SL59; IT-notice answer row added to the facilitator guide.
- Compact module bar + slide index replaced the 6 dots (v1–v2); v3 replaces both with a menu drawer and a bottom-right counter; header shows current module.
- Outgoing chat timestamp darkened for contrast (prototype deviation).

## Next action (when resuming)
Apply the customer's verified reporting/support details, date, venue and prayer times in `config/customer-config.json`; rebuild; re-run `build/qa/render.cjs` and `build/qa/interact.cjs`; rehearse on the projector. For design feedback use `00-start/DESIGN_CORRECTION_PROMPT.md`.
