from unittest.mock import patch, Mock

from chalicelib.services.compound.get_compound_ids import get_compound_ids


@patch("chalicelib.services.compound.get_compound_ids.CompoundJSONExtractor")
def test_get_compound_ids(MockCompoundJSONExtractor: Mock):
    expected = [{"compound_id": 1}]
    MockCompoundJSONExtractor.return_value.read_compound_ids.return_value = expected
    actual = get_compound_ids()
    MockCompoundJSONExtractor.return_value.read_compound_ids.assert_called_once()
    assert actual == expected
