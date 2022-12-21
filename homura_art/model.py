from pathlib import Path
import shutil

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
import hydrus_api


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
    hash = TextField(unique=True)
    import_time = DateTimeField(default=dt.datetime.now())
    rating = IntegerField(default=1000)
    used = BooleanField(default=False)
    used_time = DateTimeField(null=True)
    ext = TextField()

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


class Subscription(BaseModel):
    source = ForeignKeyField(Source, backref="subscriptions")
    query = TextField()


class Post(BaseModel):
    source = ForeignKeyField(Source, backref="posts")
    index = IntegerField()
    filtered = BooleanField(default=False)

    @property
    def path(self):
        source = self.source
        match source.source_type:
            case "hydrus":
                client = hydrus_api.Client(source.key, source.address)
                allowed_ext = [".png", ".jpg", ".webp"]
                ext = client.get_file_metadata(file_ids=[self.index])[0]["ext"]
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
                return Path
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


models = BaseModel.__subclasses__()
database.create_tables(models)
