#jira story automation from github issues with the help of Flask application

Github-->webhook-->URL-->json-->EC2(python-flask API) -->API_call_Json-->Jira story

we need to write a python flask api to read and create jira stories only when "/jira" was provided in the comments.

configure the ec2 that is running the flask api as webhook to send the json packages when a change is made in the issues.

once the script detects the /jira comment it will create the jira ticet with the title and body same as the issue.
