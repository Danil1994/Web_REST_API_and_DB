from dataclasses import asdict

from web_app.db.models import ExtendedDriver, ReportRepository

sorted_report = ReportRepository.get_all_drivers(False)

driver_list = []
for driver in sorted_report:
    obj = ExtendedDriver.from_peewee_obj(driver)
    driver_list.append(asdict(obj))

print(driver_list)
