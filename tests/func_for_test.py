import unittest
from datetime import datetime
from typing import Any

from faker import Faker
from flask import json
from peewee import SqliteDatabase
from task_6 import time_format

from web_app.data_transformation_func import Driver
from web_app.db.models import ALL_MODELS, Report

not_random_drivers_list = [Driver(abbr='SVF',
                                  name='Sebastian Vettel',
                                  car='FERRARI',
                                  start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                                  end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                                  lap_time='0:01:04.415'),
                           Driver(abbr='LHM',
                                  name='Lewis Hamilton',
                                  car='MERCEDES',
                                  start_time=datetime.strptime('2018-05-24_12:03:00.837', time_format),
                                  end_time=datetime.strptime('2018-05-24_12:04:05.114', time_format),
                                  lap_time='0:01:04.484'),
                           Driver(abbr='KRF',
                                  name='Kimi Raikkonen',
                                  car='RED BULL',
                                  start_time=datetime.strptime('2018-05-24_12:03:01.581', time_format),
                                  end_time=datetime.strptime('2018-05-24_12:04:07.215', time_format),
                                  lap_time='0:01:05.776')]

asc_drivers_dict = [{'abbr': 'SVF',
                     'car': 'FERRARI',
                     'driver_name': 'Sebastian Vettel',
                     'end_time': '2018-05-24 12:04:03.332000',
                     'lap_time': '0:01:04.415',
                     'start_time': '2018-05-24 12:02:58.917000'},
                    {'abbr': 'LHM',
                     'car': 'MERCEDES',
                     'driver_name': 'Lewis Hamilton',
                     'end_time': '2018-05-24 12:04:05.114000',
                     'lap_time': '0:01:04.484',
                     'start_time': '2018-05-24 12:03:00.837000'},
                    {'abbr': 'KRF',
                     'car': 'RED BULL',
                     'driver_name': 'Kimi Raikkonen',
                     'end_time': '2018-05-24 12:04:07.215000',
                     'lap_time': '0:01:05.776',
                     'start_time': '2018-05-24 12:03:01.581000'}]


class DataBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_db = SqliteDatabase(":memory:")
        self.test_db.bind(ALL_MODELS)
        self.test_db.connect()
        self.test_db.create_tables(ALL_MODELS)
        self.random_driver_list = create_random_drivers_list(3)
        self.random_drivers_dict = create_random_drivers_dict(3)
        self.driver = self.random_driver_list[0]

        Report.create(abbr='SVF',
                      name='Sebastian Vettel',
                      car='FERRARI',
                      start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                      end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                      lap_time='0:01:04.415')
        Report.create(abbr='LHM',
                      name='Lewis Hamilton',
                      car='MERCEDES',
                      start_time=datetime.strptime('2018-05-24_12:03:00.837', time_format),
                      end_time=datetime.strptime('2018-05-24_12:04:05.114', time_format),
                      lap_time='0:01:04.484')
        Report.create(abbr='KRF',
                      name='Kimi Raikkonen',
                      car='RED BULL',
                      start_time=datetime.strptime('2018-05-24_12:03:01.581', time_format),
                      end_time=datetime.strptime('2018-05-24_12:04:07.215', time_format),
                      lap_time='0:01:05.776')

    def tearDown(self):
        self.test_db.drop_tables(ALL_MODELS)
        self.test_db.close()


def random_driver() -> Driver:
    fake = Faker()
    random_name = fake.name()
    random_car = fake.uuid4()
    random_abbr = fake.pystr(3, 3)
    start_time = fake.pystr_format(time_format)
    end_time = fake.pystr_format(time_format)
    lap_time = fake.pystr_format(time_format)
    return Driver(random_abbr, random_name, random_car, start_time, end_time, lap_time)


def create_random_drivers_list(number) -> list[Driver]:
    drivers = []
    for _ in range(number):
        driver = random_driver()
        drivers.append(driver)

    return drivers


def create_random_drivers_dict(number) -> list[dict[str, Any]]:
    drivers = []
    for _ in range(number):
        driver = random_driver()
        data_driver_dict = {"abbr": driver.abbr,
                            "car": driver.car,
                            "end_time": driver.end_time,
                            "lap_time": driver.lap_time,
                            "name": driver.name,
                            "start_time": driver.start_time}
        drivers.append(data_driver_dict)

    drivers_json = json.dumps(drivers)
    drivers_list = json.loads(drivers_json)
    return drivers_list


# x = create_random_drivers_dict(1)
# print(x)
