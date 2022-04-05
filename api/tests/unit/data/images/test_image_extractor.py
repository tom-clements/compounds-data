from pathlib import Path
from typing import Optional
from unittest.mock import patch

from jinja2 import Template

from chalicelib.data.images.image_extractor import CompoundImageExtractor


class TestCompoundImageExtractor:
    @staticmethod
    def _mock_get_template(file_name: str) -> Template:
        assert file_name in ["compound", "compound_not_found"]
        if file_name == "compound":
            return Template("{{ compound_id }} {{ img_data }}")
        else:
            return Template("{{ compound_id }}")

    @staticmethod
    def mock_read_compound_image_from_id(compound_id: int) -> Optional[bytes]:
        if compound_id == 1:
            return b"testimagebytes"
        else:
            return None

    @patch.object(CompoundImageExtractor, "_get_template", _mock_get_template)
    @patch.object(CompoundImageExtractor, "read_compound_image_from_id", mock_read_compound_image_from_id)
    def test_read_compound_html_from_id(self):
        extractor = CompoundImageExtractor()
        expected = "1 dGVzdGltYWdlYnl0ZXM="
        actual = extractor.read_compound_html_from_id(1)
        assert actual == expected

        expected = "2"
        actual = extractor.read_compound_html_from_id(2)
        assert actual == expected

    def test_files_exist(self):
        public_files = ["compound.html", "compound_not_found.html"]
        for f in public_files:
            assert (Path(__file__).parents[4] / Path(f"chalicelib/public/{f}")).exists()
