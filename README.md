Training & Workshop Library
A collection of practical training and workshop materials, organised for reuse, delivery, and continued improvement.
The initial categories cover cybersecurity awareness, phishing, Wazuh, incident response, and SOC operations. Additional topics can follow the same structure.
Browse the workshops
Use the [workshop catalogue](CATALOG.md) to check material availability, versions, and review dates. Open a workshop below to find its overview and resources.
Starter status: The entries below provide an organisational structure. Their folders contain instructions and placeholders; they do not yet contain the existing training materials. Suggested audiences can change when each workshop is populated.
Workshop	Suggested audience
[Cybersecurity Awareness](workshops/cybersecurity-awareness/README.md)	Staff across departments
[Phishing Awareness](workshops/phishing-awareness/README.md)	Staff across departments
[Wazuh Architecture & Deployment](workshops/wazuh-architecture-deployment/README.md)	IT administrators and security practitioners
[Wazuh Security Operations](workshops/wazuh-security-operations/README.md)	SOC analysts and security practitioners
[Incident Response](workshops/incident-response/README.md)	Response teams and relevant business stakeholders
[SOC Operations](workshops/soc-operations/README.md)	SOC analysts and team leads


Find the right material
Each workshop has its own README and the following resource folders:
Location	Contents
slides/	HTML presentations, PowerPoint files, and PDF slide exports
trainer-notes/	Delivery instructions, timing, demonstrations, and answer guides
handouts/	Participant guides, checklists, and reference sheets
exercises/	Scenarios, worksheets, lab instructions, and sample data
research/	References, source notes, and evidence supporting the material
assets/	Images and other files used by that workshop


The workshop README should identify the current slide deck, participant handout, and trainer guide once those files exist.
Use a workshop
1. Open the workshop README. Check its audience, duration, prerequisites, and learning outcomes.
2. Check the material status and last review date. Use Ready materials for delivery; review drafts before using them.
3. Open the linked slides or download the workshop files. For an HTML presentation, keep the assets and other supporting files together, then open its entry HTML file in a browser. Follow any workshop-specific instructions.
4. Read the trainer notes before delivering the session. Adjust examples, reporting channels, and exercises for your audience.
To download the repository, use Code → Download ZIP on GitHub and extract the archive. Access to private materials requires repository access.
GitHub's repository file view does not run an uploaded HTML presentation. Use the downloaded files or a separately published presentation link.
Add or update materials
Copy the [workshop template](templates/workshop/README.md) for a new topic, then follow the [maintenance guide](docs/MAINTAINING.md).
Use lowercase folder names with hyphens, such as phishing-awareness. Keep the same folder for revisions to a workshop. Give each version a short change note instead of creating folders named final, final-new, or final-v2.
A workshop can use a lecture, demonstration, lab, discussion, case study, or a combination. Choose the approach that suits the learning objectives and audience.
Material status
Status	Meaning
Starter	An entry exists, but workshop materials have not been added
Draft	Material development is in progress
Review	Materials are available and need a content or delivery review
Ready	The maintainer has checked the materials for the stated audience and environment
Archived	Retained for reference; not the current delivery version


Record a version and review date when a workshop reaches Ready. A readiness label does not guarantee that a product feature or security example remains current; check the sources before delivery.
Sources and attribution
Keep source links, publication dates, and checked dates in the workshop's research/ folder. Prefer official documentation and original reports for technical claims. Distinguish fictional training scenarios from documented incidents.
Follow the [source and publication guide](docs/SOURCES_AND_SHARING.md) when adding references, screenshots, or third-party assets.
Feedback and improvements
Use GitHub Issues, if enabled, to report a correction or suggest an improvement. Include the workshop name, filename or slide number, the issue, and a supporting source where relevant. Contributors should describe their changes and review the affected materials before requesting a merge.
Sharing and reuse
Check the repository visibility and any material-specific permissions before sharing a link. Keep credentials, participant records, and client-specific reports outside this collection.
The repository does not currently include a general reuse licence. Check with the maintainer before redistributing or adapting original materials. Third-party content retains its own terms and attribution requirements.
Library maintenance
- [Workshop catalogue](CATALOG.md)
- [How to add and update a workshop](docs/MAINTAINING.md)
- [Sources, attribution, and sharing](docs/SOURCES_AND_SHARING.md)
- [Change history](CHANGELOG.md)
- [Reusable workshop template](templates/workshop/README.md)
