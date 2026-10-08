# Workshop visual audit

**Workshop:** Cybersecurity Awareness: Impersonation and Phishing (fictional organisation “Meranti”), full-day HTML workshop, 76 slides.
**Audit date:** 8 October 2026. **Companion file:** `WORKSHOP_VISUAL_ASSET_MANIFEST.json` (same IDs, slide mappings, filenames and priorities).
**Scope of this document:** analysis and production specifications only. No images were generated and no workshop file was changed.

How to read priorities: **Essential** = needed to explain a concept or fix a substantial visual problem. **Recommended** = materially improves understanding or engagement. **Optional** = adds atmosphere with limited teaching benefit. **None** = the slide already works well.

Everything marked *measured* was taken from the rendered deck in canvas pixels (the deck is authored on a 1600×900 canvas and scaled to the screen). Everything marked *proposed* is a specification to be confirmed when the asset is placed.

---

## 1. Workshop identity, files reviewed and review limitations

### 1.1 Entry point and version (verified)

| Item | Finding |
|---|---|
| Live entry point | `Cybersecurity_Awareness_Claude_Package/dist/workshop.html` (single self-contained file, 644 KB; styles, script, slide data, notes and avatars embedded). Opened by double-click, offline, no server. |
| Version in use | The **v3 presentation redesign of 8 October 2026** (menu drawer, 1600×900 scaled canvas, consolidated tokens, redesigned cover). Evidence: `docs/REDESIGN_NOTE_2026-10-08.md`; `CHANGELOG.md` top entry; `validation/QA_REPORT.md` v3 section; `dist/workshop.html` modified 2026-10-08 03:54 local; git branch `clarity-rework` with the redesign **uncommitted** in the working tree (`master` holds the older v1/v2 builds). |
| Other versions present | `06-prototype/prototype.html` (six-slide v1 prototype with a bottom toolbar and dots). Superseded; kept as a reference baseline. Not audited as a deliverable. |
| Slide count and order | 76 slides, SL01–SL76. The order in `04-content/slides.json`, the embedded `#deck-data` block and the `<section>` order in the built file were compared and are identical. |
| Built from | `04-content/slides.json` (titles, timing, notes, decision options, source IDs), `src/slides/M0–M7.html` (slide bodies), `src/content/{choices,notes,modules,source-groups}.json`, `src/css/{base,deck}.css`, `src/js/deck.js`, `src/shell.html`, `config/customer-config.json`, `02-research/sources.json`; builder `build/build.py` with `build/generated.py` (openers, takeaways, agenda, recap) and `build/avatars.py`. |
| Customer state | All customer fields in `config/customer-config.json` are null/unverified: date, venue, organisation, reporting route, support contact and `reporting.screenshot_asset`. SL38, SL70 and About show bracketed placeholders. |

### 1.2 Files reviewed

- Presentation: `dist/workshop.html`; `src/shell.html`; `src/js/deck.js` (reveal, vote, reset, drawer logic); `src/css/base.css` (tokens, canvas, shell, overlays); `src/css/deck.css` (all slide components).
- Slide content: `src/slides/M0.html` … `M7.html` (61 fragments); `04-content/slides.json` (all 76 records: what-line, key point, notes, options, sources); `src/content/choices.json` (vote feedback), `src/content/notes.json` (extended presenter notes for every slide), `src/content/modules.json`, `src/content/source-groups.json`; `build/generated.py` (how the 15 generated slides are assembled); `build/build.py` (tokens, QR tile generator, source lines, placeholders).
- Design instructions, latest first: `docs/REDESIGN_NOTE_2026-10-08.md`; `docs/superpowers/specs/2026-10-02-deck-clarity-rework-design.md` (photos decision, pause points, explanation layer); `05-design/DESIGN_SPEC.md`, `05-design/LAYOUT_AND_ASSET_RULES.md`, `05-design/TEMPLATE_CATALOG.md`, `05-design/design-tokens.json` (earlier v1 baseline; where it differs, the later files win).
- Research and sources: `02-research/sources.json` (S1–S21), `02-research/CLAIMS_AND_CASES.md` (what may and may not be shown for each real case; statistics policy), `dist/SOURCE_INDEX.md`.
- Facilitation: `dist/facilitator-guide.md`, `08-facilitator/TABLETOP.md`, `08-facilitator/ASSESSMENT.md`, `04-content/INTERACTION_STATES.md`.
- Existing visual assets: `dist/Image_ref/profile-pictures/*.png` (9 portraits + README), `dist/Image_ref/random-person.jpeg`, `random-person2.jpeg`, `dist/Image_ref/Cybersecurity-Awareness-Profile-Pictures.zip`, `src/img/avatars/*.jpg` (9), `06-prototype/reference_screenshots/*.png`, generated QR tiles in the build.
- Validation: `validation/QA_REPORT.md`, `validation/qa-results.json`, `validation/interaction-results.json`, `validation/screenshots/{1920x1080,1366x768,1280x720,390x844,firefox}`.

### 1.3 Rendering performed for this audit (verified)

- Fresh renders of **all 76 slides at 1920×1080 and 1366×768** in headless Chromium (playwright-core 1.55.1, Chromium build 1234), default state plus every vote option and every revealed state (93 frames at 1920×1080, 121 at 1366×768), plus the open menu drawer. Every frame was inspected visually.
- A measurement pass recorded, per slide, the header block, each content column’s box and the top of the Key point footer in canvas pixels. Placement coordinates in this report come from that pass.
- Layout facts used throughout (measured): header strip y 0–72; title block y 96–226 on content slides; evidence/explanation area starts y 258; the Key point footer starts at y 744 on ordinary content slides and y 806 on pause-point slides (where the Key point is hidden until the vote/reveal); horizontal safe area x 80–1520. Standard column boxes: two-column `.grid` left x 80–882 and right x 926–1520 (594 px wide); `.grid.wide` right x 1003–1520; `.grid.even` right x 822–1520 (698 px wide).

### 1.4 Limitations

- **Not tested on a physical projector**, Safari, Edge or interactive Firefox (the project’s own QA has the same gap). Colour and contrast judgements are from rendered pixels on a calibrated-neutral assumption; projected gamma will lift the navy, which argues for keeping backdrops darker than they look on a monitor.
- Interaction states were exercised programmatically; the three-option votes and the reveals behave as the QA report describes. No screen-reader session.
- Facilitator timing, speech and room layout were not observed; recommendations about engagement assume a projected session in a meeting room with tables.
- The contents of the two unused `random-person*.jpeg` files were inspected visually; the apparent embedded text mark on `random-person2.jpeg` should be confirmed at full size before any use.
- Nothing in this report changes the workshop. Asset dimensions and placements are proposals derived from the current layout; the implementer must re-run `build/qa/render.cjs` (fit) and `build/qa/interact.cjs` (contrast, safety) after placing any asset.

---

## 2. Main visual findings and overall art direction

### 2.1 What the deck already does well

- **A coherent, restrained system.** Dark navy canvas, two navy surfaces, warm-white text, teal reserved for emphasis and primary actions, amber for numbered markers and warnings, coral only for confirmed harm, and a light “paper” palette for everything that is evidence (email, chat, documents, screens). Arial/Helvetica throughout. Borders are used once per surface; no gradients, shadows or glows. This is the direction to keep.
- **Evidence is editable HTML, not pictures.** Every email, chat, profile, browser page, consent screen, phone and QR tile is built from components (`.mail`, `.chat`, `.profile`, `.browser`, `.phone`, `.qrsvg`). Wording, addresses and markers can be changed without touching an image. This is exactly right for a workshop that must stay inert, offline and sector-neutral.
- **Minimal shell.** Brand mark top-left, module label and hamburger menu top-right, slide counter bottom-right. Drawer with slide index, notes, sources, fullscreen, keyboard help, About and per-slide reset. Nothing permanent at the bottom. **This audit does not recommend any change to the shell.**
- **Consistent structure.** Label → title → one-line “what this slide shows” → evidence and explanation → Key point → source line. Participants always know where to look.
- **Honest colour.** Suspicious evidence stays neutral until a vote or reveal; the verdict words (“Recommended”, “Reconsider”, “Verify first”) always accompany colour.
- **Nine AI-generated portraits** in a matching studio style are used consistently as avatars, cast strips and role cards, with the disclosure on the cover and in About.

### 2.2 What is visually missing

1. **Three mechanisms are explained in words that need a picture.** The relayed sign-in (SL43), the device-code trick (SL45) and the “paste into a system tool” consequence (SL54) describe something happening *between* machines and people. The current layouts show screens side by side but not who sits where or where the access goes. For an audience with limited security knowledge these are the slides most likely to be nodded through without understanding.
2. **Abstract categories look identical.** The four kinds of access grant (SL42), the three verification routes (SL38), the four Pause/Verify/Report/Recover steps (SL69) and the four “what happened” cards (SL71) are rows of same-shaped cards whose only difference is text. From the back of a room they blur. A small, consistent line-icon set gives each category a shape that recurs across the day and can carry into the printed response card.
3. **Two comparisons show only one side.** SL33 says a desktop would show more detail but only shows the phone. SL12 defines cloning versus takeover in a single sentence that participants will need again on SL15 and SL36.
4. **The tabletop debrief talks about a chain that is never drawn** (SL66).
5. **Breaks and module openers are large plain fields.** This is a deliberate calm, and it should stay calm. A single, very quiet backdrop family can mark “new module” and “break” without introducing a second visual language.
6. **No workplace imagery at all.** Portraits aside, the day is 420 minutes of panels and text. Two believable scene photographs of existing characters, in the scenes that are otherwise read aloud (the phone call, the deadline chat), would give the room a face for “you” without adding decoration everywhere.

### 2.3 What should *not* be added

- No images on evidence slides (email, chat, browser, phone, consent, QR): the evidence must remain the only thing to read.
- No images on pause-point slides (votes and reveals): nothing should compete with the three options or the hidden answer.
- No “deepfake” or hacker imagery on SL24 or SL07; no stock padlocks, hooded figures, binary rain, glowing shields.
- No charts built on the two statistics in the presenter notes until the data and policy questions in §4 (CHART-001) are settled.
- No logos or letterheads (SL32, SL35, SL37): the lesson is that these prove nothing.
- No pictures of the IT caller’s face (SL23): the caller must remain unverifiable.

### 2.4 Art direction for all new assets (keep the established direction)

| Element | Rule for new assets |
|---|---|
| Palette | Diagrams use only the tokens: navy `#0B1220` / surfaces `#141E30`, `#1B2840`; lines `#2A3A52`, `#405572`; text `#F3F6FA`, `#B4C0D2`, `#8A98AE`; teal `#2DD4BF` for the safe route, emphasis and “interaction”; amber `#FBBF24` only for the thing to notice (a marker, a warning); coral `#FB7185` only for confirmed harm or a prohibited action; paper `#FFFFFF`, `#F3F6FA`, `#E8EEF5` with ink `#19283B` for anything that represents a screen or document. Photographs are desaturated slightly and colour-graded toward cool neutrals so they sit on navy; a single warm accent (desk lamp, late light) is allowed. |
| Line and shape | 2 px strokes at canvas scale; corner radii 8 / 14 / 20 px; node boxes follow `.card`/`.ev` styling (dark cards for explanation, paper cards for screens). Arrows plain, 2 px, with simple triangular heads; no 3-D, no shadows. |
| Type in diagrams | Arial/Helvetica; labels 18–21 px canvas (never below 18 px); eyebrow labels 13 px uppercase tracking 1.5 px in `#8A98AE`. Text stays editable: diagrams are SVG with real `<text>` or HTML. |
| Colour meaning | Teal = the safe/independent route or the person acting legitimately; amber = the thing being abused or the clue; coral = the harmful outcome; grey dotted = unknown / not established. Words always accompany colour. |
| Photographs | Believable Malaysian office interiors, natural light, shallow depth of field, no visible brand logos, no readable screen text, no real company names. Characters match the portrait references exactly (face, hair, hijab colour, glasses, clothing style). No new characters’ faces. |
| Icons | Single-weight line icons, 2 px stroke on a 48 px grid, rounded joins, `currentColor` so they inherit text colour; teal when they mark a safe route, text-2 grey otherwise. |
| Backdrops | Never behind body text. Maximum ~10 % luminance variation over the navy; readable text contrast must stay ≥ 7:1 for titles and ≥ 4.5:1 for body (the QA script checks this). |
| Format and embedding | The deck’s Content-Security-Policy allows images only as `data:` URIs and the build rejects remote assets, so every raster is embedded (keep each ≤ 180–250 KB JPEG) and every diagram is inline SVG or HTML. |

---

## 3. Complete slide-by-slide audit

All 76 slides, in presentation order. The stable locator is the `data-slide` section in the source fragment, or the generator for the 15 slides built from `slides.json`. Interaction states that matter for the visual are listed beneath the slide.

