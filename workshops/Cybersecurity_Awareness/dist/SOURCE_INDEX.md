# Source index

Primary sources cited in the workshop. Publication date is shown separately from event dates. Full reports are not republished; links go to the publishers. Generated from `02-research/sources.json`.

**Recheck:** 2 October 2026, 06:23–06:35 UTC, by retrieving each primary URL and comparing it with the specific claim used. Evidence: `validation/source_recheck_2026-10-02.json`. Status legend: supported; partially supported (wording adjusted); claim not found (not used on slides); retrieval failed (earlier review relied on).

## Payment, impersonation and voice

### S7: FBI IC3 Business Email Compromise
- Published: undated live guidance (no date invented)
- Link: <https://www.ic3.gov/CrimeInfo/BEC>
- Use and limits: Verify payment changes through a separate channel; contact the financial institution promptly after fraud. 'Use existing records' is the course's practical form of the separate-channel advice.
- Recheck 2 Oct 2026: partially supported. Page says 'secondary channels', not 'known contact / not the contact info in the request'. The financial-institution advice is supported. Suggest wording: 'verify through a separate channel'.
- Cited on: SL03, SL04B, SL05, SL06, SL20, SL21, SL24, SL25, SL26, SL36, SL38, SL64, SL71

### S5: FTC Business Impersonator Scams
- Published: undated live guidance (no date invented)
- Link: <https://consumer.ftc.gov/features/pass-it-on/impersonator-scams/business-impersonator-scams>
- Use and limits: Cross-channel impersonation and independent contact.
- Recheck 2 Oct 2026: supported. No date on page. Also mentions payment via gift cards, crypto, wire transfer.
- Cited on: SL09, SL09B, SL11, SL13, SL15, SL15B, SL16, SL25, SL33, SL33B

### S6: FTC impersonation scams analysis
- Published: April 2024
- Link: <https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/04/impersonation-scams-not-what-they-used-be>
- Use and limits: Combined impersonation and renewal/callback pretexts.
- Recheck 2 Oct 2026: supported. Combined business+government impersonation was nearly half of all fraud reported to the FTC in 2023. Phony subscription renewal was the 2nd most common scam type; callers then seek remote access for a 'refund'.
- Cited on: SL13, SL56

### S9: Hong Kong Government LCQ9
- Published: 26 June 2024
- Link: <https://www.info.gov.hk/gia/general/202406/26/P2024062600192p.htm>
- Use and limits: January 2024 incident: approximately HK$200m, five local bank accounts, prerecorded meeting with no interaction.
- Recheck 2 Oct 2026: supported. Phishing email impersonated the CFO of the UK head office. Video built from public clips and voices. Later payment instructions came by instant messaging. All details match.
- Cited on: SL07, SL24

### S8: Joint Scattered Spider advisory
- Published: 29 July 2025 update
- Link: <https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/scattered-spider>
- Use and limits: Helpdesk impersonation, voice phishing and MFA pressure. Recheck 2 Oct 2026 could not retrieve the page (timeouts/connection resets); statements rest on the 30 Sep 2026 research review.
- Recheck 2 Oct 2026: not checked retrieval failed. Not verified. The 29 July 2025 update date and the helpdesk/MFA-fatigue content are unconfirmed.
- Cited on: SL12, SL12B, SL20, SL23, SL23B, SL44, SL53, SL65

## Email, files, QR and phishing taxonomy

### S10: MITRE ATT&CK T1566
- Published: undated live guidance (no date invented)
- Link: <https://attack.mitre.org/techniques/T1566/>
- Use and limits: Taxonomy: attachments, links, services and voice. Not an awareness certification.
- Recheck 2 Oct 2026: supported
- Cited on: SL09, SL09B, SL29, SL30, SL31

### S3: Microsoft Email threat landscape Q1 2026
- Published: 30 April 2026
- Link: <https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/>
- Use and limits: QR and attachment delivery patterns. Provider telemetry, not global prevalence.
- Recheck 2 Oct 2026: supported. Also: QR codes embedded in email body +336% in March (5% of volume); CAPTCHA-gated phishing +125% to 11.9M in March.
- Cited on: SL33, SL33B, SL34, SL35

