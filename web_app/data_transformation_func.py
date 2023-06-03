from dataclasses import asdict
from datetime import datetime
from typing import Any, Dict, List

from task_6 import Driver

from web_app.db.models import ReportRepository, ExtendedDriver, ShortDriver


def _get_order(response_order: str) -> bool:
    return response_order.lower() == 'desc'


def _normalize_string(data: str) -> str:
    return data.upper().strip()


def made_report(order: bool) -> List[Dict[str, Any]]:
    drivers_list = []
    sorted_report = ReportRepository.get_all_drivers(order)
    for driver in sorted_report:
        obj = ExtendedDriver.from_peewee_obj(driver)
        drivers_list.append(asdict(obj))
    return drivers_list


def made_short_report(order: bool) -> list[dict[str, Any]]:
    short_drivers_list = []
    sorted_report = ReportRepository.get_all_drivers(order)
    for driver in sorted_report:
        obj = ShortDriver.from_peewee_obj(driver)
        short_drivers_list.append(asdict(obj))
    return short_drivers_list


def find_info_about_driver(driver_abbr: str) -> Driver | None:

    driver_abbr = _normalize_string(driver_abbr)
    driver_info = ReportRepository.get_one_driver(driver_abbr)

    return driver_info


def made_driver_info_dict(driver: Driver) -> dict[str, datetime | None | str]:
    driver_info = ReportRepository.get_one_driver(driver.abbr)
    obj = ExtendedDriver.from_peewee_obj(driver_info)

    return asdict(obj)
