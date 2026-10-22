const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('liveGlass', {
  getSettings: () => ipcRenderer.invoke('settings:get'),
  saveSettings: value => ipcRenderer.invoke('settings:save', value),
  toggle: () => ipcRenderer.invoke('translation:toggle'),
  scan: () => ipcRenderer.invoke('translation:scan'),
  clear: () => ipcRenderer.invoke('translation:clear'),
  getStatus: () => ipcRenderer.invoke('app:status'),
  onStatus: callback => { const handler = (_e, value) => callback(value); ipcRenderer.on('app:status', handler); return () => ipcRenderer.removeListener('app:status', handler); },
  onOverlayItems: callback => { const handler = (_e, value) => callback(value); ipcRenderer.on('overlay:items', handler); return () => ipcRenderer.removeListener('overlay:items', handler); }
});
