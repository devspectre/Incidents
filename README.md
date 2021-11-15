# Incidents
Simply python backend for fire incidents analytics


# Summary
If you run the project, you can access these two endpoints.
- `/api/ht` `GET`

Check health of system


- `/api/incidents/{incident_number}` `GET`

Get insight of incident with map and weather details
# Run

## Pre-requistics
You should have `Python` and `virtualenv` installed on your machine.

## Install Dependencies
[Activate your virtual environment](https://docs.python.org/3/tutorial/venv.html).

```bash
pip install -r requirements.txt
```

## Run Flask server
```bash
flask run
```

This will run api server on `http://127.0.0.1:5000/`(assuming you do not change port).

Then you can test the api on browser
