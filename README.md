# Incidents
Simply python application based on [Flask](https://flask.palletsprojects.com/) and [Jinja](https://jinja.palletsprojects.com/) to get insights of fire incidents



# Installation

## Pre-requistics
You should have [Python](https://realpython.com/installing-python/), [pip](https://pip.pypa.io/en/stable/installation/) and [virtualenv](https://programwithus.com/learn/python/pip-virtualenv-mac) installed on your machine.

## Install Dependencies
[Activate your virtual environment](https://docs.python.org/3/tutorial/venv.html).
```bash
source venv/bin/activate
```

Then install dependencies using pip
```bash
pip install -r requirements.txt
```


# Run
```bash
flask run
```

This will run api server on `http://127.0.0.1:5000/`(assuming you do not change port).

Then you can test the api on browser



# Summary
If you run the project, you can access these two endpoints.
- `/api/ht` `GET`

Check health of system


- `/api/incidents/{incident_number}` `GET`

Get insight of incident with map and weather details


Test with these urls
[http://127.0.0.1:5000/incidents/F01705150050](http://127.0.0.1:5000/incidents/F01705150050)

[http://127.0.0.1:5000/incidents/F01705150090](http://127.0.0.1:5000/incidents/F01705150090)

# Notes
Red circle indicates the place where the incident happened.
Blue markers are the units engaged the incident.
If you click on the markers, you can see more details about the units.

![image](https://user-images.githubusercontent.com/46239206/141819270-e07906d2-adcc-48b8-a45e-bce4c0a9aba4.png)
![image](https://user-images.githubusercontent.com/46239206/141819400-0b5450df-8c7f-4fc8-a104-1336f5a8ac91.png)


# Caveats
The app uses API of weatherapi.com but it requires adding payment method to the account to get historic data.
For this reason, the app uses current weather, so don't think the weather data is correct.