## Sign-in, sessions, codes, consent and MFA

### S11: Microsoft evolving identity attacks
- Published: 29 May 2025
- Link: <https://www.microsoft.com/en-us/security/blog/2025/05/29/defending-against-evolving-identity-attack-techniques/>
- Use and limits: Consent phishing, device-code phishing, device registration/join abuse and AiTM. Recheck did not find 'account linking' wording; SL39 presents linking as course explanation.
- Recheck 2 Oct 2026: partially supported. Consent phishing, device code phishing, device join/registration and AiTM are confirmed. 'Account linking' was not found.
- Cited on: SL10, SL12, SL12B, SL14, SL29, SL32, SL35, SL37, SL42, SL43, SL46, SL47, SL47B, SL49, SL62

### S12: Microsoft AI-enabled device-code campaign
- Published: 6 April 2026
- Link: <https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/>
- Use and limits: A real sign-in service can authorise an attacker-originated session.
- Recheck 2 Oct 2026: supported. Title 'Inside an AI-enabled device code phishing campaign'. Codes are generated dynamically to stay inside the 15-minute validity window.
- Cited on: SL37, SL42, SL45, SL45B, SL49, SL63, SL71

### S13: CISA phishing-resistant MFA fact sheet
- Published: October 2022
- Link: <https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf>
- Use and limits: Phishing-resistant authentication; do not generalise to all approvals/consent.
- Recheck 2 Oct 2026: supported. Document is dated October 2022, although the URL path says 2023-01. It calls FIDO/WebAuthn 'the only widely available phishing-resistant authentication'. If you can't use it yet, consider number matching.
- Cited on: SL43, SL44, SL48

### S14: Cloudflare phishing incident disclosure
- Published: 9 August 2022
- Link: <https://blog.cloudflare.com/2022-07-sms-phishing-attacks/>
- Use and limits: July 2022 SMS campaign; three credential submissions, hardware keys prevented attempted access.
- Recheck 2 Oct 2026: supported. The attack began on 20 July 2022 at 22:49 UTC.
- Cited on: SL48

## Fake support, verification and repair

### S15: Microsoft threats targeting Teams
- Published: 7 October 2025
- Link: <https://www.microsoft.com/en-us/security/blog/2025/10/07/disrupting-threats-targeting-microsoft-teams/>
- Use and limits: Collaboration-platform IT impersonation and remote access abuse.
- Recheck 2 Oct 2026: supported. Usually follows email bombing. Teams voice/video calls impersonate IT.
- Cited on: SL52, SL53, SL65

### S16: Microsoft ClickFix analysis
- Published: 21 August 2025
- Link: <https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/>
- Use and limits: Fake verification and repair prompts that induce command execution.
- Recheck 2 Oct 2026: supported. Lures include fake CAPTCHA/human verification. The command is silently copied to the clipboard.
- Cited on: SL54, SL54B

### S17: Microsoft CrashFix
- Published: 5 February 2026
- Link: <https://www.microsoft.com/en-us/security/blog/2026/02/05/clickfix-variant-crashfix-deploying-python-rat-trojan/>
- Use and limits: Fake extension/browser problem/repair pretext. Inert reconstruction only.
- Recheck 2 Oct 2026: supported. Delivered via malicious ads leading to a fake Chrome Web Store listing. Payload is ModeloRAT (Python).
- Cited on: SL55

## Learning programme and frameworks

### S20: NIST SP 800-50 Rev. 1
- Published: September 2024
- Link: <https://csrc.nist.gov/pubs/sp/800/50/r1/final>
- Use and limits: Behaviour change, role relevance, evaluation and lifecycle learning.
- Recheck 2 Oct 2026: supported
- Cited on: SL16, SL22, SL36, SL38, SL57, SL66, SL66B, SL69, SL70, SL70B, SL72, SL73, SL74, SL76

