"""Global hotkey interface; platform permissions must be verified first."""


class HotkeyManager:
    """Placeholder for F6/Escape hotkey handling."""

    def start(self) -> None:
        raise NotImplementedError("Global hotkeys are not implemented yet")

    def stop(self) -> None:
        raise NotImplementedError("Global hotkeys are not implemented yet")
