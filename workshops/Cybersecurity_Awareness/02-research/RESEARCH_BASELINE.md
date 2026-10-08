# Background research snapshot

The following brief was created on 30 September 2026. It provides research context. The current PROJECT_BRIEF, MASTER_STORYBOARD and execution prompt supersede its slide counts, build sequencing and draft production instructions.

# Cybersecurity Awareness: Impersonation and Phishing

Research brief and story-led HTML workshop blueprint

Prepared 30 September 2026 • Proposed delivery: 10:00–17:00 MYT

## Recommendation and scope

Use one workplace story to connect social-media impersonation, phishing, payment fraud and recovery. Participants should repeatedly decide what to do with incomplete information, explain their decision, then see the consequence and the safer process.

The supplied agenda covers social-media impersonation: definition, mechanics, types, examples, detection, response, Provintell support for SIRIM, and a quiz. Preserve those outcomes. Expand the channels to email, WhatsApp, Teams, phone calls, QR codes, sign-in pages and app permissions. Do not assume the new audience is SIRIM solely because the old slide names SIRIM.

This deliverable is the research and production blueprint, not the completed HTML presentation. It assumes a mixed, nontechnical employee audience with some managers, finance, HR and IT staff. The proposed teaching timings, characters, activities and evaluation targets are instructional recommendations, not claims that a standard prescribes this exact course.

Research covers established and emerging attack families documented through the review date. No finite workshop can cover every campaign or future variant. Teach repeatable decisions across channels; keep technical variants in trainer notes.

## Evidence and claims to use carefully

- Phishing and impersonation deserve substantial coverage, but “most successful cyberattacks start with spear phishing” is not supported by the sources reviewed. Verizon's 2026 DBIR identifies vulnerability exploitation as the leading entry point, at 31% of breaches in its dataset. Its publication year differs from its incident collection window: 1 November 2024 to 31 October 2025. [S1, S2]
- Microsoft reported QR-code phishing increasing from 7.6 million in January to 18.7 million in March 2026 in its telemetry. This describes one provider's observed volume, not the percentage of organisations breached or the likelihood that a particular message succeeds. [S3]
- MyCERT's 19 March 2026 advisory describes scam-call impersonation and fake government assistance offers among observed Malaysian threats. Use this as local context without presenting reported incidents as all cybercrime in Malaysia. [S4]
- Distinguish observed incident facts, researchers' assessments, and our own classroom reconstructions. A named attack group is unnecessary for an employee to learn the correct response.
- Training supports risk reduction alongside technical controls and business procedures. Do not promise that a one-day workshop eliminates phishing or proves compliance.

## Learning outcomes

By the end, participants should be able to:

1. Distinguish a copied identity from an attacker using a genuine compromised account.
2. Identify the action a sender wants: money, information, login, permission, device linking, software installation, or remote access.
3. Verify a sensitive request using contact details or an application they already trust.
4. Explain why a familiar logo, correct grammar, HTTPS, or a known sender is insufficient evidence of safety.
5. Recognise suspicious MFA, device-code, app-consent and account-linking requests in plain language.
6. Report a suspicious message or a mistaken action through the organisation's actual process.
7. Apply additional checks for payment changes, personnel data and account recovery.

## Full-day agenda

| Time | Session | Participant action |
|---|---|---|
| 10:00–10:20 | Opening scene and baseline | Choose a response to an apparently normal request; explain confidence |
| 10:20–11:05 | Module 1: The borrowed identity | Inspect a cloned profile, a genuine compromised account, and a brand impersonation page |
| 11:05–11:15 | Break | 10 minutes |
| 11:15–12:00 | Module 2: The trusted request | Work through manager impersonation, vendor payment changes, voice fraud and deepfakes |
| 12:00–13:00 | Module 3: The message that fits your job | Inspect Outlook, mobile, QR and shared-file examples; practise independent verification |
| 13:00–14:15 | Lunch and prayer | Provisional 75-minute block |
| 14:15–15:05 | Module 4: Beyond the password | Explore MFA prompts, session theft, device codes, consent and linked devices |
| 15:05–15:40 | Module 5: The helpful stranger | Investigate Teams support impersonation, fake verification and software-repair prompts |
| 15:40–16:05 | Tea and prayer | Provisional 25-minute block |
| 16:05–16:40 | Module 6: Stop the chain | Team tabletop with a payment request, suspicious login and colleague report |
| 16:40–17:00 | Module 7: Report, recover and retain | Reporting practice, parallel post-assessment and questions |

