import json
from decimal import Decimal
from typing import List, Any, Dict

from db import get_db


def get_data() -> List[Dict[str, Any]]:
    with open("pipeline/data/compounds.json", "r") as f:
        data = json.load(f, parse_float=Decimal)
    return data


def add_data_to_db(data: List[Dict[str, Any]], table_name: str):
    dynamodb = get_db()
    table = dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        for document in data:
            batch.put_item(Item=document)


def insert_data(table_name: str):
    data = get_data()
    add_data_to_db(data, table_name)
