'use strict';
const initialTasks = [
  {id: 'proposal', title: 'Submit research proposal as a PDF through the module portal', date: '2026-11-06T12:00', source: 'source-proposal', status: 'unreviewed'},
  {id: 'consent', title: 'Upload completed consent form to the module portal', date: '2026-11-11T17:00', source: 'source-consent', status: 'unreviewed'}
];
let tasks = initialTasks.map(task => ({...task}));
let editingId = null;
let fullReview = false;
let activeEvidence = null;
let toastTimer;
const $ = id => document.getElementById(id);
const editor = $('editor');
function announce(message) {
  clearTimeout(toastTimer);
  $('announcement').textContent = message;
  toastTimer = setTimeout(() => { $('announcement').textContent = ''; }, 6500);
}
function formatDate(value) {
  if (!value) return 'No deadline specified';
  return new Intl.DateTimeFormat('en-GB', {weekday: 'short', day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false}).format(new Date(value));
}
function button(text, className, action) {
  const element = document.createElement('button');
  element.textContent = text;
  element.className = className;
  element.type = 'button';
  element.addEventListener('click', action);
  return element;
}
function render() {
  $('tasks').replaceChildren();
  tasks.forEach((task, index) => {
    const card = document.createElement('article'); card.className = `task${activeEvidence === task.id ? ' active-evidence' : ''}`;
    const top = document.createElement('div'); top.className = 'task-top';
    const content = document.createElement('div');
    const number = document.createElement('div'); number.className = 'task-number'; number.textContent = `${task.source ? 'EXTRACTED NOTE' : 'YOUR NOTE'} / ${String(index + 1).padStart(2, '0')}`;
    const title = document.createElement('h3'); title.textContent = task.title;
    content.append(number, title);
    const status = document.createElement('span'); status.className = `status ${task.status !== 'unreviewed' ? 'checked' : ''}`;
    status.textContent = ({unreviewed: 'Needs checking', confirmed: 'Confirmed by you', corrected: 'Edited by you', added: 'Added by you'})[task.status];
    top.append(content, status);
    const date = document.createElement('p'); date.className = 'deadline'; date.textContent = formatDate(task.date);
    const actions = document.createElement('div'); actions.className = 'task-actions';
    if (task.source) actions.append(button(activeEvidence === task.id ? 'Evidence selected ↗' : 'Find in email ↗', 'secondary evidence-button', () => showEvidence(task)));
    actions.append(button('Confirm correct', 'secondary', () => { task.status = 'confirmed'; render(); announce('Task marked correct by you. This is not an automatic accuracy check.'); }));
    actions.append(button('Edit task', 'text-button', () => openEditor(task)));
    card.append(top, date, actions); $('tasks').append(card);
  });
  const checked = tasks.filter(task => task.status !== 'unreviewed').length;
  $('progress-text').textContent = `${checked} of ${tasks.length} tasks checked`;
  $('progress').max = tasks.length; $('progress').value = checked;
  $('review-status').textContent = fullReview ? 'Full email reviewed by you' : 'Full email not reviewed';
}
function showEvidence(task) {
  activeEvidence = task.id; render();
  document.querySelectorAll('.highlight').forEach(element => element.classList.remove('highlight'));
  const passage = $(task.source); passage.classList.add('highlight'); passage.focus({preventScroll: true});
  passage.scrollIntoView({behavior: 'smooth', block: 'center'});
  announce('Source passage highlighted. Compare both the action and deadline before confirming.');
}
function openEditor(task = null) {
  editingId = task ? task.id : null;
  $('editor-title').textContent = task ? 'Edit task' : 'Add new task';
  $('task-title').value = task ? task.title : '';
  $('task-date').value = task ? task.date : '';
  $('form-error').textContent = '';
  editor.showModal(); $('task-title').focus();
}
$('edit-form').addEventListener('submit', event => {
  event.preventDefault();
  const title = $('task-title').value.trim();
  if (!title) { $('form-error').textContent = 'Enter a required action.'; $('task-title').focus(); return; }
  const date = $('task-date').value;
  if (editingId) {
    const task = tasks.find(item => item.id === editingId);
    task.title = title; task.date = date; task.status = 'corrected';
  } else {
    tasks.push({id: `manual-${Date.now()}`, title, date, source: null, status: 'added'});
  }
  fullReview = false; render(); editor.close(); announce('Task saved in this page. Review the full email again if needed.');
});
['close-editor', 'cancel-edit'].forEach(id => $(id).addEventListener('click', () => editor.close()));
$('review-email').addEventListener('click', () => {
  activeEvidence = null; render();
  $('review-guide').hidden = false;
  document.querySelectorAll('.highlight').forEach(element => element.classList.remove('highlight'));
  $('email-heading').scrollIntoView({behavior: 'smooth', block: 'start'});
  $('finish-review').focus({preventScroll: true});
  announce('Read the complete original email. Add any requirement missing from the suggested tasks.');
});
$('quick-add-task').addEventListener('click', () => openEditor());
$('finish-review').addEventListener('click', () => {
  fullReview = true; render();
  announce('Full-email review recorded. Individual task checks remain your decision.');
  $('review-guide').hidden = true;
  $('review-email').focus({preventScroll: true});
});
$('reset').addEventListener('click', () => {
  tasks = initialTasks.map(task => ({...task})); fullReview = false; activeEvidence = null;
  $('review-guide').hidden = true;
  document.querySelectorAll('.highlight').forEach(element => element.classList.remove('highlight'));
  render(); announce('Demo reset. Your page edits have been cleared.');
});
render();