Total: 420 minutes; learning and activities: 310 minutes; breaks: 110 minutes. Lunch/prayer blocks are planning allowances, not verified prayer times. Confirm the venue, date and local timetable; Friday congregational prayer may require a longer midday block. If needed, reduce optional technical examples instead of rushing response practice.

## Story concept: “The Request Before 5 PM”

Set the story at fictional Meranti Services. A client deadline approaches. Four recurring characters carry the narrative: Aina in operations, Farid in finance, Mei in IT support, and Ravi as department head. Use fictional staff, business names, addresses and data throughout.

Open with a short scene: Aina receives a collaboration request that appears relevant to her work. Later, Farid receives a vendor change request, while someone claiming to be Mei offers help with an account problem. Participants see what each employee could reasonably know at that moment.

| Act | Evidence participants receive | Decision and reveal |
|---|---|---|
| 1: A familiar face | Social profile, copied work history, message about a project | Choose whether to trust, ignore or verify; reveal the copied identity |
| 2: A believable request | Professional email and a relevant document invitation | Identify the requested action; open the known company portal instead |
| 3: An approval | Sign-in or permission screen | Determine which session, device or app would gain access |
| 4: Someone offers help | Teams message or scripted support call | Verify a support ticket before sharing a screen or allowing control |
| 5: The payment deadline | Existing supplier thread and changed bank details | Call the established vendor contact and follow dual approval |
| 6: Someone speaks up | A colleague says they already approved something | Practise a supportive report and see how early reporting changes the outcome |

This is a fictional composite. Do not imply all researched techniques occurred in one real attack. Give advanced variants their own side scenes rather than forcing every attack into one implausible chain.

Use a repeatable scene rhythm: show the evidence; ask for a choice; hear the reason; reveal missing context; demonstrate a safer action; connect it to a verified source. Include legitimate messages that deserve verification, so the activity does not reward calling everything malicious.

## Module detail and attack coverage

### Module 1: Identity and social-media impersonation

Explain impersonation as falsely presenting oneself as a trusted person or organisation. Phishing uses deceptive communication to induce an action; spear phishing targets a particular person or group. These concepts overlap and can form stages of the same incident.

| Method | What the learner sees | What to teach |
|---|---|---|
| Cloned profile | Familiar photo, name, role and copied posts | A copied profile does not establish control of the genuine person's account |
| Compromised genuine account | A message from a real colleague's established account | A genuine account can carry an unauthorised request |
| Brand/support impersonation | A page, advert or direct message offering account help | Find support through the service's known app or saved website |
| Recruitment/collaboration pretext | A plausible contact relevant to the recipient's work | Check the organisation and process before disclosing work information |
| Government/authority impersonation | Threats, claimed investigations or benefit offers | Stop and verify with the agency through independently sourced details |

Evidence: FTC documents business impersonation across calls, messages and social platforms, including compromised accounts and combined impersonation schemes. MyCERT provides Malaysian authority and assistance-scam context. [S4, S5, S6]

Exercise: show three fictional profiles and a message from each. Ask “What can you establish from this screen?” and “What would you verify elsewhere?” Treat uncertainty as a reason to verify, not a failure.

Response if impersonated: preserve the profile URL, account handle, screenshots and timestamps; report through platform processes; tell internal security and communications for work-related impersonation; warn affected contacts through a trusted channel. If the genuine account may be compromised, use the platform's official recovery route and review access with support. Do not assume changing a password removes a cloned account.

### Module 2: Pressure, payment and voice

| Method | Classroom example | Safer action |
|---|---|---|
| Manager impersonation | “I need you to handle a confidential payment before 5” | Verify through the staff directory and keep the normal approval process |
| Vendor/BEC fraud | Bank details change inside an expected invoice conversation | Call the vendor using existing records and obtain required second approval |
| Voice impersonation | Caller knows names and asks for a reset or code | Call back through the established service desk |
| Synthetic voice/video | Familiar manager appears to approve a transfer | Validate the transaction through a separate authorised workflow |
| Channel switching | Email asks the employee to move to private chat | Treat the move as context to examine, not automatic proof of fraud |

FBI guidance supports independent verification of payment changes. The Scattered Spider joint advisory documents helpdesk impersonation and voice-based attempts to reset passwords or MFA. [S7, S8]