| Slide | Stable ID / source locator | Module and title | Main learning point | Existing visuals | Recommended addition or change | Asset ID(s) | Placement | Priority | Reason |
|---|---|---|---|---|---|---|---|---|---|
| 01 | SL01 · src/slides/M0.html · section[data-slide="SL01"] | Opening: The request before 5 PM | Establish the fictional cast and the baseline decision: what would you check before paying? | Cover headline; HTML email mock (Nadia portrait avatar EX-005); fictional-scenario credit line | Optional subtle backdrop behind the left column only; no new foreground image | BG-001 | Full-canvas background layer, focal interest confined to x 0–740 (left column), darkened so headline stays ≥ 7:1 | Optional | Headline and email are already the two agreed focal points; a third foreground image would compete. A barely visible dusk-office backdrop adds opening atmosphere without touching readability. |
| | ↳ interaction states | | | | State 2 (“Open the first message”): email expands to full message plus PDF attachment line; backdrop must stay clear behind the taller email card (x 789–1520, y 200–660). | | | | |
| 02 | SL02 · generated by build/generated.py (layout=agenda) from 04-content/slides.json id SL02 | Opening: Today’s workshop | Today is about one habit: when a message asks for money, information or access, check it through a route you already trust. | Two-column text: outcomes, ground rules, day list; Key point | No additional visual | — | — | None | The day list is already a clean ordered map and the build forbids clock times; an agenda graphic would duplicate it. |
| 03 | SL03 · src/slides/M0.html · section[data-slide="SL03"] | Opening: A request that fits the job | A correct sender address and a familiar conversation do not prove who is writing. A change to bank details always needs an independent check. | Annotated HTML email with three amber markers; marker legend | No additional visual | — | — | None | The email is the evidence and is already annotated in editable HTML; any added picture would distract from reading the sender line and attachment path. |
| 04 | SL04 · src/slides/M0.html · section[data-slide="SL04"] | Opening: Another familiar name appears | A display name and urgency tell you nothing about who controls the account. Pressure to skip a check is a reason to slow down. | HTML chat with Ravi portrait (EX-004), three bubbles; discussion question | Optional scenario image of Farid under deadline pressure in the empty right-column area | IMG-002 | Right column x 926–1520, y 500–760 (measured free area below the hint ends at y 565 at 1920 → canvas 486); image 594×270 canvas px | Optional | Chat evidence works alone. A believable photo of Farid at his desk at 16:46 humanises the story for a first-time audience and is reusable on SL20. |
| 05 | SL05 · src/slides/M0.html · section[data-slide="SL05"] | Opening: What should Farid do next? | Verify through a contact you already hold, such as the supplier record, then follow the normal approval process. Replying to the same email cannot verify anything. | Decision cards A/B/C; feedback box | No additional visual | — | — | None | Pause-point slide: anything beside the three options dilutes the vote. The free band (y 647–806) is used by the Key point once a choice is made. |
| | ↳ interaction states | | | | Choice states: A and B show “! Reconsider” amber feedback; C shows “✓ Recommended” teal feedback and reveals the Key point. | | | | |
| 06 | SL06 · src/slides/M0.html · section[data-slide="SL06"] | Opening: The callback changes the picture | Independent verification gives you facts the message never could. Hold the payment, keep the evidence and report. | Email recap (unmarked until reveal); revealed findings 01–03 and amber highlights | No additional visual | — | — | None | The reveal already changes the picture (highlights appear, findings fill the right column to y ≈ 715). No room and no need. |
| | ↳ interaction states | | | | Revealed state: two sentences highlighted amber in the email; three numbered findings; Key point appears. | | | | |
| 07 | SL07 · src/slides/M0.html · section[data-slide="SL07"] | Opening: When the meeting looked convincing | Even a convincing meeting can be fabricated. A separate, authorised payment check is what stops the loss. | Large stat “HK$200m”, three-event timeline, callout | No additional visual | — | — | None | The stat-plus-timeline is already the clearest form for a documented case; the source policy forbids victim imagery or reconstructed screens. |
| 08 | SL08 · generated by build/generated.py (layout=opener) from 04-content/slides.json id SL08 | Module 1 · The borrowed identity: Module 1: The borrowed identity | Identity on a screen is easy to borrow. Verify the person through a route you already trust. | Generated opener: why-line, cast portraits (Aina, Siti, Daniel, Farid), outcomes panel | Optional reusable opener backdrop | BG-002 | Full canvas, texture confined to top band y 0–190 and lower-right y 520–900; text columns stay on plain navy | Optional | Openers have empty bands above the title (y 72–200) and below the outcomes panel. One shared, very quiet backdrop marks “new module” without adding a new theme. |
| 09 | SL09 · src/slides/M1.html · section[data-slide="SL09"] | Module 1 · The borrowed identity: Impersonation and phishing | Impersonation borrows a trusted identity; phishing asks you to act; spear phishing aims at you specifically. One message can do all three. | Three definition cards; three-step white sequence with arrows and labels | No additional visual | — | — | None | The three-step sequence already functions as the diagram and the slide is full (content to y 707 of 744). An overlap/Venn drawing would repeat the key point. |
| 10 | SL10 · src/slides/M1.html · section[data-slide="SL10"] | Module 1 · The borrowed identity: What can someone learn about Aina? | Public work details make a fake message feel expected. Knowing them does not prove the sender works with you. | HTML social profile with five amber markers; legend | No additional visual | — | — | None | The annotated profile is the teaching object; markers map 1:1 to the legend. |
| 11 | SL11 · src/slides/M1.html · section[data-slide="SL11"] | Module 1 · The borrowed identity: Two profiles with the same face | You cannot tell from the screen. Photos, names, posts and follower counts can all be copied. Contact the person through the staff directory. | Two side-by-side HTML profiles with identical Aina portrait; stacked vote | No additional visual | — | — | None | The comparison is the visual. The identical photos are the point and are already in place. |
| | ↳ interaction states | | | | Vote states: A/B → “The screen cannot tell you that” (amber); C → “Verify outside both profiles” (teal) and Key point. | | | | |
| 12 | SL12 · src/slides/M1.html · section[data-slide="SL12"] | Module 1 · The borrowed identity: A genuine account, an unusual request | A genuine account can still be used by someone else, and even a genuine request needs permission. Verify the purpose separately and share only what is needed. | HTML chat (Siti portrait EX-006) with highlight; two findings; hint sentence on cloning vs compromise | Add a compact clone-versus-takeover comparison diagram under the hint | INFO-001 | Right column x 926–1520, y 575–705 (measured free: hint ends y 557, foot starts 715); 594×130 canvas px | Recommended | The hint sentence introduces the module’s hardest distinction in one line of text. A two-panel picture (copied account beside the real one; stranger behind the real account) lets participants see why both cases produce the same message, and prepares the SL15 table. |
| 13 | SL13 · src/slides/M1.html · section[data-slide="SL13"] | Module 1 · The borrowed identity: The support page that found you | If support found you, do not use it. Start from the app, your saved bookmark or your IT helpdesk. | HTML browser mock of a social post and a “support” reply with handle/link details | No additional visual | — | — | None | The browser mock is the evidence; the question “who started this conversation?” is answered in text. Nothing visual is missing. |
| 14 | SL14 · src/slides/M1.html · section[data-slide="SL14"] | Module 1 · The borrowed identity: A collaboration that sounds relevant | Re-check whenever a conversation reaches money, access or information, however friendly it has been. | HTML chat (Daniel portrait EX-007) with two amber markers; pair-exercise prompt | No additional visual | — | — | None | Exercise slide: participants must read the messages themselves; the markers are deliberately minimal. |
| 15 | SL15 · src/slides/M1.html · section[data-slide="SL15"] | Module 1 · The borrowed identity: Someone is using your name | A copied profile needs a platform report; a taken-over account needs official recovery. Both need you to warn contacts through a trusted channel. | Situation strip; three findings; tick table (copied profile vs taken-over account) | No additional visual (INFO-001 on SL12 prepares this table) | — | — | None | Slide is full (table ends y 705, foot at 723). The tick table is already the comparison diagram. |
| 16 | SL16 · src/slides/M1.html · section[data-slide="SL16"] | Module 1 · The borrowed identity: Verify before you classify | Verify through the staff directory, then check the contract may be shared that way. | Decision cards A/B/C; feedback | No additional visual | — | — | None | Pause-point vote; keep the room focused on the three options. |
| | ↳ interaction states | | | | Vote states: A/B amber “Reconsider”; C teal “Recommended” plus Key point. | | | | |
| 17 | SL17 · generated by build/generated.py (layout=takeaway) from 04-content/slides.json id SL17 | Module 1 · The borrowed identity: Module 1 takeaways | Contact people through the directory, not through the message. | Generated takeaway: numbered list, habit box | No additional visual | — | — | None | Takeaway slides are deliberately plain so the three sentences and habit are the only thing on screen. |
| 18 | SL18 · src/slides/M1.html · section[data-slide="SL18"] | Short break: Short break | Scheduled break; nothing advances automatically. | Break title, “Next” panel | Optional reusable break backdrop | BG-003 | Full canvas; texture confined to top-left y 0–330 and bottom band y 720–900; text stays on plain navy | Optional | Break slides sit on screen for 10–75 minutes. A calm, darker backdrop reads as “paused” from across the room without adding content. |
| 19 | SL19 · generated by build/generated.py (layout=opener) from 04-content/slides.json id SL19 | Module 2 · The trusted request: Module 2: The trusted request | Urgency and authority are reasons to check, not reasons to skip the check. | Generated opener: cast (Ravi, Farid, Nadia, Caller) | Optional reusable opener backdrop | BG-002 | As SL08 | Optional | As SL08. |
| 20 | SL20 · src/slides/M2.html · section[data-slide="SL20"] | Module 2 · The trusted request: An urgent request from the manager | Normal approval still applies when the deadline is close. Confirm with Ravi on his directory number. | HTML chat (Ravi portrait) three bubbles; side explanation | Optional scenario image of Farid under deadline pressure (reuse) | IMG-002 | Right column x 926–1520, y 460–740 (hint ends y 441); 594×270 canvas px | Optional | Same scene family as SL04 (Farid, chat, deadline). Reusing IMG-002 keeps the cast consistent and costs nothing extra. |
| 21 | SL21 · src/slides/M2.html · section[data-slide="SL21"] | Module 2 · The trusted request: What the pressure asks you to skip | Urgency, secrecy and “I’ll approve it later” all try to remove a check. The risk is the exception, even if the sender is genuine. | Enlarged single chat bubble with three amber markers; legend | Optional three small line icons beside the legend items (urgency, secrecy, exception) | ICON-001 | Inline at 36 px canvas, left of each legend item in the right column (x 926–1520, y 350–560) | Optional | The markers already link text to evidence. Icons only add a memory hook for the three tactics; harmless, low value. |
| 22 | SL22 · src/slides/M2.html · section[data-slide="SL22"] | Module 2 · The trusted request: A polite way to pause | Name the route and the next step: “I’ll call you back on your directory number, then raise it for approval.” | Quote, three numbered steps, two white request cards, strong-response box | No additional visual | — | — | None | Practice instructions; a picture of two people role-playing would add nothing participants need to do the exercise. |
| 23 | SL23 · src/slides/M2.html · section[data-slide="SL23"] | Module 2 · The trusted request: The voice on the phone | Knowing names proves nothing. Hang up and call the service desk on its known number. Never read out a sign-in code. | Captioned call transcript (IT-caller portrait EX-009 labelled “illustration”); question; hint | Add a scenario photograph of Aina taking the unexpected call at her desk | IMG-001 | Right column x 926–1520, y 470–740 (hint ends y 450, foot 744); 594×270 canvas px | Recommended | This is the only audio scene and it is read aloud. A believable picture of Aina with the phone, hesitant, anchors the script and gives the room a face for “you” in this situation. Must not show the caller. |
| 24 | SL24 · src/slides/M2.html · section[data-slide="SL24"] | Module 2 · The trusted request: A face or voice cannot approve a payment | Do not rely on spotting glitches. A separate, authorised payment process works whether the video is real or fake. | Context strip; two comparison cards (spotting glitches vs independent verification); lede | No additional visual | — | — | None | A picture of a “deepfake” call would invite the glitch-spotting habit the slide argues against. The two-card comparison is the right form. |
| 25 | SL25 · src/slides/M2.html · section[data-slide="SL25"] | Module 2 · The trusted request: Which number will you call? | Call the number already in your records, never one supplied with the change. | Two white evidence cards (email number vs finance record); decision A/B/C | No additional visual | — | — | None | Pause-point vote; the two cards already are the comparison. |
| | ↳ interaction states | | | | Vote states: A/C amber; B teal plus Key point. | | | | |
| 26 | SL26 · src/slides/M2.html · section[data-slide="SL26"] | Module 2 · The trusted request: Keep the process when the request is genuine | Verification checks who is asking. Authorisation decides whether it may happen. A genuine change still goes through approval. | Context; decision A/B/C | No additional visual | — | — | None | Pause-point vote; legitimate-change example should stay text-only to avoid hinting. |
| | ↳ interaction states | | | | Vote states: A/C amber; B teal plus Key point. | | | | |
| 27 | SL27 · generated by build/generated.py (layout=takeaway) from 04-content/slides.json id SL27 | Module 2 · The trusted request: Module 2 takeaways | Call back on a number you already have before you pay, reset or share. | Generated takeaway | No additional visual | — | — | None | As SL17. |
| 28 | SL28 · generated by build/generated.py (layout=opener) from 04-content/slides.json id SL28 | Module 3 · The message that fits your job: Module 3: The message that fits your job | Ask three questions of every message: who is asking, what would I authorise, and how can I check outside this message? | Generated opener: cast (Aina, Farid, Ravi, Nadia) | Optional reusable opener backdrop | BG-002 | As SL08 | Optional | As SL08. |
| 29 | SL29 · src/slides/M3.html · section[data-slide="SL29"] | Module 3 · The message that fits your job: A message that fits your work | Look for the action: sign in, share data, open a file. Then verify outside the message. Any of these could be genuine. | Three white inbox cards with “Requested action” rows; three-question steps | No additional visual | — | — | None | The inbox cards and the three questions are already paired; the slide is full (y 716 of 744). |
| 30 | SL30 · src/slides/M3.html · section[data-slide="SL30"] | Module 3 · The message that fits your job: The sender behind the display name | A mismatched address is a warning sign, but a matching one does not prove safety. Verify the request itself. | HTML email with From/Reply-to highlighted and two markers; directory-address callout | No additional visual | — | — | None | This is an annotated email example in editable HTML, already exactly what the brief asks for. |
| 31 | SL31 · src/slides/M3.html · section[data-slide="SL31"] | Module 3 · The message that fits your job: The destination behind the label | Read the web address from the right, up to the first single slash. The last part, attacker.test, owns the site. | Link-label card; browser preview showing the inert URL; revealed hostname highlight and three-row key | No additional visual | — | — | None | The URL anatomy reveal is an existing deterministic diagram (HTML). Nothing is missing. |
| | ↳ interaction states | | | | Revealed state: “.attacker.test” highlighted amber; three-row key appears; Key point appears. | | | | |
| 32 | SL32 · src/slides/M3.html · section[data-slide="SL32"] | Module 3 · The message that fits your job: A polished message can still deceive | Polish and logos prove nothing. Judge the action requested and check it in the system you normally use. | Two white message cards with GENUINE / DECEPTIVE verdict rows; lede | No additional visual | — | — | None | A logo or letterhead image would undercut the point that polish proves nothing. |
| 33 | SL33 · src/slides/M3.html · section[data-slide="SL33"] | Module 3 · The message that fits your job: The same request on a phone | Phones hide the full sender and link. Open the app or website yourself instead of tapping the message. | HTML phone frame with an SMS notification; text card “On a desktop you would also see” | Replace the text card with a desktop mail-header mock of the same message (annotated HTML) | INFO-002 | Right column x 822–1520, y 400–700, replacing the white “On a desktop…” card; 698×300 canvas px | Recommended | The learning point is a comparison (phone hides detail, desktop shows it) but only one side is shown. A side-by-side of the same request with the full sender and link preview visible makes the hidden detail concrete. |
| 34 | SL34 · src/slides/M3.html · section[data-slide="SL34"] | Module 3 · The message that fits your job: A QR code moves the request | Treat a QR code like a link you cannot read. Use the known portal instead. | HTML email with inert generated QR tile (EX-010); destination card | No additional visual; chart candidate blocked | CHART-001 | Presenter notes only (not on slide) until data decision is made | None | The slide works. The Microsoft QR-volume figures live in presenter notes and the claims policy keeps broad statistics off core slides; see CHART-001 (blocked). |
| 35 | SL35 · src/slides/M3.html · section[data-slide="SL35"] | Module 3 · The message that fits your job: A shared file is still a request | A file type or brand does not make it safe. If you did not expect it, check with the sender through a known contact first. | Shared-file invitation card; three file-type cards (PDF, HTML, SVG) | No additional visual | — | — | None | File-type cards already act as icons; realistic file thumbnails would imply these formats are inherently dangerous, which the slide denies. |
| 36 | SL36 · src/slides/M3.html · section[data-slide="SL36"] | Module 3 · The message that fits your job: Would you approve this? | Some requests are genuine. The right answer depends on the action and the route, not on calling everything phishing. | Four dark exercise cards; reveal adds verdict rows | No additional visual | — | — | None | Exercise: tables vote by hand; the free band (y 508–806) fills with verdicts on reveal. |
| | ↳ interaction states | | | | Revealed state: each card gains a VERIFY FIRST / PROCEED / HOLD AND REPORT row; Key point appears. | | | | |
| 37 | SL37 · src/slides/M3.html · section[data-slide="SL37"] | Module 3 · The message that fits your job: The signals that do not prove safety | Logos, padlocks, known senders and completed MFA do not validate the request. HTTPS still matters: it protects the connection. | Six-row signals table | Optional small line icons in the Signal column | ICON-001 | Inline 32 px canvas, left of each signal name (x 96–130) | Optional | The table is the correct form. Icons (logo, envelope, padlock, shield, pen, phone-tick) only help scanning for readers who skim. |
| 38 | SL38 · src/slides/M3.html · section[data-slide="SL38"] | Module 3 · The message that fits your job: Your verification route | Use a known app or bookmark, an established contact, or your organisation’s process. Never the contact details inside the message. | Context; three route cards; caption | Add three route icons inside the cards | ICON-001 | Top-left of each card above the eyebrow, 56 px canvas; cards grow by ≈ 64 px into the free band (cards end y 530, foot 744) | Recommended | The three routes are the habit of the whole day and appear again in the recap. Distinct icons (bookmark/app, directory record, ticket/process) make them recognisable at a glance and reusable in the participant card. |
| 39 | SL39 · generated by build/generated.py (layout=takeaway) from 04-content/slides.json id SL39 | Module 3 · The message that fits your job: Module 3 takeaways | Go to the app or website yourself instead of using the link. | Generated takeaway | No additional visual | — | — | None | As SL17. |
| 40 | SL40 · src/slides/M3.html · section[data-slide="SL40"] | Lunch break: Lunch break | Scheduled break; nothing advances automatically. | Break | Optional reusable break backdrop | BG-003 | As SL18 | Optional | As SL18. |
| 41 | SL41 · generated by build/generated.py (layout=opener) from 04-content/slides.json id SL41 | Module 4 · Beyond the password: Module 4: Beyond the password | Before approving anything, ask: what does this give, and to whom? Did I start it? | Generated opener with glossary (right column full to y 764); cast (Aina, Mei) | Optional reusable opener backdrop (top band only) | BG-002 | As SL08, but texture confined to y 0–100 because the glossary fills the right column | Optional | As SL08; keep the glossary surface plain. |
| 42 | SL42 · src/slides/M4.html · section[data-slide="SL42"] | Module 4 · Beyond the password: Access can be granted without sharing a password | A session, an MFA approval, an app permission or a linked device can each let someone act as you. | Four white cards (session, MFA request, app permission, linked device) with “Grants” rows; lede | Add one line icon to each card | ICON-001 | Top of each card above the eyebrow, 56 px canvas (cards x 80–427 / 445–791 / 809–1156 / 1174–1520); cards grow ≈ 64 px into the free band (y 541–744) | Recommended | Four abstract grant types in identical cards are hard to tell apart from the back of the room. Four distinct icons give each a shape that recurs on SL44–SL47 and SL49. |
| 43 | SL43 · src/slides/M4.html · section[data-slide="SL43"] | Module 4 · Beyond the password: The login session an attacker can reuse | Sign in from your bookmark or app, not from a link. Phishing-resistant MFA, such as security keys and passkeys, blocks this relay. | Three white browser/phone cards in a row with → arrows; lede | Replace the three-card row with a relay diagram that keeps the three stages and adds the attacker’s relay and the session path | FLOW-001 | Full content width x 80–1520, y 258–640 (replaces the card row; the lede stays below) | Essential | The current row shows three screens but not where the attacker sits or how the session travels. Participants cannot see why the real MFA prompt does not help, which is the whole teaching point of the slide. |
| 44 | SL44 · src/slides/M4.html · section[data-slide="SL44"] | Module 4 · Beyond the password: An approval you did not start | Deny any prompt you did not start and report it. Never approve just to make the prompts stop. | HTML phone with two authenticator prompts; answer box; hint | No additional visual | — | — | None | The phone mock-up is the evidence and already enlarged; the remaining right-column space (y 589–744) is too small for a meaningful image. |
| 45 | SL45 · src/slides/M4.html · section[data-slide="SL45"] | Module 4 · Beyond the password: A real sign-in page, someone else’s code | Only enter a code for a sign-in you started yourself. Here the code would sign in the sender’s device as Aina. | Message card with DEMO-ONLY code; browser “Enter code” mock; two findings | Add a device-code flow diagram showing whose device starts the sign-in and whose device gets signed in | FLOW-002 | Right column x 822–1520, y 575–740 (findings end y 566); 698×165 canvas px; if too tight, replace the two findings (the flow carries both facts) | Essential | This is the most counter-intuitive concept in the deck: a genuine page, a real code, and still the wrong person gets in. Text alone leaves “whose device?” abstract; a two-lane flow shows the code travelling from the sender’s device to Aina and the session going back to the sender. |
| 46 | SL46 · src/slides/M4.html · section[data-slide="SL46"] | Module 4 · Beyond the password: The app asking for your permission | A real permission screen does not make the app trustworthy. Ask IT to approve apps through the normal process. | HTML consent screen with four permissions, two highlighted and marked; legend; answer box | No additional visual | — | — | None | Annotated consent mock is already the right format; the fictional app icon “MH” is intentionally generic. |
| 47 | SL47 · src/slides/M4.html · section[data-slide="SL47"] | Module 4 · Beyond the password: Linking another device | Linking gives another device ongoing access to your account. Link only devices you own and set up yourself. | Message card with inert QR tile (EX-011); “What the app shows” card; two comparison cards; hint | Add a compact join-versus-link diagram under the QR card | FLOW-003 | Left column x 80–778, y 590–740 (card ends y 577); 698×150 canvas px | Recommended | The two comparison cards say the difference in words. A picture of “you joining one conversation” versus “another device gaining your whole account” shows the scale of what linking grants. |
| 48 | SL48 · src/slides/M4.html · section[data-slide="SL48"] | Module 4 · Beyond the password: A defence that stopped the attempted access | Strong controls and quick reporting work together. Some MFA types resist phishing much better than others. | Large stat “3”, three-event timeline, callout | No additional visual | — | — | None | Documented case in the same stat-plus-timeline form as SL07; FLOW-001 on SL43 already explains why keys bound to the genuine site stop the relay. |
| 49 | SL49 · src/slides/M4.html · section[data-slide="SL49"] | Module 4 · Beyond the password: What does this approval grant? | Check where the request came from through a route you know. If you did not start it, deny it and report it. | Three white mini-cards (code, consent, MFA); decision A/B/C | No additional visual | — | — | None | Pause-point vote; the three mini-cards recall SL45–SL47 and the ICON-001 icons can appear on them for continuity (no new asset). |
| | ↳ interaction states | | | | Vote states: A/C amber; B teal plus Key point. | | | | |
| 50 | SL50 · generated by build/generated.py (layout=takeaway) from 04-content/slides.json id SL50 | Module 4 · Beyond the password: Module 4 takeaways | Approve only what you started and recognise. | Generated takeaway | No additional visual | — | — | None | As SL17. |
| 51 | SL51 · generated by build/generated.py (layout=opener) from 04-content/slides.json id SL51 | Module 5 · The helpful stranger: Module 5: The helpful stranger | Real help can be checked: a ticket you raised, through a portal or number you know. | Generated opener: cast (Mei, Aina, Farid) | Optional reusable opener backdrop | BG-002 | As SL08 | Optional | As SL08. |
| 52 | SL52 · src/slides/M5.html · section[data-slide="SL52"] | Module 5 · The helpful stranger: Mei offers help in chat | Verify a support offer with the helpdesk through a route you know. A name and photo in chat prove nothing. | HTML chat (Mei portrait EX-003) with address/External label and three markers; legend | No additional visual | — | — | None | Annotated chat is the evidence; the “External” label and address are the clues participants must read. |
| 53 | SL53 · src/slides/M5.html · section[data-slide="SL53"] | Module 5 · The helpful stranger: Remote access changes the stakes | No ticket, no session. Check with the helpdesk first, and never send a login code to prove anything. | White remote-control request mock with inert Decline/Allow buttons; two questions; decision A/B/C | No additional visual | — | — | None | Pause-point vote; the request dialogue is already the visual. |
| | ↳ interaction states | | | | Vote states: A/C amber; B teal plus Key point. | | | | |
| 54 | SL54 · src/slides/M5.html · section[data-slide="SL54"] | Module 5 · The helpful stranger: The verification page asks too much | No real check asks you to open a system tool and paste text. Stop, close it and contact IT. | HTML browser mock: fake CAPTCHA, “Additional verification” step, red STOP box; question; hint | Add a three-step flow showing what the paste step would actually do | FLOW-004 | Right column x 926–1520, y 460–740 (hint ends y 441); 594×270 canvas px | Recommended | The mock shows the lure but the question “What would that step actually do?” is answered only in a sentence. A flow from page → system tool → software runs → stranger controls the computer makes the consequence visible without showing any command. |
| 55 | SL55 · src/slides/M5.html · section[data-slide="SL55"] | Module 5 · The helpful stranger: A browser problem becomes a repair request | Install software and get fixes only through approved sources and your IT team. | Large word “CrashFix”, four-event timeline | No additional visual | — | — | None | The four-event timeline is the diagram; the source policy forbids reproducing the real extension or messages. |
| 56 | SL56 · src/slides/M5.html · section[data-slide="SL56"] | Module 5 · The helpful stranger: The notice asks you to call | Check the account through the service or team you already know, not the number in the notice. | HTML email (initial avatar “S”) with highlighted callback line and DEMO-NUMBER; answer box | No additional visual | — | — | None | Annotated email example; the DEMO placeholder must stay visibly fake. |
| 57 | SL57 · src/slides/M5.html · section[data-slide="SL57"] | Module 5 · The helpful stranger: Which support request can you proceed with? | Verified help can go ahead under normal rules: stay present and share only what the fix needs. | Two white evidence cards (portal ticket, Mei chat); decision A/B/C | No additional visual | — | — | None | Pause-point vote on a genuine example; keep it plain so it does not look different from the suspicious cases. |
| | ↳ interaction states | | | | Vote states: B/C amber; A teal plus Key point. | | | | |
| 58 | SL58 · generated by build/generated.py (layout=takeaway) from 04-content/slides.json id SL58 | Module 5 · The helpful stranger: Module 5 takeaways | No ticket you raised, no remote access. | Generated takeaway | No additional visual | — | — | None | As SL17. |
| 59 | SL59 · src/slides/M5.html · section[data-slide="SL59"] | Tea break: Tea break | Scheduled break; nothing advances automatically. | Break | Optional reusable break backdrop | BG-003 | As SL18 | Optional | As SL18. |
| 60 | SL60 · generated by build/generated.py (layout=opener) from 04-content/slides.json id SL60 | Module 6 · Stop the chain: Module 6: Stop the chain | You do not need the full picture to report. Report what you saw and let the right team connect the dots. | Generated opener: cast (Aina, Farid, Ravi, Mei) | Optional reusable opener backdrop | BG-002 | As SL08 | Optional | As SL08. |
| 61 | SL61 · src/slides/M6.html · section[data-slide="SL61"] | Module 6 · Stop the chain: Your team at Meranti | Every role matters: operations spots the request, finance holds payments, managers protect time to check, IT handles access. | Four role cards with portraits (EX-001, EX-002, EX-004, EX-003); two task panels | No additional visual | — | — | None | Role cards already carry the portraits; the slide is full. |
| 62 | SL62 · src/slides/M6.html · section[data-slide="SL62"] | Module 6 · Stop the chain: Evidence 1: the document invitation | Use a known route before signing in or sharing. | Evidence board: T1 active, T2–T4 locked; white card; record prompts; reveal note | No additional visual | — | — | None | The evidence board is a purpose-built diagram of “what is known so far”. |
| | ↳ interaction states | | | | Revealed state: preferred-response note under the prompts; Key point appears. | | | | |
| 63 | SL63 · src/slides/M6.html · section[data-slide="SL63"] | Module 6 · Stop the chain: Evidence 2: the account approval | Report immediately, thank the reporter, and let IT review access. Do not wait for proof. | Evidence board: T1 summary, T2 active | No additional visual | — | — | None | As SL62. |
| | ↳ interaction states | | | | Revealed state as SL62. | | | | |
| 64 | SL64 · src/slides/M6.html · section[data-slide="SL64"] | Module 6 · Stop the chain: Evidence 3: the bank change | Hold, call back from records and keep approvals. A link to card 2 is a guess until IT confirms it. | Evidence board: T1–T2 summaries, T3 active | No additional visual | — | — | None | As SL62. |
| | ↳ interaction states | | | | Revealed state as SL62. | | | | |
| 65 | SL65 · src/slides/M6.html · section[data-slide="SL65"] | Module 6 · Stop the chain: Evidence 4: someone offers help | Verify with the helpdesk, allow no control, and report facts and uncertainty together. | Evidence board: T1–T3 summaries, T4 active | No additional visual | — | — | None | As SL62. |
| | ↳ interaction states | | | | Revealed state as SL62. | | | | |
| 66 | SL66 · src/slides/M6.html · section[data-slide="SL66"] | Module 6 · Stop the chain: What stopped the chain? | Independent checks, normal approval and early reporting each reduced the risk. | Three debrief cards; two fact panels | Add a slim chain strip (T1→T4) marking where each decision interrupted the chain and which links are not established | INFO-003 | Full content width x 80–1520, y 635–735 (panels end y 622, foot 744); 1440×100 canvas px | Recommended | The debrief asks “what stopped the chain?” but no chain is drawn. A strip with the four cards in time order, teal stops at T1/T3/T4 and T2, and dotted “not established” links makes the facts-versus-guesses rule visible. |
| 67 | SL67 · generated by build/generated.py (layout=takeaway) from 04-content/slides.json id SL67 | Module 6 · Stop the chain: Module 6 takeaways | Report early, even if you are not sure. | Generated takeaway | No additional visual | — | — | None | As SL17. |
| 68 | SL68 · generated by build/generated.py (layout=opener) from 04-content/slides.json id SL68 | Module 7 · Report and recover: Module 7: Report and recover | Reporting a mistake quickly is the right thing to do, and it is never blamed. | Generated opener: cast (Aina, Lina, Mei) | Optional reusable opener backdrop | BG-002 | As SL08 | Optional | As SL08. |
| 69 | SL69 · src/slides/M7.html · section[data-slide="SL69"] | Module 7 · Report and recover: Pause, verify, report, recover | Pause, verify, report, recover. This is our course summary, not an official framework. | Four cards Pause / Verify / Report / Recover with examples | Add one line icon per card | ICON-001 | Left of the big word in each card, 56 px canvas; cards grow ≈ 0–20 px (cards end y 546, foot 744) | Recommended | The mnemonic is repeated on the participant card and in the recap; four consistent icons make it memorable and portable to the printed card. |
| 70 | SL70 · src/slides/M7.html · section[data-slide="SL70"] | Module 7 · Report and recover: Your actual reporting route | Keep the original, say what happened and when, and use another channel if your account may be affected. | Demo banner; four numbered steps; route panel with bracketed placeholders | No additional visual until the customer supplies a confirmed route (config supports screenshot_asset) | — | — | None | A screenshot of the real report button is the only visual that would help, and it depends on customer confirmation (config `reporting.screenshot_asset`, currently null). Nothing generic should stand in for it. |
| 71 | SL71 · src/slides/M7.html · section[data-slide="SL71"] | Module 7 · Report and recover: What happened determines the response | A password reset alone may not remove access. Report early so the right team can check sessions, apps and devices. | Four cards (clicked, credentials/approval, ran software/control, transferred money) with owner labels | Add one line icon per card | ICON-001 | Top of each card above the eyebrow, 56 px canvas; cards grow ≈ 64 px into free band (cards end y 553, foot 744) | Recommended | Four “what happened” categories are easier to find in a hurry when each has a shape; this slide is what people will try to recall after a real mistake. |
| 72 | SL72 · src/slides/M7.html · section[data-slide="SL72"] | Module 7 · Report and recover: A useful report | Include the time, channel, who it claimed to be, what you did and which device. Never include passwords or codes. | Report A card with MISSING row; coral “Never include” strip; Report B definition list | No additional visual | — | — | None | The two-report comparison is already the visual; adding a form graphic could be mistaken for an actual report form (the deck forbids forms). |
| 73 | SL73 · src/slides/M7.html · section[data-slide="SL73"] | Module 7 · Report and recover: A new request, the same decision | A genuine requester still needs a permitted reason and the approved sharing route. | Context with Lina portrait (EX-008); decision A/B/C | No additional visual | — | — | None | Pause-point post-check; must look like SL05 to measure transfer. |
| | ↳ interaction states | | | | Vote states: A/C amber; B teal plus Key point. | | | | |
| 74 | SL74 · src/slides/M7.html · section[data-slide="SL74"] | Module 7 · Report and recover: The check you will use tomorrow | Pick one request you handle at work and the route you will use to check it. | Two large fill-in sentences; instruction | No additional visual | — | — | None | Reflection slide works because it is empty; the blank line is the invitation. |
| 75 | SL75 · generated by build/generated.py (layout=recap) from 04-content/slides.json id SL75 | Module 7 · Report and recover: Today’s takeaways | When a message asks for money, information or access: pause, check through a route you already trust, and report anything unusual. | Generated recap: seven habits list | No additional visual (ICON-001 icons may be reused beside Module 3, 4 and 7 rows at implementation time; no new asset) | — | — | None | The list is the recap. Reusing already-made icons is an implementation choice, not a new asset. |
| 76 | SL76 · src/slides/M7.html · section[data-slide="SL76"] | Module 7 · Report and recover: Questions and references | Close with access to the response card and the primary-source index. | Questions text; response-card panel; reference-index panel with button; follow-up panel | No additional visual | — | — | None | Closing slide; the button opens the sources panel. A thumbnail of the response card would be a picture of text. |
| | ↳ interaction states | | | | Button state: “Open the reference index” opens the Sources side panel (22 https links). | | | | |

