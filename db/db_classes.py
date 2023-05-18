from peewee import CharField, Model

from db.db_init import database


class BaseModel(Model):
    class Meta:
        database = database


class Report(BaseModel):
    abbr = CharField(primary_key=True)
    name = CharField()
    car = CharField()
    start_time = CharField()
    end_time = CharField()
    lap_time = CharField()