Case: Hong Kong authorities described a January 2024 fraud involving an email impersonating a UK CFO, a fabricated prerecorded video conference and approximately HK$200 million transferred. The official account says the video contained no interaction. Avoid retelling this specific case as proven live, interactive AI video. [S9]

Activity: pairs practise declining an urgent request politely: “I can help once I confirm through our normal approval process.” Judge the verification route, not participants' ability to notice video glitches. Visual or audio artefacts are unreliable as the only defence.

### Module 3: Phishing in everyday work

| Family | Visual example for the deck | Decision to practise |
|---|---|---|
| Targeted email | Relevant tender, HR notice or event invitation | Verify the business context and requested action |
| Display-name/lookalike deception | Familiar name hiding a different address or misleading hostname | Expand the sender and inspect the full destination without opening it |
| Compromised-account/thread abuse | A plausible reply in a genuine conversation | Verify changes involving money, access or sensitive data |
| Smishing and chat phishing | Short mobile notification or colleague message | Open the known app; do not act from the message alone |
| QR phishing | A security notice asks the recipient to scan using a phone | Preview the destination and use the known service instead |
| Shared-file and attachment lures | Document-sharing card, PDF, HTML or SVG attachment | File branding or format does not establish safety |
| Conversation-first phishing | Harmless enquiry followed later by a request | Re-evaluate the sensitive action even after normal conversation |
| AI-assisted language | Fluent, personalised message without spelling mistakes | Grammar is a weak signal; verify identity and purpose |

MITRE describes links, attachments, services and voice as phishing sub-techniques. Microsoft documents QR and file-format shifts, plus targeted identity lures. [S3, S10, S11]

Provide a desktop and phone view of the same message. A safe fictional destination can be displayed as `https://login.company.example.attacker.test/review`; the learner should identify that the hostname ends in `attacker.test`, not `company.example`. Do not make learners memorise domain rules as their sole protection; genuine hosted pages and compromised accounts can also be abused.

Teach three inspection questions: Who is asking? What action would I take? How can I verify it outside this message? HTTPS protects the connection to a site; it does not certify the sender's business intent. The absence of an email warning does not certify safety.

### Module 4: Modern account-access deception

Keep the learner explanation short. Put protocol names and technical detail in presenter notes.

| Technique | Plain-language explanation | Learner action |
|---|---|---|
| Adversary-in-the-middle/session theft | A deceptive sign-in flow can capture a usable login session | Use approved sign-in routes; report unexpected sign-in flows |
| MFA fatigue | Someone repeatedly asks you to approve access you did not start | Deny and report; do not approve to stop the notifications |
| Device-code phishing | You enter a supplied code at a real sign-in service and authorise someone else's session | Do not enter unsolicited codes; verify the device and purpose |
| Consent phishing | An app asks permission to access your information | Check purpose and permissions; use the approved app process |
| Device-linking or registration abuse | A joining or QR process grants another device access | Link/register only devices and sessions you initiated and recognise |

Microsoft's April 2026 research describes device-code abuse using legitimate authentication to obtain tokens without stealing the password. Its May 2025 identity research includes consent and device-linking abuse. The Scattered Spider advisory documents MFA pressure. [S8, S11, S12]

Use distinct mini-scenes for fake sign-in, a genuine page with an unexpected device code, and an app-consent screen. A good answer identifies what would be authorised, not just whether the page looks genuine.

Explain that MFA remains valuable and implementations differ. Phishing-resistant authentication helps against spoofed sign-in sites; it does not legitimise an unsolicited app permission or transaction. CISA recommends phishing-resistant MFA. [S13]

Positive case: Cloudflare reported that three employees entered credentials during the July 2022 SMS attack, while hardware-key requirements prevented the attempted access. Frame this as layered protection and early reporting, not a story about careless employees. [S14]

### Module 5: Malicious help and fake verification

Teams support impersonation can use an ordinary collaboration platform to ask for remote access. Microsoft documented such activity, including compromised accounts posing as IT personnel. The organisation's real support process matters more than the application's branding. [S15]

ClickFix lures ask the user to perform a supposed repair or human-verification step that runs a command. Microsoft's 2025 research describes this technique. Its February 2026 CrashFix analysis describes a malicious extension impersonating an ad blocker, causing browser problems and leading to a repair pretext. [S16, S17]

