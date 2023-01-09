from PySide6.QtGui import QValidator
from PySide6.QtWidgets import QDialog

from homura_art.apis import apis
from homura_art.database import Source
from homura_art.views.ui.subscription_add_edit_view import Ui_SubscriptionAddEditView

sources = [source.address for source in Source.select()]


class SubscriptionAddEditView(QDialog, Ui_SubscriptionAddEditView):
    def __init__(self, subscription: dict = None, window_title="New subscription") -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(window_title)
        self.combo_box_source.addItems(sources)
        self.subscription_id = self.load(subscription)

    def load(self, subscription):
        if subscription:
            self.edit_query.setText(subscription["query"])
            self.combo_box_source.setCurrentText(subscription["source"])
            return subscription["id"]

    def result(self):
        return {
            "id": self.subscription_id,
            "query": self.edit_query.text(),
            "source": self.combo_box_source.currentText(),
        }
