from typing import Dict

from aws_lambda_typing.context import Context


def handler(event: Dict, context: Context) -> Dict:
    print(event)
    print("to remove")
    print("to be removed")

    return {"statusCode": 200}
