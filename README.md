# ESA Email Summary Assistant

I designed ESA as a local prototype for checking simulated AI summaries of university emails. My aim is to make suggested tasks easy to compare with the original email before confirming or changing them.

[Report source](A2-report.md) · [Report PDF](output/pdf/ESA_A2_Report.pdf) · [Development record](development-feedback.md) · [Screenshot checklist](screenshot-checklist.md)

## Status and scope

I defined a working interface with an original-email view, task cards, source highlights, confirmation, editing with Save and Cancel, direct task addition, progress, review acknowledgement and reset. Changes last until the page is reloaded or reset. Finish full-email review records a personal acknowledgement, not a guarantee that every requirement has been found.

I kept AI extraction and task-to-source links simulated with prepared data. There is no connected mailbox, model, backend or analytics service. Live extraction, arbitrary email input, automatic source selection and permanent storage remain undeveloped. I have not measured an improvement in accuracy or checking speed.

## Run and inspect

Open `index.html` in a browser. No installation, internet connection, account or API key is needed. I used a fictional email in HTML, JavaScript state and controls, and three CSS files for the layout and letter style. Dates keep the time written in the email without timezone conversion.

To follow the demonstration:

1. Select Find in email on the proposal card. Compare its deadline with the highlighted source, then change 6 November to 9 November 2026 at 12:00.
2. Check the consent-form deadline of 11 November at 17:00 and select Confirm correct.
3. Read the full email, find the missing ethics checklist and add it through Add new task in Anything missing?.
4. Select Finish full-email review to record the review and close the guide. Review full email opens the guide again.

## Design decisions

- I developed the A1 idea around checking evidence instead of accepting a summary without review. I kept the full email visible beside the task cards.
- I chose the ESA name and a letter style with paper details and handwritten accents. I later reduced the introduction to give the working area more space.
- In my own trial, I found limited freedom, unclear steps and thin content. I requested direct task addition, removed the repeated add button and asked for the review guide to close after completion.
- I rejected hints that name a missing requirement. I kept manual review and task addition without adding automatic omission detection.
- I captured ten screenshots and replaced inconsistent checklist states. The last two checklist panels both show Edited by you. I kept captions consistent with the captured states.

I explain these choices and the remaining limits in the [development record](development-feedback.md). My own trial is not an independent user study.

## AI assistance and contribution

I used Codex to generate the initial code and to help with later revisions, checks and report preparation.

## Checks and report files

`node tools/check-direct-add.cjs` checks selected state changes with a simplified DOM. These checks cover direct addition, cancellation, saving and review behaviour; they do not replace browser or usability testing. A full accessibility and responsive-layout audit remains open.

I keep `A2-report.md` as the editable source for the repository PDF. To rebuild it, install `report-requirements.txt` and run `python tools/build_a2_report.py`. Python is not needed to run ESA. Original screenshots remain in `assets/storyboards/`.

The prototype and screenshot snapshot is [3a4497c](https://github.com/dawsen1208/esa-email-summary-assistant/commit/3a4497c). Later commits update the documentation. I removed the old report draft from the main branch to avoid conflicting versions; it remains in Git history.
