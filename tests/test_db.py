import unittest.mock

from func_for_test import create_random_drivers_list
from peewee import SqliteDatabase

from db.db_classes import AscReport

random_drivers_list = create_random_drivers_list(10)


class TestReport(AscReport):
    class Meta:
        datetime = None


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.db = SqliteDatabase('test.db')
        self.db.connect()
        self.db.create_tables([TestReport])
