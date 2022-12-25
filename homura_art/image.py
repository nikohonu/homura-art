from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QGuiApplication, QPixmap, QScreen

from homura_art.model import File


def calc_resize_by_height(old_size, height):
    old_width, old_height = old_size
    width = (old_width * height) // old_height
    return width, height


def calc_resize_by_width(old_size, width):
    old_width, old_height = old_size
    height = (old_height * width) // old_width
    return width, height


def make_collage(files: list, any_collage_width=False):
    screen_width, screen_height = QGuiApplication.screens()[0].size().toTuple()
    images = []
    shift = 0
    collage_width = 0
    for image in [Image.open(file.path) for file in files]:
        size = calc_resize_by_height(image.size, screen_height)
        width, _ = size
        images.append((image, size, shift))
        shift += width
        collage_width += width
    if not any_collage_width and collage_width > screen_width * 1.5:
        return None
    collage = Image.new("RGB", (collage_width, screen_height), (255, 255, 255))
    for image, size, shift in images:
        collage.paste(image.resize(size, Image.LANCZOS), (shift, 0))
    return QPixmap.fromImage(
        ImageQt(
            collage.resize(
                calc_resize_by_width(collage.size, screen_width), Image.LANCZOS
            )
        )
    )
