import json
from flask import Blueprint, request, render_template, jsonify
from gateways.models import insertWeatherData, getWeatherData

api = Blueprint("api", __name__)

@api.route("/api/v1/ambient", methods=['POST'])
def userinsertdata():
    """
        Function  add new data.
    """
    data = json.loads(request.data)

    mongoData = {   "city":[data["city"], data["altitude"], data["latitude"]],
                    "temperature":data["temperature"],
                    "humidity":data["humidity"],
                    "pressure":data["pressure"]
                }

    insertWeatherData.insert_data(mongoData)

    return jsonify(data)