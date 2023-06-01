import collections
from dataclasses import asdict
from datetime import datetime
from typing import Any, Dict, List

from task_6 import Driver

from web_app.db.models import Report


def _get_order(response_order: str) -> bool:
    return response_order.lower() == 'desc'


def _normalize_string(data: str) -> str:
    return data.upper().strip()


def _report_sorted_by_order(order: bool) -> Any:
    if not order:
        sorted_report = Report.select().order_by(Report.lap_time.asc())
    else:
        sorted_report = Report.select().order_by(Report.lap_time.desc())
    print(sorted_report)
    return sorted_report


def made_report(order: bool) -> List[Dict[str, Any]]:
    drivers_list = []
    sorted_report = _report_sorted_by_order(order)
    for driver in sorted_report:
        driver_info = {"abbr": driver.abbr, "driver_name": driver.name, "lap_time": driver.lap_time,
                       "car": driver.car, "start_time": driver.start_time, "end_time": driver.end_time}

        drivers_list.append(driver_info)
    return drivers_list


def made_short_report(order: bool) -> list[dict[str, Any]]:
    short_drivers_list = []
    sorted_report = _report_sorted_by_order(order)
    for driver in sorted_report:
        driver_info = {"abbr": driver.abbr, "driver_name": driver.name, "lap_time": driver.lap_time}

        short_drivers_list.append(driver_info)
    return short_drivers_list


def _report_select(driver_abbr: str) -> Any | None:
    for driver in Report.select():
        if driver.abbr == driver_abbr:
            return driver
    return None


def find_info_about_driver(driver_abbr: str) -> Driver | None:
    driver_abbr = _normalize_string(driver_abbr)
    driver_info = _report_select(driver_abbr)

    return driver_info


def made_driver_info_dict(driver: Driver) -> dict[str, datetime | None | str]:
    info = {"driver_name": driver.name, "abbr": driver.abbr, "car": driver.car,
            "lap_time": driver.lap_time, "start_time": driver.start_time, "end_time": driver.end_time}

    return info
