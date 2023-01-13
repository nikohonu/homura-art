import asyncio
import datetime as dt
from urllib.parse import urljoin, urlparse

import hydrus_api

from homura_art.apis.api import API
from homura_art.database import (
    Post,
    PostSubscription,
    Source,
    Subscription,
    get_user_data_dir,
)


class Hydrus(API):
    def __init__(self, source: Source) -> None:
        super().__init__(source)
        address = source.address
        if not source.address.startswith("http://"):
            address = "http://" + source.address
        self.api = hydrus_api.Client(access_key=self.source.key, api_url=address)

    def get_unified_post(self, raw_post):
        created = list(raw_post["file_services"]["current"].values())[0][
            "time_imported"
        ]
        created = dt.datetime.fromtimestamp(created, dt.timezone.utc)
        raw_tags = []
        for tags in list(raw_post["tags"].values())[0]["display_tags"].values():
            for tag in tags:
                raw_tags.append(tag)
        tags = []
        for tag in raw_tags:
            tag = tag.replace(" ", "_")
            splitted_tag: list = tag.split(":")
            if len(splitted_tag) == 1:
                splitted_tag.insert(0, "")
            else:
                new_splitted_tag = []
                new_splitted_tag.append(splitted_tag[0])
                new_splitted_tag.append(":".join(splitted_tag[1:]))
                splitted_tag = new_splitted_tag
            tags.append(splitted_tag)

        return {
            "id": raw_post["file_id"],
            "created": created,
            "ext": raw_post["ext"][1:],
            "url": None,
            "tags": tags,
        }

    def search(self, query, page):
        print(query, ", page: ", page, sep="")
        query = [sub.replace("_", " ") for sub in query.split()]
        ids = self.api.search_files(query)
        limit = 100
        return [
            self.get_unified_post(post)
            for post in self.api.get_file_metadata(
                file_ids=ids[page * limit : page * limit + 100]
            )
        ]

    async def sync(self, subscription: Subscription):
        ps = (
            PostSubscription.select()
            .join(Post)
            .where(PostSubscription.subscription == subscription)
        )
        ps_not_filtred = ps.where(Post.filtred == False)
        existed_ids = [row.post.post_id for row in ps]
        have = ps_not_filtred.count()
        target = 100
        need = target - have
        page = 0
        result = []
        if need:
            while len(result) < need:
                raw_result = self.search(subscription.query, page)
                for post in raw_result:
                    if post["id"] not in existed_ids:
                        result.append(post)
                page += 1
        cache_dir = get_user_data_dir() / "cache" / str(subscription.source.id)
        cache_dir.mkdir(parents=True, exist_ok=True)
        for post in result:
            path = cache_dir / (str(post["id"]) + "." + post["ext"])
            if not path.exists():
                with open(path, "wb") as file:
                    file.write(self.api.get_file(file_id=post["id"]).content)
        return result
