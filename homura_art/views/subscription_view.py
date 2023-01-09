from PySide6.QtWidgets import QDialog

from homura_art.models.subscription_table_model import SubscriptionTableModel
from homura_art.views.subscription_add_edit_view import SubscriptionAddEditView
from homura_art.views.ui.subscription_view import Ui_SubscriptionView


class SubscriptionView(QDialog, Ui_SubscriptionView):
    def __init__(self, subscriptions: list = []) -> None:
        super().__init__()
        self.setupUi(self)
        self.model = SubscriptionTableModel(subscriptions)
        self.view.setModel(self.model)
        self.action_add.triggered.connect(self.add)
        self.action_edit.triggered.connect(self.edit)
        self.action_delete.triggered.connect(self.delete)

    def add(self):
        subscription_add_view = SubscriptionAddEditView()
        if subscription_add_view.exec():
            subscription = subscription_add_view.result()
            self.model.add(subscription)

    def get_selected_row(self):
        selected_rows = self.view.selectionModel().selectedRows()
        if selected_rows:
            return selected_rows[0].row()

    def edit(self):
        row = self.get_selected_row()
        if row != None:
            subscription = self.model.get(row)
            subscription_edit_view = SubscriptionAddEditView(
                subscription, "Edit subscription"
            )
            if subscription_edit_view.exec():
                subscription = subscription_edit_view.result()
                self.model.update(subscription)

    def delete(self):
        row = self.get_selected_row()
        if row != None:
            self.model.delete(row)

    def result(self):
        return self.model.subscriptions
