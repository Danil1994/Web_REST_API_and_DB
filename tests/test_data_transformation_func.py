from datetime import datetime

from tests.func_for_test import DataBaseTestCase
from task_6 import Driver, time_format

from tests.func_for_test import asc_drivers_dict, not_random_drivers_list
from web_app.data_transformation_func import (find_info_about_driver,
                                              made_driver_info_dict,
                                              made_report, made_short_report)


class TestFunction(DataBaseTestCase):

    def test_made_report_ascending(self):
        expected_result = asc_drivers_dict
        result = made_report(order=False)
        self.assertEqual(result, expected_result)

    def test_made_report_descending(self):
        expected_result = asc_drivers_dict
        expected_result.reverse()
        result = made_report(order=True)
        self.assertEqual(result, expected_result)

    def test_made_short_report_asc(self):
        expected_result = [{'abbr': 'SVF', 'driver_name': 'Sebastian Vettel', 'lap_time': '0:01:04.415'},
                           {'abbr': 'LHM', 'driver_name': 'Lewis Hamilton', 'lap_time': '0:01:04.484'},
                           {'abbr': 'KRF', 'driver_name': 'Kimi Raikkonen', 'lap_time': '0:01:05.776'}]
        result = made_short_report(order=False)
        self.assertEqual(result, expected_result)

    def test_made_short_report_desc(self):
        expected_result = [{'abbr': 'KRF', 'driver_name': 'Kimi Raikkonen', 'lap_time': '0:01:05.776'},
                           {'abbr': 'LHM', 'driver_name': 'Lewis Hamilton', 'lap_time': '0:01:04.484'},
                           {'abbr': 'SVF', 'driver_name': 'Sebastian Vettel', 'lap_time': '0:01:04.415'},
                           ]
        result = made_short_report(order=True)
        self.assertEqual(result, expected_result)

    def test_find_info_about_driver_existing(self):
        expected_output = Driver(abbr='SVF',
                                 name='Sebastian Vettel',
                                 car='FERRARI',
                                 start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                                 end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                                 lap_time='0:01:04.415')
        result = find_info_about_driver('SVF')
        self.assertEqual(result.abbr, expected_output.abbr)

    def test_find_info_about_driver_nonexistent(self):
        driver_abbr = 'ABC'
        expected_result = None
        result = find_info_about_driver(driver_abbr)
        self.assertEqual(result, expected_result)

    def test_made_driver_info_dict(self):
        expected_output = {'abbr': 'SVF',
                           'car': 'FERRARI',
                           'driver_name': 'Sebastian Vettel',
                           'end_time': datetime(2018, 5, 24, 12, 4, 3, 332000),
                           'lap_time': '0:01:04.415',
                           'start_time': datetime(2018, 5, 24, 12, 2, 58, 917000)}
        self.assertEqual(made_driver_info_dict(not_random_drivers_list[0]), expected_output)
