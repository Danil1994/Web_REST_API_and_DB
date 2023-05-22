import unittest.mock
from datetime import datetime

from task_6 import time_format

from func_for_test import create_random_drivers_list
from peewee import SqliteDatabase

from web_app.db.models import Report

random_drivers_list = create_random_drivers_list(10)
test_db = SqliteDatabase('test_db.db')


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        test_db.connect()
        test_db.create_tables([Report])
        self.driver = Report.create(abbr='SVF',
                                    name='Sebastian Vettel',
                                    car='FERRARI',
                                    start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                                    end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                                    lap_time='0:01:04.415')

    def tearDown(self):
        test_db.drop_tables([Report])
        test_db.close()

    def test_create_driver(self):
        report = Report.select()
        self.assertIn(self.driver, report)

    def test_delete_driver(self):
        self.driver.delete_instance()
        report = Report.select()

        self.assertNotIn(self.driver, report)
