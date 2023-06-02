from datetime import datetime
from typing import Any, Dict, List

from task_6 import Driver

from web_app.db.models import ReportRepository

report = ReportRepository()


def _get_order(response_order: str) -> bool:
    return response_order.lower() == 'desc'


def _normalize_string(data: str) -> str:
    return data.upper().strip()


def made_report(order: bool) -> List[Dict[str, Any]]:
    drivers_list = []
    sorted_report = report.get_all_drivers(order)
    for driver in sorted_report:
        driver_info = {"abbr": driver.abbr, "driver_name": driver.name, "lap_time": driver.lap_time,
                       "car": driver.car, "start_time": driver.start_time, "end_time": driver.end_time}

        drivers_list.append(driver_info)
    return drivers_list


def made_short_report(order: bool) -> list[dict[str, Any]]:
    short_drivers_list = []
    sorted_report = report.get_all_drivers(order)
    for driver in sorted_report:
        driver_info = {"abbr": driver.abbr, "driver_name": driver.name, "lap_time": driver.lap_time}

        short_drivers_list.append(driver_info)
    return short_drivers_list


def find_info_about_driver(driver_abbr: str) -> Driver | None:
    driver_abbr = _normalize_string(driver_abbr)
    driver_info = report.get_one_driver(driver_abbr)

    return driver_info


def made_driver_info_dict(driver: Driver) -> dict[str, datetime | None | str]:
    info = {"driver_name": driver.name, "abbr": driver.abbr, "car": driver.car,
            "lap_time": driver.lap_time, "start_time": driver.start_time, "end_time": driver.end_time}

    return info
