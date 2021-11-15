
from datetime import datetime
from json import load
from json.decoder import JSONDecodeError
import os

from meteostat import Point, Hourly
from flask import (
    Flask,
    request,
    render_template,
)

app = Flask(__name__)


@app.route("/ht")
def health_check():
    return "Healthy!"


@app.route("/incidents/<string:incident_number>", methods=["GET"])
def incidents(incident_number):
    """
    Endpoints for incidents
    """
    json_path = os.path.join("data", f'{incident_number}.json')
    # just define it here to inform how the response looks like
    response = {
        "status": "success",
        "data": {},
        "weather": {}
    }
    with open(json_path) as f:
        try:
            json_data = load(f)
        except JSONDecodeError:
            return {
                "status": "error",
                "data": f"Failed to decode json file: {json_path}"
            }
        start = datetime.fromisoformat(
            json_data['description']['event_opened'],
        ).replace(tzinfo=None)
        end = datetime.fromisoformat(
            json_data['description']['event_closed']
        ).replace(tzinfo=None)
        location = Point(
            json_data['address']['latitude'],
            json_data['address']['longitude']
        )
        weather_data = Hourly(location, start, end)
        weather_data.fetch()
        print(weather_data)
        if request.method == "GET":
            response["data"] = json_data
            return render_template(
                'map.html',
                data=json_data,
                weather=weather_data,
            )
