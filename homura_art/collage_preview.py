import datetime as dt
import random
import subprocess

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QPixmap, QResizeEvent, QShortcut
from PySide6.QtWidgets import QDialog

from homura_art.image import make_collage
from homura_art.model import File
from homura_art.ui.collage_preview import Ui_CollagePreview
from homura_art.ui_helper import shortcut_button_connect


class CollagePreview(QDialog, Ui_CollagePreview):
    def __init__(self) -> None:
        super(CollagePreview, self).__init__()
        self.setupUi(self)
        self.make_collage()
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        self.shortcut_next = QShortcut(QKeySequence("S"), self)
        shortcut_button_connect(self.shortcut_next, self.button_next, self.make_collage)

    def make_collage(self):
        files = list(
            File.select()
            .where(File.used == False)
            .order_by(File.rating.desc())
            .limit(32)
        )
        self.files = random.sample(files, 3)
        for i in reversed(range(1, 4)):
            self.files = self.files[:i]
            self.image = make_collage([file.path for file in self.files])
            if self.image:
                break
        self.repaint()

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
