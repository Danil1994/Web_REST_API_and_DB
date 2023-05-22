from task_6 import sorting_order_by

from web_app.db.create_db_data import (create_report,
                                       create_report_in_table,
                                       create_table)
from web_app.db.models import ALL_MODELS
from web_app.db.models import Report as TableReport


def create_table_and_data() -> None:
    create_table(ALL_MODELS)

    report = create_report()
    asc_sort_report = sorting_order_by(report, desc=False)
    create_report_in_table(asc_sort_report, TableReport)
