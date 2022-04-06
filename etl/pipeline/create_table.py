from db import get_db


def create_table(table_name: str):
    dynamodb = get_db()
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "compound_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "compound_id", "AttributeType": "N"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )
    table.wait_until_exists()