### S21: NIST CSF 2.0
- Published: 26 February 2024
- Link: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>
- Use and limits: PR.AT-01 general awareness and PR.AT-02 role-specific training.
- Recheck 2 Oct 2026: supported
- Cited on: SL76

### S18: NIST TN 2276 Phish Scale
- Published: November 2023
- Link: <https://csrc.nist.gov/pubs/tn/2276/final>
- Use and limits: Rate email exercise difficulty and recipient context. Not a validated scale for voice/video.
- Recheck 2 Oct 2026: supported. The landing-page abstract doesn't mention cues or premise alignment. These are confirmed in the linked primary PDF (nvlpubs NIST.TN.2276.pdf), sections 2.1 'Number of Cues' and 2.2 'Premise Alignment'.
- Cited on: SL76

## Risk context (trainer reference)

### S1: Verizon 2026 DBIR findings
- Published: May 2026
- Link: <https://www.verizon.com/about/news/breach-industry-wide-dbir-finds>
- Use and limits: Vulnerability exploitation leads as initial access vector at 31% of breaches analysed (2025 data). Trainer context only. Do not equate spear phishing with all human involvement.
- Recheck 2 Oct 2026: supported. Press release says report 'uses 2025 data'. Phrase as 'breaches analysed', not all breaches.
- Cited on: no slide (reference index and facilitator notes only)

### S2: Verizon 2026 DBIR
- Published: 2026
- Link: <https://www.verizon.com/business/resources/reports/dbir/>
- Use and limits: Dataset window 1 November 2024–31 October 2025.
- Recheck 2 Oct 2026: supported. Also restates 31% of breaches start with software vulnerabilities; 48% involve ransomware.
- Cited on: no slide (reference index and facilitator notes only)

## Malaysian context and external reporting

### S4: MyCERT MA-1431.032026
- Published: 19 March 2026
- Link: <https://mycert.org.my/portal/advisory?id=MA-1431.032026>
- Use and limits: Recheck 2 Oct 2026: this advisory ID is 'Hari Raya Holiday Cyber Security Best Practices'; it does not support scam-call or false-assistance claims. Not cited on any slide; listed only for reference. Find the correct MyCERT advisory before using local impersonation examples.
- Recheck 2 Oct 2026: not found on page. ID and date match, but the page does not address scam calls, impersonation or fake government assistance offers. Says Cyber999 received 1,434 incidents Jan-Feb 2026 and 7,616 in 2025; fraud is the most reported type. Wrong citation for this claim.
- Cited on: no slide (reference index and facilitator notes only)

### S19: MyCERT reporting channel
- Published: undated live guidance (no date invented)
- Link: <https://www.mycert.org.my/portal/full?id=9eb77829-7dd4-4180-814f-de3a539b7a01>
- Use and limits: External Malaysian reporting. Internal customer procedure must be supplied.
- Recheck 2 Oct 2026: supported. Page title 'MyCERT : Reporting Channel'. Email: cyber999[at]cybersecurity.my. Phone: 1-300-88-2999 (office hours); emergency +6019-266 5850 (24x7). Calls monitored 8:30am-5:30pm on business days.
- Cited on: no slide (reference index and facilitator notes only)

## Case facts used on slides

- **Hong Kong, January 2024 (S9, published 26 June 2024):** about HK$200 million; email impersonating the CFO; fabricated prerecorded video conference with no interaction; transfers to five local bank accounts; later instructions by instant messaging. Rechecked and supported.
- **Cloudflare, July 2022 (S14, published 9 August 2022):** SMS phishing; three employees entered credentials; FIDO2 hardware keys prevented the attempted logins. Rechecked and supported.
- **Device-code phishing (S12, 6 April 2026):** the legitimate sign-in flow can authorise an attacker-initiated session without exposing credentials. Rechecked and supported.
- **CrashFix (S17, 5 February 2026):** a malicious extension posing as an ad blocker crashes the browser, then shows a fake repair prompt. Rechecked and supported; the slide is a concept reconstruction.

