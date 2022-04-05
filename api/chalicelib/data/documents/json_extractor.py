import json
from typing import List, Optional

from chalicelib.data.base.base_document_extractor import DocumentExtractor
from chalicelib.models.compound import Compound


class CompoundJSONExtractor(DocumentExtractor):
    def __init__(self, file_path: str = "chalicelib/db/compounds.json"):
        self.file_path = file_path

    def read_compounds(self) -> List[Compound]:
        with open(self.file_path, "r") as f:
            data = json.load(f)
        return data

    def read_compound_ids(self) -> List[int]:
        data = self.read_compounds()
        return [d["compound_id"] for d in data]

    def read_compound_from_id(self, compound_id: int) -> Optional[Compound]:
        data = self.read_compounds()
        compound = [d for d in data if d["compound_id"] == compound_id]
        return compound[0] if compound else None
