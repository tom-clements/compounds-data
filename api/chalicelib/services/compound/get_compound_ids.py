from typing import List

from chalicelib.data.documents.json_extractor import CompoundJSONExtractor


def get_compound_ids() -> List[int]:
    extractor = CompoundJSONExtractor()
    return extractor.read_compound_ids()
