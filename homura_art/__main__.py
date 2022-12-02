import sys

from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QTableWidget,
                               QTabWidget, QVBoxLayout, QWidget)

from homura_art.collage_tab import CollageTab
from homura_art.elo_tab import EloTab
from homura_art.inbox_tab import InboxTab
from homura_art.used_tab import UsedTab


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.tabs = QTabWidget()
        self.tabs.addTab(InboxTab(), "Inbox")
        self.tabs.addTab(EloTab(), "Elo")
        self.tabs.addTab(CollageTab(), "Collage")
        self.tabs.addTab(UsedTab(), "Used")
        self.setCentralWidget(self.tabs)


def main():
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
