import logging

from typing import List

from peewee import IntegrityError, OperationalError
from task_6 import Driver, create_list_object

from config import Settings
from web_app.db.db_init import database

logger = logging.getLogger(__name__)


def create_report() -> List[Driver]:
    return create_list_object(Settings.PATH_FILE)


def create_table(table:  database) -> None:
        with database:
            try:
                database.create_tables([table])
                logger.debug(f"Table {table.__name__} created successfully")
            except OperationalError:
                logger.debug(f"Table {table.__name__} already exists. Dropping and recreating...")
                database.drop_tables(table)
                database.create_tables(table)
                logger.debug(f"Table {table.__name__} recreated successfully")


def create_report_in_table(report: List[Driver], table: database) -> None:
    for driver in report:
        try:
            table.create(abbr=driver.abbr,
                         name=driver.name,
                         car=driver.car,
                         lap_time=driver.lap_time,
                         start_time=driver.start_time,
                         end_time=driver.end_time)
        except IntegrityError:
            logger.error(f"Driver with abbreviation {driver.abbr} already exists in table {table.__name__}")
