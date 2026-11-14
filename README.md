# ESA Email Summary Assistant

ESA is a local prototype for checking simulated AI summaries of university emails. Suggested tasks appear beside the original email, with source highlights, editable details and manual review controls. The main purpose is to support comparison before task details are accepted or changed.

[Report source](A2-report.md) · [Report PDF](output/pdf/ESA_A2_Report.pdf) · [Development record](development-feedback.md) · [Screenshot checklist](screenshot-checklist.md)

## Status and scope

Working features include the original-email view, task cards, source highlights, confirmation, editing with Save and Cancel, direct task addition, progress, review acknowledgement and reset. Changes last until the page is reloaded or reset. Finish full-email review records an acknowledgement; completion does not guarantee that every requirement has been found.

AI extraction and task-to-source links are simulated with prepared data. No mailbox, model, backend or analytics service is connected. Live extraction, arbitrary email input, automatic source selection and permanent storage remain undeveloped. Improvements in accuracy and checking speed have not been measured.

## Run and inspect

Open `index.html` in a browser. No installation, internet connection, account or API key is needed. HTML contains the fictional email, JavaScript manages page state and controls, and three CSS files provide the layout and letter style. Dates keep the time written in the email without timezone conversion.

Demonstration sequence:

1. Select Find in email on the proposal card. Compare the suggested deadline with the highlighted source, then change 6 November to 9 November 2026 at 12:00.
2. Check the consent-form deadline of 11 November at 17:00 and select Confirm correct.
3. Read the full email, find the missing ethics checklist and add the requirement through Add new task in Anything missing?.
4. Select Finish full-email review to record completion and close the guide. Review full email opens the guide again.

## Design decisions

- Source comparison: the A1 question about checking summary claims led to a layout with the full email beside the task cards. Find in email connects each prepared card to a source paragraph.
- Visual style: the ESA name, paper details and handwritten accents create a letter style. A smaller introduction gives the working area more space.
- Direct controls: self-review identified limited freedom, unclear steps and thin content. Direct task addition replaced an extra navigation step, the repeated add button was removed, and review completion now closes the guide.
- Review limits: hints naming a missing requirement were excluded. Manual reading and task addition remain available without automatic omission detection.
- Screenshot consistency: ten captures document the three demonstration cases. Replacement checklist captures use matching status labels, and captions follow the recorded screen states.

The [development record](development-feedback.md) explains the decisions, changes and checks. Self-review feedback does not represent an independent user study.

## AI assistance and contribution

Initial code generation, later revisions, checks and report preparation were supported by Codex.

## Checks and report files

`node tools/check-direct-add.cjs` checks selected state changes with a simplified DOM. Coverage includes direct addition, cancellation, saving and review behaviour. These checks do not replace browser or usability testing. A full accessibility and responsive-layout audit remains open.

`A2-report.md` is the editable source for the repository PDF. To rebuild the PDF, install `report-requirements.txt` and run `python tools/build_a2_report.py`. Python is not needed to run ESA. Original screenshots remain in `assets/storyboards/`.

The prototype and screenshot snapshot is [3a4497c](https://github.com/dawsen1208/esa-email-summary-assistant/commit/3a4497c). Later commits update the documentation. The old report draft was removed from the main branch to avoid conflicting versions and remains available in Git history.
