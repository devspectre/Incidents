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


Test with this url
[http://127.0.0.1:5000/incidents/F01705150050](http://127.0.0.1:5000/incidents/F01705150050)