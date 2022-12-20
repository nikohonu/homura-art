from pathlib import Path

from appdirs import user_data_dir
from peewee import (
    BooleanField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
    TimestampField,
    CompositeKey,
)
import datetime as dt


def get_user_data_dir():
    return Path(user_data_dir("homura-art", "Niko Honu"))


database_path = get_user_data_dir() / "data.db"
database_path.parent.mkdir(parents=True, exist_ok=True)
database = SqliteDatabase(database_path, pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta:
        database = database


class Namespace(BaseModel):
    name = TextField(unique=True)


class Subtag(BaseModel):
    name = TextField(unique=True)


class Tag(BaseModel):
    namespace = ForeignKeyField(Namespace, backref="tags")
    subtag = ForeignKeyField(Subtag, backref="tags")
    rating = IntegerField(default=1000)

    class Meta:
        indexes = ((("namespace", "subtag"), True),)


class File(BaseModel):
    hash = TextField()
    import_time = DateTimeField(default=dt.datetime.now())
    rating = IntegerField(default=1000)
    used = BooleanField(default=False)
    used_time = TimestampField(null=True)


class FileTag(BaseModel):
    file = ForeignKeyField(File, backref="file_tags")
    tag = ForeignKeyField(Tag, backref="files_tag")

    class Meta:
        primary_key = CompositeKey("file", "tag")


class Source(BaseModel):
    address = TextField(unique=True)
    key = TextField(null=True)
    source_type = TextField()


class Subscription(BaseModel):
    source = ForeignKeyField(Source, backref="subscriptions")
    query = TextField()


class Post(BaseModel):
    source = ForeignKeyField(Source, backref="posts")
    index = IntegerField()
    saved = BooleanField(default=False)

    class Meta:
        indexes = ((("source", "index"), True),)


class PostTag(BaseModel):
    post = ForeignKeyField(Post, backref="post_tags")
    tag = ForeignKeyField(Tag, backref="posts_tag")

    class Meta:
        primary_key = CompositeKey("post", "tag")


class FilePost(BaseModel):
    file = ForeignKeyField(File, backref="file_posts")
    post = ForeignKeyField(Post, backref="files_post")

    class Meta:
        primary_key = CompositeKey("file", "post")


class PostSubscription(BaseModel):
    post = ForeignKeyField(Post, backref="post_subscriptions")
    subscription = ForeignKeyField(Subscription, backref="posts_subscription")

    class Meta:
        primary_key = CompositeKey("post", "subscription")


models = BaseModel.__subclasses__()
database.create_tables(models)
