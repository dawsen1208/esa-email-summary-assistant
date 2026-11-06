# ESA Email Summary Assistant

Prose word count: 571 (whitespace count excluding headings, this line, list markers and setup commands).

A local prototype for checking simulated AI summaries of university emails. [A2 report PDF](output/pdf/ESA_A2_Report.pdf) · [Editable report](A2-report.md) · [Development record](development-feedback.md) · [Bilingual screenshot checklist](screenshot-checklist.md).

## Status and scope

Implemented: original-email view, task cards, source highlights, confirmation, editing with save/cancel, direct manual task addition, progress, full-email review acknowledgement and reset. Changes last until reload/reset. Completing review records the user's acknowledgement; it does not certify completeness.

Simulated: AI extraction, initial task content and task-to-source mappings are prepared data. No model, mailbox, backend or analytics is connected. Automatic omission detection is outside scope. Live extraction, arbitrary email input, automated evidence selection, persistent storage and comparative evaluation remain undeveloped. No accuracy or speed improvement is claimed.

## Run and inspect

Open `index.html` in a current browser. No installation, internet, account or API key is required. HTML holds the fictional email; JavaScript manages state and interactions; three CSS files provide base styles and the correspondence theme. Dates retain the written email time without timezone conversion.

Walkthrough: inspect the proposal evidence and correct 6 November to 9 November 2026 at 12:00; verify and confirm the consent-form deadline of 11 November at 17:00; read the full email and add the omitted ethics checklist manually. Add new task opens the form directly. Finish full-email review displays acknowledgement and closes guidance; Review full email reopens it.

## Development record

- Initial assisted build: translated the A1 verification idea into source and task panels with fixed evidence links, making the interaction demonstrable without live inference.
- Student design decisions: adopted the ESA name and correspondence style, then reduced the introduction to prioritise the working area.
- Student self-review found limited freedom, unclear flow and thin content. Direct task addition replaced an indirect route; duplicate controls were removed and review completion now closes guidance. Broader usability concerns remain unevaluated.
- Scope decision: rejected specific omission-answer hints. Manual review and addition remain available without implying automated detection.
- Evidence checks: the student supplied ten screenshots. Inconsistent checklist states were identified and replaced; the final two panels retain Edited by you. Eight report pages were rendered and visually inspected.

Detailed decisions and checks are in [development-feedback.md](development-feedback.md). Earlier changes are documented there; the initial Git import did not reconstruct a fictional commit history.

## AI assistance and contribution

Codex generated the initial code and assisted revisions, checks, report text, diagram and PDF layout. The student supplied the project idea, scope decisions, self-review and screenshots. No external code template or live model was reused.

Examples of reviewing assistance: the student rejected omission feedback, requested direct task addition, removed duplicate controls and reduced the introduction. Screenshot review prompted replacement captures; report labels were adapted to actual states rather than changing images. The student remains responsible for the submitted claims and references.

## Checks and optional report rebuild

`node tools/check-direct-add.cjs` checks selected state transitions using a simplified DOM. It is not a browser or usability test. Screenshots document the demonstrated desktop interactions; a full accessibility and responsive audit remains outstanding.

To rebuild the report, install `report-requirements.txt` and run `python tools/build_a2_report.py`. Python is not needed to run ESA. PDF focus views leave the original PNGs unchanged.

## Submission files

Submitted prototype and screenshot snapshot: [3a4497c](https://github.com/dawsen1208/esa-email-summary-assistant/commit/3a4497c). Later commits package the report and documentation. The PDF includes repository links, rationale, architecture, three illustrated examples and references. Publication records were checked against ACL Anthology and Microsoft Research; undated course slides are attributed to the University of Birmingham.

Original screenshots are in `assets/storyboards/`. The earlier report draft is retained as historical working material; use `A2-report.md` and the PDF. Course PDFs, extracted lecture text and local authoring notes are excluded. No additional ZIP or video is required.
