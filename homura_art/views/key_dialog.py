from appdirs import user_config_dir
from hydrus_api import Client
from PySide6.QtWidgets import QDialog, QMainWindow

from homura_art.views.ui.key_dialog import Ui_KeyDialog


class KeyDialog(QDialog, Ui_KeyDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
