from flask import Flask,request,jsonify
import requests
from requests.auth import HTTPBasicAuth
import json

#create a flask app
app = Flask(__name__)

def createJira(Title,body):
    url = "https://kamaleshsai33.atlassian.net/rest/api/3/issue"

    API_TOKEN="<token>"

    auth = HTTPBasicAuth("<email>", API_TOKEN)

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
                    "text": body,
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
            "summary": Title,
            
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

@app.route("/jira", methods=['POST'])
def jira_test():
    # Get the incoming JSON data
    data = request.get_json()
    Title = data.get("issue",{}).get("title","")
    body = data.get("issue",{}).get("body","")

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    action = data.get('action', '')

    # Proceed only if the action is 'created' and it's a comment
    if action == 'created' and 'comment' in data:
    # Extract the body of the issue from the incoming JSON
        issue_body = data.get("comment",{}).get("body", "")
        # Check if the body contains '/jira'
        if "/jira" in issue_body:
            # If '/jira' is found in the body, create a JIRA ticket
            jira_response = createJira(Title,body)
            return jsonify({"message": "JIRA ticket created", "jira_response": json.loads(jira_response)}), 200
        else:
            return jsonify({"error": "The body does not contain '/jira'"}), 400
        
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
