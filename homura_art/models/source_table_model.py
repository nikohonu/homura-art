from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class SourceTableModel(QAbstractTableModel):
    def __init__(self, sources: list) -> None:
        super().__init__()
        self.sources = sources
        self.headers = ["Id", "Address", "API", "Key"]

    def rowCount(self, parent) -> int:
        return len(self.sources)

    def columnCount(self, parent) -> int:
        return 4

    def data(self, index: QModelIndex, role):
        if role == Qt.ItemDataRole.DisplayRole:
            source = self.sources[index.row()]
            return list(source.values())[index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]

    def _gen_new_id(self):
        if self.sources:
            return max(s["id"] for s in self.sources) + 1
        else:
            return 1

    def _get_row_by_id(self, index):
        source = next(filter(lambda x: x["id"] == index, self.sources), None)
        return self.sources.index(source) if source else None

    def get(self, row):
        return self.sources[row]

    def add(self, source):
        index = self._gen_new_id()
        source["id"] = index
        self.sources.append(source)
        self.layoutChanged.emit()

    def update(self, source):
        index = source["id"]
        row = self._get_row_by_id(index)
        self.sources[row] = source
        self.layoutChanged.emit()

    def delete(self, row):
        del self.sources[row]
        self.layoutChanged.emit()
