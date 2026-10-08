# Design: deck clarity rework

Date: 2 October 2026. Status: approved in brainstorming, awaiting written-spec review.
Applies to: `dist/workshop.html` and its sources (`04-content/slides.json`, `src/slides/*.html`, `src/content/*.json`, `src/css`, `src/js`, `build/`).

## 1. Goal

Participants should understand, on every slide and in every module, what it is trying to achieve, without the trainer clicking to uncover hidden content. The deck is facilitator-led, but each slide must stand on its own: a participant who drifts off, or reads it later, can still follow.

## 2. Decisions taken

| Topic | Decision |
|---|---|
| Delivery | Facilitator-led; every slide self-explanatory (option B) |
| Interactions | Keep 16 deliberate pause points; everything else shows its content from the start (option B) |
| Module framing | Opener slide and takeaway slide for every module M1–M7, plus one “Today’s workshop” slide after the cover |
| Photos | Use `dist/Image_ref/profile-pictures/` for all nine characters |
| Language | English only |
| Approach | Rework in place on the existing build; renumber to SL01–SL76 |
| Breaks | Titles “Short break”, “Lunch break”, “Tea break”; no clock times and no prayer wording anywhere participants see |
| Clock times | Removed from all participant-facing screens; kept in presenter notes and facilitator guide only |

## 3. Slide structure (76 slides)

Old IDs in brackets. **Bold** = new slide. ★ = pause point (keeps a click).

- **M0 Opening:** SL01 Cover (01) · **SL02 Today’s workshop** · SL03 Email (02) · SL04 Ravi chat (03) · SL05 ★ What should Farid do? (04) · SL06 ★ Callback (05) · SL07 Hong Kong case (06)
- **M1 The borrowed identity:** **SL08 Opener** · SL09 Terms (07) · SL10 Aina’s profile (08) · SL11 ★ Two profiles (09) · SL12 Siti chat (10) · SL13 Fake support (11) · SL14 Collaboration (12) · SL15 Clone vs takeover (13) · SL16 ★ Decision (14) · **SL17 Takeaway**
- **Short break:** SL18 (15)
- **M2 The trusted request:** **SL19 Opener** · SL20 Urgent manager (16) · SL21 Pressure tactics (17) · SL22 Roleplay (18) · SL23 Phone call (19) · SL24 Face or voice (20) · SL25 ★ Which number? (21) · SL26 ★ Genuine change (22) · **SL27 Takeaway**
- **M3 The message that fits your job:** **SL28 Opener** · SL29 Inbox (23) · SL30 Sender (24) · SL31 ★ URL (25) · SL32 Polished messages (26) · SL33 Phone view (27) · SL34 QR (28) · SL35 Shared files (29) · SL36 ★ Four-card exercise (30) · SL37 Signals table (31) · SL38 Your route (32) · **SL39 Takeaway**
- **Lunch break:** SL40 (33)
- **M4 Beyond the password:** **SL41 Opener with glossary** · SL42 Access types (34) · SL43 Relayed sign-in (35) · SL44 MFA prompts (36) · SL45 Device code (37) · SL46 App consent (38) · SL47 Device linking (39) · SL48 Cloudflare case (40) · SL49 ★ Decision (41) · **SL50 Takeaway**
- **M5 The helpful stranger:** **SL51 Opener** · SL52 Fake Mei (42) · SL53 ★ Remote access (43) · SL54 Fake CAPTCHA (44) · SL55 CrashFix (45) · SL56 Renewal notice (46) · SL57 ★ Genuine support (47) · **SL58 Takeaway**
- **Tea break:** SL59 (48)
- **M6 Stop the chain:** **SL60 Opener** · SL61 Roles (49) · SL62–SL65 ★ Tabletop T1–T4 (50–53) · SL66 Debrief (54) · **SL67 Takeaway**
- **M7 Report and recover:** **SL68 Opener** · SL69 Pause/verify/report/recover (55) · SL70 Reporting route (56) · SL71 After a mistake (57) · SL72 Useful report (58) · SL73 ★ HR request (59) · SL74 Reflection (60) · **SL75 Takeaway and whole-day recap** · SL76 Questions and references (61)

Pause points (16): SL05, SL06, SL11, SL16, SL25, SL26, SL31, SL36, SL49, SL53, SL57, SL62, SL63, SL64, SL65, SL73. These are the same slides agreed in the review; the earlier figure of “14” in conversation was a counting error.

## 4. Interaction rules

