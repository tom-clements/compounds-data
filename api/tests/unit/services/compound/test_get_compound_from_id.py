from unittest.mock import patch, Mock

import pytest

from chalicelib.models.compound import Compound
from chalicelib.services.compound.get_compound_from_id import get_compound_from_id


@pytest.mark.parametrize("compound_id,expected", [(1, {"compound_id": 1}), (2, None)])
@patch("chalicelib.services.compound.get_compound_from_id.get_document_extractor")
def test_get_compound_from_id(mock_get_document_extractor: Mock, compound_id: int, expected: Compound):
    mock_get_document_extractor.return_value.read_compound_from_id.return_value = expected
    actual = get_compound_from_id(compound_id)
    mock_get_document_extractor.return_value.read_compound_from_id.assert_called_once_with(compound_id)
    assert actual == expected
