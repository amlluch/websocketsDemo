from typing import Dict

from aws_lambda_typing.context import Context


def handler(event: Dict, context: Context) -> Dict:
    print(event)
    print("Small change")
    print("prueba para revertir")

    return {"statusCode": 200}