Build a static or inert browser mock-up with a fake verification/repair instruction. Stop the scene before execution. Do not provide a runnable command, read or write the clipboard, install an extension or invoke a shell. The lesson is to stop when an unsolicited page directs operating-system actions and contact approved support.

Optional gallery: callback scams, malicious search adverts and fake meeting/download updates. Use one example to practise the same safe action instead of adding a separate lecture for every campaign name. FTC describes fake renewal notices and impersonation chains. [S6]

## Real-world case and visual evidence register

| Case/source | Verified teaching point | Suggested visual | Limits |
|---|---|---|---|
| Hong Kong government, June 2024 account of January incident [S9] | Email plus fabricated video contributed to payment fraud | Reconstructed meeting invitation and payment timeline | Label reconstruction; preserve the prerecorded/no-interaction detail |
| Cloudflare, August 2022 disclosure [S14] | SMS targeted staff; keys stopped access after credential entry | Source's SMS/login screenshots with attribution | Historical case; do not imply all MFA provides the same resistance |
| Microsoft, April 2026 [S12] | Device-code phishing can authorise attacker access | Inert device-code prompt | A genuine login domain alone does not validate the request |
| Microsoft, February 2026 [S17] | Fake extension and browser failure created a repair pretext | Before/after browser storyboard | Do not recreate the malicious extension |
| Joint Scattered Spider advisory, July 2025 [S8] | Helpdesk identity procedures are an attack target | Fictional caller/helpdesk transcript | Campaign/advisory evidence, not proof of attribution for any unrelated breach |
| Microsoft Q1 2026 [S3] | QR and attachment delivery patterns evolve | Synthetic email with inert QR tile | Provider telemetry; not global incidence |
| MyCERT, March 2026 [S4] | Local authority impersonation and false aid offers | Fictional Malaysian scam-message card | Do not attach invented losses or victim names |

Use authentic excerpts/screenshots when needed, with source, date and redaction. Do not call a synthetic mock-up “an actual intercepted email.” Do not put live malicious URLs or functional account-linking QR codes on screen. For third-party image reuse, check permissions and attribution requirements; when uncertain, use an attributed reconstruction.

## HTML presentation specification

Build a local, self-contained HTML deck with embedded CSS/JavaScript and bundled assets. Use the established dark theme and consistent semantic colours. Reuse proven navigation, notes, fullscreen and touch mechanics if the legacy source is available; the prior files have not been inspected for code reuse in this research task.

Target about 50 core screens plus a short optional reference gallery. Plan roughly 4 opening screens, 6 identity screens, 7 pressure/payment screens, 10 phishing-inspection screens, 8 identity-access screens, 5 fake-help screens, 6 tabletop screens and 4 response/closing screens. Screen count is a production estimate; pauses and exercises account for much of the session.

Required interactions:

- Mock inbox with selectable messages, sender details, link previews and a report action.
- Profile comparison with progressive evidence reveal.
- Conversation reveal, including “not enough evidence; verify” as a valid choice.
- Three brief account-access scenes: sign-in, device code and consent.
- Branching decisions that converge back into the main narrative, so delivery stays on schedule.
- Annotated reveal after a participant answers, explaining both the clue and its limitations.
- Tabletop evidence board, optional timer and trainer-controlled conclusion.
- Presenter notes with source, case status, expected answers, timing and debrief.
- References accessible from each factual scene and in an end-of-deck index.

Show one main decision per screen. Avoid long paragraphs and tiny full-desktop screenshots. Enlarge relevant UI areas while preserving enough context. Provide keyboard navigation, visible focus, readable contrast, text labels alongside colours, captions for audio/video, reduced motion and a print stylesheet. Fit common projector viewports without arbitrary scale hacks; allow deliberate scrolling for long notes/reference views.

Keep exercises functional without external polling, fonts or APIs. Large audiences can vote by hands or table discussion. Pair activities work without participant laptops. Any score is local and anonymous unless a separately approved evaluation process needs identifiable records. Never collect passwords, OTPs, tokens or personal account data.

## Final tabletop and assessment

Run the 35-minute tabletop in groups. Give each group an operations, finance, manager and IT role. Reveal four evidence cards in order: supplier message; bank change; support contact; employee admission of an approval. Ask each role to record what they know, what remains unverified, the next safe action and who needs to know. Reveal outcomes based on their process choices.

