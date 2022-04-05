from unittest.mock import patch, Mock

import pytest

from chalicelib.models.compound import Compound
from chalicelib.services.compound.get_compound_image_from_id import (
    get_compound_image_from_id,
    get_compound_image_html_from_id,
)


@pytest.mark.parametrize("compound_id,expected", [(1, b"testimagebytes"), (2, None)])
@patch("chalicelib.services.compound.get_compound_image_from_id.CompoundImageExtractor")
def test_get_compound_image_from_id(MockCompoundImageExtractor: Mock, compound_id: int, expected: Compound):
    MockCompoundImageExtractor.return_value.read_compound_image_from_id.return_value = expected
    actual = get_compound_image_from_id(compound_id)
    MockCompoundImageExtractor.return_value.read_compound_image_from_id.assert_called_once_with(compound_id)
    assert actual == expected


@pytest.mark.parametrize("compound_id,expected", [(1, "html text"), (2, None)])
@patch("chalicelib.services.compound.get_compound_image_from_id.CompoundImageExtractor")
def test_get_compound_image_html_from_id(MockCompoundImageExtractor: Mock, compound_id: int, expected: Compound):
    MockCompoundImageExtractor.return_value.read_compound_html_from_id.return_value = expected
    actual = get_compound_image_html_from_id(compound_id)
    MockCompoundImageExtractor.return_value.read_compound_html_from_id.assert_called_once_with(compound_id)
    assert actual == expected
