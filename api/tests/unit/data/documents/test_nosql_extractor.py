from unittest.mock import patch, PropertyMock

import pytest

from chalicelib.data.documents.nosql_extractor import CompoundNoSQLExtractor


class TestCompoundNoSQLExtractor:
    @pytest.mark.parametrize(
        "compound_id,get_item_return,expected", [(1, {"Item": {"compound_id": 1}}, {"compound_id": 1}), (2, {}, None)]
    )
    @patch("chalicelib.data.documents.nosql_extractor.CompoundNoSQLExtractor.table", new_callable=PropertyMock)
    def test_read_compound_from_id(self, mock_table, compound_id, get_item_return, expected):
        mock_table.return_value.get_item.return_value = get_item_return
        extractor = CompoundNoSQLExtractor()
        actual = extractor.read_compound_from_id(compound_id)
        mock_table.return_value.get_item.assert_called_with(Key={"compound_id": compound_id})
        assert actual == expected

    @patch("chalicelib.data.documents.nosql_extractor.CompoundNoSQLExtractor.table", new_callable=PropertyMock)
    def test_read_compound_ids(self, mock_table):
        expected = [1]
        mock_table.return_value.scan.return_value = {"Items": [{"compound_id": 1}]}
        extractor = CompoundNoSQLExtractor()
        actual = extractor.read_compound_ids()
        mock_table.return_value.scan.assert_called_once()
        assert actual == expected
