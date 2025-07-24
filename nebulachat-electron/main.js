const { app, BrowserWindow } = require('electron')
const path = require('path')
const { spawn } = require('child_process')

function createWindow () {
  const win = new BrowserWindow({
    width: 1000,
    height: 720,
    webPreferences: {
      nodeIntegration: true
    }
  })
  win.loadURL('http://localhost:5000')
}

app.whenReady().then(() => {
  const python = spawn('python', ['main.py'], { cwd: path.join(__dirname, 'app') })
  python.stdout.on('data', (data) => console.log(`PYTHON: ${data}`))
  python.stderr.on('data', (data) => console.error(`PYTHON ERR: ${data}`))
  createWindow()
})