from unittest.mock import patch, Mock

import pytest

from chalicelib.models.compound import Compound
from chalicelib.services.compound.get_compound_from_id import get_compound_from_id


@pytest.mark.parametrize("compound_id,expected", [(1, {"compound_id": 1}), (2, None)])
@patch("chalicelib.services.compound.get_compound_from_id.CompoundJSONExtractor")
def test_get_compound_from_id(MockCompoundJSONExtractor: Mock, compound_id: int, expected: Compound):
    MockCompoundJSONExtractor.return_value.read_compound_from_id.return_value = expected
    actual = get_compound_from_id(compound_id)
    MockCompoundJSONExtractor.return_value.read_compound_from_id.assert_called_once_with(compound_id)
    assert actual == expected
