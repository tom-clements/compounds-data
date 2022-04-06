from unittest.mock import patch, Mock

from chalicelib.services.compound.get_compound_ids import get_compound_ids


@patch("chalicelib.services.compound.get_compound_ids.get_document_extractor")
def test_get_compound_ids(mock_get_document_extractor: Mock):
    expected = [{"compound_id": 1}]
    mock_get_document_extractor.return_value.read_compound_ids.return_value = expected
    actual = get_compound_ids()
    mock_get_document_extractor.return_value.read_compound_ids.assert_called_once()
    assert actual == expected
