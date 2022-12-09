import os
import shutil
import sys

from peewee import fn
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QPixmap, QPaintEvent, QPainter, QResizeEvent
from PySide6.QtCore import Qt

from homura_art.collage_tab import CollageTab
from homura_art.elo_tab import EloTab
from homura_art.inbox_tab import InboxTab
from homura_art.model import File
from homura_art.ui.main_window import Ui_MainWindow
from homura_art.used_tab import UsedTab
from homura_art.utilities import sync
import hydrus_api

ACCCESS_KEY = os.environ.get("ACCCESS_KEY", "")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.client = hydrus_api.Client(ACCCESS_KEY)
        self.files, self.pathes = self.get_random_files()
        self.left_image = QPixmap(self.pathes[0])
        self.right_image = QPixmap(self.pathes[1])
        self.left_win_button.clicked.connect(self.left_win)
        self.right_win_button.clicked.connect(self.right_win)
        self.tie_button.clicked.connect(self.tie)
        self.skip_button.clicked.connect(self.get_next)
        self.delete_left_button.clicked.connect(self.delete_left)
        self.delete_right_button.clicked.connect(self.delete_right)


    def delete(self, file):
        self.client.delete_files([file.hash_str])
        file.delete_instance()
        self.get_next()

    def delete_left(self):
        self.delete(self.files[0])

    def delete_right(self):
        self.delete(self.files[1])

    def play(self, result):
        def get_expected_score(r_a, r_b):
            return 1 / (1 + 10 ** ((r_a - r_b) / 400))

        def get_new_rating(r_a, r_b, score):
            return r_a + 32 * (score - get_expected_score(r_a, r_b))

        self.files[0].rating = get_new_rating(
            self.files[0].rating, self.files[1].rating, result
        )
        self.files[1].rating = get_new_rating(
            self.files[1].rating, self.files[0].rating, 1 - result
        )
        self.files[0].save()
        self.files[1].save()
        self.client.archive_files([file.hash_str for file in self.files])
        print(self.files)

    def left_win(self):
        self.play(1)
        self.get_next()

    def right_win(self):
        self.play(0)
        self.get_next()

    def tie(self):
        self.play(0.5)
        self.get_next()

    def get_next(self):
        self.files, self.pathes = self.get_random_files()
        self.left_image = QPixmap(self.pathes[0])
        self.right_image = QPixmap(self.pathes[1])
        self.repaint()

    def repaint(self):
        w = self.left_file.width()
        h = self.left_file.height()
        self.left_file.setPixmap(
            self.left_image.scaled(w, h, aspectMode=Qt.AspectRatioMode.KeepAspectRatio)
        )
        self.right_file.setPixmap(
            self.right_image.scaled(w, h, aspectMode=Qt.AspectRatioMode.KeepAspectRatio)
        )

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.repaint()
        return super().resizeEvent(event)

    def get_random_files(self):
        allow_extensions = [".png", ".jpg", ".webp"]
        while True:
            ok = True
    
            files = File.select().order_by(fn.Random()).limit(2)
            hashes = [file.hash_str for file in files]
            extensions = [data["ext"] for data in self.client.get_file_metadata(hashes)]
            responses = [self.client.get_file(hash) for hash in hashes]
            for extension in extensions:
                if extension not in allow_extensions:
                    ok = False
            pathes = []
            for response, extension, name in zip(
                responses, extensions, ["left", "right"]
            ):
                path = f"/tmp/{name}{extension}"
                pathes.append(path)
                with open(path, "wb") as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            if ok:
                return files, pathes


def main():
    if ACCCESS_KEY:
        sync(ACCCESS_KEY)
        app = QApplication([])
        widget = MainWindow()
        widget.show()
        widget.resize(1025, 768)
        sys.exit(app.exec())
    else:
        print("Export ACCCESS_KEY before run")


if __name__ == "__main__":
    main()
