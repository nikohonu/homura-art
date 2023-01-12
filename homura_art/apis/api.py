from homura_art.database import Source, Subscription


class API:
    def __init__(self, source: Source) -> None:
        self.source = source
        self.sub_limit = 100

    async def sync(self, suscription: Subscription):
        pass
