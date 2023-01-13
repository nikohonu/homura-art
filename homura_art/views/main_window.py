import asyncio

from PySide6.QtWidgets import QMainWindow

import homura_art.apis as apis
from homura_art.database import Source, Subscription
from homura_art.views.inbox_tab import InboxTab
from homura_art.views.source_view import SourceView
from homura_art.views.subscription_view import SubscriptionView
from homura_art.views.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.action_manage_sources.triggered.connect(self.manage_sources)
        self.action_manage_subscriptions.triggered.connect(self.manage_subscription)
        self.action_sync.triggered.connect(self.sync)
        self.tab_widget.addTab(InboxTab(), "Inbox")

    def manage_sources(self):
        sources = [
            {
                "id": source.id,
                "address": source.address,
                "api": source.api,
                "login": source.login,
                "key": source.key,
            }
            for source in Source.select()
        ]
        source_view = SourceView(sources)
        if source_view.exec():
            sources = source_view.result()
        else:
            return
        for s in sources:
            source = Source.get_or_none(Source.id == s["id"])
            if not source:
                source = Source.create(
                    id=s["id"],
                    address=s["address"],
                    api=s["api"],
                    login=s["login"],
                    key=s["key"],
                )
            else:
                source.address = s["address"]
                source.api = s["api"]
                source.login = s["login"]
                source.key = s["key"]
                source.save()

    def manage_subscription(self):
        subscriptions = [
            {
                "id": subscription.id,
                "query": subscription.query,
                "source": subscription.source.id,
            }
            for subscription in Subscription.select().join(Source)
        ]
        subscription_view = SubscriptionView(subscriptions)
        if subscription_view.exec():
            sources = subscription_view.result()
        else:
            return
        for s in subscriptions:
            subscription = Subscription.get_or_none(Subscription.id == s["id"])
            if not subscription:
                subscription = Subscription.create(
                    id=s["id"],
                    query=s["query"],
                    source=Source.get_by_id(s["source"]),
                )
            else:
                subscription.query = s["query"]
                subscription.source = Source.get_by_id(s["source"])
                subscription.save()

    def sync(self):
        asyncio.run(apis.sync())