- **Pause-point slides** are exactly: votes SL05, SL11, SL16, SL25, SL26, SL49, SL53, SL57, SL73; reveals SL06, SL31, SL62, SL63, SL64, SL65; and the exercise SL36. These are the only slides with interactive controls inside the slide. Their Key point box appears after the vote or reveal. “Reset slide” remains for them.
- **SL36 four-card exercise:** the 12 per-card buttons are removed. Tables vote by hand; one reveal button shows each card’s hidden fact and recommended action.
- **All other slides** render fully: complete chats (no message-by-message stepping), inspection details shown as labelled callouts, completed step sequences, the clone-versus-takeover table with ticks, the full signals table, and the answers that were previously behind choices (old SL36, SL38, SL46) shown as text.
- Evidence on open slides carries numbered amber markers (①②③) with short notes. The original rule “suspicious evidence stays neutral until a reveal” now applies only to pause-point slides.
- The cover button, the SL76 “Open the reference index” button and the footer controls remain. They are navigation, not slide interactions.

## 5. Explanation layer

Every content slide (all except the cover, breaks and SL76) has:

1. **“What this slide shows”**: one plain sentence under the title.
2. **Key point box**: same teal style and position on every slide; one or two sentences to remember.
3. **Plain definitions** of technical terms at first use (phishing, spear phishing, impersonation, MFA, session, device code, app permission/consent, linked device, ClickFix). M4’s opener includes a compact glossary.

**Module opener template:** module number and title; “Why this matters” (one sentence); “By the end you’ll be able to” (2–3 bullets); “Who you’ll meet” (photos with roles). No clock times.

**Module takeaway template:** three takeaways; “Your habit from this module” (one line). SL75 also lists the seven module habits as the whole-day recap.

**SL02 Today’s workshop:** four outcomes for the day; agenda as an ordered list of modules and breaks without clock times; ground rules (everything is fictional, there are no wrong questions, nobody needs to share a personal incident, reporting is never blamed).

Content still must fit 1366×768 and 1440×900 without shrinking evidence text below current sizes. A slide that cannot fit is split and the split is recorded.

## 6. Photos

- Source: `dist/Image_ref/profile-pictures/{aina,farid,mei,ravi,nadia,siti,daniel,lina,it-caller}.png` (README states AI-generated fictional characters). `random-person*.jpeg` are not used.
- Each image is resized at build time to a small square avatar (target about 20 KB, JPEG or WebP) and embedded as a data URI, so `workshop.html` stays one offline file.
- Used consistently for email senders, chat headers, social profiles, role cards, the cover cast and module openers. Impersonators use the impersonated person’s photo (fake Ravi, fake Mei, the copied Aina profile). The phone call scene labels the IT caller photo as an illustration.
- Alt text: name and role, or empty alt where the name is already displayed beside the photo.
- Credit line on the cover and in the help panel: “Portraits are AI-generated; no real person is depicted.”
- If an image file is missing, the build falls back to the existing initial avatar.

## 7. Breaks and times

- Break slides show only the break name and “We return with Module N · Title”. No clock times, durations or prayer wording.
- Prayer references are removed from slides, the module bar and the participant card. The facilitator guide keeps break lengths but drops prayer wording. The `prayer_schedule_confirmed` config field becomes unused and is no longer listed as a customer input.
- Module bar tooltips and labels show module names without times. Presenter notes and the facilitator guide keep start/end times per slide.

## 8. Timing

- Programme remains 420 minutes; break lengths unchanged (10, 75, 25); module totals unchanged (M0 20, M1 45, M2 45, M3 60, M4 50, M5 35, M6 35, M7 20).
- Openers and takeaways: 2 minutes each. SL02: 3 minutes; cover reduced to 1 minute.
- Time comes from open slides that no longer need click-through time. Pause-point slides, the roleplay (SL22) and the tabletop keep their current minutes. Exact per-slide minutes are set in `slides.json` during implementation; the build enforces totals.

## 9. Supporting outputs

- `slides.json`: 76 entries, new IDs, titles, objectives, timings, notes, `what_this_shows`, `key_point`, and a `pause_point` flag.
- Facilitator guide: module goals, takeaways and habits; runbook phrased as “say this, then ask this”, because answers are now on screen.
- Participant card: adds the seven habits and a short glossary; still one A4 page.
- Source index, README and QA report regenerated with the new numbering. Old-to-new ID mapping recorded in the QA report.

## 10. Validation

- The build fails if a content slide lacks “What this shows” or a Key point; if interactive controls appear outside the pause-point list; if any participant-facing text contains a clock time on break, opener or agenda slides, or the word “prayer”; or if totals change.
- Re-render all 76 slides at 1440×900, 1366×768 and 390px (default and revealed states), inspect the images, and fix issues.
- Re-run the interaction tests, adapted to the 16 pause points, plus contrast checks including text over photos.
- Existing safety checks remain: no forms, no live links to mock domains, no network requests, and inert mock material.

## 11. Out of scope

Translation; new attack topics; changes to palette, typography or navigation; customer-specific reporting details (still placeholders until verified).
