import json
from datetime import datetime
from typing import Any, Dict, List

from dict2xml import dict2xml
import xml.etree.ElementTree as ET
from flasgger import swag_from
from flask import Response, abort, request
from flask_restful import Resource

from web_app.constants import MyEnum
from web_app.data_transformation_func import (_get_order,
                                              find_info_about_driver,
                                              made_driver_info_dict,
                                              made_report, made_short_report)


def output_formatted_data_from_dict(format_value: MyEnum, info_list: List[Any] | dict) -> Response:
    if format_value == MyEnum.xml:
        resp = dict2xml(info_list, wrap="driver", indent=" ")
        return Response(response=resp, status=200, headers={'Content-Type': 'application/xml'})
    else:
        json_str = json.dumps(info_list)
        return Response(response=json_str.encode('utf-8'), status=200, headers={'Content-Type': 'application/json'})


def output_formatted_data_from_list(format_value: MyEnum, info_list: List[Any] | dict) -> Response:
    if format_value == MyEnum.xml:
        drivers = ET.Element("response")

        for driver_info in info_list:
            driver = ET.SubElement(drivers, "driver")
            for key, value in driver_info.items():
                ET.SubElement(driver, key).text = str(value)

        resp = ET.tostring(drivers, encoding="unicode")

        return Response(response=resp, status=200, headers={'Content-Type': 'application/xml'})
    else:
        json_str = json.dumps(info_list)
        return Response(response=json_str.encode('utf-8'), status=200, headers={'Content-Type': 'application/json'})


class Report(Resource):

    @swag_from('swagger/report.yml')
    def get(self) -> List[Dict[str, Any]] | Response:
        order = _get_order(request.args.get('order', default='asc'))
        response_format = MyEnum(request.args.get('format', default='json'))
        response = made_report(order)

        return output_formatted_data_from_list(response_format, response)


class ShortReport(Resource):
    @swag_from('swagger/short_report.yml')
    def get(self) -> List[Dict[str, Any]] | Response:
        order = _get_order(request.args.get('order', default='asc'))
        response_format = MyEnum(request.args.get('format', default='json'))
        response = made_short_report(order)

        return output_formatted_data_from_list(response_format, response)


class ReportDriver(Resource):

    @swag_from('swagger/report_driver.yml')
    def get(self, driver_abbr: str) -> dict[str, datetime | None | str] | Response:
        response_format = MyEnum(request.args.get('format', default='json'))
        driver = find_info_about_driver(driver_abbr)

        if not driver:
            abort(404, response={"message": "Driver {} doesn't exist".format(driver_abbr)})
        response = made_driver_info_dict(driver)

        return output_formatted_data_from_dict(response_format, response)