**Coverage check.** 76 slides reviewed. Slides with a new or changed visual: SL01, SL04, SL08, SL12, SL18, SL19, SL20, SL21, SL23, SL28, SL33, SL34, SL37, SL38, SL40, SL41, SL42, SL43, SL45, SL47, SL51, SL54, SL59, SL60, SL66, SL68, SL69, SL71. Priority counts across slides: Essential: 2, None: 49, Optional: 15, Recommended: 10. Every asset ID in the table has a brief in §4; every brief lists these slides and no others.

---

## 4. Detailed asset briefs

Asset IDs: `FLOW-` process flows and decision diagrams, `INFO-` infographics and comparisons, `ICON-` icon set, `IMG-` character/scenario photographs, `BG-` backdrops, `CHART-` data charts. 14 unique new assets (16 existing assets are catalogued separately in §5.3).

Unless stated otherwise, every brief below is a **proposed specification**; the dimensions marked “measured” come from the current layout.

### FLOW-001 · Relayed sign-in (adversary-in-the-middle) diagram

- **Category / method:** process flow · editable inline SVG (drawn in a vector tool or coded). Not an AI bitmap: the arrows and labels carry the meaning.
- **Priority / batch:** Essential · Batch 1.
- **Slides:** 43 · SL43 “The login session an attacker can reuse” (Module 4).
- **Learning purpose:** show *where the attacker sits* and *where the session goes*, so participants understand why a real MFA prompt does not protect them when they arrived from a link, and why phishing-resistant MFA does.
- **Plain description:** one wide diagram with three lanes left to right: Aina and her phone (left), the attacker’s relay page in the middle (amber frame), the real service on the right (paper card, teal frame). Arrows show her typed details going through the relay to the real service, the genuine MFA prompt coming back to her phone, her approval going back, the service issuing a session, and the relay keeping that session and reusing it from “someone else’s browser”.
- **Exact content, labels and reading order:**
  1. Lane A (x 0–420): paper card “Aina” with the avatar (EX-001 at 44 px), below it a small phone card “Your phone · Approve sign-in?” (text preserved from the current step 2).
  2. Lane B (x 500–940): amber-framed paper card titled “1 · A lookalike page”, URL bar text `sign-in.meranti-docs.example`, body “Sign in to continue · The page passes what you type to the real service.” (preserved). Eyebrow above the card in amber: “Attacker’s relay”.
  3. Lane C (x 1020–1440): paper card “The real service” with teal frame, URL `login.service.example` (reserved name), body “Sends the genuine MFA prompt. Issues the session.”
  4. Arrows, numbered with amber markers in this order: ① Aina → relay (“what you type”); ② relay → real service (“forwarded”); ③ real service → Aina’s phone (“2 · A real MFA prompt”, dashed teal); ④ phone → real service (“you approve”); ⑤ real service → relay (“the session”); ⑥ relay → a small grey browser icon labelled “3 · The session · Someone else’s browser · Signed in as Aina” (text preserved from the current step 3), arrow coral.
  5. Footer line inside the diagram, 18 px, text-2: “The relay keeps the session the service issued. It can be reused without the password or another prompt.” (preserved).
  6. Optional annotation (static, no reveal, because SL43 is not a pause point): a small teal key glyph at the real-service card with the label “Security key / passkey: only works with the genuine site, so step ① fails.” This reinforces the Key point without a second diagram.
