from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from config import Config
from web_app.db.db_init import database
from web_app.api import Report, ReportDriver, ShortReport


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    return app


app = create_app(Config)
api = Api(app)
api.add_resource(Report, '/api/v1/report')
api.add_resource(ShortReport, '/api/v1/report/drivers')
api.add_resource(ReportDriver, '/api/v1/report/drivers/<driver_abbr>')
swagger = Swagger(app)


@app.before_request
def before_request():
    database.connect()


@app.after_request
def after_request(response):
    database.close()
    return response
