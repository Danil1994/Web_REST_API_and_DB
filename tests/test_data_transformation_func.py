import unittest
from datetime import datetime
from unittest.mock import patch

from task_6 import time_format

from tests.func_for_test import create_random_drivers_list
from web_app.data_transformation_func import (Driver, find_info_about_driver,
                                              made_driver_info_dict,
                                              made_report, made_short_report)


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.report = create_random_drivers_list(3)
        self.driver1 = Driver(abbr='SVF',
                              name='Sebastian Vettel',
                              car='FERRARI',
                              start_time=datetime.strptime('2018-05-24_12:02:58.917', time_format),
                              end_time=datetime.strptime('2018-05-24_12:04:03.332', time_format),
                              lap_time='0:01:04.415')

        self.driver2 = Driver(abbr='LHM',
                              name='Lewis Hamilton',
                              car='MERCEDES',
                              start_time=datetime.strptime('2018-05-24_12:03:00.837', time_format),
                              end_time=datetime.strptime('2018-05-24_12:04:05.114', time_format),
                              lap_time='0:01:04.484')
        self.driver3 = Driver(abbr='KRF',
                              name='Kimi Raikkonen',
                              car='RED BULL',
                              start_time=datetime.strptime('2018-05-24_12:03:01.581', time_format),
                              end_time=datetime.strptime('2018-05-24_12:04:07.215', time_format),
                              lap_time='0:01:05.776')

        self.drivers_list = [self.driver1, self.driver2, self.driver3]

    @patch('web_app.data_transformation_func.AscReport.select')
    def test_made_report_asc_order(self, mock_asc_report):
        mock_asc_report.return_value = [
            type('MockedAscReport', (), {'abbr': 'AB', 'name': 'John', 'lap_time': 123,
                                         'car': 'Red car', 'start_time': '2022-01-01 10:00:00',
                                         'end_time': '2022-01-01 11:00:00'}),
            type('MockedAscReport', (), {'abbr': 'CD', 'name': 'Jane', 'lap_time': 456,
                                         'car': 'Blue car', 'start_time': '2022-01-01 11:00:00',
                                         'end_time': '2022-01-01 12:00:00'})
        ]
        expected_result = [
            {"abbr": "AB", "driver_name": "John", "lap_time": 123, "car": "Red car",
             "start_time": "2022-01-01 10:00:00", "end_time": "2022-01-01 11:00:00"},
            {"abbr": "CD", "driver_name": "Jane", "lap_time": 456, "car": "Blue car",
             "start_time": "2022-01-01 11:00:00", "end_time": "2022-01-01 12:00:00"}
        ]

        self.assertEqual(made_report(False), expected_result)
        mock_asc_report.assert_called_once()

    @patch('web_app.data_transformation_func.DescReport.select')
    def test_made_report_desc_order(self, mock_desc_report):
        mock_desc_report.return_value = [
            type('MockedDescReport', (), {'abbr': 'EF', 'name': 'Mike', 'lap_time': 789,
                                          'car': 'Green car', 'start_time': '2022-01-01 12:00:00',
                                          'end_time': '2022-01-01 13:00:00'}),
            type('MockedDescReport', (), {'abbr': 'GH', 'name': 'Kate', 'lap_time': 321,
                                          'car': 'Yellow car', 'start_time': '2022-01-01 13:00:00',
                                          'end_time': '2022-01-01 14:00:00'})
        ]
        expected_result = [
            {"abbr": "EF", "driver_name": "Mike", "lap_time": 789, "car": "Green car",
             "start_time": "2022-01-01 12:00:00", "end_time": "2022-01-01 13:00:00"},
            {"abbr": "GH", "driver_name": "Kate", "lap_time": 321, "car": "Yellow car",
             "start_time": "2022-01-01 13:00:00", "end_time": "2022-01-01 14:00:00"}
        ]

        self.assertEqual(made_report(True), expected_result)
        mock_desc_report.assert_called_once()

    @patch('web_app.data_transformation_func.AscReport.select')
    def test_made_short_report_asc_order(self, mock_asc_report):
        mock_asc_report.return_value = [
            type('MockedAscReport', (), {'abbr': 'AB', 'name': 'John', 'lap_time': 123, }),
            type('MockedAscReport', (), {'abbr': 'CD', 'name': 'Jane', 'lap_time': 456, })
        ]
        expected_result = [
            {"abbr": "AB", "driver_name": "John", "lap_time": 123, },
            {"abbr": "CD", "driver_name": "Jane", "lap_time": 456, }
        ]

        self.assertEqual(made_short_report(False), expected_result)
        mock_asc_report.assert_called_once()

    def test_made_driver_info_dict(self):
        expected_output = {'abbr': 'SVF',
                           'car': 'FERRARI',
                           'driver_name': 'Sebastian Vettel',
                           'end_time': datetime(2018, 5, 24, 12, 4, 3, 332000),
                           'lap_time': '0:01:04.415',
                           'start_time': datetime(2018, 5, 24, 12, 2, 58, 917000)}
        self.assertEqual(made_driver_info_dict(self.driver1), expected_output)

    @patch('web_app.data_transformation_func.AscReport.select')
    def test_info_driver_about(self, mock_asc_report):
        mock_asc_report.return_value = self.drivers_list
        for driver in self.drivers_list:
            self.assertEqual(find_info_about_driver(driver.abbr), driver)