- **Decision conditions:** none (descriptive flow).
- **Grouping, emphasis, colour meaning:** amber frame = the deceptive element; teal frame = the genuine service and the safe control; coral arrow = the harmful outcome (stolen session); dashed teal = genuine messages that nevertheless do not help; grey = the attacker’s other machine. Words accompany every colour.
- **Initial vs revealed:** all visible at once (non-pause slide).
- **Presenter explanation it supports:** “Nothing on her screen is fake except the address. The prompt is real, the approval is real, the service is real. The only thing that changed is that a relay sat in the middle and kept what the service handed back.”
- **Composition / focal point:** the relay card is the focal point; arrows ⑤–⑥ must be the most visible path.
- **Placement / space (measured):** replaces the current three-card `.seq.aitm` row at x 80–1520, y 258–632; the lede “MFA still blocks many attacks…” stays below it at y ≈ 660–700; footer at 744.
- **Dimensions:** 1440 × 380 canvas px; SVG viewBox `0 0 1440 380`; at 1920×1080 it renders 1728 × 456 device px, at 1366×768 1229 × 324 device px (labels must stay ≥ 18 px canvas).
- **Colour/style:** tokens only (§2.4). **Transparency:** n/a (inline on navy). **Standalone/background:** standalone diagram.
- **Filename:** `flow-001-relayed-signin.svg`.
- **Alt text:** “Diagram: Aina types into a lookalike sign-in page run by an attacker. The page forwards her details to the real service, which sends a genuine MFA prompt to her phone. She approves. The service issues a session, which the attacker’s relay keeps and reuses from their own browser.”
- **Reference assets:** `src/slides/M4.html` section SL43 (texts to preserve); `src/css/deck.css` `.browser`, `.aitm`.
- **Sources:** S11 Microsoft, “Defending against evolving identity attack techniques”, 29 May 2025; S13 CISA phishing-resistant MFA fact sheet, October 2022. Keep the description conceptual; no proxy code, no capture screens, no credential fields (build rule).
- **Avoid:** masks, hoodies, skulls, binary; any real vendor logos; any suggestion that MFA is useless (the key glyph and footer text prevent this).
- **Simpler alternative:** keep the three cards and add only a slim amber bracket under cards 1–3 labelled “attacker’s relay sits here”, with one coral arrow from card 3 back to card 1. Loses the session path but still answers “where is the attacker?”.

