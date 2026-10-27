export function createMemoryStore(initialItems = []) {
  let items = [...initialItems];
  return {
    all() { return items.map((item) => ({ ...item })); },
    get(id) { const item = items.find((candidate) => candidate.id === id); return item ? { ...item } : null; },
    replace(nextItems) { items = [...nextItems]; return this.all(); },
    update(id, patch) { let found = false; items = items.map((item) => { if (item.id !== id) return item; found = true; return { ...item, ...patch }; }); return found ? this.get(id) : null; },
    reset(nextItems = []) { items = [...nextItems]; return this.all(); }
  };
}
