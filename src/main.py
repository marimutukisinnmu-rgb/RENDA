"""RENDA desktop application entry point."""

import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("RENDA")
        self.setMinimumSize(420, 300)

        self.status = QLabel("停止中")
        self.status.setObjectName("statusLabel")

        self.start_button = QPushButton("開始 / 停止 (F6)")
        self.start_button.setEnabled(False)
        self.start_button.setToolTip("クリックエンジンとホットキーは次の開発段階で実装します")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("RENDA Auto Clicker"))
        layout.addWidget(self.status)
        layout.addWidget(self.start_button)
        layout.addWidget(QLabel("現在はGUIの土台です。クリック機能はまだ有効ではありません。"))

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
