import json
from typing import Dict

import boto3
import os

from aws_lambda_typing.context import Context


def handler(event: Dict, context: Context):
    sqs = boto3.client('sqs')
    queue_url = os.environ['QUEUE_URL']
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(event)
    )
    return response
