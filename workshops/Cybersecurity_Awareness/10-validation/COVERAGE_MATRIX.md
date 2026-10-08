# Coverage matrix

Status as of the v2 clarity rework (76 slides), 2 October 2026. “Implemented” means present in `dist/workshop.html`; “tested” cites `validation/QA_REPORT.md`. “Customer confirmed” is not claimed for anything.

| Requirement | Topic | Location | Status |
|---|---|---|---|
| REQ01 | Full-day timing | all; agenda SL02; breaks SL18/SL40/SL59 | Implemented; build enforces 420 min and module totals |
| REQ02 | Sector-neutral reusable content | M0–M7 (fictional Meranti) | Implemented; config separates customer details |
| REQ03 | Social-media impersonation | SL09–SL16 | Implemented; rendered and checked |
| REQ04 | Public information used in lures | SL10 | Implemented |
| REQ05 | Clone versus compromised account | SL11, SL12–SL12B, SL15–SL15B | Implemented |
| REQ06 | Manager/vendor/BEC | SL03–SL06, SL20–SL26 | Implemented |
| REQ07 | Voice/deepfake | SL07, SL23, SL24 | Implemented; Hong Kong prerecorded/no-interaction detail preserved |
| REQ08 | Polite authority challenge | SL22 | Implemented |
| REQ09 | Email/mobile/QR/files | SL29–SL38 | Implemented; QR tiles non-decodable |
| REQ10 | False signs of safety | SL30, SL32, SL37 | Implemented |
| REQ11 | Genuine sensitive requests | SL26, SL36 (card 3), SL57, SL73 | Implemented |
| REQ12 | MFA/session/device code/consent/linking | SL41–SL49 | Implemented; MFA value and limits stated; glossary on SL41B |
| REQ13 | Teams/support/remote access | SL52, SL53, SL57 | Implemented; no live session |
| REQ14 | ClickFix/CrashFix/callback | SL54–SL56 | Implemented; no command or clipboard action |
| REQ15 | Role-specific tabletop | SL61–SL66 | Implemented; rubric in facilitator guide |
| REQ16 | Actual reporting demonstration | SL70–SL70B | Implemented as labelled demo; customer route pending |
| REQ17 | Response after different mistakes | SL71, SL72 | Implemented |
| REQ18 | Assessment/refresher | SL05, SL73, SL74 | Implemented; no scores collected |
| REQ19 | Primary source attribution | source lines, notes, reference index, dist/SOURCE_INDEX.md | Implemented; recheck 2 Oct 2026 recorded |
| REQ20 | Design consistency/offline/accessibility | prototype base CSS + deck.css | Implemented and tested (render, interaction, contrast); no full WCAG claim |
| REQ21 | Claude full execution and continuity | PROGRESS_LEDGER.md | Implemented |
| REQ22 | Self-explanatory slides: what-line, an on-screen takeaway placed with its evidence (or consolidated into the slide’s own cards/table/feedback), module openers/takeaways, day recap | SL01–SL76 + continuation slides (89) | Implemented; build enforces `key_point` for notes and the pause-slide takeaway rule; tested (docs/TAKEAWAY_REWORK_2026-10-08.md) |
