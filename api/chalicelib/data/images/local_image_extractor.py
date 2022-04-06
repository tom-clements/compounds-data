import base64
from pathlib import Path
from typing import Optional

from jinja2 import Template
from chalicelib.data.base.base_image_extractor import ImageExtractor


class CompoundLocalImageExtractor(ImageExtractor):
    def __init__(self, file_path: str = "chalicelib/db/images"):
        self.file_path = file_path

    @staticmethod
    def _get_template(file_name: str) -> Template:
        with open(f"chalicelib/public/{file_name}.html", "r") as f:
            html_template = f.read()
        return Template(html_template)

    def read_compound_html_from_id(self, compound_id: int) -> str:
        image = self.read_compound_image_from_id(compound_id)
        if image:
            template = self._get_template("compound")
            data = {"img_data": base64.b64encode(image).decode("utf-8"), "compound_id": compound_id}
            return template.render(data)
        else:
            template = self._get_template("compound_not_found")
            data = {"compound_id": compound_id}
            return template.render(data)

    def read_compound_image_from_id(self, compound_id: int) -> Optional[bytes]:
        try:
            with open(Path(self.file_path) / f"{compound_id}.png", "rb") as f:
                image = f.read()
            return image
        except FileNotFoundError:
            return None
