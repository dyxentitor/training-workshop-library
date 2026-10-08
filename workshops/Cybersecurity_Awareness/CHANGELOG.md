# Changes

## 8 October 2026: layout fix (88 → 89 slides)
- Every slide is a three-row grid (header, body, footer): the footer row takes the source line’s actual height and the body row is what remains, so a source line can never be pushed out of the canvas; the render check now fails any body content below the footer’s top edge (no tolerance). The build wraps each slide’s body in `<div class="body">`.
- One spacing rule: a `.takeaway` that follows a sibling inside a container without its own gap gets 24 px above its rule (SL06, SL07, SL37, SL38, SL42, SL43, SL48, SL61B, SL66B, SL71 were at 0 px). Vote-slide feedback-to-takeaway gap 14 px; feedback padding 10 px.
- SL03 and SL04 show their question without the answer; new connected slide SL04B “What the two messages can prove” carries both points (S7). SL03 and SL04 2 min each, SL04B 2 min; opening module still 20 minutes.
- SL42: cards and takeaway separated in a flow stack, takeaway as a row with the practical check. SL61B and SL66B: panels top-aligned under the introduction, takeaway as one block. SL11, SL43, SL57: small fit corrections (tight aside, brief split, card widths).
- “Another familiar name appears” (SL04) has never carried a source line in any version of the plan; nothing was restored and no citation was invented. Record and mapping: `docs/LAYOUT_FIX_2026-10-08.md`.

## 8 October 2026: takeaway presentation rework (87 → 88 slides)
- The full-width green “Key point” banner that the build pinned above every source line is gone. Each teaching point now sits inside the content it explains as a `.takeaway` block (teal rule, optional small label, one statement, supporting lines), in the aside or beneath the diagram, table or cards; on vote and reveal slides it appears with the feedback or reveal (`.if-chosen` / `.if-revealed`). Module openers carry no banner; their lessons moved to the next teaching slide (SL09, SL21, SL52, SL61B, SL71) or were already there (SL29, SL42). Points that only repeated a slide’s own cards, table, findings, feedback or habit panel were consolidated.
- New connected takeaway slide SL23B “What proves who is calling?” after SL23 (6 min → 4 + 2): one statement and three actions. Answer boxes on SL22, SL44, SL46 and SL56 use the same takeaway treatment.
- Build: footer injection, `split_keypoint` and the `.keypoint`/`.answerbox` styles removed; new checks refuse a takeaway outside the vote/reveal wrapper on a pause slide and any leftover banner markup. Feedback, choices and takeaways no longer flex-shrink; spacing trims on choices, feedback, footer and the large tick table. `key_point` remains the notes/guide summary.
- Record and migration table: `docs/TAKEAWAY_REWORK_2026-10-08.md`.

## 8 October 2026: readability rework (76 → 87 slides)
- Type scale raised so supporting text reads at a projector distance: title 56, lead 32, h3 28, body 28, evidence copy 26 (new `--t-read`), supporting copy 24, small 20, label 14 canvas px (was 52/30/26/26/21/18/13). Narrow-screen scale raised to match.
- Slide header restructured: kicker and pill share one row and the title uses the full width; a reveal button is pinned at the right. Explanation cards and panels are columns with a thin top rule instead of filled boxes; the answer box uses the same left-rule style as callouts; agenda, takeaway and recap lose their outer box (the opener keeps a translucent panel over the photograph).
- Eleven crowded slides split into a continuation slide placed directly after the parent, with the parent’s minutes divided and all original wording, evidence, notes and sources kept: SL09→SL09B (definitions / one story, three steps), SL12→SL12B (chat and question / findings and diagram), SL15→SL15B (three responses / sorting table), SL33→SL33B (SMS and question / inspection), SL41→SL41B (opener / glossary), SL45→SL45B (message and genuine page / device-code diagram), SL47→SL47B (invitation and app prompt / join-versus-link diagram), SL54→SL54B (verification page / consequence diagram), SL61→SL61B (team roles / how it runs), SL66→SL66B (timeline strip / supported versus not established), SL70→SL70B (reporting steps / organisation’s route). No new vote or reveal; the 16 pause points are unchanged.
- Bookkeeping: IDs may carry a continuation letter; the build regex, hash parser, tests, validator and facilitator timetable accept it; counter and index numbers are positions. Details and mapping: `docs/READABILITY_REWORK_2026-10-08.md`, `docs/READABILITY_INVENTORY_2026-10-08.md`.

