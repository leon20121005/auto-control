## Development

### Install Dependencies
```
pip install pyautogui
pip install keyboard
```

## Deployment
Use PyInstaller to bundle Python application and all its dependencies into a single executable file. User can run the executable file without installing Python interpreter or any packages.

### Installation
```
pip install pyinstaller
```

### Usage

For Windows:
```
pyinstaller -F .\autoControl.py
```

For Mac OS X:
```
pyinstaller -F ./autoControl.py
```

The bundled application will be placed in `dist` folder.
