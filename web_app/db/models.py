from dataclasses import dataclass
from datetime import datetime
from typing import Type

from peewee import CharField, Model
from task_6 import Driver

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


class ReportRepository:

    @property
    def model(self) -> Type[Report]:
        return Report

    def get_all_drivers(self, order: bool) -> list[Driver] | None:
        if not order:
            sorted_report = self.model.select().order_by(self.model.lap_time.asc())
        else:
            sorted_report = self.model.select().order_by(self.model.lap_time.desc())
        return sorted_report

    def get_one_driver(self, driver_abbr: str) -> Driver | None:
        for driver in self.model.select():
            if driver.abbr == driver_abbr:
                return driver
        return None


@dataclass
class ExtendedDriver:
    abbr: str
    driver_name: str
    car: str
    start_time: datetime
    end_time: datetime
    lap_time: str

    @classmethod
    def from_peewee_obj(cls, driver: Driver):
        return cls(
            abbr=driver.abbr,
            driver_name=driver.name,
            car=driver.car,
            start_time=driver.start_time,
            end_time=driver.end_time,
            lap_time=driver.lap_time
        )


@dataclass
class ShortDriver:
    abbr: str
    driver_name: str
    lap_time: str

    @classmethod
    def from_peewee_obj(cls, driver: Driver):
        return cls(
            abbr=driver.abbr,
            driver_name=driver.name,
            lap_time=driver.lap_time,
        )
