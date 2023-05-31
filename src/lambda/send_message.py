from typing import Dict

from aws_lambda_typing.context import Context


def handler(event: Dict, context: Context) -> Dict:
    print(event)

    return {"statusCode": 200}