### FLOW-002 · Device-code flow: whose device is signed in

- **Category / method:** process flow · editable inline SVG.
- **Priority / batch:** Essential · Batch 1.
- **Slides:** 45 · SL45 “A real sign-in page, someone else’s code” (Module 4).
- **Learning purpose:** make visible that the code belongs to a sign-in *someone else started*, and that entering it on the genuine page signs in *their* device.
- **Plain description:** a two-lane flow. Top lane “The sender’s device”, bottom lane “Aina”. Four steps across: the sender starts a sign-in and gets a code → the sender messages the code to Aina → Aina enters the code on the genuine page → the service signs in the sender’s device as Aina.
- **Exact labels and reading order:**
  1. Lane labels (13 px eyebrow): top “SENDER’S DEVICE · starts the sign-in”; bottom “AINA · receives the code”.
  2. Node 1 (top, teal-neutral paper card): “Sender starts a sign-in” → service returns “Code: DEMO-ONLY” (use the existing `.code` placeholder style; never a plausible real code).
  3. Node 2 (diagonal arrow top→bottom, amber): “Sends the code to Aina: ‘enter this to open the document’”.
  4. Node 3 (bottom, paper card with teal URL `login.service.example/device`): “Aina enters DEMO-ONLY on the genuine page”.
  5. Node 4 (arrow bottom→top, coral): “The service signs in the sender’s device as Aina”. End node (top, grey): “Signed in as Aina”.
  6. Caption 18 px: “No password changes hands, and the service is real.” (preserved from finding 02).
- **Decision conditions:** none; one branch label on node 3 in teal: “Only enter a code for a sign-in you started yourself” (the Key point).
- **Colour meaning:** amber = the code travelling outside its owner; coral = the wrong device gaining access; teal = genuine service and the safe rule.
- **Initial vs revealed:** all visible (non-pause slide).
- **Presenter explanation it supports:** “Look where the code was born. The page is real, the code is real, but it is the sender’s sign-in. Typing it finishes *their* login, not yours.”
- **Composition:** the diagonal amber arrow and the return coral arrow are the focal pair; keep the two lanes clearly separated by a 1 px `#2A3A52` rule.
- **Placement / space (measured):** right column x 822–1520; the two findings end at y 566 and the footer starts at 744 → 698 × 165 free. **Preferred:** accompany, placed at y 575–740. **Fallback:** replace the two findings (the diagram carries both facts) and use 698 × 300 at y 420–720.
- **Dimensions:** 698 × 165 canvas px (fallback 698 × 300); SVG viewBox accordingly.
- **Transparency:** n/a. **Standalone/background:** standalone.
- **Filename:** `flow-002-device-code.svg`.
- **Alt text:** “Diagram: the sender starts a sign-in on their own device and receives a code. They send the code to Aina. Aina enters it on the genuine sign-in page. The service signs in the sender’s device as Aina.”
- **Reference assets:** `src/slides/M4.html` section SL45.
- **Sources:** S12 Microsoft, AI-enabled device-code phishing campaign, 6 April 2026 (victims authorise the attacker’s session through the legitimate flow without exposing credentials). Do not claim the real service is a fake website (claims policy).
- **Avoid:** a plausible real code format; any brand UI; a second person’s face.
- **Simpler alternative:** two small device glyphs with a single curved arrow from “their device” through Aina’s keyboard back to “their device”, labelled “the code signs in *their* device”. Loses the service node.

### FLOW-003 · Joining a group versus linking a device

- **Category / method:** comparison diagram · editable inline SVG.
- **Priority / batch:** Recommended · Batch 2.
- **Slides:** 47 · SL47 “Linking another device” (Module 4).
- **Learning purpose:** show the difference in *scale* between joining one conversation and giving another device the whole account.
- **Plain description:** two mini-diagrams side by side. Left “Joining a group”: a single Aina avatar being added (plus sign) to a circle of three small people icons labelled “one conversation”. Right “Linking a device”: Aina’s account (a card with her avatar and “all your chats”) with a second device icon attached by a chain-link glyph, labelled “another device · reads and sends as you”.
- **Exact labels and reading order:** left eyebrow “JOINING A GROUP”, caption “Adds **you** to one conversation.” (preserved); right eyebrow “LINKING A DEVICE”, caption “Gives **another device** ongoing access to your account.” (preserved). Reading order left → right.
- **Colour meaning:** left all teal/neutral (benign); right: the second device and link in amber (the thing to notice), account card in paper. No coral (linking can be legitimate).
- **Initial vs revealed:** all visible.
- **Presenter explanation it supports:** “The invitation said ‘join’. Look what the app actually asked: link a device. That is not one chat, that is everything.”
- **Placement / space (measured):** left column x 80–778; the message card ends at y 577; footer at 744 → 698 × 150 at y 590–740.
- **Dimensions:** 698 × 150 canvas px; viewBox `0 0 698 150`. **Transparency:** n/a. **Standalone.**
- **Filename:** `flow-003-join-vs-link.svg`.
- **Alt text:** “Two small diagrams. Joining: you are added to one group conversation. Linking: another device is connected to your whole account and can read and send as you.”
- **Reference assets:** `src/slides/M4.html` section SL47; EX-001 avatar at 32 px.
- **Sources:** course explanation; notes say the cited Microsoft article does not use “account linking” wording, so present linking as general product behaviour, not a sourced incident. No messaging-app logo.
- **Avoid:** WhatsApp/Telegram branding, real QR codes.
- **Simpler alternative:** add the two icons from ICON-001 (group, linked-device) to the two existing comparison cards and skip the diagram.

### FLOW-004 · What the “paste into a system tool” step actually does

- **Category / method:** process flow · editable inline SVG.
- **Priority / batch:** Recommended · Batch 1.
- **Slides:** 54 · SL54 “The verification page asks too much” (Module 5).
- **Learning purpose:** answer the on-slide question “What would that step actually do?” with a picture of consequence, without showing any command.
- **Plain description:** a four-node vertical flow in the right column: web page instruction → you open a system tool and paste → software downloads and runs → a stranger controls the computer; with a teal side branch “Stop · close the page · contact IT” leaving after node 1.
- **Exact labels and reading order (top to bottom):**
  1. Node 1 (paper card, amber frame): “The page says: open a system tool, paste, press Enter.”
  2. Node 2 (paper card): “You paste text you cannot read into a tool that runs commands.” (no example text, no tool name)
  3. Node 3 (dark card, coral left bar): “Software downloads and runs on your computer.”
  4. Node 4 (dark card, coral): “Someone else can now control or watch the computer.”
  5. Branch from node 1, teal arrow to a teal card: “STOP · Close the page. Contact IT through the usual route.” with the label “No real check asks for this.”
- **Decision conditions:** one: “Did a web page ask you to open a system tool?” → yes → stop. Shown as the teal branch label.
- **Colour meaning:** amber frame = the lure; coral = harm; teal = the safe exit.
- **Initial vs revealed:** all visible.
- **Presenter explanation it supports:** “Nothing is being verified. The page is using your hands to run its program.”
- **Placement / space (measured):** right column x 926–1520; hint ends y 441; footer 744 → 594 × 270 at y 460–740.
- **Dimensions:** 594 × 270 canvas px. **Transparency:** n/a. **Standalone.**
- **Filename:** `flow-004-clickfix-consequence.svg`.
- **Alt text:** “Diagram: a web page tells you to open a system tool and paste text. Doing so runs software on your computer. That software gives a stranger control. The safe path: stop, close the page, contact IT.”
- **Reference assets:** `src/slides/M5.html` section SL54 (the red STOP box style `.stopbox` for colour matching).
- **Sources:** S16 Microsoft, “Think before you ClickFix”, 21 August 2025. The build forbids commands, clipboard actions and runnable text: the diagram must contain none.
- **Avoid:** terminal screenshots, command strings, OS logos, keyboard shortcuts.
- **Simpler alternative:** a single sentence strip under the browser mock: “page → you paste → software runs → stranger in control”, in the existing `.callout` style.

### INFO-001 · Copied profile versus taken-over account

- **Category / method:** comparison diagram · editable inline SVG.
- **Priority / batch:** Recommended · Batch 1.
- **Slides:** 12 · SL12 “A genuine account, an unusual request” (Module 1). Prepares the SL15 tick table and SL36 card 2.
- **Learning purpose:** show the two ways a familiar-looking message can come from the wrong person.
- **Plain description:** two small panels. Left “Copied profile”: two account cards side by side, both with Aina’s avatar and name, one labelled “real”, the other “copy” in amber; a message arrow leaves the copy. Right “Taken-over account”: one account card (real) with a faceless grey silhouette standing behind it, labelled “someone else is typing”; a message arrow leaves the real account. Under both: “Both can send this message.”
- **Exact labels and reading order:** eyebrows “COPIED PROFILE (cloning)” and “TAKEN-OVER ACCOUNT (compromise)”; card captions “Real · Aina”, “Copy · ‘Aina’”, “Real · Siti” (use Siti here to match the slide’s chat, EX-006 avatar at 28 px); arrows labelled “sends the request”; footer caption “Both can send this message. Verify outside the chat.” Reading order left panel then right panel.
- **Colour meaning:** amber outline = the copy; grey silhouette = unknown person (never a face); teal rule under the footer caption = the safe route.
- **Initial vs revealed:** all visible.
- **Presenter explanation it supports:** the existing hint sentence; the presenter points to the panel while saying “cloning copies a profile; compromise means someone else controls the real one.”
- **Placement / space (measured):** right column x 926–1520; hint ends y 557; footer 715 → 594 × 130 at y 575–705.
- **Dimensions:** 594 × 130 canvas px. **Transparency:** n/a. **Standalone.**
- **Filename:** `info-001-clone-vs-takeover.svg`.
- **Alt text:** “Two small diagrams. Copied profile: a second account with the same name and photo sits beside the real one. Taken-over account: the real account, but someone else is operating it. Both can send the same message.”
- **Reference assets:** `src/slides/M1.html` section SL12; EX-001 and EX-006 avatars; `.profile`/`.pavatar` styling.
- **Sources:** S5 FTC Business Impersonator Scams; S11 Microsoft evolving identity attacks.
- **Avoid:** a villain face; a red cross; any platform logo.
- **Simpler alternative:** two icons from ICON-001 (“copied profile”, “taken-over account”) placed before the two halves of the hint sentence.

