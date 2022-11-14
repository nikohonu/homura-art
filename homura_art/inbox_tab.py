import subprocess
from pathlib import Path

from appdirs import user_data_dir
from PIL import Image, ImageQt
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QListView, QVBoxLayout, QWidget


def get_pictures_path():
    result = subprocess.run(["xdg-user-dir", "PICTURES"], capture_output=True)
    return Path(result.stdout.decode().replace("\n", ""))


class InboxModel(QAbstractListModel):
    def __init__(self) -> None:
        super().__init__()
        art_path = get_pictures_path() / "art"
        self.files = [file for file in art_path.glob("*")]
        self.images = []
        for file in self.files:
            image = Image.open(file)
            image.thumbnail((100, 100), Image.ANTIALIAS)
            mode = image.mode
            width, height = image.size
            match len(mode):
                case 1:
                    background = 255
                case 3:
                    background = (255, 255, 255)
                case 4:
                    background = (255, 255, 255, 255)
                case _:
                    raise (ValueError("Invalid image mode"))
            square_image = Image.new(mode, (100, 100), background)
            square_image.paste(image, (50 - width // 2, 50 - height // 2))
            self.images.append(ImageQt.toqpixmap(square_image))

    def rowCount(self, parent) -> int:
        return len(self.images)

    def data(self, index: QModelIndex, role: int):
        if role == Qt.DecorationRole:
            return self.images[index.row()]
        if role == Qt.DisplayRole:
            return self.files[index.row()].stem


class InboxTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.root_layout = QVBoxLayout()
        self.view = QListView()
        self.view.setViewMode(QListView.ViewMode.IconMode)
        self.view.setFlow(QListView.Flow.LeftToRight)
        # self.view.setLayoutMode(QListView.Batched)
        self.view.setResizeMode(QListView.Adjust)
        self.view.setUniformItemSizes(True)
        self.view.setWrapping(True)
        self.view.setModel(InboxModel())
        self.setLayout(self.root_layout)
        self.root_layout.addWidget(self.view)
