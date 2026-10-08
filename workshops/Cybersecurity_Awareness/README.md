# Cybersecurity Awareness: Claude execution package

Version 1.0, 2 October 2026 MYT. This package contains a complete build specification, authored slide plan and six-slide executable reference. It does not contain a finished 61-screen presentation. Claude is to build that presentation using this package.

## Start
1. Extract this folder into Claude's working directory.
2. Give Claude the text in `00-start/CLAUDE_START_PROMPT.md`.
3. Ask Claude to read this folder and execute the full build. It should continue through all modules without routine module-approval pauses.
4. Open `06-prototype/prototype.html` to review the visual foundation.
5. Supply customer reporting details and date/venue when available. Missing details do not block the generic build; they must stay visibly unconfirmed.

## Read order
`00-start/CLAUDE_START_PROMPT.md`; `01-course/PROJECT_BRIEF.md`; `01-course/DECISIONS_AND_REQUIREMENTS.md`; `03-story/STORY_FLOW.md`; `04-content/MASTER_STORYBOARD.md`; `04-content/slides.json`; `05-design/DESIGN_SPEC.md`; the prototype and screenshots; `07-implementation/BUILD_PLAN.md`; `10-validation/ACCEPTANCE_CRITERIA.md`.

## Authority
The user's latest instructions prevail. The current project brief and start prompt supersede older handover instructions to stop after one module. The research snapshot is background, not implementation authority. The prototype is the supplied visual baseline; no aesthetic approval beyond choosing this direction has been recorded. Continue with it and report material changes without inventing approval.

## Folder guide
- `00-start`: prompt and practical handover steps.
- `01-course`: scope, decisions, agenda and requirement map.
- `02-research`: primary-source index, claims and verification limits.
- `03-story`: characters, scene connections, knowledge boundaries and example bank.
- `04-content`: 61-screen plan, machine-readable content and scripts for every module.
- `05-design`: design, tokens, layouts and asset rules.
- `06-prototype`: working reference plus screenshots and its prior QA record.
- `07-implementation`: architecture and build sequence.
- `08-facilitator`: runbook, exercises, tabletop, assessment and response guidance.
- `09-participant`: printable quick reference draft and 30-day refresher.
- `10-validation`: checks, coverage and continuity record.
- `11-customer`: configuration example and handover checklist.
- `12-delivery`: what Claude should produce; no final build placed here yet.

The core course is reusable across sectors. A first government-sector audience does not make this government-specific. All Meranti messages/people are fictional. Only labelled documented cases describe actual incidents. Source publications stay online; the package contains attributed summaries and links, not republished full reports.

Prototype note timings came from the earlier roughly 17-minute demonstration. The final opening uses the canonical 20-minute M0 allocation in slides.json; replace the prototype note headings when generating the full deck.
