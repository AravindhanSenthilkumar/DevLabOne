const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 1280,
    height: 850,
    title: "DevLab-One Workspace Manager",
    titleBarStyle: 'hiddenInset', // Integrated window traffic lights for premium native macOS look
    backgroundColor: '#090d16',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  // Load the running Vite development server
  win.loadURL('http://localhost:5173/');
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
