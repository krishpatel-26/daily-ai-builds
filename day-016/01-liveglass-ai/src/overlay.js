const root = document.getElementById('translations');
function render(payload) {
  root.replaceChildren();
  const items = Array.isArray(payload?.items) ? payload.items : [];
  const opacity = Math.min(1, Math.max(.5, Number(payload?.opacity) || .92));
  for (const item of items) {
    const node = document.createElement('div');
    node.className = 'translation' + (Number(item.confidence) < 55 ? ' low-confidence' : '');
    node.style.left = Math.max(0, Number(item.x) || 0) + 'px';
    node.style.top = Math.max(0, Number(item.y) || 0) + 'px';
    node.style.width = Math.max(24, Number(item.width) || 24) + 'px';
    node.style.minHeight = Math.max(14, Number(item.height) || 14) + 'px';
    node.style.opacity = String(opacity);
    node.title = 'Original: ' + String(item.original || '');
    const label = document.createElement('span'); label.className = 'tag'; label.textContent = 'EN';
    const text = document.createElement('span'); text.textContent = String(item.text || '');
    node.append(label, text); root.append(node);
  }
}
window.liveGlass.onOverlayItems(render);
