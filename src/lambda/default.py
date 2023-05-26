import json
from typing import Dict

import boto3
import os

from aws_lambda_typing.context import Context


def handler(event: Dict, context: Context) -> Dict:
    sqs = boto3.client('sqs')
    queue_url = os.environ['QUEUE_URL']
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(event)
    )
    print(response)
    return {"statusCode": 200}
