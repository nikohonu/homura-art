from PySide6.QtGui import QValidator
from PySide6.QtWidgets import QDialog

from homura_art.apis import apis
from homura_art.views.ui.source_add_edit_view import Ui_SourceAddEditView


class SourceAddEditView(QDialog, Ui_SourceAddEditView):
    def __init__(self, source: dict = None, window_title="New source") -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(window_title)
        self.combo_box_api.addItems(list(apis.keys()))
        self.source_id = self.load(source)

    def load(self, source):
        if source:
            self.edit_address.setText(source["address"])
            self.combo_box_api.setCurrentText(source["api"])
            self.edit_key.setText(source["key"])
            return source["id"]

    def result(self):
        return {
            "id": self.source_id,
            "address": self.edit_address.text(),
            "api": self.combo_box_api.currentText(),
            "key": self.edit_key.text(),
        }