Suggested rubric, 0–2 points each: identifies the sensitive action; selects an independent verification route; follows the approval process; reports enough detail promptly; avoids further interaction or evidence destruction. This ten-point rubric is a workshop design choice, not a NIST certification score.

Use a short baseline and equivalent post-session scenarios with different surface details. Include at least one legitimate but sensitive request and one case where the correct choice is to verify before classifying. Compare reasoning as well as answers. Ask the learner to demonstrate finding the reporting route.

After 30 days, use a short refresher scenario and, if authorised, a proportionate simulation. Track reporting rate, time to first useful report, unsafe approvals, and completion of role-specific checks. Do not treat open-tracking as proof of reading or a click as proof of compromise: security scanners and client behaviour can affect measurements. Rate email exercise difficulty and context using the NIST Phish Scale before comparing campaigns. [S18]

## Employee response card

Use four remembered actions: Pause, Verify, Report, Recover. Present this as our course mnemonic, not an official standard.

| Situation | Immediate employee action | Security/IT follow-up to explain |
|---|---|---|
| Suspicious message; no interaction | Use the approved report action; preserve the original | Assess and investigate related messages |
| Opened a link | Stop interacting and report what happened | Establish whether further access, download or execution occurred |
| Entered credentials or approved access | Contact security through a trusted channel immediately | Revoke relevant sessions/tokens, review access and reset credentials as appropriate |
| Granted app consent or linked a device | Report the app/device and time | Remove unauthorised grants/devices and investigate activity |
| Ran a command or allowed remote control | Stop the interaction; follow the incident procedure and contact IT using another device if needed | Contain the endpoint and preserve evidence; avoid unplanned wiping/rebooting |
| Transferred money | Notify finance/security and contact the bank's established fraud channel immediately | Attempt recovery, preserve transaction records and coordinate external reports |
| Found a cloned profile | Preserve identifying details and notify security/communications | Platform report/takedown, warning to affected contacts, check for account compromise |

Reporting should state the time, channel, claimed sender, action taken and device involved, with the original message or safe screenshot if available. Do not include passwords or codes. Do not forward suspicious content to a broad colleague list. Do not wait for certainty before reporting.

Put the customer's verified reporting button, mailbox and phone number on the final deck. Use explicit placeholders until confirmed. MyCERT lists Cyber999 as an external Malaysian reporting route; internal escalation remains the first organisational route. Recheck contact details before delivery. [S4, S19]

## Industry alignment

| Reference | Application in this workshop | What it does not establish |
|---|---|---|
| NIST SP 800-50 Rev. 1 [S20] | Behaviour-focused outcomes, role relevance, evaluation and refreshers | That this single course proves organisational compliance |
| NIST CSF 2.0 PR.AT-01 and PR.AT-02 [S21] | General employee awareness plus finance, HR, manager and IT decisions | A certification or prescribed slide sequence |
| NIST TN 2276 Phish Scale [S18] | Interpret simulation results with email difficulty and recipient context | A universal score for voice/deepfake scenarios |
| MITRE ATT&CK T1566 [S10] | Check coverage across attachments, links, services and voice | A teaching method or mandatory awareness syllabus |
| CISA phishing-resistant MFA guidance [S13] | Explain the difference between authentication methods | That MFA prevents every fraudulent approval or transaction |
| FBI BEC and joint Scattered Spider guidance [S7, S8] | Independent verification and stronger recovery/helpdesk checks | Malaysia-specific reporting or legal obligations |

The original “How PROVINTELL can help SIRIM” section should become a short, concrete response and support demonstration. Only include services and response commitments confirmed for this customer. Separate staff reporting duties from SOC investigation, communications, bank contact and takedown ownership.

## Production inputs still needed

The research and draft structure can stand without these details, but the final HTML should confirm the session date and venue, audience departments and size, presentation language, reporting contacts, actual email/chat client, and customer-approved support processes. Anonymised previous simulation results can support a local debrief if available and approved; never invent them.

Before presenting, review source freshness, confirm UI screenshots match the customer environment, test the offline deck on the projector, check keyboard/touch navigation, and rehearse the long lunch/prayer transition. A trainer should be able to skip optional technical scenes without breaking the story.

## Source register

All sources below are primary publications or official guidance. Accessed/researched 30 September 2026. Reusable links are provided instead of republishing full copyrighted reports.

