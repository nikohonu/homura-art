import sys

from PySide6.QtWidgets import QApplication

from homura_art.views.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    widget = MainWindow(app)
    widget.show()
    widget.resize(1025, 768)
    app.exec()


if __name__ == "__main__":
    main()
