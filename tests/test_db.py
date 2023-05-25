from tests.func_for_test import DataBaseTestCase

from web_app.db.create_db_data import create_report_in_table
from web_app.db.models import Report


class DataBaseCreateReport(DataBaseTestCase):
    def test_create_report_in_table(self):
        create_report_in_table(self.random_driver_list, Report)
        report = Report.select().where(Report.abbr == self.driver.abbr)
        self.assertEqual(report, self.driver)
