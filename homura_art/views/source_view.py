from PySide6.QtWidgets import QDialog

from homura_art.models.source_table_model import SourceTableModel
from homura_art.views.source_add_edit_view import SourceAddEditView
from homura_art.views.ui.source_view import Ui_SourceView


class SourceView(QDialog, Ui_SourceView):
    def __init__(self, sources: list = []) -> None:
        super().__init__()
        self.setupUi(self)
        self.model = SourceTableModel(sources)
        self.view.setModel(self.model)
        self.action_add.triggered.connect(self.add)
        self.action_edit.triggered.connect(self.edit)
        self.action_delete.triggered.connect(self.delete)

    def add(self):
        source_add_view = SourceAddEditView()
        if source_add_view.exec():
            source = source_add_view.result()
            self.model.add(source)

    def get_selected_row(self):
        selected_rows = self.view.selectionModel().selectedRows()
        if selected_rows:
            return selected_rows[0].row()

    def edit(self):
        row = self.get_selected_row()
        if row != None:
            source = self.model.get(row)
            source_edit_view = SourceAddEditView(source, "Edit source")
            if source_edit_view.exec():
                source = source_edit_view.result()
                self.model.update(source)

    def delete(self):
        row = self.get_selected_row()
        if row != None:
            self.model.delete(row)

    def result(self):
        return self.model.sources
