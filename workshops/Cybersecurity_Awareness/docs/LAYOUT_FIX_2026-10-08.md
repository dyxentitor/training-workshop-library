# Layout fix: spacing, content fit, takeaway placement and footer visibility (8 October 2026)

Scope: `dist/workshop.html` and its sources on branch `clarity-rework`, starting from the uncommitted 88-slide takeaway build (last commit `17c0334`). The brief: fix the remaining stacking, footer-visibility, takeaway-separation and column-alignment defects, with slides 3, 4, 48 and 71 (positions in the 88-slide build) as the named examples, without changing the images, backdrops, type scale, narrative, sequence or interactions. The pre-fix build, QA results and screenshots were kept for comparison (`validation/screenshots/layout-fix/`).

**Slide count: 88 → 89.** One connected explanation slide, SL04B, follows SL04. SL03 and SL04 go from 3 minutes each to 2, SL04B takes 2; the opening module stays 20 minutes and the programme 420.

## Causes found (inspected, not assumed)

1. **The footer on “Another familiar name appears” (SL04) was never there.** Every committed version of `04-content/slides.json` has `source_ids: []` for this slide (it was SL03 before the 2 October renumbering; the S7 citation that moved was the decision slide's, now SL05), and `04-content/modules/M0_CONTENT.md` records it as “Fictional/logistical course design”. The build emits no `.foot` when a slide has no sources, so nothing was hidden, clipped, covered or pushed out. What disappeared from the bottom of this slide in the takeaway rework was the old key-point banner, which had occupied the footer position. No citation was invented for SL04: its evidence is fictional and its question has no external claim. The two teaching points for scenes 01 and 02 now sit on SL04B, which cites S7 (FBI IC3 BEC) with the same “Fictional scenario. Guidance:” line as SL03, SL05 and SL06. S7 supports the independent-check claim (“use secondary channels … to verify requests for changes in account information”); it does not mention urgency, so the “pressure is a reason to slow down” line remains course guidance, as it was.
2. **Takeaway rules touching the element above (10 slides).** `.takeaway` is a top-rule block with no outer margin. Wherever it followed a sibling inside a container that has no `gap` (the slide itself on SL37, SL38, SL42, SL43, SL61B, SL66B, SL71; a plain column on SL07 and SL48; the reveal wrapper on SL06) the 2 px teal rule sat at 0 px on the cards, table, diagram or findings above. Containers with a gap (`.stack`, `.side`, `.findings`) were fine, which is why the defect looked inconsistent.
3. **“How the tabletop runs” (SL61B) and “What the evidence supports” (SL66B).** Both used `.grid.even.mid` (`align-items:center`) and the grid's `flex:1`, so the two panels floated in the middle of the body at different heights, with a large gap under the introduction and another above the full-width takeaway, which split its statement and support into two columns.
4. **Footer region not reserved.** `.foot{margin-top:auto}` in a flex column pushed the source line down when content grew, so a tall state moved the footer into the bottom padding (the previous fit rule tolerated 24 px of this) instead of showing the overflow. Nine states sat within 0–8 px of the footer.
5. **Questions and answers on one screen (SL03, SL04).** Both open slides showed the discussion question and its takeaway together, so the room read the answer before discussing. SL13, SL14, SL34, SL35, SL44 and SL56 also show a labelled answer under their question; those labels (“What Aina should do”, “The safer route”, “After the exercise”) were the agreed treatment in the takeaway rework and are unchanged.

## The treatment

- **Slide grid (`src/css/base.css`).** Every slide is now a three-row grid: `auto minmax(0,1fr) auto` for the header, the body (wrapped by the build in `<div class="body">`) and the footer. The footer row takes the source line's actual height (a wrapped line takes more), the body row is exactly what remains, and body content that does not fit shows over the footer instead of moving it. `build/qa/render.cjs` now fails any landscape state whose body content ends below the footer's top edge (or below the 840 px padding line on slides without a source line); the old 24 px tolerance is gone. Narrow screens use `auto 1fr auto` so the page still grows; print uses three auto rows.
- **One spacing rule for takeaways.** A `.takeaway` that follows a sibling inside a container without its own gap gets `margin-top: var(--sp-4)` (24 px); containers that already space their children (`.stack`, `.side`, `.findings`, `.record`, cards, panels, grids) are excluded, so nothing is double-spaced. The vote-slide gap between the feedback box and its takeaway is 14 px (was 10) and the feedback box's vertical padding is 10 px (was 12).
- **SL03.** The email, its three numbered findings and the question stay; the takeaway moved to SL04B. The question is the discussion prompt (“Discuss with the room” label, `h3.big-question`), matching SL04.
- **SL04.** The chat stays dominant; the aside holds the discussion question and the photograph at the standard scene size (270 px, the same as SL20 and SL23; the 1859 × 846 image shows uncropped with the face intact). No takeaway on the slide.
- **SL04B “What the two messages can prove”.** Two takeaway blocks side by side, centred as one group: “The email · 16:42” (sender address and familiar conversation prove nothing; bank changes need an independent check) and “The chat · 16:46” (display name and urgency prove nothing; anyone can set a name and copy a photo; pressure to skip a check is a reason to slow down). Source S7. Presenter notes added; SL04's notes point forward to it.
- **SL42 (#49).** Cards and takeaway in a flow stack with a 24 px gap; the takeaway is a row: the statement left, “None of them needs your password to be shared” and “Check what access you are granting: what does it give? To whom? Did you start it?” right. The four mechanisms and their explanations are unchanged.
- **SL61B (#72).** Flow stack: the two panels top-aligned directly under the introduction, then one stacked takeaway block (“You do not need the full picture to report.” / “Report what you saw and let the right team connect the dots.”). The four recorded items, the run order and the causation warning are unchanged.
- **SL66B (#78).** Same flow treatment as SL61B.
- **Fit corrections under the stricter rule.** SL11 aside uses `.side.tight`; SL43 uses the brief takeaway split; SL57's evidence cards are 0.9 / 1.1 so the longer chat quotation keeps to two lines. No text size was reduced and no content was removed.

## Original → updated mapping (positions in the on-screen counter)

| SL01 · The request before 5 PM | 1 → 1 | retained; slide grid and body wrapper only |
| SL02 · Today’s workshop | 2 → 2 | retained; slide grid and body wrapper only |
| SL03 · A request that fits the job | 3 → 3 | takeaway moved to SL04B; question promoted to the discussion prompt (2 min) |
| SL04 · Another familiar name appears | 4 → 4 | takeaway moved to SL04B; photograph at the standard scene size under the question (2 min) |
| SL04B · What the two messages can prove | — → 5 | new: explanation stage for scenes 01 and 02 (2 min, S7) |
| SL05 · What should Farid do next? | 5 → 6 | retained; slide grid and body wrapper only |
| SL06 · The callback changes the picture | 6 → 7 | revealed takeaway now 24 px below the findings (shared rule) |
| SL07 · When the meeting looked convincing | 7 → 8 | takeaway now 24 px below the callout (shared rule) |
| SL08 · Module 1: The borrowed identity | 8 → 9 | retained; slide grid and body wrapper only |
| SL09 · Impersonation and phishing | 9 → 10 | retained; slide grid and body wrapper only |
| SL09B · One message can do all three | 10 → 11 | retained; slide grid and body wrapper only |
| SL10 · What can someone learn about Aina? | 11 → 12 | retained; slide grid and body wrapper only |
| SL11 · Two profiles with the same face | 12 → 13 | dense aside uses the tight gap so the vote takeaway clears the footer row |
| SL12 · A genuine account, an unusual request | 13 → 14 | retained; slide grid and body wrapper only |
| SL12B · Two checks before sharing the list | 14 → 15 | retained; slide grid and body wrapper only |
| SL13 · The support page that found you | 15 → 16 | retained; slide grid and body wrapper only |
| SL14 · A collaboration that sounds relevant | 16 → 17 | retained; slide grid and body wrapper only |
| SL15 · Someone is using your name | 17 → 18 | retained; slide grid and body wrapper only |
| SL15B · Copied profile or taken-over account? | 18 → 19 | retained; slide grid and body wrapper only |
| SL16 · Verify before you classify | 19 → 20 | retained; slide grid and body wrapper only |
| SL17 · Module 1 takeaways | 20 → 21 | retained; slide grid and body wrapper only |
| SL18 · Short break | 21 → 22 | retained; slide grid and body wrapper only |
| SL19 · Module 2: The trusted request | 22 → 23 | retained; slide grid and body wrapper only |
| SL20 · An urgent request from the manager | 23 → 24 | retained; slide grid and body wrapper only |
| SL21 · What the pressure asks you to skip | 24 → 25 | retained; slide grid and body wrapper only |
| SL22 · A polite way to pause | 25 → 26 | retained; slide grid and body wrapper only |
| SL23 · The voice on the phone | 26 → 27 | retained; slide grid and body wrapper only |
| SL23B · What proves who is calling? | 27 → 28 | retained; slide grid and body wrapper only |
| SL24 · A face or voice cannot approve a payment | 28 → 29 | retained; slide grid and body wrapper only |
| SL25 · Which number will you call? | 29 → 30 | retained; slide grid and body wrapper only |
| SL26 · Keep the process when the request is genuine | 30 → 31 | retained; slide grid and body wrapper only |
| SL27 · Module 2 takeaways | 31 → 32 | retained; slide grid and body wrapper only |
| SL28 · Module 3: The message that fits your job | 32 → 33 | retained; slide grid and body wrapper only |
| SL29 · A message that fits your work | 33 → 34 | retained; slide grid and body wrapper only |
| SL30 · The sender behind the display name | 34 → 35 | retained; slide grid and body wrapper only |
| SL31 · The destination behind the label | 35 → 36 | retained; slide grid and body wrapper only |
| SL32 · A polished message can still deceive | 36 → 37 | retained; slide grid and body wrapper only |
| SL33 · The same request on a phone | 37 → 38 | retained; slide grid and body wrapper only |
| SL33B · The same text message, inspected | 38 → 39 | retained; slide grid and body wrapper only |
| SL34 · A QR code moves the request | 39 → 40 | retained; slide grid and body wrapper only |
| SL35 · A shared file is still a request | 40 → 41 | retained; slide grid and body wrapper only |
| SL36 · Would you approve this? | 41 → 42 | retained; slide grid and body wrapper only |
| SL37 · The signals that do not prove safety | 42 → 43 | takeaway row now 24 px below the table (shared rule) |
| SL38 · Your verification route | 43 → 44 | takeaway row now 24 px below the route cards (shared rule) |
| SL39 · Module 3 takeaways | 44 → 45 | retained; slide grid and body wrapper only |
| SL40 · Lunch break | 45 → 46 | retained; slide grid and body wrapper only |
| SL41 · Module 4: Beyond the password | 46 → 47 | retained; slide grid and body wrapper only |
| SL41B · Words we will use | 47 → 48 | retained; slide grid and body wrapper only |
| SL42 · Access can be granted without sharing a password | 48 → 49 | cards and takeaway in a flow stack; takeaway as a row with the practical check as its second line |
| SL43 · The login session an attacker can reuse | 49 → 50 | takeaway row uses the brief split (short statement, long support) so it clears the footer row |
| SL44 · An approval you did not start | 50 → 51 | retained; slide grid and body wrapper only |
| SL45 · A real sign-in page, someone else’s code | 51 → 52 | retained; slide grid and body wrapper only |
| SL45B · Whose device the code would sign in | 52 → 53 | retained; slide grid and body wrapper only |
| SL46 · The app asking for your permission | 53 → 54 | retained; slide grid and body wrapper only |
| SL47 · Linking another device | 54 → 55 | retained; slide grid and body wrapper only |
| SL47B · Joining a group or linking a device? | 55 → 56 | retained; slide grid and body wrapper only |
| SL48 · A defence that stopped the attempted access | 56 → 57 | takeaway now 24 px below the timeline (shared rule) |
| SL49 · What does this approval grant? | 57 → 58 | retained; slide grid and body wrapper only |
| SL50 · Module 4 takeaways | 58 → 59 | retained; slide grid and body wrapper only |
| SL51 · Module 5: The helpful stranger | 59 → 60 | retained; slide grid and body wrapper only |
| SL52 · Mei offers help in chat | 60 → 61 | retained; slide grid and body wrapper only |
| SL53 · Remote access changes the stakes | 61 → 62 | retained; slide grid and body wrapper only |
| SL54 · The verification page asks too much | 62 → 63 | retained; slide grid and body wrapper only |
| SL54B · What that step would actually do | 63 → 64 | retained; slide grid and body wrapper only |
| SL55 · A browser problem becomes a repair request | 64 → 65 | retained; slide grid and body wrapper only |
| SL56 · The notice asks you to call | 65 → 66 | retained; slide grid and body wrapper only |
| SL57 · Which support request can you proceed with? | 66 → 67 | evidence cards widened for the longer quotation (0.9 / 1.1) so the vote takeaway clears the footer row |
| SL58 · Module 5 takeaways | 67 → 68 | retained; slide grid and body wrapper only |
| SL59 · Tea break | 68 → 69 | retained; slide grid and body wrapper only |
| SL60 · Module 6: Stop the chain | 69 → 70 | retained; slide grid and body wrapper only |
| SL61 · Your team at Meranti | 70 → 71 | retained; slide grid and body wrapper only |
| SL61B · How the tabletop runs | 71 → 72 | panels top-aligned in a flow stack; takeaway as one stacked block |
| SL62 · Evidence 1: the document invitation | 72 → 73 | retained; slide grid and body wrapper only |
| SL63 · Evidence 2: the account approval | 73 → 74 | retained; slide grid and body wrapper only |
| SL64 · Evidence 3: the bank change | 74 → 75 | retained; slide grid and body wrapper only |
| SL65 · Evidence 4: someone offers help | 75 → 76 | retained; slide grid and body wrapper only |
| SL66 · What stopped the chain? | 76 → 77 | retained; slide grid and body wrapper only |
| SL66B · What the evidence supports | 77 → 78 | panels top-aligned in a flow stack (was vertically centred) |
| SL67 · Module 6 takeaways | 78 → 79 | retained; slide grid and body wrapper only |
| SL68 · Module 7: Report and recover | 79 → 80 | retained; slide grid and body wrapper only |
| SL69 · Pause, verify, report, recover | 80 → 81 | retained; slide grid and body wrapper only |
| SL70 · Your actual reporting route | 81 → 82 | retained; slide grid and body wrapper only |
| SL70B · Your organisation’s route | 82 → 83 | retained; slide grid and body wrapper only |
| SL71 · What happened determines the response | 83 → 84 | takeaway row now 24 px below the cards (shared rule) |
| SL72 · A useful report | 84 → 85 | retained; slide grid and body wrapper only |
| SL73 · A new request, the same decision | 85 → 86 | retained; slide grid and body wrapper only |
| SL74 · The check you will use tomorrow | 86 → 87 | retained; slide grid and body wrapper only |
| SL75 · Today’s takeaways | 87 → 88 | retained; slide grid and body wrapper only |
| SL76 · Questions and references | 88 → 89 | retained; slide grid and body wrapper only |

## Validation

See `validation/QA_REPORT.md`, section “Layout fix (8 October 2026): 89 slides”.
