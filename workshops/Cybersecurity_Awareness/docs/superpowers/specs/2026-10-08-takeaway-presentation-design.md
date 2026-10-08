# Takeaway presentation redesign (8 October 2026)

Scope: the 87-slide deck on branch `clarity-rework` (commit `17c0334`, readability rework). The brief: stop presenting every teaching point as a full-width green "Key point" banner pinned to the bottom of the slide, and present each point where it belongs, without losing any instruction or qualification. Photographs, backdrops, type scale and the readability splits are kept.

## 1. Technical cause (inspected, not assumed)

- `build/build.py render_slide` appends `keypoint_html(s['key_point'])` to every non-exempt slide's `.foot`; generated layouts (agenda, opener, glossary, recap) render the same box and `checks.split_keypoint` moves it into the footer. The takeaway slides (`layout: takeaway`) never had the box: the habit panel is their takeaway.
- `src/css/base.css`: `.foot{margin-top:auto}` pushes the footer to the bottom of the flex column; `.keypoint` is a filled, full-width, left-ruled box. Pause slides hide it until `.chosen` / `.revealed`.
- The footer is therefore **flow layout, not absolute positioning**, but the `margin-top:auto` footer separates the point from its evidence, and the box sits between the source line and the counter.
- The `key_point` field also feeds presenter notes (`deck.js`), the facilitator guide (`make_docs.py`) and `checks.check_plan_fields` (required on every non-exempt slide). Those stay: the field becomes the notes/guide summary; the on-screen treatment is authored per slide.
- Tests and QA scripts that assert `.keypoint` (`build/tests/test_generated.py`, `build/qa/interact.cjs`) are updated with the migration.

## 2. Component design

One reusable block, in the main content area, participating in the slide's normal grid/stack:

```html
<div class="takeaway">
  <p class="tlabel">Remember</p>                 <!-- optional teal label -->
  <p class="tmain">Knowing names does not prove identity.</p>
  <ul class="tacts"><li>Hang up.</li><li>Call the service desk using its known number.</li><li>Never read out a sign-in code.</li></ul>
  <p class="tnote">Optional qualification in supporting type.</p>
</div>
```

- Typography and spacing only: a 2 px teal top rule, teal small-caps label, main statement at `--t-h3` (28 px) bold in `--text`, supporting lines at `--t-copy` (24 px) in `--text-2` with a short teal dash. No fill, no full-width box.
- `.takeaway.row` (two columns: statement left, support right) for wide diagram slides where height is scarce.
- `.lesson` for a dedicated takeaway slide: one 44 px statement, supporting action lines at body size, vertically centred, generous space.
- Visibility on pause slides: reveal slides wrap the block in the existing `.if-revealed`; vote slides use a new `.if-chosen` (hidden until `.slide.chosen`). `checks.check_open_slide` rejects both on open slides.
- The old `.keypoint` and `.answerbox` styles are removed after migration; `.callout` stays for the SL07 question.

## 3. Decision rules applied (per the brief)

A. Module openers (SL08, SL19, SL28, SL41, SL51, SL60, SL68): no banner. Lesson moved to the next relevant teaching slide unless already present there.
B. Scenario/explanation slides: takeaway inside the aside or beneath the evidence, after the question and any hint, so the order evidence → question → answer is kept. Where the hint or answer box already carried the point, it is merged (one statement, no triple repetition).
C. Diagram/comparison slides: takeaway directly under the diagram/table/cards, same width and alignment.
D. Crowded: SL23 (transcript, question, hint and photograph fill the aside) gets a connected slide SL23B.
E. Dedicated takeaway slide: SL23B only.
F. Functional warnings/exercise controls (stopbox, `.never`, routebanner, feedback, reveal notes) are untouched.
Consolidation: where the banner repeated the slide's own cards, table, findings, lede or feedback verbatim, the duplicate is dropped and the slide uses `.stack.center` where the removal would otherwise leave a gap.

## 4. Bookkeeping

- SL23 6 min → SL23 4 + SL23B 2; `slide_count` 88; module totals and the 420-minute programme unchanged; pause IDs unchanged.
- Notes/sources: SL23B carries S8 and a note; the SL23 answer stays on SL23.
- `validate_package.py` expects 88; `MANIFEST.json` hashes refreshed; docs: `docs/TAKEAWAY_REWORK_2026-10-08.md` (inventory and migration table), CHANGELOG, dist/README, ledger, coverage matrix, QA report.
- Validation: unit tests, strict build, `render.cjs` at 1920×1080 / 1366×768 / 1280×720 / 390×844, `interact.cjs`, manual inspection of every changed slide in default and revealed/chosen states.