| ID | Document and date | Link and use |
|---|---|---|
| S1 | Verizon, 2026 DBIR findings, May 2026 | [Official findings](https://www.verizon.com/about/news/breach-industry-wide-dbir-finds), risk context |
| S2 | Verizon, 2026 Data Breach Investigations Report | [Report landing page](https://www.verizon.com/business/resources/reports/dbir/), collection period and methodology |
| S3 | Microsoft, Email threat landscape: Q1 2026, 30 April 2026 | [Research](https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/), QR and attachment trends |
| S4 | MyCERT MA-1431.032026, 19 March 2026 | [Advisory](https://mycert.org.my/portal/advisory?id=MA-1431.032026), Malaysian examples and response contacts |
| S5 | FTC, Business Impersonator Scams | [Guidance](https://consumer.ftc.gov/features/pass-it-on/impersonator-scams/business-impersonator-scams), cross-channel impersonation |
| S6 | FTC, Impersonation scams: not what they used to be, April 2024 | [Analysis](https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/04/impersonation-scams-not-what-they-used-be), combined impersonation and callback pretexts; [social-media guidance](https://consumer.ftc.gov/consumer-alerts/2020/10/scams-start-social-media) |
| S7 | FBI IC3, Business Email Compromise | [Guidance](https://www.ic3.gov/CrimeInfo/BEC), verification and incident response; [known-number verification guidance](https://www.ic3.gov/PSA/2017/PSA170504) |
| S8 | Joint Scattered Spider advisory, updated 29 July 2025 | [Government HTML](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/scattered-spider) and [FBI/IC3 PDF](https://www.ic3.gov/CSA/2025/250729.pdf), helpdesk and MFA attacks |
| S9 | Hong Kong Government, LCQ9: Combating frauds involving deepfake, 26 June 2024 | [Official account](https://www.info.gov.hk/gia/general/202406/26/P2024062600192p.htm), dated incident facts |
| S10 | MITRE ATT&CK, Phishing T1566 | [Technique reference](https://attack.mitre.org/techniques/T1566/), coverage taxonomy |
| S11 | Microsoft, Defending against evolving identity attack techniques, 29 May 2025 | [Research](https://www.microsoft.com/en-us/security/blog/2025/05/29/defending-against-evolving-identity-attack-techniques/), consent/device and targeted lure examples |
| S12 | Microsoft, Inside an AI-enabled device code phishing campaign, 6 April 2026 | [Research](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/), current account-access deception |
| S13 | CISA, Implementing Phishing-Resistant MFA | [Official PDF](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf), authentication protection |
| S14 | Cloudflare, The mechanics of a sophisticated phishing scam and how we stopped it, 9 August 2022 | [First-party incident disclosure](https://blog.cloudflare.com/2022-07-sms-phishing-attacks/), prevention case and screenshots |
| S15 | Microsoft, Disrupting threats targeting Microsoft Teams, 7 October 2025 | [Research](https://www.microsoft.com/en-us/security/blog/2025/10/07/disrupting-threats-targeting-microsoft-teams/), collaboration-channel impersonation |
| S16 | Microsoft, Think before you Click(Fix), 21 August 2025 | [Research](https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/), fake verification/repair |
| S17 | Microsoft, New ClickFix variant CrashFix, 5 February 2026 | [Research](https://www.microsoft.com/en-us/security/blog/2026/02/05/clickfix-variant-crashfix-deploying-python-rat-trojan/), fake-extension case |
| S18 | NIST TN 2276, November 2023 | [Publication](https://csrc.nist.gov/pubs/tn/2276/final) and [PDF](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2276.pdf), email exercise difficulty |
| S19 | MyCERT, Reporting Channel | [Official route](https://www.mycert.org.my/portal/full?id=9eb77829-7dd4-4180-814f-de3a539b7a01), reporting reference; current contacts verified via S4 because direct page retrieval failed |
| S20 | NIST SP 800-50 Rev. 1, September 2024 | [Publication and download](https://csrc.nist.gov/pubs/sp/800/50/r1/final), learning programme design |
| S21 | NIST CSF 2.0, 26 February 2024 | [Official PDF](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), awareness outcomes |

Additional local leads for the next content review: MyCERT MA-1439.052026, “Boss Impersonation” Scam Email (12 May 2026), and MA-1464.062026, Malware Campaign Delivering Malicious VBScript via WhatsApp Desktop. Official search/index entries identify these advisories, but full retrieval failed during this review. Do not derive detailed attack steps, counts or screenshots from these titles alone. Reopen the advisories before making them core case studies.
