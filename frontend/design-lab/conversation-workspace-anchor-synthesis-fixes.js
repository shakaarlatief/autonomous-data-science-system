const root = document.documentElement;
const expandButton = document.querySelector('#expand-home');

function syncExpandVisibility() {
  if (!expandButton) return;
  const show = root.dataset.composition === 'a6' && root.dataset.home !== 'project';
  expandButton.style.display = show ? 'inline-block' : 'none';
}

document.querySelector('#composition-select')?.addEventListener('change', () => queueMicrotask(syncExpandVisibility));
document.querySelectorAll('[data-composition]').forEach((button) => {
  button.addEventListener('click', () => queueMicrotask(syncExpandVisibility));
});
document.querySelectorAll('[data-thread]').forEach((button) => {
  button.addEventListener('click', () => queueMicrotask(syncExpandVisibility));
});

syncExpandVisibility();
