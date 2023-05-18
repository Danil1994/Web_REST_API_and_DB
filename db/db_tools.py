from task_6 import sorting_order_by

from db.create_db_data import (create_report,
                               create_report_in_table,
                               create_table)
from db.db_classes import Report

create_table(Report)

report = create_report()

asc_sort_report = sorting_order_by(report, False)
create_report_in_table(asc_sort_report, Report)
