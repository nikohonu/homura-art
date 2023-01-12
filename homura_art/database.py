import datetime as dt
import shutil
from pathlib import Path

import hydrus_api
from appdirs import user_data_dir
from peewee import (
    BooleanField,
    CompositeKey,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
    TimestampField,
)
from playhouse.sqlite_ext import JSONField


def get_user_data_dir():
    return Path(user_data_dir("homura-art", "Niko Honu"))


database_path = get_user_data_dir() / "database.db"
database_path.parent.mkdir(parents=True, exist_ok=True)
database = SqliteDatabase(database_path, pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta:
        database = database


class Source(BaseModel):
    address = TextField(null=True)
    api = TextField()
    login = TextField(null=True)
    key = TextField(null=True)


class Subscription(BaseModel):
    query = TextField()
    source = ForeignKeyField(Source, backref="subscriptions")


class Post(BaseModel):
    ext = TextField()
    source = ForeignKeyField(Source)
    post_id = IntegerField(null=False)
    archived = BooleanField(default=False)


class PostSubscription(BaseModel):
    post = ForeignKeyField(Post)
    subscription = ForeignKeyField(Subscription)

    class Meta:
        indexes = ((("post", "subscription"), True),)


class TagType(BaseModel):
    name = TextField()


class Tag(BaseModel):
    tag_type = ForeignKeyField(TagType)
    name = TextField()


class TagPost(BaseModel):
    post = ForeignKeyField(Post)
    tag = ForeignKeyField(Tag)

    class Meta:
        indexes = ((("post", "tag"), True),)


# class Post()

"""
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
    hash = TextField(unique=True)
    import_time = DateTimeField(default=dt.datetime.now())
    rating = IntegerField(default=1000)
    used = BooleanField(default=False)
    used_time = DateTimeField(null=True)
    ext = TextField()
    safe_rating = IntegerField(null=True)

    @property
    def path(self):
        return get_user_data_dir() / self.hash[:3] / f"{self.hash}{self.ext}"


class FileTag(BaseModel):
    file = ForeignKeyField(File, backref="file_tags")
    tag = ForeignKeyField(Tag, backref="files_tag")

    class Meta:
        primary_key = CompositeKey("file", "tag")


class Source(BaseModel):
    address = TextField(unique=True)
    key = TextField(null=True)
    source_type = TextField()

class Post(BaseModel):
    source = ForeignKeyField(Source, backref="posts")
    index = IntegerField()
    filtered = BooleanField(default=False)
    skiped = BooleanField(default=False)

    @property
    def path(self):
        source = self.source
        match source.source_type:
            case "hydrus":
                client = hydrus_api.Client(source.key, source.address)
                allowed_ext = [".png", ".jpg", ".webp"]
                try:
                    data = client.get_file_metadata(file_ids=[self.index])[0]
                    if data["file_services"]["deleted"]:
                        raise Exception("Fix this, model.py")
                        self.skiped = True
                        self.save()
                        return ""
                    ext = data["ext"]
                except hydrus_api.ConnectionError:
                    raise ConnectionError()
                if ext not in allowed_ext:
                    return ""
                tmp_path = Path("/tmp/homura-art")
                tmp_path.mkdir(exist_ok=True)
                path = tmp_path / f"{self.source.id}-{self.index}{ext}"
                if path.exists():
                    return path
                response = client.get_file(file_id=self.index)
                with open(path, "wb") as file:
                    shutil.copyfileobj(response.raw, file)
                return path
            case _:
                return ""

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


def get_file_path(hash, ext):
    return get_user_data_dir() / hash[:3] / f"{hash}"


class Log(BaseModel):
    action = TextField()
    data = JSONField()
"""

models = BaseModel.__subclasses__()
database.create_tables(models)
