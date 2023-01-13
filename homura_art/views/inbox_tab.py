from PySide6.QtWidgets import QWidget

from homura_art.models.post_list_model import PostListModel
from homura_art.views.ui.inbox_tab import Ui_InboxTab


class InboxTab(QWidget, Ui_InboxTab):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.model = PostListModel()
        self.view.setModel(self.model)
