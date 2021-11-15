from datetime import datetime
from json import load
from json.decoder import JSONDecodeError
import os
import requests

from flask import (
    Flask,
    request,
    render_template,
)

app = Flask(__name__)
WEATHER_API_BASE_URL = 'http://api.weatherapi.com/v1'
WEATHER_API_KEY = '04fb3aa2bc6d4d0db3e151857211511'


@app.route("/api/ht")
def health_check():
    return "Healthy!"


@app.route("/api/incidents/<string:incident_number>", methods=["GET"])
def incidents(incident_number):
    """
    Endpoints for incidents
    """
    json_path = os.path.join("data", f'{incident_number}.json')
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
        lat = json_data['address']['latitude']
        lon = json_data['address']['longitude']
        start_date = start.strftime('%Y-%m-%d')

        # in prod, the method should be history.json instead of current.json
        # just using current.json as history.json requires payment
        url = (
            f"{WEATHER_API_BASE_URL}"
            f"/current.json?key={WEATHER_API_KEY}"
            f"&q={lat},{lon}"
            f"&dt={start_date}"
        )
        response = requests.get(url)
        weather_data = None
        if response.status_code == 200:
            weather_data = response.json()

        if request.method == "GET":
            return render_template(
                'map.html',
                apparatus=json_data['apparatus'],
                address=json_data['address'],
                description=json_data['description'],
                fire_department=json_data['fire_department'],
                weather=weather_data,
                version=json_data['version']
            )
