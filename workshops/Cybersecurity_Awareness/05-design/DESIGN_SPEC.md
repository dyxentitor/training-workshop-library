# Design specification · v1

Status: supplied visual direction for the full build. The user has authorised the preparation of the full execution package. No separate aesthetic approval has been recorded. Continue the build using this baseline and report material deviations.

## Direction
A dark workplace investigation. Realistic light-coloured email and chat evidence, restrained accents, large text and controlled reveals. Reusable across sectors. Meranti and all story characters are fictional. Preserve readable examples and facilitator control.

## Tokens and implementation authority
`prototype.html` is the executable visual baseline. Its `:root` defines authoritative colour tokens:

| Token | Value | Use |
|---|---|---|
| background | #0B1220 | Slide canvas |
| surface | #162236 | Dark panels and controls |
| text-primary | #F3F6FA | Main text |
| text-secondary | #B8C4D6 | Supporting text |
| accent | #2DD4BF | Interaction and identity |
| info | #60A5FA | Source links |
| warning | #FBBF24 | Verification concerns after a choice/reveal |
| danger | #FB7185 | Reserved for confirmed harmful consequences |
| ink | #19283B | Text on light evidence |
| line | #33445B | Dark borders |

Font: Arial, Helvetica, sans-serif. This deliberate offline system-font implementation avoids external downloads. Do not silently substitute another font. If user later approves bundled Inter, update the reference screenshots and version together.

Desktop: 68px masthead, 74px footer, 4vw side gutters, 18–34px major gaps, 18px main panel radius, 9px control radius. Headings scale within explicit CSS clamps. Body examples are 21–22px, discussion questions 27–32px. Supporting UI metadata can be smaller. Avoid shrinking main evidence to solve overflow. The 80px cover heading is an intentional exception to content-slide typography.

## Components
- `.cover`, `.scene`, `.notification`, `.cast`: narrative introduction.
- `.grid`, `.mail`, `.mailbar`, `.mailbody`, `.sender`, `.details`, `.attachment`: email inspection.
- `.chat`, `.chathead`, `.chatstream`, `.bubble`, `.chatcontrols`: message progression.
- `.choices`, `.choice`, `.feedback`: decision and explanatory feedback.
- `.findings`, `.finding`, `.callout`, `.mark`: evidence and conclusion.
- `.casegrid`, `.stat`, `.timeline`, `.event`, `.source`: documented incident.
- `.top`, `.bottom`, `.dots`, `.nav`, `.modal`: presentation shell.

Reuse these classes. Use existing layouts when extending. Add a new component only when content needs it and document the reason. Do not redesign the whole deck when adding content.

## Colour and evidence rules
Suspicious evidence stays neutral until the learner decides or the trainer reveals findings. Do not add red banners or icons that disclose the answer. Colour must accompany text. A matching sender or genuine domain does not prove account control. Show uncertainty honestly. Character initials are identity aids, not a security judgement.

## Interaction contract
Navigation: arrows, Page Up/Down, Home/End, numbered dot buttons, footer buttons, horizontal swipe on noninteractive space. N opens current notes, F toggles fullscreen. Escape closes dialogs. No autoplay. Keep decision state on navigation; reload resets it. No persistent personal data.

Slide-specific reveals occur only through explicit controls. Native buttons expose expanded/pressed states. Feedback uses a live region. Native dialogs trap focus and support Escape. Respect reduced motion. Keep a visible focus indicator.

## Responsive and offline behaviour
No remote assets, libraries, fonts, analytics, fetch calls, credential forms or live attack destinations. Source links are explicit outbound navigation. Desktop layouts should fit 1440×900 and 1366×768 in default states. Small screens below 900px stack panels and allow vertical reading with sticky navigation. Never scale the entire deck as an image. Print stylesheet is a convenience, not a separate verified PDF deliverable.

## Evidence and source policy
Fictional story slides carry a scenario label. Real incidents show source and date. Never invent victim messages or pass recreations off as original captures. The Hong Kong case describes prerecorded video and no interaction. Links and domains in mock messages are reserved `.example` addresses. Attachment and destination controls never navigate to them.

## Extension limits
Customer logo, date, reporting contacts and role-specific examples may change after confirmation. Palette, visual hierarchy, shell, component states, typography and overall rhythm should remain stable. Keep service claims and reporting details as explicit placeholders until confirmed. Retain sector-neutral core content.

Desktop inspection details appear as overlays within the email to preserve canvas height. On mobile they expand inline. Keep both states readable. The case statistic is capped at 94px to fit its column. Final viewport-specific overrides in prototype.html take precedence over earlier defaults.
