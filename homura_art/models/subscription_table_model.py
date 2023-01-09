from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


class SubscriptionTableModel(QAbstractTableModel):
    def __init__(self, subscriptions: list) -> None:
        super().__init__()
        self.subscriptions = subscriptions
        self.headers = ["Id", "Query", "Source"]

    def rowCount(self, parent) -> int:
        return len(self.subscriptions)

    def columnCount(self, parent) -> int:
        return 3

    def data(self, index: QModelIndex, role):
        if role == Qt.ItemDataRole.DisplayRole:
            subscription = self.subscriptions[index.row()]
            return list(subscription.values())[index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]

    def _gen_new_id(self):
        if self.subscriptions:
            return max(s["id"] for s in self.subscriptions) + 1
        else:
            return 1

    def _get_row_by_id(self, index):
        subscription = next(filter(lambda x: x["id"] == index, self.subscriptions), None)
        return self.subscriptions.index(subscription) if subscription else None

    def get(self, row):
        return self.subscriptions[row]

    def add(self, subscription):
        index = self._gen_new_id()
        subscription["id"] = index
        self.subscriptions.append(subscription)
        self.layoutChanged.emit()

    def update(self, subscription):
        index = subscription["id"]
        row = self._get_row_by_id(index)
        self.subscriptions[row] = subscription
        self.layoutChanged.emit()

    def delete(self, row):
        del self.subscriptions[row]
        self.layoutChanged.emit()
