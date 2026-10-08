# Interaction states and answer visibility

The content JSON supplies decisions and evidence, while this contract defines how to show them.

| Component | Initial state | User/trainer action | Revealed state | Reset |
|---|---|---|---|---|
| Email | Message visible; inspection closed | Sender/destination controls | Readable details with no navigation | Toggle closed |
| Chat | First entry visible | Reveal next | One additional entry, no autoplay | Replay from entry one |
| Decision | All choices neutral; no answer | Select one after discussion | Selected state plus explanation | Clear selection per slide |
| Annotation | Original evidence neutral | Reveal | Marked evidence and newly disclosed facts | Hide findings |
| Profile comparison | Both profiles neutral | Inspect detail | More context; independent verification still needed | Hide details |
| Browser/code/consent | Inert screenshot-like panel | Inspect/choose | Meaning of access and safe route | Restore initial view |
| QR | Labelled inert demo tile | Reveal destination | Text-only destination or linking explanation | Hide |
| Evidence board | First card only | Trainer unlocks next | Next card plus discussion prompt | Restart exercise |
| Reporting | Verified route or visibly labelled demo | Step through | Facts required for a report | No submit action |
| Sources | Short source label | Open reference index | Scrollable source list | Close with Escape |

Incorrect choices get a respectful explanation, not a shame animation. Correct choices explain why the route is independent and what authorisation remains. A reveal can add new evidence that learners could not know earlier. Store state by slide ID so one interaction never modifies another slide. Per-slide reset should preserve the active slide and restore only that slide’s state.

Pure discussion decisions may use trainer reveal instead of on-screen options. Objective choices in slides.json have explicit answer feedback; do not silently change the preferred option. Participant identity and votes need no backend.
