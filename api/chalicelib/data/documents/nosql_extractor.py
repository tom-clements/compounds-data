from typing import List, Optional

import boto3

from chalicelib.data.base.base_document_extractor import DocumentExtractor
from chalicelib.models.compound import Compound


class CompoundNoSQLExtractor(DocumentExtractor):
    def __init__(self, table_name: str = "compounds"):
        self.table_name = table_name

    @property
    def db(self):
        return boto3.resource("dynamodb")

    @property
    def table(self):
        return self.db.Table(self.table_name)

    def read_compounds(self) -> List[Compound]:
        response = self.table.query()
        return response["Items"]

    def read_compound_ids(self) -> List[int]:
        response = self.table.scan(ProjectionExpression="compound_id")
        return [int(compound_id["compound_id"]) for compound_id in response["Items"]]

    def read_compound_from_id(self, compound_id: int) -> Optional[Compound]:
        response = self.table.get_item(Key={"compound_id": compound_id})
        if "Item" in response:
            item = response["Item"]
            item["compound_id"] = compound_id
            return item
        else:
            return None
