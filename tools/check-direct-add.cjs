// State/handler smoke check only; this does not emulate browser layout or focus.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
class Element {
  constructor() { this.children = []; this.handlers = {}; this.value = ''; this.hidden = true; this.open = false; }
  append(...items) { this.children.push(...items); }
  replaceChildren(...items) { this.children = items; }
  addEventListener(type, fn) { this.handlers[type] = fn; }
  focus() {}
  showModal() { this.open = true; }
  close() { this.open = false; }
  scrollIntoView() {}
}
const elements = new Map();
const get = id => { if (!elements.has(id)) elements.set(id, new Element()); return elements.get(id); };
const html = fs.readFileSync('index.html', 'utf8');
for (const id of ['quick-add-task', 'review-email', 'editor']) assert(html.includes(`id="${id}"`));
assert(!html.includes('id="add-task"'), 'Remove duplicate task-add entry');
const context = vm.createContext({document: {getElementById: get, createElement: () => new Element(), querySelectorAll: () => []}, Intl, Date, setTimeout: () => 1, clearTimeout: () => {}});
vm.runInContext(fs.readFileSync('script.js', 'utf8'), context);
const run = code => vm.runInContext(code, context);
const click = id => get(id).handlers.click();
click('quick-add-task');
assert.equal(get('editor').open, true);
assert.equal(get('task-title').value, '');
assert.equal(get('review-guide').hidden, true, 'Adding must not require opening review guidance');
click('cancel-edit');
assert.equal(run('tasks.length'), 2);
click('review-email');
assert.equal(get('review-guide').hidden, false);
click('finish-review');
assert.equal(run('fullReview'), true, 'Review must work without finding the omitted item');
assert.equal(get('review-guide').hidden, true, 'Finish must dismiss review guidance');
assert.equal(get('announcement').textContent, 'Full-email review recorded. Individual task checks remain your decision.');
click('review-email');
assert.equal(get('review-guide').hidden, false, 'Review guidance can be reopened');
click('finish-review');
click('quick-add-task');
get('task-title').value = 'Attach completed ethics checklist';
get('task-date').value = '2026-11-09T12:00';
get('edit-form').handlers.submit({preventDefault() {}});
assert.equal(run('tasks.length'), 3);
assert.equal(run('tasks[2].status'), 'added');
assert.equal(run('tasks[2].source'), null);
assert.equal(run('fullReview'), false);
assert.equal(get('editor').open, false);
assert.equal(get('tasks').children.length, 3);
assert.equal(get('progress-text').textContent, '1 of 3 tasks checked');
console.log('PASS: direct add, cancel, save, card rendering, review reset and acknowledgement-only completion. Browser verification remains pending.');
