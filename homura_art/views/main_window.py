import json
import math
import random
import tempfile
from pathlib import Path

from appdirs import user_config_dir
from hydrus_api import Client
from PySide6.QtGui import (
    QImageReader,
    QKeySequence,
    QPixmap,
    QResizeEvent,
    QShortcut,
    Qt,
)
from PySide6.QtWidgets import QMainWindow

from homura_art.image import make_collage
from homura_art.views.collage_dialog import CollageDialog
from homura_art.views.key_dialog import KeyDialog
from homura_art.views.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.config = self.load_config()
        self.client = Client(access_key=self.config["key"])
        self.tmp_path = Path(tempfile.gettempdir()) / "homura-art"
        self.tmp_path.mkdir(parents=True, exist_ok=True)
        self.tag_service = self.get_tag_service()
        self.queue = self.generate_queue()
        self.new_queue = []
        self.action_delete_left.triggered.connect(self.delete_left)
        self.action_delete_right.triggered.connect(self.delete_right)
        self.action_left_win.triggered.connect(lambda: self.win(1))
        self.action_right_win.triggered.connect(lambda: self.win(0))
        self.action_collage.triggered.connect(self.open_collage)

    def load_config(self):
        config_dir = Path(user_config_dir("homura-art", "Niko Honu"))
        config_dir.mkdir(exist_ok=True, parents=True)
        config_file_path = config_dir / "config.json"
        if config_file_path.exists():
            with config_file_path.open() as file:
                config = json.load(file)
        else:
            config = {}
        if "key" not in config:
            key_dialog = KeyDialog()
            if key_dialog.exec():
                config["key"] = key_dialog.edit_key.text()
                with config_file_path.open("w") as file:
                    json.dump(config, file)
            else:
                self.app.exit()
        return config

    def get_tag_service(self):
        for service in self.client.get_services()["local_tags"]:
            if service["name"] == "my tags" and service["type"] == 5:
                return service["service_key"]

    def generate_queue(self):
        ids_witout_elo = self.client.search_files(
            ["system:archive", "-elo:*", "system:filetype is image"]
        )
        ids_with_elo = self.client.search_files(
            ["system:archive", "elo:*", "system:filetype is image"]
        )
        files_with_elo = []
        for file_with_elo in self.client.get_file_metadata(file_ids=ids_with_elo):
            tags = file_with_elo["tags"][self.tag_service]["storage_tags"]
            print(tags)
            elo = 0
            ext = file_with_elo["ext"]
            for tag in tags["0"]:
                if tag.startswith("elo:"):
                    elo = int(tag.split(":")[1])
                    print(elo)
            files_with_elo.append([file_with_elo["file_id"], elo, ext])
        queue = []
        if files_with_elo:
            files_with_elo = sorted(files_with_elo, key=lambda f: f[1], reverse=True)
            good_files_count = math.ceil(len(files_with_elo) * 0.1)
            good_files = files_with_elo[:good_files_count]
            files_with_elo = files_with_elo[good_files_count:]
            need_good_file_count = min(8, good_files_count)
            queue = random.sample(good_files, need_good_file_count)
            print("good file", queue)
        if files_with_elo:
            need_file_with_elo_count = min(24, len(files_with_elo))
            queue += random.sample(files_with_elo, need_file_with_elo_count)
            print("elo file", queue)
        if ids_witout_elo:
            need_ids_without_elo = min(32, len(ids_witout_elo))
            ids = random.sample(ids_witout_elo, need_ids_without_elo)
            for file_with_elo in self.client.get_file_metadata(file_ids=ids):
                ext = file_with_elo["ext"]
                queue.append([file_with_elo["file_id"], 1000, ext])
            print("ids without elo", queue)
        print(self.tmp_path)
        for file in queue:
            id = file[0]
            path = self.tmp_path / (str(id) + file[2])
            if not path.exists():
                with path.open("wb") as f:
                    f.write(self.client.get_file(file_id=id).content)
            file[2] = path
        random.shuffle(queue)
        self.left = queue.pop()
        self.right = queue.pop()
        self.update_images()
        return queue

    def repaint(self):
        w = self.file.width()
        h = self.file.height()
        self.file.setPixmap(
            self.image.scaled(w, h, aspectMode=Qt.AspectRatioMode.KeepAspectRatio)
        )

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.repaint()
        return super().resizeEvent(event)

    def update_images(self):
        self.image = make_collage([self.left[2], self.right[2]], True)
        self.repaint()

    def delete(self, file):
        self.client.delete_files(file_ids=[file[0]])
        if self.queue:
            return self.queue.pop()
        else:
            if len(self.new_queue) >= 2:
                self.queue = self.new_queue
                self.new_queue = []
            else:
                self.queue = self.generate_queue()
                print("gen queue by delete")

    def delete_left(self):
        file = self.delete(self.left)
        if file:
            self.left = file
            self.update_images()

    def delete_right(self):
        file = self.delete(self.right)
        if file:
            self.right = file
            self.update_images()

    def play(self, rating_a, rating_b, result):
        def get_expected_score(r_a, r_b):
            return 1 / (1 + 10 ** ((r_a - r_b) / 400))

        def get_new_rating(r_a, r_b, score):
            return r_a + 32 * (score - get_expected_score(r_a, r_b))

        result_a = get_new_rating(rating_a, rating_b, result)
        result_b = get_new_rating(rating_b, rating_a, 1 - result)
        return result_a, result_b

    def update_elo(self, file, new_elo):
        print(file, new_elo)
        self.client.add_tags(
            file_ids=[file[0]],
            service_keys_to_actions_to_tags={
                self.tag_service: {
                    0: [f"elo:{int(new_elo)}"],
                    1: [f"elo:{int(file[1])}"],
                }
            },
        )
        file[1] = new_elo
        return file

    def win(self, result):
        left_new_elo, right_new_elo = self.play(self.left[1], self.right[1], result)
        self.left = self.update_elo(self.left, left_new_elo)
        self.right = self.update_elo(self.right, right_new_elo)
        if result == 1:
            self.new_queue.append(self.left)
        elif result == 0:
            self.new_queue.append(self.right)
        elif result == 0.5:
            self.new_queue.append(self.left)
            self.new_queue.append(self.right)
        if len(self.queue) < 2:
            if len(self.new_queue) > 1:
                self.queue = self.new_queue + self.queue
                self.new_queue = []
            else:
                self.queue = self.generate_queue()
                print("gen queue by win")
                return
        self.left = self.queue.pop()
        self.right = self.queue.pop()
        self.update_images()

    def open_collage(self):
        CollageDialog(self.client).exec()
