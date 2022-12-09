from pathlib import Path

from appdirs import user_data_dir
from peewee import (BlobField, BooleanField, DateField, DateTimeField,
                    ForeignKeyField, IntegerField, Model, SqliteDatabase,
                    TextField, TimestampField, UUIDField)


def get_user_data_dir():
    return Path(user_data_dir("homura-art", "Niko Honu"))


database_path = get_user_data_dir() / "data.db"
database_path.parent.mkdir(parents=True, exist_ok=True)
database = SqliteDatabase(database_path, pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta:
        database = database


class Art(BaseModel):
    hash = BlobField()
    import_time = TimestampField()
    rating = IntegerField(default=1000)
    used = BooleanField(default=False)
