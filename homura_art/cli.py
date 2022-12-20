import click

# from homura_art.model import Post, PostSubscription, Source, Subscription
from homura_art.model import Post, PostSubscription, Source, Subscription
from peewee import IntegrityError
import hydrus_api


@click.group()
def cli():
    pass


@click.command()
@click.argument("address")
@click.option(
    "-k",
    "--key",
    help="Api key of the source.",
    type=str,
)
@click.option(
    "-t",
    "--type",
    "source_type",
    help="Type of the source.",
    type=click.Choice(["hydrus"]),
    required=True,
)
def source_add(address, key, source_type):
    require_key = ["hydrus"]
    if source_type in require_key and not key:
        print(
            "This source type requires a key. Use '-k'/'--key' to set the source key."
        )
    try:
        Source.create(address=address, key=key, source_type=source_type)
    except IntegrityError:
        print("This source already exists!")


@click.command()
def source_list():
    for source in Source.select():
        print(f"id:{source.id} {source.address} type:{source.source_type}")


@click.command()
@click.argument("query")
@click.option(
    "-s",
    "--source",
    help="Id of the source.",
    type=click.Choice([str(s.id) for s in Source.select()]),
    required=True,
)
def subscription_add(query, source):
    source = Source.get_by_id(int(source))
    Subscription.create(source=source, query=query)


@click.command()
def subscription_list():
    for subscription in Subscription.select():
        print(
            f"id:{subscription.id} {subscription.source.address} query:{subscription.query}"
        )


def process_hydrus_tags(post):
    pass


def process_hydrus_query(subscription):
    source = subscription.source
    have = (
        PostSubscription.select()
        .join(Post)
        .where((PostSubscription.subscription == subscription) & (Post.saved == False))
        .count()
    )
    if have >= 100:
        print(
            f"id:{subscription.id} {source.address} query:{subscription.query} is ok!"
        )
        return
    client = hydrus_api.Client(source.key, source.address)
    ids = client.search_files([subscription.query])
    index = -1
    while have < 100:
        index += 1
        id = ids[index]
        post, created = Post.get_or_create(index=id, source=source)
        if created:
            PostSubscription.create(post=post, subscription=subscription)
            have += 1
        if post.saved:
            continue
        _, created = PostSubscription.get_or_create(
            post=post, subscription=subscription
        )
        if created:
            have += 1


@click.command()
def subscription_sync():
    for subscription in Subscription.select():
        match subscription.source.source_type:
            case "hydrus":
                process_hydrus_query(
                    subscription,
                )
            case _:
                print("Wrong source type!")


cli.add_command(source_add)
cli.add_command(source_list)
cli.add_command(subscription_add)
cli.add_command(subscription_list)
cli.add_command(subscription_sync)


def main():
    cli()


if __name__ == "__main__":
    main()
