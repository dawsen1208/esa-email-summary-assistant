# ESA Development Feedback and Change Record

## Project direction and contribution

I defined ESA around the A1 question of whether source links could help students check university email summaries. I chose a local HTML, CSS and JavaScript prototype with one fictional email. I chose the name, letter style, scope of manual review and three demonstration cases. I reviewed the prototype, requested changes and captured the screenshots.

I used Codex to generate the initial code and to help with later revisions, checks, documentation and report layout. The decisions below record what I reviewed and chose; they do not claim that I wrote all the code without assistance.

## Self-review on 6 November 2026

In my own trial, I found limited freedom, an unclear flow and thin content. This was my own feedback, not an independent participant study. I did not collect timing or accuracy data.

### Direct task addition

I found that adding a task required opening the full-email review guide first. I asked for Add new task directly in Anything missing? to remove this extra step.

Before: Anything missing? → Review full email → review guide → Add a missing task → form.

After: Anything missing? → Add new task → form.

I kept Review full email as a separate option. Saving a new task creates an Added by you card and resets the full-email review status. Finish full-email review still records a personal acknowledgement and does not detect missing requirements.

The visible add button relates to the signifiers and gulf of execution discussed in Lecture 06. Removing a step also relates to unnecessary memory demands in Lecture 05. These are reasons for the design, not evidence of measured improvements.

### One add button and a closing review guide

I then asked to remove Add a missing task from Review for missing requirements. Add new task in Anything missing? became the single entry point. I also asked for Finish full-email review to show the existing message and close the guide. Focus returns to Review full email, which can reopen the guide.

Checks using a simplified DOM covered opening the empty form, saving, cancelling, resetting review, closing and reopening the guide, and keeping the existing completion message. These checks do not establish browser layout, focus behaviour in a real browser or accessibility. The three concerns from my trial are not all resolved by this change.

### Scope of review feedback

I considered showing a hint naming a missed requirement after Finish full-email review. I rejected it because it would add answer checking and would need an explanation of how the system knows what was missed. I kept manual reading and task addition. Checked progress is not a guarantee that the task list is complete.

## Visual changes

I chose paper details, email imagery and handwritten accents to make ESA look like a checking desk. After reviewing the screen, I found that the introduction took too much space. I asked for a compact title, one short explanation, a smaller note and reduced spacing. The decorative note is hidden on small screens. These changes give the email and tasks more space without changing the review flow. A full responsive-layout audit remains open.

## Screenshot evidence

I captured ten screenshots and stored them in `assets/storyboards/`. They show selected desktop actions, not a general usability result.

### Figure 2 Correcting the proposal deadline

The four captures show the wrong 6 November 2026 deadline, the highlighted source stating 9 November at 12:00, the edit form and the saved correction. The result shows Edited by you and 1 of 2 tasks checked. Files `01` to `04` record this sequence.

### Figure 3 Confirming the consent-form task

The first capture shows the highlighted 11 November 2026 at 17:00 source, Needs checking and progress of 1 of 2. The second shows Confirmed by you and 2 of 2. Full-email review is still unfinished. Files `05` and `06` show that checking one task is separate from reviewing the whole email.

### Figure 4 Adding the ethics checklist

The four captures show manual review, entry of the checklist and its 9 November 2026 at 12:00 deadline, the added task after editing and the completed full-email review. I replaced `09-checklist-added.png` and `10-review-finished.png` after noticing different checklist labels. Both final captures now show Edited by you. The last capture also shows Full email reviewed by you, the existing completion message and the closed guide. Earlier captures remain in Git history.
