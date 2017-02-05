const { app, BrowserWindow } = require('electron');
const path = require('path');
const url = require('url');
const spawn = require('child_process').spawn;

const isProd = process.env.NODE_ENV === 'production';

const productionURL = url.format({
  pathname: path.join(__dirname, 'index.html'),
  protocol: 'file:',
  slashes: true,
});
const developmentURL = 'http://127.0.0.1:3000';

let mainWindow;

function createWindow () {
  mainWindow = new BrowserWindow({
    width: 800, 
    height: 600,
  });

  const craProc = spawn('yarn', ['start'], {
    cwd: path.join(__dirname, 'client'),
  });

  mainWindow.loadURL(isProd ? productionURL : developmentURL);

  mainWindow.webContents.openDevTools();

  mainWindow.on('closed', function () {
    mainWindow = null;
    craProc.kill('SIGINT');
  });
}

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
  }
});

app.on('ready', createWindow);
