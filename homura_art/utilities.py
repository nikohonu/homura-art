import hashlib
from pathlib import Path

import hydrus_api

from homura_art.model import Post, PostSubscription, Subscription


def get_hash(path: Path):
    """ "This function returns the SHA-256 hash
    of the file passed into it"""
    h = hashlib.sha256()
    with path.open("rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def process_hydrus_query(subscription):
    source = subscription.source
    have = (
        PostSubscription.select()
        .join(Post)
        .where(
            (PostSubscription.subscription == subscription)
            & (Post.filtered == False)
            & (Post.skiped == False)
        )
        .count()
    )
    if have >= 100:
        print(f"id:{subscription.id} {source.address} query:{subscription.query} | ok!")
        return
    client = hydrus_api.Client(source.key, source.address)
    ids = client.search_files([subscription.query])
    index = -1
    old = have
    while have < 100:
        index += 1
        id = ids[index]
        post, created = Post.get_or_create(index=id, source=source)
        if created:
            PostSubscription.create(post=post, subscription=subscription)
            have += 1
            continue
        if post.filtered:
            continue
        _, created = PostSubscription.get_or_create(
            post=post, subscription=subscription
        )
        if created:
            have += 1
    print(
        f"id:{subscription.id} {source.address} query:{subscription.query} | added {have-old} posts."
    )


def sync():
    for subscription in Subscription.select():
        match subscription.source.source_type:
            case "hydrus":
                process_hydrus_query(
                    subscription,
                )
            case _:
                print("Wrong source type!")
