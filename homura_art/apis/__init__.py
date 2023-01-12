import asyncio

from homura_art.apis.danbooru import Danbooru
from homura_art.apis.hydrus import Hydrus
from homura_art.database import Source, Subscription

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
    while not data.empty():
        su, so, post = await data.get()
        print(su.api, so.query, post)
