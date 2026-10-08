# M4 content script

## SL34: Access can be granted without sharing a password
Time: 14:15–14:21 (6 minutes). Layout: comparison. Evidence: guidance.
Objective: Understand permissions and sessions

Screen copy:
- A sign-in, permission or device approval can grant access.

Evidence to create: Four inert cards: login session, MFA request, app permission, linked device.
Interaction: Identify the access each card represents.
Reveal: Check what session, device or app receives access.
Facilitator notes: Keep technical protocol detail in notes.
Sources: S11, S12

## SL35: The login session an attacker can reuse
Time: 14:21–14:28 (7 minutes). Layout: browser. Evidence: fictional.
Objective: Understand session theft at a high level

Screen copy:
- A deceptive sign-in flow may capture a usable session.

Evidence to create: Annotated static sign-in sequence, no credential fields.
Interaction: Reveal the access consequence.
Reveal: Use approved sign-in routes and report suspicious flows.
Facilitator notes: Describe AiTM conceptually. No proxy code or live capture. Do not say MFA is pointless.
Sources: S11, S13

## SL36: An approval you did not start
Time: 14:28–14:34 (6 minutes). Layout: mobile. Evidence: fictional.
Objective: Respond to MFA pressure

Screen copy:
- Deny an unexpected request.
- Report repeated or suspicious prompts.

Evidence to create: Mock approval notification repeated twice.
Interaction: Choose deny/report or approve-to-stop.
Reveal: Do not approve access you did not initiate.
Facilitator notes: MFA remains useful. Number matching reduces some risks but does not legitimise an unsolicited request.
Sources: S8, S13

## SL37: A real sign-in page, someone else’s code
Time: 14:34–14:42 (8 minutes). Layout: browser. Evidence: fictional.
Objective: Recognise device-code phishing

Screen copy:
- Whose device or session would this code authorise?

Evidence to create: Document invitation supplies a DEMO-ONLY code and genuine-looking static service page.
Interaction: Reveal who initiated the request.
Reveal: Enter codes only for recognised sessions you initiated.
Facilitator notes: No real device code. Verify purpose even when the service address is genuine.
Sources: S12

## SL38: The app asking for your permission
Time: 14:42–14:49 (7 minutes). Layout: browser. Evidence: fictional.
Objective: Assess app consent

Screen copy:
- An app asks to read messages or files.
- Use the approved application process.

Evidence to create: Fictional Meeting Helper requests unnecessary access.
Interaction: Inspect permission list, choose IT approval route.
Reveal: A real consent screen does not validate the app’s purpose.
Facilitator notes: Unknown publisher alone is not definitive. Do not ask learners to grant real consent.
Sources: S11

## SL39: Linking another device
Time: 14:49–14:55 (6 minutes). Layout: qr. Evidence: fictional.
Objective: Recognise device-linking abuse

Screen copy:
- Link only devices and sessions you recognise and initiated.

Evidence to create: Inert WhatsApp-style linked-device screen; fictional invitation.
Interaction: Reveal difference between joining a group and linking a device.
Reveal: A linking QR can authorise access to an account.
Facilitator notes: Use labelled nonfunctional placeholder, never a scannable account-link code.
Sources: S11

## SL40: A defence that stopped the attempted access
Time: 14:55–15:00 (5 minutes). Layout: case. Evidence: documented.
Objective: Understand layered controls

Screen copy:
- Cloudflare reported three credential submissions.
- Hardware-key requirements prevented the attempted access.

Evidence to create: July 2022 SMS campaign, disclosed August 2022.
Interaction: Compare credential exposure with prevented access.
Reveal: Staff reporting and technical controls work together.
Facilitator notes: Historical positive case. Do not promise keys prevent consent or payment fraud.
Sources: S14, S13

## SL41: What does this approval grant?
Time: 15:00–15:05 (5 minutes). Layout: decision. Evidence: fictional.
Objective: Distinguish authentication from business authority

Screen copy:
- A trusted service asks you to approve an unfamiliar session.

Evidence to create: Genuine-looking code/consent/MFA mini-cards.
Interaction: Identify grant and independent route.
Reveal: Pause and verify origin and purpose.
Facilitator notes: Ask for learner explanation rather than technical vocabulary.
Sources: S11, S12


### SL41 explicit decision key
- Approve because the service is genuine: The request may authorise someone else’s session or an unwanted app.
- Check the initiating session or app through the known route: Verify what access is granted and why before acting. [Preferred]
- Disable MFA to avoid prompts: MFA remains useful; report suspicious requests rather than disabling it.
