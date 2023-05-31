from typing import List

from peewee import IntegrityError
from task_6 import Driver

from logger import initialize_logger
from web_app.db.db_init import database

logger = initialize_logger()


def create_table(tables: database) -> None:
    with database:
        logger.debug("Dropping tables and recreating...")
        database.drop_tables(tables)
        database.create_tables(tables)
        for table in tables:
            logger.debug(f"Table {table.__name__} created successfully")


def create_report_in_table(report: List[Driver], table: database) -> None:
    for driver in report:
        try:
            table.create(abbr=driver.abbr,
                         name=driver.name,
                         car=driver.car,
                         lap_time=driver.lap_time,
                         start_time=driver.start_time,
                         end_time=driver.end_time)
            logger.debug(f"Record {driver.abbr} created successfully")
        except IntegrityError:
            logger.error(f"Driver with abbreviation {driver.abbr} already exists in table {table.__name__}")
