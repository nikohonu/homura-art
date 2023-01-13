import datetime as dt
import time

import pytz
from dateutil import parser
from PIL import Image, ImageQt
from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt

from homura_art.database import Post, Tag, TagPost, TagType


class PostListModel(QAbstractListModel):
    def get_post_title(self, post):
        created = parser.parse(post.created)
        if not created.tzinfo:
            created = pytz.utc.localize(created, is_dst=None).astimezone(
                pytz.timezone(time.tzname[0])
            )
        return created.strftime("%Y-%M-%d %H:%M")

    def image_to_pixmap(self, file):
        image = Image.open(file)
        return ImageQt.toqpixmap(image)

    def __init__(self) -> None:
        self.posts = (
            Post.select()
            .where((Post.filtred == False) & (Post.ext << ["jpg", "png", "webp"]))
            .order_by(Post.created.desc())
            .limit(102)
        )
        self.posts_title = [self.get_post_title(post) for post in self.posts]
        self.posts_thumbnails = [
            self.image_to_pixmap(post.get_thumbnail_path()) for post in self.posts
        ]
        print(self.posts_thumbnails)
        super().__init__()

    def rowCount(self, parent) -> int:
        return self.posts.count()

    def data(self, index: QModelIndex, role: int):
        if role == Qt.DecorationRole:
            return self.posts_thumbnails[index.row()]
        if role == Qt.DisplayRole:
            return self.posts_title[index.row()]


#     self.sources = sources
#     self.headers = ["Id", "Address", "API", "Login", "Key"]
#
# def rowCount(self, parent) -> int:
#     return len(self.sources)
#
# def columnCount(self, parent) -> int:
#     return 5
#
# def data(self, index: QModelIndex, role):
#     if role == Qt.ItemDataRole.DisplayRole:
#         source = self.sources[index.row()]
#         return list(source.values())[index.column()]
#
# def headerData(self, section, orientation, role):
#     if role == Qt.ItemDataRole.DisplayRole:
#         if orientation == Qt.Horizontal:
#             return self.headers[section]
#
# def _gen_new_id(self):
#     if self.sources:
#         return max(s["id"] for s in self.sources) + 1
#     else:
#         return 1
#
# def _get_row_by_id(self, index):
#     source = next(filter(lambda x: x["id"] == index, self.sources), None)
#     return self.sources.index(source) if source else None
#
# def get(self, row):
#     return self.sources[row]
#
# def add(self, source):
#     index = self._gen_new_id()
#     source["id"] = index
#     self.sources.append(source)
#     self.layoutChanged.emit()
#
# def update(self, source):
#     index = source["id"]
#     row = self._get_row_by_id(index)
#     self.sources[row] = source
#     self.layoutChanged.emit()
#
# def delete(self, row):
#     del self.sources[row]
#     self.layoutChanged.emit()
