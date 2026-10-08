# Claims and case boundaries

Use sourced paraphrases with source/date on the relevant screen and in notes. Keep quoted excerpts short. The case summaries below are intentionally concise; they do not license inventing missing details.

| Case | Facts allowed | What to avoid |
|---|---|---|
| Hong Kong, January 2024, S9 | About HK$200m, CFO impersonation email, fabricated prerecorded meeting, no interaction, five local bank accounts, later messaging | Live interactive AI claim; invented victim dialogue; an unsupported company identity |
| Cloudflare July 2022, S14 | Three credential submissions; hardware keys prevented attempted access | Claim all MFA has equivalent resistance or staff blame |
| Device-code campaign April 2026, S12 | Legitimate authentication flow can grant an attacker-originated session | Claim the real service itself is a fake website |
| CrashFix February 2026, S17 | Fake extension and browser-problem/repair pretext | Invented financial loss or runnable extension/commands |
| Scattered Spider July 2025 advisory, S8 | Helpdesk/voice/MFA manipulation documented in joint guidance | Attribute an unrelated breach based on similarity alone |
| MyCERT March 2026, S4 | Malaysian impersonation and false-assistance context | Government-only course, population-wide incident totals |

## Risk statistics
Do not put broad statistics on the core slides just to sound authoritative. Optional opening notes may mention S1/S2's 31% vulnerability-exploitation figure with report scope/window, and S3 QR telemetry with provider attribution. Do not say 'most attacks are spear phishing', 'MFA makes you safe', 'training prevents all phishing', or 'one-day attendance proves compliance'.

## Technical explanations
HTTPS protects a connection to a destination, not the business intent. A genuine account can be compromised. A permission or device-code screen can be genuine while the surrounding request is deceptive. Phishing-resistant MFA helps against spoofed sign-in origins; transaction authorisation and app-consent controls still matter. MFA denial/reporting is useful; do not advise disabling MFA.

## Verification before delivery
Reopen core sources, confirm the specific statement is supported, record date/status in sources.json and retain incident date separately. If a source is unavailable, preserve the clearly attributed previously reviewed statement, identify the limitation, and avoid expanding it from secondary speculation. Do not label references fully reverified when only selected links were checked.
