from typing import Optional

from chalicelib.models.compound import Compound
from chalicelib.services.document_extractor import get_document_extractor


def get_compound_from_id(compound_id: int) -> Optional[Compound]:
    extractor = get_document_extractor()
    return extractor.read_compound_from_id(compound_id)
