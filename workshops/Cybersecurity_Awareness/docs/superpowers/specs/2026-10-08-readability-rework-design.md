# Readability rework design, 8 October 2026

Scope: `dist/workshop.html` and its sources (`src/slides/M*.html`, `04-content/slides.json`, `src/content/notes.json`, `src/css/*.css`, `src/js/deck.js`, `build/*`). The baseline is commit `2f5a021` on `clarity-rework` (76 slides, asset pack integrated). The user's brief (8 Oct 2026) asked for larger text, clearer hierarchy, fewer competing containers and deliberate splitting of crowded slides, with the narrative, evidence, questions, answer logic, notes and sources preserved. The brief says to proceed without approval pauses, so this record is written for review rather than approval.

## Diagnosis (from the 1366×768 renders of the baseline)

- Titles are already 52 px canvas and the what-line 26 px, but almost every supporting element (markers, findings, card text, evidence copy, hints, feedback) sits at 21 px canvas, which projects at roughly 15 px on a 1366-wide screen.
- Slides that hold only one evidence block and one explanation (SL03, SL04, SL10, SL13, SL14, SL20–SL23, SL30–SL32, SL34, SL35, SL44, SL46, SL52, SL56, the decisions, the cases) have unused vertical space: they can carry a larger type scale without splitting.
- Eleven slides stack three to five containers and cannot stay readable at the target sizes: SL09, SL12, SL15, SL33, SL41, SL45, SL47, SL54, SL61, SL66, SL70.
- Dark `.card`/`.panel`/`.scene` boxes give every explanation the same border and fill as the evidence, so nothing stands out.

## Decisions

1. **Type scale** (canvas px): display 76, title 56, lead 32, h3 28, body 28, copy 24, small 20, label 14. Evidence copy (mail, chat, transcript, notification) uses body 28; findings and markers use h3 28 / copy 24.
2. **Containers**: `.card`, `.panel` and the agenda/takeaway/recap `.scene` lose their fill and border and become columns with a thin top rule. Boxes stay on evidence mock-ups (paper), interactive controls (choices, feedback), the opener outcomes panel (sits over a photograph), the habit box, the known-evidence chips and the answer callout (now the same left-rule style as `.callout`).
3. **Splits** (11 new slides, 76 → 87). IDs keep the parent ID with a letter suffix (`SL09B`), so original IDs, deep links, notes keys and pause-point IDs are untouched. Each split divides the parent's minutes; module totals and the 420-minute programme are unchanged.

| Parent | Continuation | Why |
|---|---|---|
| SL09 definitions | SL09B one story, three steps | three cards + three-step sequence |
| SL12 chat + question | SL12B two findings + copied/taken-over diagram | evidence before findings |
| SL15 three responses | SL15B which action fits which situation (table) | findings + table |
| SL33 SMS + question | SL33B the same SMS inspected | evidence before inspection |
| SL41 opener | SL41B words we will use (glossary) | opener too full |
| SL45 message + genuine page + question | SL45B whose device the code authorises (diagram) | question before answer |
| SL47 invitation + what the app shows | SL47B joining vs linking (diagram) | evidence before comparison |
| SL54 verification page + question | SL54B what that step would do (diagram) | question before mechanism |
| SL61 team roles | SL61B how the tabletop runs | roles + instructions |
| SL66 timeline strip | SL66B supported vs not established | strip + two panels |
| SL70 four reporting steps | SL70B your organisation's route | steps + route fields |

4. **Continuation signalling**: the continuation slide keeps the parent's kicker with "· continued" and the same evidence-kind pill; titles are distinct so the menu index stays descriptive.
5. **No new reveals or votes.** Progressive disclosure is achieved by the slide order. The 16 pause points are unchanged.
6. **Bookkeeping**: fragment and hash regexes accept the letter suffix; `slide_count` becomes 87; the facilitator guide and validator read the count from the data; the legacy `#slide-N` numeric link stays index-based (documented).

## Not changed

Navigation, keyboard, drawer, counter, exercise state, offline packaging, CSP, assets, portraits, sources, module order, character roles, correct-answer logic, careful wording about outcomes.
