import unittest
from unittest.mock import patch

from flask import json

from tests.func_for_test import DataBaseTestCase
from tests.func_for_test import create_random_drivers_dict
from web_app.create_app import app


class TestReport(DataBaseTestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.data = create_random_drivers_dict(10)
        cls.one_driver = {'abbr': 'SVF', 'car': 'FERRARI', 'end_time': '2018-05-24_12:04:03.332',
                          'lap_time': '0:01:04.415',
                          'name': 'Sebastian Vettel', 'start_time': '2018-05-24_12:02:58.917'}

    @patch('web_app.api.made_report')
    def test_report_json(self, mock_made_report) -> None:
        mock_made_report.return_value = self.data
        response = self.client.get('/api/v1/report')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertTrue(response.json)
        mock_made_report.assert_called_once()

    @patch('web_app.api.made_report')
    def test_report_xml(self, mock_made_report) -> None:
        mock_made_report.return_value = self.data
        response = self.client.get('/api/v1/report?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_made_report.assert_called_once()

    @patch('web_app.api.made_short_report')
    def test_short_report_json(self, mock_short_report) -> None:
        mock_short_report.return_value = self.data
        response = self.client.get('/api/v1/report/drivers?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        mock_short_report.assert_called_once()

    @patch('web_app.api.made_short_report')
    def test_short_report_xml(self, mock_short_report) -> None:
        mock_short_report.return_value = self.data
        response = self.client.get('/api/v1/report/drivers?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_short_report.assert_called_once()

    @patch('web_app.api.made_driver_info_dict')
    @patch('web_app.api.find_info_about_driver')
    def test_report_driver_json(self, mock_driver_info, mock_made_driver_info_dict) -> None:
        mock_driver_info.return_value = self.one_driver
        mock_made_driver_info_dict.return_value = self.one_driver
        response = self.client.get('/api/v1/report/drivers/SVF?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        mock_driver_info.asseert_called_once()
        mock_made_driver_info_dict.assert_called_once()

    @patch('web_app.api.made_driver_info_dict')
    @patch('web_app.api.find_info_about_driver')
    def test_report_driver_xml(self, mock_driver_info, mock_made_driver_info_dict) -> None:
        mock_driver_info.return_value = self.one_driver
        mock_made_driver_info_dict.return_value = self.one_driver
        response = self.client.get('/api/v1/report/drivers/SVF?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/xml')
        mock_driver_info.asseert_called_once()
        mock_made_driver_info_dict.assert_called_once()

    @patch('web_app.api.made_driver_info_dict')
    @patch('web_app.api.find_info_about_driver')
    def test_report_driver_not_found(self, mock_driver_info, mock_made_driver_info_dict) -> None:
        mock_driver_info.return_value = None
        mock_made_driver_info_dict.return_value = self.one_driver
        response = self.client.get('http://localhost:5080/api/v1/report/drivers/XXX?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        expected = {"message": "Driver XXX doesn't exist"}
        self.assertEqual(json.loads(response.data), expected)
        mock_driver_info.asseert_called_once()
        mock_made_driver_info_dict.assert_not_called()
