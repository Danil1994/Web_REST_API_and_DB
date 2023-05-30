from unittest import mock

from tests.func_for_test import DataBaseTestCase

from web_app.db.create_db_data import create_report_in_table, create_table, create_report
from web_app.db.models import Report


class DataBaseCreateReport(DataBaseTestCase):
    @mock.patch('web_app.db.create_db_data.create_list_object')
    def test_create_report(self, mock_list_object):
        create_report()
        mock_list_object.assert_called_once()

    @mock.patch('web_app.db.create_db_data.database')
    @mock.patch('web_app.db.create_db_data.logger')
    def test_create_table(self, mock_logger, mock_database):
        tables = [Report]
        mock_database.drop_tables.return_value = None
        mock_database.create_tables.return_value = None

        create_table(tables)

        mock_logger.debug.assert_any_call("Dropping tables and recreating...")
        mock_database.drop_tables.assert_called_once_with(tables)
        mock_database.create_tables.assert_called_once_with(tables)
        mock_logger.debug.assert_called_with("Table {} created successfully".format(tables[0].__name__))

    @mock.patch('web_app.db.create_db_data.logger')
    def test_create_report_in_table(self, mock_logger):
        create_report_in_table(self.random_driver_list, Report)
        create_report_in_table([self.driver], Report)
        report = Report.select().where(Report.abbr == self.driver.abbr)
        self.assertEqual(report, self.driver)

        mock_logger.debug.assert_called()
        mock_logger.error.assert_called()
