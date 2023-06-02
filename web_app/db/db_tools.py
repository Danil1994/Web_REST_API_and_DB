from typing import List

from task_6 import Driver, create_list_object, sorting_order_by

from config import Settings
from web_app.db.create_db_data import create_report_in_table, create_table
from web_app.db.models import ALL_MODELS
from web_app.db.models import self as TableReport


def create_report() -> List[Driver]:
    return create_list_object(Settings.PATH_FILE)


def create_table_and_data() -> None:
    create_table(ALL_MODELS)

    report = create_report()
    asc_sort_report = sorting_order_by(report, desc=False)
    create_report_in_table(asc_sort_report, TableReport)
