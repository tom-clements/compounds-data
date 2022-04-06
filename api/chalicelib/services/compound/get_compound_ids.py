from typing import List

from chalicelib.services.document_extractor import get_document_extractor


def get_compound_ids() -> List[int]:
    extractor = get_document_extractor()
    return extractor.read_compound_ids()
