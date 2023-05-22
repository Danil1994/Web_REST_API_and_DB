import unittest
import datetime
from peewee import SqliteDatabase

from task_6 import sorting_order_by
from web_app.db.models import Report

from tests.func_for_test import (create_random_drivers_list,
                                 not_random_drivers_list,
                                 asc_drivers_dict)

from web_app.data_transformation_func import (made_driver_info_dict, made_report,
                                              made_short_report)

test_db = SqliteDatabase('test_db.db')
random_drivers_list = create_random_drivers_list(5)
sorted_report = sorting_order_by(not_random_drivers_list, desc=False)


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        test_db.connect()
        test_db.create_tables([Report])
        for driver in not_random_drivers_list:
            Report.create(abbr=driver.abbr,
                          name=driver.name,
                          car=driver.car,
                          start_time=driver.start_time,
                          end_time=driver.end_time,
                          lap_time=driver.lap_time)

    def tearDown(self):
        test_db.drop_tables([Report])
        test_db.close()

    def test_made_report(self):
        self.assertEqual(made_report(False), asc_drivers_dict)
        asc_drivers_dict.reverse()
        self.assertEqual(made_report(True), asc_drivers_dict)

    def test_made_short_report(self):
        expected_output = [{'abbr': 'SVF', 'driver_name': 'Sebastian Vettel', 'lap_time': '0:01:04.415'},
                           {'abbr': 'LHM', 'driver_name': 'Lewis Hamilton', 'lap_time': '0:01:04.484'},
                           {'abbr': 'KRF', 'driver_name': 'Kimi Raikkonen', 'lap_time': '0:01:05.776'}]
        self.assertEqual(made_short_report(False), expected_output)
        expected_output.reverse()
        self.assertEqual(made_short_report(True), expected_output)

    def test_made_driver_info_dict(self):
        expected_output = {'abbr': 'SVF',
                           'car': 'FERRARI',
                           'driver_name': 'Sebastian Vettel',
                           'end_time': datetime.datetime(2018, 5, 24, 12, 4, 3, 332000),
                           'lap_time': '0:01:04.415',
                           'start_time': datetime.datetime(2018, 5, 24, 12, 2, 58, 917000)}
        self.assertEqual(made_driver_info_dict(not_random_drivers_list[0]), expected_output)
