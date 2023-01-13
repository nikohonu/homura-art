import asyncio

from homura_art.apis.danbooru import Danbooru
from homura_art.apis.hydrus import Hydrus
from homura_art.database import (
    Post,
    PostSubscription,
    Source,
    Subscription,
    Tag,
    TagPost,
    TagType,
)

apis = {"Danbooru API": Danbooru, "Hydrus Network Client API": Hydrus}


async def sync_source(source, data: asyncio.Queue):
    print(source.api, "start")
    for subscription in (
        Subscription.select().join(Source).where(Subscription.source == source)
    ):
        api = apis[source.api](source)
        for post in await api.sync(subscription):
            await data.put((source, subscription, post))
    print(source.api, "end")



async def sync():
    data = asyncio.Queue()
    tasks = []
    for source in Source.select():
        tasks.append(asyncio.create_task(sync_source(source, data)))
    for task in tasks:
        await task
    print("Inserting in database")
    i = 0
    max_i = data.qsize()
    while not data.empty():
        if i % 10 == 0:
            print(i, max_i)
        i += 1
        so, su, raw_post = await data.get()
        post = Post.get_or_none(source=so, post_id=raw_post["id"])
        created = False
        if not post:
            post = Post.create(
                source=so,
                post_id=raw_post["id"],
                created=raw_post["created"],
                ext=raw_post["ext"],
            )
            created = True
        PostSubscription.get_or_create(post=post, subscription=su)
        if created:
            for splitted_tag in raw_post["tags"]:
                tag_type, _ = TagType.get_or_create(name=splitted_tag[0])
                tag, _ = Tag.get_or_create(tag_type=tag_type, name=splitted_tag[1])
                TagPost.create(post=post, tag=tag)
