# Layout and asset rules

Use the prototype's cover, email, chat, decision, annotated and case layouts. Additional layouts needed by authored content: profile/comparison, browser/mobile evidence, response card, roleplay/exercise, evidence board, reference index and intermission. Derive these from the same typography, spacing, surfaces and controls. Add only these content-driven patterns; do not build a reusable presentation framework.

## Main copy and density
One main decision or concept per screen. Primary headings should be readable at the projector distance. Since the readability rework of 8 October 2026 the canvas type scale is: title 56, lead 32, h3 28, body 28, evidence copy 26, supporting copy 24, small 20, label 14 canvas px (`src/css/base.css`). Enlarge the relevant evidence instead of shrinking full screenshots; when a slide cannot hold its content at that scale, split it into a continuation slide (`SLxxB`, directly after its parent, dividing the parent’s minutes) rather than shrinking the type. Explanation columns use a thin top rule, not a filled box; boxes are kept for paper evidence mock-ups, interactive controls, the opener outcomes panel and the habit box. Supporting source metadata may be smaller. Do not pack instructions, evidence and answer into one tiny panel. Split content if needed and update the storyboard/timing.

## Neutral evidence
Genuine and suspicious messages share the same initial style. Selection teal means an interaction state, not a verdict. Use amber after a reveal for verification concerns, coral for confirmed harmful outcomes. Add explicit words so colour is never the only meaning. A scene title should not give away a decision before the audience inspects evidence.

## Visual assets
Mock workplace interfaces belong in editable HTML/CSS. No generated image is needed to reproduce a precise email, QR destination, statistic or source fact. Process and comparison diagrams are editable inline SVG with namespaced ids (never rasterised text); icons are decorative companions to written labels, never the only carrier of meaning. Character portraits and scene photographs are AI-generated illustrations of the fictional cast, disclosed on the cover and in About; the IT caller is never shown. Scene photographs sit inside the explanation column, never behind evidence; optional backdrops stay off dense evidence, vote and source slides. Use actual approved logos only when supplied; show course/Meranti text otherwise. Do not imply Meranti is the real customer's brand. Do not generate customer staff faces or recreate actual victims.

If an authentic screenshot is necessary, obtain it from the primary publication, preserve context, redact irrelevant personal identifiers, check reuse rights, and cite it. A reconstruction is labelled as one. Never fetch/display a live malicious page to obtain evidence. Do not include live malicious URLs in click targets.

## Motion and controls
Reveal one conversation entry or evidence layer at a time. Preserve replay/reset controls for teaching. Short fades only. No autoplay, continuous background motion, confetti, alarms or mandatory countdown. An optional activity timer must be pausable and must not navigate automatically.

## Projection and mobile
Desktop slides should fit 1440×900 and 1366×768 in default and designated expanded states. Do not use whole-slide zoom/transform hacks. At 390px, allow one vertical reading flow and keep footer controls reachable, with no horizontal overflow. Overlay previews on desktop may expand inline on mobile. Notes/reference content can scroll inside a dedicated dialog; do not create nested scroll owners for the slide itself.
