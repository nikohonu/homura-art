import datetime as dt
import random
import shutil
import subprocess
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QImageReader, QKeySequence, QPixmap, QResizeEvent, QShortcut
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

from homura_art.model import File, FilePost, Post
from homura_art.ui.collage_preview import Ui_CollagePreview
from homura_art.ui.main_window import Ui_MainWindow
from homura_art.utilities import get_hash, sync


class CollagePreview(QDialog, Ui_CollagePreview):
    def __init__(self) -> None:
        super(CollagePreview, self).__init__()
        self.setupUi(self)
        self.image = QPixmap("/tmp/collage.png")
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)

    def repaint(self):
        w = self.file.width()
        h = self.file.height()
        self.file.setPixmap(
            self.image.scaled(w, h, aspectMode=Qt.AspectRatioMode.KeepAspectRatio)
        )

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.repaint()
        return super().resizeEvent(event)


class MainWindow(QMainWindow, Ui_MainWindow):
    def generate_queue(self):
        queue = []
        posts = list(
            Post.select().where((Post.filtered == False) & (Post.skiped == False))
        )
        if len(posts) < 24:
            sync()
            posts = list(Post.select().where(Post.filtered == False))
        files = list(File.select())
        random.shuffle(files)
        if len(posts) < 24:
            need = min(32 - len(posts), len(files))
        else:
            need = 8
        while files:
            file = files.pop()
            queue.append({"path": file.path, "type": "file", "file": file})
            print(len(queue), need)
            if len(queue) == need:
                break
        # post
        random.shuffle(posts)
        # files
        while posts:
            post = posts.pop()
            path = post.path
            if not path:
                post.skiped = True
                post.save()
                continue
            queue.append({"path": post.path, "type": "post", "post": post})
            if len(queue) == 32:
                break
        random.shuffle(queue)
        return queue

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.new_queue = []
        self.queue = self.generate_queue()
        self.left = self.queue.pop()
        self.right = self.queue.pop()
        self.left_image = QPixmap(self.left["path"])
        self.right_image = QPixmap(self.right["path"])

        self.shortcut_left_win = QShortcut(QKeySequence("A"), self)
        self.shortcut_right_win = QShortcut(QKeySequence("D"), self)
        self.shortcut_tie = QShortcut(QKeySequence("W"), self)
        self.shortcut_delete_left = QShortcut(QKeySequence("Q"), self)
        self.shortcut_delete_right = QShortcut(QKeySequence("E"), self)
        self.shortcut_collage_button = QShortcut(QKeySequence("S"), self)

        self.shortcut_left_win.activated.connect(self.left_win)
        self.shortcut_right_win.activated.connect(self.right_win)
        self.shortcut_tie.activated.connect(self.tie)
        self.shortcut_delete_left.activated.connect(self.delete_left)
        self.shortcut_delete_right.activated.connect(self.delete_right)
        self.shortcut_collage_button.activated.connect(self.get_collage)

        self.left_win_button.clicked.connect(self.left_win)
        self.right_win_button.clicked.connect(self.right_win)
        self.tie_button.clicked.connect(self.tie)
        self.delete_left_button.clicked.connect(self.delete_left)
        self.delete_right_button.clicked.connect(self.delete_right)
        self.collage_button.clicked.connect(self.get_collage)

    def delete(self, item):
        if item["type"] == "post":
            item["post"].filtered = True
            item["post"].save()
        if item["type"] == "file":
            item["file"].delete_instance(recursive=True)
        if not self.queue:
            if len(self.new_queue) >= 2:
                self.queue = self.new_queue
                self.new_queue = []
            else:
                self.queue = self.generate_queue()
            print("queue:", len(self.queue), "new queue:", len(self.new_queue))
        item = self.queue.pop()
        print("queue:", len(self.queue), "new queue:", len(self.new_queue))
        return item

    def delete_left(self):
        self.left = self.delete(self.left)
        self.left_image = QPixmap(self.left["path"])
        self.repaint()

    def delete_right(self):
        self.right = self.delete(self.right)
        self.right_image = QPixmap(self.right["path"])
        self.repaint()

    def archive(self, item):
        if item["type"] == "file":
            return item
        else:
            hash = get_hash(item["path"])
            file = File.get_or_none(File.hash == hash)
            post = item["post"]
            if file:
                FilePost.create(file=file, post=post)
            else:
                path = item["path"]
                file = File.create(hash=hash, ext=path.suffix)
                new_path = file.path
                new_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(path, new_path, copy_function=shutil.copy2)
                FilePost.create(file=file, post=post)
            post.filtered = True
            post.save()
            return {"path": file.path, "type": "file", "file": file}

    def play(self, rating_a, rating_b, result):
        def get_expected_score(r_a, r_b):
            return 1 / (1 + 10 ** ((r_a - r_b) / 400))

        def get_new_rating(r_a, r_b, score):
            return r_a + 32 * (score - get_expected_score(r_a, r_b))

        result_a = get_new_rating(rating_a, rating_b, result)
        result_b = get_new_rating(rating_b, rating_a, 1 - result)
        return result_a, result_b

    def win(self, result):
        self.left = self.archive(self.left)
        self.right = self.archive(self.right)
        if result == 1:
            self.new_queue.append(self.left)
        elif result == 0:
            self.new_queue.append(self.right)
        self.left["file"].rating, self.right["file"].rating = self.play(
            self.left["file"].rating, self.right["file"].rating, result
        )
        self.left["file"].save()
        self.right["file"].save()
        if len(self.queue) < 2:
            if len(self.new_queue) > 1:
                self.queue = self.new_queue + self.queue
                self.new_queue = []
            else:
                self.queue = self.generate_queue()
        print("queue:", len(self.queue), "new queue:", len(self.new_queue))
        self.left = self.queue.pop()
        self.right = self.queue.pop()
        self.left_image = QPixmap(self.left["path"])
        self.right_image = QPixmap(self.right["path"])
        self.repaint()

    def left_win(self):
        self.win(1)

    def right_win(self):
        self.win(0)

    def tie(self):
        self.win(0.5)

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

    def get_collage(self):
        files = list(
            File.select()
            .where(File.used == False)
            .order_by(File.rating.desc())
            .limit(16)
        )
        files = random.sample(files, 3)
        paths = [str(file.path) for file in files]
        cmd = f"montage {' '.join(paths)} -geometry x1080 -mode Concatenate /tmp/collage.png"

        subprocess.call(cmd, shell=True)

        if CollagePreview().exec():
            for file in files:
                file.used = True
                file.used_time = dt.datetime.now()
                file.save()
        else:
            print("Cancel!")


def main():
    QImageReader.setAllocationLimit(0)
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    widget.resize(1025, 768)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
