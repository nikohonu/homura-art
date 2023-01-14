import datetime as dt
from pathlib import Path
import random
import subprocess
import tempfile

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QPixmap, QResizeEvent, QShortcut
from PySide6.QtWidgets import QDialog, QMessageBox

from homura_art.image import make_collage
from homura_art.views.ui.collage_preview import Ui_CollageDialog


class CollageDialog(QDialog, Ui_CollageDialog):
    def __init__(self, client) -> None:
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.tmp_path = Path(tempfile.gettempdir()) / "homura-art"
        self.tmp_path.mkdir(parents=True, exist_ok=True)
        self.tag_service = self.get_tag_service()
        self.make_collage()
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        self.action_next.triggered.connect(self.make_collage)

    def get_tag_service(self):
        for service in self.client.get_services()["local_tags"]:
            if service["name"] == "my tags" and service["type"] == 5:
                return service["service_key"]

    def make_collage(self):
        ids_with_elo = self.client.search_files(
            ["system:archive", "elo:*", "system:filetype is image", "-meta:used"]
        )
        files = []
        for file_with_elo in self.client.get_file_metadata(file_ids=ids_with_elo):
            tags = file_with_elo["tags"][self.tag_service]["storage_tags"]
            print(tags)
            elo = 0
            ext = file_with_elo["ext"]
            for tag in tags["0"]:
                if tag.startswith("elo:"):
                    elo = int(tag.split(":")[1])
                    print(elo)
            files.append([file_with_elo["file_id"], elo, ext])
        files = sorted(files, key=lambda f: f[1], reverse=True)[:32]
        for file in files:
            id = file[0]
            path = self.tmp_path / (str(id) + file[2])
            if not path.exists():
                with path.open("wb") as f:
                    f.write(self.client.get_file(file_id=id).content)
            file[2] = path
        if len(files) < 3:
            QMessageBox.warning(self, "Error", "There is no file for making collage.")
        self.files = random.sample(files, 3)
        for i in reversed(range(1, 4)):
            self.files = self.files[:i]
            self.image = make_collage([file[2] for file in self.files])
            if self.image:
                break
        self.repaint()
        return True

    def accept(self) -> None:
        ids = [file[0] for file in self.files]
        self.client.add_tags(
            file_ids=ids,
            service_keys_to_actions_to_tags={
                self.tag_service: {
                    0: [f"meta:used"],
                }
            },
        )
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
