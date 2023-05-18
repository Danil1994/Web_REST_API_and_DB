from peewee import CharField, Model

from web_app.db.db_init import database


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


ALL_MODELS = [Report]
