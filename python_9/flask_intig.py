from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

#create a flask app
app = Flask(__name__)

@app.route("/")
def createJira():
    url = "https://kamaleshsai33.atlassian.net/rest/api/3/issue"

    API_TOKEN=""


    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "To test the jirs issue deployment",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        
        "issuetype": {
        "id": "10009"
        },
        "project": {
        "key": "SK"
        },
        "summary": "First JIRA Ticket",
        
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0')