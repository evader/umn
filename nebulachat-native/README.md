
# NebulaChat Native Installer

To build native executables:

### Linux/macOS

```bash
chmod +x install.sh
./install.sh
```

### Windows

Use `pyinstaller` or `nuitka`:

```bash
pip install pyinstaller
pyinstaller main.py --onefile --name NebulaChat
```
