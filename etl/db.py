import boto3


def get_db():
    return boto3.resource("dynamodb")
