import sentry_sdk
import pymongo

from sentry_sdk.integrations.flask import FlaskIntegration
from settings import setMongo, swagger
from flask_swagger_ui import get_swaggerui_blueprint


def sentry():
    sentry_sdk.init(
        dsn="https://c9f0c6caa77c415f95d3dec207c547d7@sentry.io/2608021",
        integrations=[FlaskIntegration()]
    )

def mongodb_middleware_weather():
    myclient = pymongo.MongoClient(setMongo["url"])
    mydb = myclient[setMongo["dbname"]]
    connection = mydb[setMongo["dbcolweather"]]
    return connection

def configureSwagger(app):
    swaggerBlueprint = get_swaggerui_blueprint(
        swagger['url'],
        swagger['descriptorUrl'],
        config={
            'app_name': "File Weather API"
        }
    )
    app.register_blueprint(swaggerBlueprint,
                           url_prefix=swagger['url'])