### INFO-002 · Desktop view of the same text-message request (annotated mock)

- **Category / method:** annotated example · HTML/CSS using the existing `.mail`, `.mailmeta`, `.details` components. No image file.
- **Priority / batch:** Recommended · Batch 2.
- **Slides:** 33 · SL33 “The same request on a phone” (Module 3).
- **Learning purpose:** make the comparison real: what the desktop shows that the phone hides.
- **Plain description:** replace the white text card “On a desktop you would also see…” with a compact desktop mail header of the *same* request, with three amber markers on the parts the phone hid.
- **Exact content and features to highlight (proposed wording; content owner confirms):**
  - Mail bar: “Mail / Inbox · Aina” · “Thursday, 14:02”.
  - FROM: “MERANTI-IT” `<alerts@mrnt-review.example>` ← marker ① “Full sender address (the phone showed only ‘MERANTI-IT’)”.
  - Subject: “Your work account needs review today”.
  - Link line: label “Review your account” with a hover-preview strip underneath showing `https://mrnt-review.example/a1` ← marker ② “Whole link visible before you click”.
  - A `.details.static` strip: “Aina’s saved IT portal bookmark: it.meranti.example” ← marker ③ “Room to compare with your saved address”.
  - Inert note: “Training mock. Nothing opens.”
- **Reading order:** phone (left, existing) → desktop (right) → markers 1–3 → hint “Mobile is not unsafe in itself; it just hides detail.” (existing).
- **Reveal timing:** none; SL33 is not a pause point, so the annotations are visible from the start (consistent with the deck rule that open slides show everything).
- **Colour meaning:** amber markers = what to notice; no verdict colour (the message is suspicious but the slide’s point is visibility, not verdict).
- **Presenter explanation it supports:** “Same message. On the desktop you can read who it is really from and where it really goes. On the phone you cannot, so you go to the app yourself.”
- **Placement / space (measured):** right column x 822–1520; the eyebrow and question occupy y 258–370; the replaced card occupied y ≈ 404–520; the mock may run y 400–700 (698 × 300). Footer at 744.
- **Dimensions:** 698 × 300 canvas px (HTML; no fixed pixel size). **Transparency:** n/a. **In-slide component.**
- **Filename:** none (markup in `src/slides/M3.html`, SL33 section).
- **Alt text:** inherent (HTML text).
- **Reference assets:** `.mail` mock on SL30 for the sender-detail pattern; the SMS text on SL33.
- **Sources:** S5 FTC; S3 Microsoft Email threat landscape Q1 2026 (phishing channels). Addresses must use reserved `.example`/`.test` names and be text, never links (build rule).
- **Avoid:** a screenshot of a real mail client; brand icons.
- **Simpler alternative:** keep the text card but add the three bullet lines above as a `.details` strip.

### INFO-003 · Chain strip: four evidence cards and where the chain was interrupted

- **Category / method:** infographic (timeline strip) · editable inline SVG.
- **Priority / batch:** Recommended · Batch 2.
- **Slides:** 66 · SL66 “What stopped the chain?” (Module 6 debrief).
- **Learning purpose:** show the four tabletop events in time order with the three decisions that reduced risk, and mark what is *not* established, so the facts-versus-guesses rule is visible.
- **Plain description:** a single horizontal strip with four small cards (T1 13:50, T2 14:05, T3 15:20, T4 15:45) joined by dotted grey connectors labelled “not established”, and teal “stop” markers under T1, T3 and T4 (independent verification), a second teal marker under T3 (normal approval) and a teal flag over T2 (early reporting).
- **Exact labels and reading order (left → right):**
  - T1 “Document invitation · 13:50” · stop marker “Known route used”.
  - connector “? not established”.
  - T2 “Code entered and reported · 14:05” · flag “Reported early → IT reviews sessions”.
  - connector “? not established (T2 caused T3 is a guess)”.
  - T3 “Bank change + urgent chat · 15:20” · two markers “Callback from record” and “Normal approval kept”.
  - connector “? not established”.
  - T4 “Offer of help · 15:45” · stop marker “No ticket → no control”.
  - Legend (13 px): teal mark = decision that reduced risk; dotted grey = link for IT to investigate.
- **Colour meaning:** teal = decisions (supported by the evidence); dotted grey = unknown; no coral (nothing is confirmed harmful in the exercise).
- **Initial vs revealed:** all visible (debrief, non-pause).
- **Presenter explanation it supports:** “Three small decisions, three interruptions. Notice the dotted lines: we still do not know who sent what or whether one caused the next. That is IT’s job, not the table’s.”
- **Placement / space (measured):** full content width x 80–1520; fact panels end y 622; footer 744 → 1440 × 100 at y 635–735.
- **Dimensions:** 1440 × 100 canvas px. **Transparency:** n/a. **Standalone.**
- **Filename:** `info-003-chain-strip.svg`.
- **Alt text:** “Timeline strip of T1 document invitation, T2 code entered, T3 bank change, T4 offer of help. Teal marks show independent verification at T1, T3 and T4, normal approval at T3 and early reporting at T2. Dotted links between cards are labelled ‘not established’.”
- **Reference assets:** `src/slides/M6.html` SL62–SL66 (`.known .kcard` styling for the four cards); `08-facilitator/TABLETOP.md`.
- **Sources:** course exercise (fictional composite). Must not assert causation (facilitator rule).
- **Avoid:** arrows that imply cause between cards; a single “attacker” figure.
- **Simpler alternative:** add a one-line text strip “T1 · T2 · T3 · T4” with teal check marks under T1, T2, T3, T4 in the existing `.callout` style.

### ICON-001 · Workshop line-icon set (14 core icons, 8 optional)

- **Category / method:** icon set · editable SVG symbols (one sprite `<symbol>` file or sixteen small SVGs), 2 px stroke on a 48 × 48 grid, round joins, `fill="none" stroke="currentColor"`.
- **Priority / batch:** Recommended · Batch 1 (the eight Recommended placements); Optional placements in Batch 3.
- **Slides and placements:**
  - 38 · SL38 “Your verification route”: `route-app` (bookmark/app window), `route-contact` (directory card with handset), `route-process` (ticket). Recommended.
  - 42 · SL42 “Access can be granted without sharing a password”: `grant-session` (browser window with a clock), `grant-mfa` (phone with a tick bubble), `grant-app` (puzzle piece/plug), `grant-device` (two devices joined by a link). Recommended.
  - 69 · SL69 “Pause, verify, report, recover”: `pause` (open hand), `verify` (handset over a directory card, same family as `route-contact`), `report` (flag), `recover` (circular arrow with a shield outline). Recommended.
  - 71 · SL71 “What happened determines the response”: `clicked` (cursor on a link), `credentials` (key), `ran-software` (play triangle on a window), `money` (banknote/coins). Recommended.
  - 21 · SL21 pressure tactics (Optional): `urgency` (clock), `secrecy` (speech bubble with a line through it), `exception` (skipped step: three dots with the middle crossed). 
  - 37 · SL37 signals table (Optional): `logo` (badge), `sender` (envelope), `padlock`, `no-warning` (shield outline), `fluent` (pen), `mfa-done` (phone tick, reuse `grant-mfa`).
  - Permitted reuse without a new asset: SL49 mini-cards (code/consent/MFA → `credentials`, `grant-app`, `grant-mfa`), SL75 recap rows, the printed participant card.
- **Learning purpose:** give same-shaped categories a distinct, recurring shape so participants recognise “a route”, “a grant”, “a step”, “what happened” across slides and on the printed card.
- **Exact list.** Core set (14, for the recommended placements): `route-app`, `route-contact`, `route-process` (SL38); `grant-session`, `grant-mfa`, `grant-app`, `grant-device` (SL42); `pause`, `report`, `recover` (SL69; `verify` reuses `route-contact`); `clicked`, `credentials`, `ran-software`, `money` (SL71). Optional additions (8): `urgency`, `secrecy`, `exception` (SL21); `logo`, `sender`, `padlock`, `no-warning`, `fluent` (SL37; `mfa-done` reuses `grant-mfa`). Produce the optional eight only if those placements are approved.
- **Composition / placement:** on cards, 56 px canvas, top-left above the eyebrow, colour `#2DD4BF` (teal) on SL38/SL69 (safe routes/steps) and `#B4C0D2` on SL42/SL71 (neutral categories); inline beside text at 32–36 px. Cards on SL38, SL42 and SL71 grow by about 64 px into measured free space (cards currently end at y 530, 490 and 553; footers at 744).
- **Dimensions:** 48 × 48 design grid; exported SVG symbols; no raster.
- **Colour/style:** single weight, no fills except small dots; must read at 32 px canvas (27 px at 1366×768).
- **Transparency:** yes (vector). **Standalone:** decorative companions to a written label; `aria-hidden="true"`.
- **Filename:** `icon-001-workshop-icons.svg` (sprite) or `icons/<name>.svg`.
- **Alt text:** decorative (labels carry the meaning).
- **Reference assets:** `.card`, `.ev`, `.eyebrow`, `.marker` in `src/css/deck.css` for size and colour tokens; the existing 24 px amber marker circle sets the visual weight to match.
- **Sources:** n/a.
- **Avoid:** filled glyph styles (Material-style solid icons), emoji, brand marks, padlock-as-security cliché anywhere except the SL37 “HTTPS padlock” row where it is literal.
- **Simpler alternative:** use only the SL38/SL69 seven icons (routes and steps) and leave SL42/SL71 as text.

### IMG-001 · Aina takes an unexpected call at her desk

- **Category / method:** character scene photograph · AI image generation with character reference; photographic.
- **Priority / batch:** Recommended · Batch 2.
- **Slides:** 23 · SL23 “The voice on the phone” (Module 2).
- **Learning purpose:** give the read-aloud call a face and a place; let the room see “you” hesitating before reading out a code.
- **Plain description:** Aina at an ordinary office desk, desk phone (or mobile) to her ear, other hand hovering near the keyboard, eyes on her monitor, expression uncertain, slightly leaning back. Monitor shows an unreadable soft-focus screen (no text). Daylight office, shallow depth of field.
- **Exact scene:** subject Aina (match EX-001: young Malay woman, teal/dark-green hijab, cream top, warm complexion, no glasses); medium shot from slightly left of centre at eye level; desk with keyboard, a monitor turned slightly away, a notebook; background out-of-focus open-plan office with a window. No caller shown. No visible text, logos or brand devices. Time of day: late morning.
- **Composition / focal point:** Aina’s face and the phone are the focal point in the left two-thirds; the right third stays quiet (defocused background) so a caption could overlay if needed. Horizontal 2.2:1 crop.
- **Placement / space (measured):** right column x 926–1520, y 470–740 (hint ends at 450); displayed 594 × 270 canvas px with 14 px radius, below the hint.
- **Dimensions:** deliver 1800 × 820 px (2.2:1); JPEG quality 80, target ≤ 180 KB before base-64 embedding (≈ 240 KB in the HTML). Transparency: no. Standalone image.
- **Colour/style:** natural light, slightly desaturated, cool-neutral grade, one warm accent allowed (notebook, lamp); no HDR look, no vignette.
- **Filename:** `img-001-aina-unexpected-call.jpg`.
- **Alt text:** “Aina at her desk holding a desk phone to her ear, looking uncertain at her screen.”
- **Reference assets (must be supplied to the generator):** `dist/Image_ref/profile-pictures/aina.png` (1254 × 1254, AI-generated; the only authorised likeness).
- **Sources:** fictional scene; the cover disclosure “Portraits are AI-generated; no real person is depicted” covers it.
- **Avoid:** the caller; headsets with company branding; any readable screen; a laughing or terrified expression (the tone is “unsure”).
- **Simpler alternative:** none needed; omit the image and keep the slide as is.
- **Image-generation prompt (copy-ready):**

  > Photorealistic editorial photograph, Malaysian open-plan office, late morning daylight. Subject: Aina, a young Malay woman in her late twenties wearing a dark teal hijab and a cream blouse, matching the attached reference portrait exactly (face, skin tone, hijab colour and style). She sits at a tidy desk holding a black desk-phone handset to her ear, her other hand resting near the keyboard, eyes on her monitor, expression uncertain and thoughtful, lips slightly parted, leaning back a little. The monitor is turned slightly away and shows only soft, unreadable light. Medium shot, eye level, camera slightly left of centre, 50 mm look, shallow depth of field, background softly out of focus: a window, a plant, colleagues’ desks without faces. Colour grade cool and slightly desaturated with one warm accent (a wooden notebook on the desk). No visible text, logos, brands or signage anywhere. No other recognisable person. Keep the right third of the frame uncluttered. Aspect ratio 2.2:1, 1800×820 pixels, no transparency, no border, no caption.

