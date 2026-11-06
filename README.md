# ESA Email Summary Assistant

Prose word count: 837 (whitespace count excluding headings, this line, and list markers).

A local interactive prototype for checking simulated AI summaries of university emails. The project continues the A1 investigation into source links, student verification, and the separate problem of omitted requirements.

## Status

Implemented: original-email view, task cards, linked source highlights, user confirmation, editing with save/cancel, manual task addition, review progress, full-email review acknowledgement, and demo reset. Changes last only until reload or reset.

Simulated: AI extraction, initial summary content, and mappings between claims and source passages. All are manually prepared data. Confirmation records the user's judgement; it does not verify factual accuracy automatically.

Not implemented: real model integration, arbitrary email input, automatic evidence selection, persistent storage, and comparative user evaluation. Automatic omission detection is outside the current submission scope. No effectiveness study has been conducted.

## Run or inspect

Open `index.html` in a current browser. No installation, build, account, API key, or internet connection is required. Alternatively, open this folder in VS Code and preview it using a local static server.

Files: `index.html` contains the interface and fictional email; `style.css` provides base styles, `desk.css` provides the ESA visual theme, and `correspondence.css` adds letter-inspired details; `script.js` contains demo data and interaction logic.

## Demonstration walkthrough

1. Select Find in email on the proposal card. The suggested deadline is 6 November, while the source states 9 November 2026 at 12:00. Edit the deadline and save. The card shows that you edited it.
2. Open the consent-form evidence. Compare the action and 11 November 2026 at 17:00 deadline, then confirm it.
3. Find the omitted ethics checklist requirement in the email. Select Add new task in Anything missing? to open the form directly, enter the requirement and proposal deadline, and save. Use Review full email and Finish full-email review to record the separate acknowledgement.
4. Cancel an edit, reload the page, and reset the demo to inspect the boundaries of temporary state.

## Technology

HTML provides semantic structure, CSS provides responsive layout, and vanilla JavaScript manages temporary state and DOM updates. No external libraries, model, backend, analytics, or email service are connected. Dates use the time written in the email without timezone conversion.

## Development record

Initial AI-assisted build: converted the A1 verification concept into a two-panel source-and-summary interface. Evidence links target fixed passages so the interaction can be demonstrated without model integration.

Added editable tasks and manual omission review because verifying existing claims cannot establish completeness. Added separate progress states to avoid equating checked cards with a complete summary.

Added visible simulation disclosure, temporary-state disclosure, reset, empty-title validation, and keyboard focus styles. Browser verification remains pending; no independent user-test outcomes are claimed.

Visual revision: renamed the project ESA at the student's request; A1 used a descriptive paper title rather than a product name. Introduced a checking-desk style with blue task controls, a paper-like email, and yellow source highlights. Selected cards have a blue edge and evidence-selection label to connect actions with source feedback. Demo details remain available in an expandable disclosure. The student has not yet evaluated this revision.

Correspondence revision: added a decorative postmark, airmail border, paper tape, margin annotation, handwritten-style notes, and staggered task cards. Body text remains in a reading font. Narrow screens remove card rotation and offsets. Decorations do not add controls or change task status. Handwriting uses available local fonts, so its appearance varies by device. Browser visual verification remains pending because the preview browser blocks local file URLs.

Student self-review, 6 November 2026: the student found freedom limited, the flow unclear and content thin. They requested direct task addition from Anything missing? rather than navigating through full-email review. Codex implemented Add new task as the primary action and kept review as a secondary link. See [feedback and revision record](development-feedback.md). This addresses the extra navigation; broader feedback remains unresolved pending further review.

## AI assistance and student contribution

Follow-up interaction revision: removed the duplicate add button from review guidance. Finish full-email review shows the existing acknowledgement and hides the guidance card; Review full email can reopen it. Add new task in Anything missing? is the single task-creation entry. Handler checks cover closing, reopening and unchanged acknowledgement text; browser verification remains pending.

Scope decision, 6 November 2026: the student chose not to add specific omission feedback after Finish full-email review. It remains a user acknowledgement, not a completeness check. General review guidance and manual task addition remain available. Code inspection confirms the handler only sets the review flag, renders state and announces acknowledgement; browser verification remains pending.

Codex generated the initial HTML, CSS, JavaScript, and documentation from the student's request and A1 context. This initial code is assisted work. The student should inspect and adapt it, record actual checks and decisions, and cite relevant commits. Do not claim student review or testing before completing it.

## Submission

Repository: https://github.com/dawsen1208/esa-email-summary-assistant. Final submitted commit remains to be selected after screenshots and reference checks. The [English report draft](A2-report-draft.md) includes the architecture diagram and figure placeholders. Follow the [bilingual screenshot checklist](screenshot-checklist.md) to capture three interaction sequences. The report remains a draft: actual screenshots, final reference checks and the final submission identifier are outstanding. Local course PDFs, extracted lecture text and private authoring notes are excluded from this repository. Use fictional data only in this demonstration.
