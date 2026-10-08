# Template catalog

| Layout key in slides.json | Prototype basis | Extension rule |
|---|---|---|
| cover | .cover/.scene | Preserve opening hierarchy |
| email | .mail/.grid | Inert attachment and scoped inspection |
| chat | .chat/.bubble | Progressive entries and replay |
| decision | .choices/.feedback | Explicit options/feedback; neutral initial state |
| annotated | .mail/.findings | Reveal context only after discussion |
| case | .casegrid/.timeline | Source/date and reconstruction label |
| comparison | .grid plus existing text/surface styles | Two readable evidence views |
| profile | .sender/.avatar styles in larger evidence view | Fictional profiles; no red answer cues |
| browser | .mailbar/.mailbody evidence language | Static access/consent/repair panel |
| mobile | .chat/evidence colours | Enlarged phone content; avoid tiny full-device screenshot |
| qr | browser/evidence layout | Nonfunctional demo tile with text destination reveal |
| response | .finding/.callout | Short actions with ownership |
| roleplay | decision/context hierarchy | Clear task, roles and trainer instructions |
| voice | chat/text hierarchy | Captioned script; no audio dependency |
| exercise | context plus evidence cards | Table task and trainer reveal |
| evidence_board | evidence panels | One new card at a time; retain known facts |
| report_demo | response/evidence styles | Verified route or explicit generic demo, no submit |
| reflection | heading plus concise question | Discussion without form collection |
| references | source/modal styles | Grouped source index with explicit links |
| intermission | cover hierarchy, simplified | Break interval and return time; no autoplay |

These are reusable teaching layouts, not a new UI framework. Keep source data editable. All choices and evidence panels use the same focus/state styles. Only add a new layout when a concrete content requirement cannot fit these patterns, document it and compare its rendering to the baseline.