### IMG-002 · Farid reads an urgent chat before the payment cut-off

- **Category / method:** character scene photograph · AI image generation with character reference.
- **Priority / batch:** Optional · Batch 3.
- **Slides:** 04 · SL04 “Another familiar name appears” (Opening) and 20 · SL20 “An urgent request from the manager” (Module 2). One file, reused.
- **Learning purpose:** atmosphere and continuity: the same character under the same kind of pressure in both modules.
- **Plain description:** Farid at his desk in late-afternoon light, looking at a chat window on his monitor (unreadable), hand on the mouse, concerned; a wall clock or window light suggesting end of day without showing a readable time.
- **Exact scene:** subject Farid (match EX-002: Malay man around thirty, short dark hair, light stubble, light-blue shirt); medium shot from slightly right; desk with monitor, keyboard, a printed invoice face-down; background defocused finance office. No readable time, no readable text, no logos.
- **Composition / focal point:** Farid’s face and the monitor edge; left third quiet.
- **Placement / space (measured):** SL04 right column x 926–1520, y 500–760 (hint ends at 486, footer 773); SL20 right column y 460–740 (hint ends at 441, footer 744). Displayed 594 × 270 canvas px.
- **Dimensions:** deliver 1800 × 820 px (2.2:1); JPEG ≤ 180 KB. Transparency: no. Standalone.
- **Filename:** `img-002-farid-deadline.jpg`.
- **Alt text:** “Farid at his desk in the late afternoon, looking at a chat message on his monitor with a hand near the mouse, concerned.”
- **Reference assets:** `dist/Image_ref/profile-pictures/farid.png`.
- **Avoid:** a visible clock face showing a time (the deck keeps clock times off participant screens except in scene labels); a visible chat UI; Ravi’s face.
- **Simpler alternative:** omit.
- **Image-generation prompt (copy-ready):**

  > Photorealistic editorial photograph, Malaysian finance office, late afternoon with warm low window light from the left. Subject: Farid, a Malay man around thirty with short dark hair and light stubble, wearing a light-blue button shirt, matching the attached reference portrait exactly. He sits at his desk looking at his monitor with a concerned, focused expression, one hand on the mouse, the other resting on a face-down printed document. The monitor shows only a soft, unreadable glow. Medium shot, eye level, camera slightly right of centre, 50 mm look, shallow depth of field; background softly blurred office with a window and no readable clock, text, logos or signage. Colour grade cool and slightly desaturated with the warm window light as the only warm accent. No other recognisable person. Keep the left third of the frame uncluttered. Aspect ratio 2.2:1, 1800×820 pixels, no transparency, no border, no caption.

### BG-001 · Cover backdrop: office at dusk, out of focus

- **Category / method:** backdrop · AI image generation or stock-style illustration, then heavy darkening in post; photographic.
- **Priority / batch:** Optional · Batch 3.
- **Slides:** 01 · SL01 “The request before 5 PM” (cover).
- **Learning purpose:** none; sets the “end of the working day” mood that the headline and the 16:42 context line describe.
- **Plain description:** a very dark, defocused view across an empty office toward a window at dusk, bluish interior, a few desk lamps as warm points. Only the left-bottom quadrant carries any discernible shape; the right half is almost plain navy so the email card sits on a clean field.
- **Mood / subject / dominant colours:** quiet, end-of-day; navy `#0B1220` dominates (≥ 85 % of pixels within 8 % luminance of it), muted blue-grey shapes, two or three warm lamp points no brighter than `#8A6A3A`.
- **Focal area and clear zones:** focal interest x 0–740, y 560–900 of the 1600×900 canvas (below the headline block); **clear zones** (must be plain): the headline block x 80–760, y 160–560; the email card x 780–1540, y 180–680 (state 2, opened message, is taller: y 200–760); the footer lines y 860–900.
- **Crop and positioning:** deliver 2560 × 1440, cover-fit to the canvas, anchored bottom-left.
- **Overlay/darkening:** multiply with navy at 70–80 %; final image should look nearly black on a monitor. Projection will lift it.
- **Reuse:** cover only.
- **Readability when projected:** headline contrast on the darkest area must remain ≥ 7:1 (`#F3F6FA` on ≤ `#1B2840`); re-run `build/qa/interact.cjs` contrast check after placement.
- **Dimensions:** 2560 × 1440 (16:9); JPEG ≤ 250 KB. Transparency: no. Background.
- **Filename:** `bg-001-cover-dusk.jpg`.
- **Alt text:** decorative (CSS background or `aria-hidden`).
- **Reference assets:** `src/css/deck.css` `.cover`; token `--bg`.
- **Avoid:** city skylines, server rooms, glowing screens, any people, any readable signage, gradients that look like a glow (the redesign removed glows).
- **Simpler alternative:** no backdrop (current state); the cover already reads well.
- **Image-generation prompt (copy-ready):**

  > Very dark, heavily defocused photograph of an empty modern office at dusk, seen from desk height across a few unoccupied desks toward a large window; deep navy-blue interior tones, two small warm desk lamps as soft bokeh points, the window a faint cooler blue-grey. Almost no detail, extremely low contrast, as if underexposed by three stops; the right half of the frame fades to plain dark navy. No people, no screens with content, no text, logos or signage. Aspect ratio 16:9, 2560×1440 pixels, no transparency, no vignette, no border.

### BG-002 · Module-opener backdrop: faint navy texture

