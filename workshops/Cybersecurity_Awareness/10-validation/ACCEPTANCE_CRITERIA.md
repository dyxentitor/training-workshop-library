# Acceptance criteria

## Content
- Every planned slide exists or a documented split updates the plan consistently.
- 420-minute programme matches the agenda, including 310 learning/activity and 110 breaks.
- Seven modules, all agreed additions, legitimate requests and action-specific recovery remain covered.
- All facts link to source IDs; fabricated scenes stay labelled. No copied-profile/takeover conflation.
- No unsupported breach statistic, blanket MFA claim or invented customer incident/service commitment.
- Case facts match CLAIMS_AND_CASES.md.

## Design
- Prototype palette, type stack, hierarchy, evidence style and controls stay recognisable.
- Every slide renders at 1440×900 and 1366×768 without unintended clipping in default/key revealed states.
- Expanded previews, long addresses, selected feedback, complete chats and notes/reference dialogs are readable.
- At 390px, no horizontal overflow; one intended vertical slide flow. Navigation stays accessible.
- Contrast checks cover actual text/background/control pairs; do not claim full accessibility compliance from token inspection alone.
- Initial colours/headings do not disclose a decision answer.

## Interaction
- First/last, next/back, Home/End, Page Up/Down and hash entry work for the full count.
- Compact module index supports direct access without 61 crowded dots.
- Sender/destination toggles, chat/replay, decision explanations, reveal/hide and per-slide reset work where specified.
- Notes match active slide; dialogs close with Escape and preserve focus appropriately.
- Keyboard shortcuts do not interfere with native controls/typing.
- Fullscreen fails gracefully if unavailable; touch navigation avoids interactive controls and vertical-scroll gestures.
- Inactive slides cannot receive focus. Status messages/selected state remain understandable without colour.

## Offline/privacy
- file:// opens without server, assets or runtime fetches.
- No CDN/external fonts/analytics; no unexpected network requests while presenting.
- Only explicit source links navigate externally.
- Mock links/files/QRs are inert; no real codes, credential forms, command execution, clipboard writes or support sessions.
- No identifying scores or personal data persistence.

## Evidence of completion
Render and inspect all slides, then record tested states, viewports, failures/fixes and limitations in QA_REPORT.md. Do not fabricate screenshots, browser passes or approvals. Keep the actual source/build command and final output paths. The current package has prototype validation only; the 61-screen build has not happened here.

## Live-delivery gate
Customer reporting/support route, date/venue/prayer arrangements and facilitator rehearsal remain separate confirmation items. Their absence does not block the generic build. Do not represent unconfirmed demo workflow as a customer's verified process.
