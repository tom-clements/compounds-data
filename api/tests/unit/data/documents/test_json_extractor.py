from typing import List, Dict
from unittest.mock import patch

from chalicelib.data.documents.json_extractor import CompoundJSONExtractor


class TestCompoundJSONExtractor:
    @staticmethod
    def mock_read_compounds() -> List[Dict[str, int]]:
        return [{"compound_id": 1}]

    @patch.object(CompoundJSONExtractor, "read_compounds", mock_read_compounds)
    def test_read_compound_from_id(self):
        extractor = CompoundJSONExtractor()
        expected = {"compound_id": 1}
        actual = extractor.read_compound_from_id(1)
        assert actual == expected

        expected = None
        actual = extractor.read_compound_from_id(2)
        assert actual == expected

    @patch.object(CompoundJSONExtractor, "read_compounds", mock_read_compounds)
    def test_read_compound_ids(self):
        extractor = CompoundJSONExtractor()
        expected = [1]
        actual = extractor.read_compound_ids()
        assert actual == expected