- **Category / method:** backdrop · generated or hand-made abstract texture (fine diagonal paper grain or faint topographic lines), exported as JPEG or as an inline SVG pattern.
- **Priority / batch:** Optional · Batch 3.
- **Slides:** 08, 19, 28, 41, 51, 60, 68 (all seven module openers). One file reused.
- **Learning purpose:** none; marks “a new module starts” from across the room while the content stays on plain navy.
- **Mood / subject / dominant colours:** focused, quiet; `#0B1220` with texture lines no lighter than `#141E30`.
- **Focal area and clear zones:** texture only in the top band y 0–190 (above the title) and the lower-right y 520–900 right of x 855; **clear zones:** both text columns (x 80–811 and the outcomes/glossary panel x 855–1520, y 100–770). On SL41 the glossary fills the right column to y 764, so the texture is confined to the top band.
- **Crop and positioning:** full canvas, anchored top-left; no scaling differences between openers.
- **Overlay/darkening:** opacity ≤ 12 % over the navy.
- **Reuse:** all openers; may also serve the recap SL75 if wanted later (not recommended now).
- **Projection:** at 12 % the texture disappears on weak projectors, which is acceptable; it must never become visible behind text.
- **Dimensions:** 2560 × 1440 JPEG ≤ 120 KB, or an SVG pattern tile 400 × 400 (preferred: a few KB, crisp at any scale). Transparency: tile transparent if SVG. Background.
- **Filename:** `bg-002-opener-texture.jpg` or `bg-002-opener-pattern.svg`.
- **Alt text:** decorative.
- **Avoid:** circuit boards, hexagons, globes, network nodes, lock glyphs: anything that reads as “cyber”.
- **Simpler alternative:** a single 1 px teal rule under the kicker on openers (CSS only; no asset).
- **Generation prompt (if generated rather than drawn):**

  > Abstract, nearly invisible background texture: fine diagonal paper-grain lines on a flat deep navy field (#0B1220), lines at most 8 % lighter than the field, denser in the top-left corner and fading to plain navy across the centre. No shapes, no symbols, no gradients that look like light, no text. Aspect ratio 16:9, 2560×1440 pixels, no transparency.

### BG-003 · Break backdrop: calm, darker variant

- **Category / method:** backdrop · same family as BG-002, lower luminance, optionally with a soft out-of-focus window light in the top-left.
- **Priority / batch:** Optional · Batch 3.
- **Slides:** 18, 40, 59 (the three breaks). One file reused.
- **Learning purpose:** none; signals “paused” for the 10–75 minutes the slide is on screen.
- **Mood / subject / dominant colours:** calm; navy with a faint cooler blue-grey light patch top-left no lighter than `#1B2840`.
- **Focal area and clear zones:** light patch x 0–600, y 0–330; **clear zones:** title block x 80–811, y 380–560 and the “Next” panel x 855–1520, y 350–590; bottom band y 720–900 plain.
- **Overlay/darkening:** opacity ≤ 15 %.
- **Reuse:** all three breaks.
- **Projection:** same rule as BG-002.
- **Dimensions:** 2560 × 1440 JPEG ≤ 150 KB. Transparency: no. Background.
- **Filename:** `bg-003-break.jpg`.
- **Alt text:** decorative.
- **Avoid:** coffee cups, clocks, countdowns (the deck forbids countdowns), food.
- **Simpler alternative:** reuse BG-002 at lower opacity, or none.
- **Generation prompt:**

  > Abstract, very dark background: a flat deep navy field (#0B1220) with one soft, heavily blurred patch of cool blue-grey light in the top-left corner, as if from a distant window, fading to plain navy by the centre of the frame. Extremely low contrast, no shapes, no objects, no text. Aspect ratio 16:9, 2560×1440 pixels, no transparency.

### CHART-001 · QR-code phishing volume observed by one provider (Jan–Mar 2026) — BLOCKED

- **Category / method:** chart · standard charting tool (bar chart with editable labels). **Status: blocked pending data and a content decision. Do not produce yet.**
- **Priority / batch:** Optional · Batch 3 (parked).
- **Slides:** 34 · SL34 “A QR code moves the request” (Module 3) — currently referenced only in the presenter notes, not on the slide.
- **Question the chart would answer:** “Is QR-code phishing a growing channel?” (one provider’s observed volume).
- **Underlying data as recorded in the workshop:** `src/content/notes.json` SL34: “Microsoft reported QR-code phishing in its telemetry rising from about 7.6 million in January to 18.7 million in March 2026. That is one provider’s observed volume, not global prevalence or success rate.” Source S3, Microsoft Email threat landscape Q1 2026, 30 April 2026.
- **Exact values available:** January 2026 ≈ 7.6 million messages; March 2026 = 18.7 million messages. **February is not recorded** and the unit definition (messages observed, blocked, or detected) must be confirmed from S3.
- **Chart type if unblocked:** vertical bar chart, three bars (Jan, Feb, Mar 2026), y-axis “QR-code phishing messages observed (millions)”, x-axis “2026”, caption “Microsoft telemetry; one provider’s observed volume, not global prevalence or success rate.”
- **Caveats:** the claims policy (`02-research/CLAIMS_AND_CASES.md`) says not to put broad statistics on core slides to sound authoritative, and to attribute QR telemetry to the provider. A content-owner decision is required before any chart goes on a participant-facing slide.
- **Does the data already exist in the workshop?** Partially (two of three months, in notes only).
- **Non-numerical alternative (recommended instead):** keep SL34 as it is; the inert QR tile plus the destination card already teach “treat a QR code like a link you cannot read”. The presenter can quote the two figures with attribution.
- **Other statistic reviewed and rejected for charting:** Verizon 2026 DBIR “31 % of breaches began with vulnerability exploitation” (S1/S2) is trainer-only context in the SL09 notes and explicitly not for slides.
- **Dimensions if ever produced:** 594 × 260 canvas px in the SL34 right column. **Filename:** `chart-001-qr-volume.svg`.
- **Alt text if produced:** “Bar chart of QR-code phishing messages observed by Microsoft, January and March 2026 (one provider’s telemetry).”

---

## 5. Backdrop and reuse plan

### 5.1 Where a backdrop helps and where plain is better

| Slide type | Treatment | Why |
|---|---|---|
| Workshop opening (SL01) | BG-001, optional, left-bottom quadrant only, near-black | Sets the “16:42, end of day” mood; keeps the two focal points (headline, email) on clean fields. |
| Agenda (SL02) and takeaways (SL17, 27, 39, 50, 58, 67) and recap (SL75) | **Plain** | These are read slowly; the list is the only content and must stay on flat navy. |
| Module openers (SL08, 19, 28, 41, 51, 60, 68) | BG-002, optional, one shared texture, top band and lower-right only | Marks a new module without a new theme; one file for seven slides. |
| Workplace scenarios (chat, email, profile, browser, phone: SL03–04, 10–14, 20–23, 29–35, 43–47, 52–56) | **Plain** | The evidence must be the only thing to read; scene photographs (IMG-001/002) sit *inside* the explanation column, not behind it. |
| Dense explanations (SL09, 15, 24, 37, 38, 42, 66, 69, 71, 72) | **Plain** | Information-heavy; any texture lowers legibility. |
| Email/document inspection (SL03, 06, 30, 31, 34, 56) | **Plain** | Paper surfaces on navy already give maximum figure-ground contrast. |
| Exercises and votes (SL05, 11, 16, 22, 25, 26, 36, 49, 53, 57, 61–65, 73, 74) | **Plain** | Nothing may compete with the options or the task. |
| Breaks (SL18, 40, 59) | BG-003, optional, one shared file | Calm, darker, readable as “paused” across the room. |
| Close (SL76) | **Plain** | Panels and a button; keep it clean. |

Three unique backdrops in total (BG-001, BG-002, BG-003). No exceptions requested.

### 5.2 Reuse map for new assets

| Asset | Used on | Reuse note |
|---|---|---|
| ICON-001 | SL38, SL42, SL69, SL71 (recommended); SL21, SL37 (optional); SL49, SL75 and the printed card (permitted reuse, no new asset) | One sprite serves the whole deck and the participant card. |
| IMG-002 | SL04, SL20 | Same character, same kind of scene; one file. |
| BG-002 | SL08, 19, 28, 41, 51, 60, 68 | One file. |
| BG-003 | SL18, 40, 59 | One file. |
| FLOW-001 | SL43 | SL48 (Cloudflare) refers to it verbally; no second copy. |
| INFO-001 | SL12 | SL15 and SL36 build on it verbally; no second copy. |

### 5.3 Audit of existing assets (verified by inspection, not by filename)

| ID | Asset | What it is | Where used | Verdict |
|---|---|---|---|---|
| EX-001 | `dist/Image_ref/profile-pictures/aina.png` | AI-generated portrait, 1254×1254 PNG; young Malay woman, dark teal hijab, cream top, light-grey studio background | SL08, 10, 11 (×2 by design), 28, 41, 51, 60, 61, 68 via 192 px avatar | **Retain.** Character reference for IMG-001. |
| EX-002 | `…/farid.png` | Malay man ~30, short dark hair, light stubble, light-blue shirt | SL08, 19, 28, 51, 60, 61 | **Retain.** Reference for IMG-002. |
| EX-003 | `…/mei.png` | Chinese woman ~30s, shoulder-length dark hair, navy blazer | SL41, 51, 52 (impersonator uses her photo by design), 60, 61, 68 | **Retain.** |
| EX-004 | `…/ravi.png` | Indian man ~40, black-framed glasses, full beard, maroon shirt | SL04, 19, 20, 21, 28, 30 (impersonator), 60, 61 | **Retain.** |
| EX-005 | `…/nadia.png` | Malay woman ~30s, dusty-pink hijab, thin-rim glasses, dark blazer | SL01, 03, 06, 19, 28 | **Retain.** |
| EX-006 | `…/siti.png` | Young Malay woman, navy hijab, light-blue blouse | SL08, 12 | **Retain.** |
| EX-007 | `…/daniel.png` | Young Chinese man, dark hair, charcoal shirt | SL08, 14 | **Retain.** |
| EX-008 | `…/lina.png` | Malay woman ~40s, beige hijab, dark blazer over white top | SL68, 73 | **Retain.** |
| EX-009 | `…/it-caller.png` | Malay man ~40, short hair, navy polo | SL19, SL23 (labelled “photo is an illustration”) | **Retain.** Must not be used as a reference for any new image; the caller stays faceless in IMG-001. |
| EX-010 / EX-011 | QR-style tiles generated by `build/build.py qr_svg()` | Decorative, non-decodable SVG with a solid “DEMO QR · NO SCAN” band | SL34, SL47 | **Retain.** Correctly inert. |
| EX-012 | `src/img/avatars/*.jpg` (9 × 192×192) | Build-time crops of EX-001…009 | 43 embedded occurrences | **Retain.** Resolution adequate (max display 86 device px at 1920×1080). Not stretched. |
| EX-013 | `dist/Image_ref/random-person.jpeg` | 1024×1024 outdoor portrait of a woman, warm bokeh; not a cast member | Unused | **Exclude.** Style conflicts with the studio portraits; not a character. |
| EX-014 | `dist/Image_ref/random-person2.jpeg` | 1024×1024 outdoor portrait; appears to carry a small embedded text mark bottom-right (confirm at full size) | Unused | **Exclude.** Embedded text and style conflict. |
| EX-015 | `dist/Image_ref/Cybersecurity-Awareness-Profile-Pictures.zip` | 17.4 MB archive of the nine portraits | Unused by build | Keep as source archive; do not ship with the deck. |
| EX-016 | `06-prototype/reference_screenshots/slide-01…06.png` | Screens of the superseded six-slide prototype (old toolbar/dots shell) | Unused | Reference only; **not** a style target for new work. |

Findings: no broken image references (every `<img>` in the built file is an embedded data URI; initials fall back where intended on SL34 and SL56); no low-resolution or stretched images; no images with distracting embedded text in the deck itself; the only style conflicts are the two unused `random-person` files. The one asset the deck is *missing* is customer-dependent: a safe screenshot of the real reporting action for SL70 (`config.reporting.screenshot_asset`, currently null); nothing generic should stand in for it.

---

## 6. Prioritised production batches

### Batch 1 — essential teaching visuals and the most valuable improvements

| Asset | Slides | Priority | Method |
|---|---|---|---|
| FLOW-001 Relayed sign-in diagram | SL43 | Essential | SVG |
| FLOW-002 Device-code flow | SL45 | Essential | SVG |
| FLOW-004 Paste-step consequence flow | SL54 | Recommended | SVG |
| INFO-001 Copied profile vs taken-over account | SL12 | Recommended | SVG |
| ICON-001 Icon set (14 core icons; recommended placements SL38, SL42, SL69, SL71) | SL38, 42, 69, 71 | Recommended | SVG symbols |

### Batch 2 — recommended supporting visuals

| Asset | Slides | Priority | Method |
|---|---|---|---|
| FLOW-003 Join vs link | SL47 | Recommended | SVG |
| INFO-002 Desktop view of the same request | SL33 | Recommended | HTML/CSS |
| INFO-003 Chain strip | SL66 | Recommended | SVG |
| IMG-001 Aina takes an unexpected call | SL23 | Recommended | AI image (reference: aina.png) |

### Batch 3 — optional atmosphere and finishing touches

| Asset | Slides | Priority | Method |
|---|---|---|---|
| IMG-002 Farid before the cut-off | SL04, SL20 | Optional | AI image (reference: farid.png) |
| BG-001 Cover dusk backdrop | SL01 | Optional | AI image, darkened |
| BG-002 Opener texture | SL08, 19, 28, 41, 51, 60, 68 | Optional | Texture / SVG pattern |
| BG-003 Break backdrop | SL18, 40, 59 | Optional | Texture |
| ICON-001 optional placements | SL21, SL37 | Optional | SVG (same sprite) |
| CHART-001 QR volume | SL34 (notes) | Blocked | Charting tool, after data decision |

### Counts

Unique new assets by category:

| Category | Count | IDs |
|---|---|---|
| annotated_example | 1 | INFO-002 |
| backdrop | 3 | BG-001, BG-002, BG-003 |
| character_scene_photo | 2 | IMG-001, IMG-002 |
| chart | 1 | CHART-001 |
| comparison_diagram | 2 | FLOW-003, INFO-001 |
| flow_diagram | 3 | FLOW-001, FLOW-002, FLOW-004 |
| icon_set | 1 | ICON-001 |
| infographic | 1 | INFO-003 |

Unique new assets by priority:

| Priority | Count | IDs |
|---|---|---|
| Essential | 2 | FLOW-001, FLOW-002 |
| Optional | 5 | BG-001, BG-002, BG-003, CHART-001, IMG-002 |
| Recommended | 7 | FLOW-003, FLOW-004, ICON-001, IMG-001, INFO-001, INFO-002, INFO-003 |

- Unique new assets: **14** (13 producible now, 1 blocked: CHART-001).
- Existing assets catalogued: **16** (13 retained, including the source archive; 2 excluded; 1 reference-only). Existing assets are counted separately and are not part of the 14.
- Slide placements of new assets: 28 (ICON-001 ×6, BG-002 ×7, BG-003 ×3, IMG-002 ×2, all others ×1). Slides with a new or changed visual: 28 of 76; slides with no change: 48.

---

## 7. ChatGPT handover (copy-ready)

> **Context.** You are receiving the visual audit of a 76-slide, single-file HTML cybersecurity-awareness workshop (`dist/workshop.html`, v3 redesign of 8 Oct 2026). The companion `WORKSHOP_VISUAL_ASSET_MANIFEST.json` lists every slide, every proposed asset, dimensions, priorities and verification status. Please help review the plan and create the assets in priority order. Do not change the slides’ wording, order or interactions.
>
> **Current visual direction (keep it).** Navy canvas `#0B1220`, surfaces `#141E30`/`#1B2840`, warm-white text `#F3F6FA`/`#B4C0D2`, teal accent `#2DD4BF` (safe route, emphasis), amber `#FBBF24` (markers, the thing to notice), coral `#FB7185` (confirmed harm only), paper `#FFFFFF`/`#F3F6FA`/`#E8EEF5` with ink `#19283B` for anything that is a screen or document. Arial/Helvetica, 2 px lines, radii 8/14/20, no gradients, shadows or glows. The deck is a 1600×900 canvas scaled to the screen; minimal shell (menu button, drawer, counter) that must not change. All evidence (email, chat, browser, phone, consent, QR) stays editable HTML. Every raster must be embedded as a data URI (CSP `img-src data:`), so keep JPEGs ≤ 180–250 KB; diagrams are inline SVG with real text.
>
> **Create first (Batch 1).** FLOW-001 relayed-sign-in diagram (SL43, Essential), FLOW-002 device-code flow (SL45, Essential), FLOW-004 paste-step consequence (SL54), INFO-001 copied-profile vs taken-over account (SL12), ICON-001 line-icon set, 14 core icons (SL38, SL42, SL69, SL71). Exact labels, reading order, node lists, colour meanings and measured sizes are in §4 of the audit.
>
> **Then (Batch 2).** FLOW-003 join vs link (SL47), INFO-002 desktop mail-header mock (SL33, HTML/CSS not an image), INFO-003 chain strip (SL66), IMG-001 Aina on the phone (SL23).
>
> **Optional (Batch 3).** IMG-002 Farid before the cut-off (SL04, SL20), BG-001 cover dusk backdrop, BG-002 opener texture, BG-003 break backdrop, optional icon placements on SL21 and SL37.
>
> **Needs AI image generation:** IMG-001, IMG-002 (character scenes), BG-001 (and optionally BG-002/BG-003 if not drawn). Copy-ready prompts are in §4. Default to no baked-in text.
>
> **Needs precise diagrams (SVG/HTML, not AI bitmaps):** FLOW-001, FLOW-002, FLOW-003, FLOW-004, INFO-001, INFO-002, INFO-003, ICON-001.
>
> **Charts:** CHART-001 (QR phishing volume) is blocked: only January (≈7.6 M) and March (18.7 M) 2026 values are recorded, in presenter notes, from Microsoft’s Q1 2026 report (one provider’s telemetry), and the content policy keeps broad statistics off core slides. Do not invent the February value. No other chart is recommended.
>
> **Existing images to supply as references (the only authorised likenesses):** `dist/Image_ref/profile-pictures/aina.png` for IMG-001; `dist/Image_ref/profile-pictures/farid.png` for IMG-002. Do not use `it-caller.png` as a reference for anything (the caller must stay faceless). Do not use `random-person.jpeg` / `random-person2.jpeg` (unused, style conflict, one appears to carry embedded text).
>
> **Reusable:** ICON-001 across SL38/42/69/71 (+ SL21/37 optional, and SL49/SL75/the printed card without a new asset); IMG-002 on two slides; BG-002 on seven openers; BG-003 on three breaks.
>
> **Still to verify before implementation:** (1) physical-projector check of any backdrop contrast; (2) re-run the deck’s own fit and contrast QA (`build/qa/render.cjs`, `build/qa/interact.cjs`) after each placement; (3) the content owner confirms the INFO-002 desktop wording and the CHART-001 decision; (4) the embedded-text mark on `random-person2.jpeg` if anyone proposes using it; (5) customer-supplied screenshot for SL70 (not a design asset; customer-dependent).
>
> **Rules that apply to every asset:** fictional Meranti only (no real brands, logos, victims or customer faces); no hooded hackers, padlock clichés, binary rain or glowing shields; no commands, codes or scannable QR codes; suspicious evidence stays neutral until a vote or reveal; words always accompany colour; nothing may be placed on pause-point slides or on top of evidence panels.

**Next step:** Send WORKSHOP_VISUAL_AUDIT.md and WORKSHOP_VISUAL_ASSET_MANIFEST.json back to ChatGPT, together with any referenced character images or other required assets. ChatGPT can then review the plan and help create the visuals in priority order.
