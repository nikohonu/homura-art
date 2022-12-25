import datetime as dt
import random
import subprocess

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QPixmap, QResizeEvent, QShortcut
from PySide6.QtWidgets import QDialog, QMessageBox

from homura_art.image import make_collage
from homura_art.model import File
from homura_art.ui.collage_preview import Ui_CollagePreview
from homura_art.ui_helper import shortcut_button_connect


class CollagePreview(QDialog, Ui_CollagePreview):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.make_collage()
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        self.shortcut_next = QShortcut(QKeySequence("S"), self)
        self.shortcut_1 = QShortcut(QKeySequence(Qt.Key.Key_1), self)
        self.shortcut_2 = QShortcut(QKeySequence(Qt.Key.Key_2), self)
        self.shortcut_3 = QShortcut(QKeySequence(Qt.Key.Key_3), self)
        shortcut_button_connect(self.shortcut_next, self.button_next, self.make_collage)
        shortcut_button_connect(self.shortcut_1, self.button_1, self.safe_1)
        shortcut_button_connect(self.shortcut_2, self.button_2, self.safe_2)
        shortcut_button_connect(self.shortcut_3, self.button_3, self.safe_3)

    def make_collage(self):
        files = list(
            File.select()
            .where(
                (File.used == False)
                & ((File.safe_rating == None) | (File.safe_rating > 0))
            )
            .order_by(File.rating.desc())
            .limit(32)
        )
        if len(files) < 3:
            QMessageBox.warning(self, "Error", "There is no file for making collage.")
        self.files = random.sample(files, 3)
        for i in reversed(range(1, 4)):
            self.files = self.files[:i]
            self.image = make_collage([file.path for file in self.files])
            if self.image:
                break
        if len(self.files) < 3:
            self.button_3.hide()
        else:
            self.button_3.show()
        if len(self.files) < 2:
            self.button_2.hide()
        else:
            self.button_2.show()
        self.repaint()
        return True

    def safe(self, index):
        self.files[index].safe_rating = 0
        self.files[index].save()
        self.make_collage()

    def safe_1(self):
        self.close()
        self.safe(0)

    def safe_2(self):
        self.safe(1)

    def safe_3(self):
        self.safe(2)

    def accept(self) -> None:
        for file in self.files:
            file.used = True
            file.used_time = dt.datetime.now()
            file.save()
        return super().accept()

    def repaint(self):
        w = self.file.width()
        h = self.file.height()
        self.file.setPixmap(
            self.image.scaled(w, h, aspectMode=Qt.AspectRatioMode.KeepAspectRatio)
        )

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.repaint()
        return super().resizeEvent(event)
