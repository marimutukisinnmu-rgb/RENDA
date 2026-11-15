# RENDA

Cross-platform desktop auto-clicker project.

## Goals

- Develop on Windows and run on macOS (including Intel Mac).
- Provide a simple desktop GUI.
- Keep platform-specific input handling isolated.
- Require normal, user-approved macOS permissions; never attempt to bypass OS privacy controls.

## Planned controls

- **F6**: toggle clicking on/off.
- **Esc**: quit the application.
- **Caps Lock**: choose left or right mouse button (planned; platform behavior must be verified).
- GUI controls for click interval and start/stop.

## Development status

Early scaffold. The click engine and global hotkeys are not implemented yet. Platform permissions and keyboard behavior must be tested on the target Mac before enabling global automation.

## Requirements

- Python 3.9+
- Dependencies are listed in [requirements.txt](requirements.txt).

## Run from source

Create and activate a virtual environment, then install dependencies:

### Windows (PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m src.main
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.main
```

macOS may request Accessibility and/or Input Monitoring permissions for the app or terminal. Grant permissions only with the Mac user's consent and through System Settings.

## Project layout

```text
RENDA/
├── .github/
│   └── copilot-instructions.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── click_engine.py
│   ├── hotkeys.py
│   └── ui/
│       └── __init__.py
├── tests/
├── assets/
├── config/
├── requirements.txt
└── README.md
```
