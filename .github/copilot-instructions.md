# RENDA coding instructions

## Project intent
Build a small, cross-platform desktop click automation app for Windows and macOS, including Intel Macs.

## Compatibility
- Keep Python 3.9 compatibility unless the project explicitly raises its minimum version.
- Do not use Windows-only APIs (such as `ctypes.windll.user32`) in shared code.
- Isolate OS-specific behavior behind small interfaces/modules.
- Do not assume Windows virtual environments or compiled packages can be copied to macOS. Install dependencies separately on each OS.

## Safety and permissions
- Never bypass macOS Accessibility, Input Monitoring, or other OS privacy permissions.
- Explain which permission is needed and let the user grant it in System Settings.
- Do not run clicks until the user explicitly starts the feature.
- Provide an obvious stop control and a safe shutdown path.
- Avoid unbounded busy loops; use a configurable interval and cooperative thread shutdown.

## Planned UX
- F6 toggles clicking on/off.
- Escape exits the app.
- Caps Lock may select left/right click, but verify behavior on macOS before implementing it.
- GUI also provides start/stop and click-interval controls.
- Display current state clearly.

## Engineering
- Keep UI, click engine, and hotkey handling separate.
- Keep callbacks thread-safe; do not update Qt widgets directly from worker threads.
- Add tests for interval validation and state transitions.
- Do not claim a feature is implemented unless it is present and tested.
