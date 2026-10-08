# Add and Update a Workshop

[Return to the library](../README.md)

## Add an existing workshop

1. Find the matching folder under `workshops/`. If none fits, copy `templates/workshop/` to a new folder such as `workshops/cloud-security-fundamentals/`.
2. Put presentation files in `slides/`, participant resources in `handouts/`, trainer resources in `trainer-notes/`, exercises in `exercises/`, supporting references in `research/`, and images or other supporting files in `assets/`.
3. Preserve the existing asset paths in an HTML deck. If the deck expects `slides/assets/`, keep those assets there or update and verify the paths. The standard `assets/` folder is a convention, not a reason to break an existing deck.
4. Update the workshop README: title, audience, duration, outcomes, prerequisites, software versions, material links, status, and review date.
5. Add or update its row in `CATALOG.md` and its link in the root `README.md`.
6. Open the slides, confirm the links, review the content, and save a commit with a clear description.

A suggested commit message is `Add phishing awareness slides and participant handout`.

## Minimum information for a usable entry

| Field | What to record |
| --- | --- |
| Title and summary | What the session covers |
| Audience and level | Who it serves and what they need to know |
| Duration and delivery | Total time including breaks; online, in person, or both |
| Learning outcomes | Actions participants should perform after the session |
| Prerequisites | Accounts, software, equipment, and preparation |
| Materials | Working links to the current files |
| Readiness | Status, version, and date of the most recent content review |

Only list a file as available after you upload it. Keep trainer answer guides separate from participant handouts, but remember that folders do not create separate access permissions.

## Use the workshop template

Copy the complete template folder. Replace the bracketed fields in its README and notes. Remove sections and files that do not fit the workshop. You do not need to fill unused folders with content.

The template includes an agenda, trainer guide, participant handout, exercise guide, and reference log. It does not require a story-based format.

## Choose stable filenames

Examples:

- `slides/index.html`
- `slides/phishing-awareness.pptx`
- `slides/phishing-awareness.pdf`
- `handouts/participant-handout.pdf`
- `trainer-notes/facilitator-guide.md`
- `research/references.md`

Keep the current files at stable paths so links continue to work. Record versions in the workshop README and change history. Git tracks the revisions to committed files, so you do not need a new topic folder for each update.

## Review before marking Ready

- Open the deck and check images, text, footer sources, and slide navigation.
- Verify links in the workshop README and catalogue.
- Check that the agenda fits the stated time, including activities and breaks.
- Verify technical instructions against the software version and environment used in the workshop.
- Check security claims and incident examples against the cited sources.
- Review the files for participant data, client details, credentials, and restricted assets.
- Record the actual review date. Leave the entry in Review if work remains.

## Update a workshop

Replace or edit the affected file, check its presentation and links, then update the version and change note. Update the review date only when you reviewed the content. A font change alone does not refresh the technical research.

Use messages such as `Correct reporting steps in phishing workshop` or `Update Wazuh deployment lab for tested version`. A commit is a saved change with a description.

For a personal collection, direct commits to the working branch can keep maintenance simple. When coauthors review changes, use a new branch and a pull request. A pull request lets someone review proposed changes before you merge them.

## Preserve a delivered edition

After you deliver a workshop, record its version and delivery date in the workshop's change notes. If you need a downloadable snapshot, create a GitHub release with a tag such as `phishing-awareness-v1.0.0` and attach the participant package.

The tag identifies a snapshot of the whole repository, even if its name refers to one workshop. Keep other workshop versions in their own README files. Avoid putting participant attendance or client feedback records in the release.

## Archive a workshop

Set its status to Archived in the README and catalogue. Explain why you stopped using it and link to the replacement if one exists. Keep its location stable unless a move serves a clear purpose; update links after moving files.

## Empty folders and browser edits

Git records files, so an empty folder needs a file to appear in the repository. The starter uses small README files in resource folders for this purpose.

To create a nested file in GitHub's browser editor, enter a path such as `workshops/cloud-security-fundamentals/README.md` under **Add file → Create new file**. Type the content and commit the change.

For frequent uploads or larger folder collections, GitHub Desktop can simplify local editing and synchronisation. Review the changed-file list before committing and pushing.
