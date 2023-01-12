import asyncio
from urllib.parse import urljoin, urlparse

import hydrus_api

from homura_art.apis.api import API
from homura_art.database import Post, PostSubscription, Source, Subscription


class Hydrus(API):
    def __init__(self, source: Source) -> None:
        super().__init__(source)
        address = source.address
        if not source.address.startswith("http://"):
            address = "http://" + source.address
        self.api = hydrus_api.Client(access_key=self.source.key, api_url=address)

    def get_unified_post(self, raw_post):
        raw_tags = []
        for tags in list(raw_post["tags"].values())[0]["display_tags"].values():
            for tag in tags:
                raw_tags.append(tag.replace(" ", "_"))
        # for file_service in raw_post["file_services"].items():
        # print(file_service)
        return {"id": raw_post["file_id"], "ext": raw_post["ext"][1:], "tags": raw_tags}

    async def sync(self, subscription: Subscription):
        print(subscription.query, "start")
        existed_ids = {
            p.post_id
            for p in PostSubscription.select().where(
                PostSubscription.subscription == subscription
            )
        }
        query = [sub.replace("_", " ") for sub in subscription.query.split()]
        ids = self.api.search_files(query)
        result = []
        limit = 2
        # for i in range(len(ids) // 100 + 1):
        for i in range(1):
            new_ids = set(ids[i * limit : i * limit + limit])
            new_ids = list(new_ids.difference(existed_ids))
            if new_ids:
                result += [
                    self.get_unified_post(raw_post)
                    for raw_post in self.api.get_file_metadata(file_ids=new_ids)
                ]
            else:
                break
        print(len(result))
        print(result[0])
        print(subscription.query, "end")
        return ["test"]
