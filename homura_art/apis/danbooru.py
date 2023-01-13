import asyncio
import shutil

import booru
from dateutil import parser
from hydrus_api import requests

from homura_art.apis.api import API
from homura_art.database import Post, PostSubscription, Subscription, get_user_data_dir


class Danbooru(API):
    def __init__(self, source) -> None:
        super().__init__(source)
        self.api = booru.Danbooru(api_key=self.source.key, login=self.source.login)

    def get_unified_post(self, raw_post):
        tags = []
        tags.append(["rating", raw_post["rating"]])
        for tag in raw_post["tag_string_general"].split():
            tags.append(["", tag])
        for tag in raw_post["tag_string_artist"].split():
            tags.append(["creator", tag])
        for tag in raw_post["tag_string_character"].split():
            tags.append(["character", tag])
        for tag in raw_post["tag_string_copyright"].split():
            tags.append(["series", tag])
        for tag in raw_post["tag_string_meta"].split():
            tags.append(["meta", tag])
        if "file_url" not in raw_post:
            return {}
        return {
            "id": raw_post["id"],
            "created": parser.parse(raw_post["created_at"]),
            "ext": raw_post["file_ext"],
            "tags": tags,
            "url": raw_post["file_url"],
        }

    async def search(self, query, page=0):
        print(query, ", page: ", page, sep="")
        response = await self.api.search(query, limit=100, page=page + 1)
        result = []
        for raw_post in booru.resolve(response):
            post = self.get_unified_post(raw_post)
            if post:
                result.append(post)
        return result

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
                raw_result = await self.search(subscription.query, page)
                for post in raw_result:
                    if post["id"] not in existed_ids:
                        result.append(post)
                page += 1
        cache_dir = get_user_data_dir() / "cache" / str(subscription.source.id)
        cache_dir.mkdir(parents=True, exist_ok=True)
        for post in result:
            path = cache_dir / (str(post["id"]) + "." + post["ext"])
            headers = {"User-Agent": "Homura Art"}
            response = requests.get(
                post["url"],
                headers=headers,
                stream=True,
            )
            if not path.exists():
                with path.open("wb") as file:
                    file.write(response.content)
                await asyncio.sleep(0.5)
        return result
