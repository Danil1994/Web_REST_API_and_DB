from web_app.db.db_tools import create_table_and_data
from unittest import mock

from tests.func_for_test import DataBaseTestCase


class DataBaseCreateReport(DataBaseTestCase):
    @mock.patch('web_app.db.db_tools.create_table')
    @mock.patch('web_app.db.db_tools.create_report')
    @mock.patch('web_app.db.db_tools.create_report_in_table')
    @mock.patch('web_app.db.db_tools.sorting_order_by')
    def test_create_table_and_data(self, mock_sorting_order_by, mock_create_report_in_table, mock_create_report, mock_create_table):
        mock_create_report.return_value = self.random_driver_list

        create_table_and_data()

        mock_sorting_order_by.assert_called_once()
        mock_create_report.assert_called_once()
        mock_create_table.assert_called_once()
        mock_create_report_in_table.assert_called_once()