## 8 October 2026: visual asset pack integrated
- Six inline SVG diagrams replace text-only explanations: relayed sign-in (SL43), device-code flow (SL45), join-versus-link (SL47), paste-step consequences (SL54), copied profile versus taken-over account (SL12) and the tabletop observation strip (SL66). Text stays editable; ids are namespaced per slide by the build.
- Fourteen line icons (one inlined sprite) sit beside the written labels on SL38, SL42, SL69 and SL71.
- SL33 now inspects the same SMS (sender label, message link, saved portal) instead of describing a desktop view; the question is “Where would Aina check this?”.
- Scene photographs (AI-generated, fictional): Aina taking the call on SL23; Farid at his desk on SL04 and SL20. Backdrops: the dusk-office photograph fills the whole window (letterbox included) on the cover at 15% and on every module opener (SL08, 19, 28, 41, 51, 60, 68) at 70% under the subtle opener pattern; faint top-left pattern on breaks. Disclosures on the cover and in About extended to scene photographs.
- Narrow content corrections: device-code access requires Aina to authenticate and authorise (SL45); a replayed session works only while valid and allowed by the service (SL43 notes); ClickFix outcomes are possible, not guaranteed (SL54); the SL66 debrief distinguishes confirmed observations from recommended responses instead of saying checks “stopped” three events. CHART-001 was not created.
- Build: `build/assets.py` with `{{asset}}`, `{{icon}}` and `{{image}}` tokens and `{{asset-uri}}` in CSS; 10 unit tests; swipe navigation ignores touches that start on a diagram.

## 8 October 2026: presentation redesign
- Removed the bottom toolbar, module bar and footer arrows; only a slide counter remains at the bottom-right.
- Added a top-right menu button and side drawer: slide index grouped by module (built from slide data), presenter notes, sources, fullscreen, keyboard help, workshop information, and “Reset this interaction” on vote/reveal slides.
- Keyboard: → / Page Down, ← / Page Up, Home/End, M, F, ?, Escape; no global Space/Enter; shortcuts pause while typing or while a panel is open.
- Layout: 1600×900 presentation canvas scaled to the window; consolidated design tokens and an 8-step type scale; key point and source line in a shared slide footer; unscaled reading layout under 900px.
- Cover: email shown as From / To / Subject / Message and opened in place; clock reduced to supporting context; cast strip removed (characters appear on module openers); date and venue shown only when confirmed, otherwise in About this workshop.
- Email slides SL03, SL30, SL34, SL56 use the same From / To / Subject structure. SL15 restructured (situation above, actions beside the comparison table).
- QA scripts rewritten for the canvas; 480 render states at 1920×1080, 1366×768, 1280×720 and 390×844; 89 interaction checks.

# Changes from the six-slide handover

Version 1.0, 2 October 2026 MYT.

- Consolidated the full reusable workshop rather than stopping after one module.
- Authored 61 planned screens with objectives, timings, content, evidence, interactions, notes and source IDs.
- Added public-information, authority-challenge, legitimate-request, reporting and recovery material.
- Added facilitator exercises/keys, role tabletop, participant card and refresher draft.
- Preserved the actual prototype and screenshot baseline with customer details kept separate.
- Documented six-slide code assumptions and full-deck validation requirements.
- Added customer placeholders, continuity ledger, coverage matrix, source limits and package integrity checks.

The full HTML presentation remains Claude's implementation task. No live sends, deployment, customer confirmation or aesthetic approval occurred through this package creation.
