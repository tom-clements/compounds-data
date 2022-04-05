from typing import Optional

from chalicelib.data.documents.json_extractor import CompoundJSONExtractor
from chalicelib.models.compound import Compound


def get_compound_from_id(compound_id: int) -> Optional[Compound]:
    extractor = CompoundJSONExtractor()
    return extractor.read_compound_from_id(compound_id)
