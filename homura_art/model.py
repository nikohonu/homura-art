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


class File(BaseModel):
    hash = BlobField(unique=True)
    import_time = TimestampField(null=True)
    rating = IntegerField(default=1000)
    used = BooleanField(default=False)

    @property
    def hash_str(self):
        return f"{int.from_bytes(self.hash, 'little'):064x}"

models = BaseModel.__subclasses__()
database.create_tables(models)
