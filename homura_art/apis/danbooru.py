import asyncio

import booru

from homura_art.apis.api import API
from homura_art.database import Subscription


class Danbooru(API):
    def __init__(self, source) -> None:
        super().__init__(source)
        self.api = booru.Danbooru(api_key=self.source.key, login=self.source.login)

    def get_unified_post(self, raw_post):
        return {}

    async def sync(self, subscription: Subscription):
        print(subscription.query, "start")
        # await asyncio.sleep(2)
        # result = await self.api.search(subscription.query, limit=1)
        # print(booru.resolve(result)[0])
        print(subscription.query, "end")
        return ["test2"]
