"""Python AWS Lambda Hello World Example
   This example Lambda function will simply return 'Hello from Lambda!' and
   a HTTP Status Code 200.
"""

import json


def lambda_handler(event, context):
    response_message = "Hello from Lambda!"

    if event["queryStringParameters"] and event["queryStringParameters"]["Name"]:
        response_message = "Hello, " + event["queryStringParameters"]["Name"] + "!"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response_message),
    }
