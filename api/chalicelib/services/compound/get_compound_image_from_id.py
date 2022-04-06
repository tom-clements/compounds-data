from typing import Optional

from chalicelib.services.image_extractor import get_image_extractor


def get_compound_image_from_id(compound_id: int) -> Optional[bytes]:
    extractor = get_image_extractor()
    return extractor.read_compound_image_from_id(compound_id)


def get_compound_image_html_from_id(compound_id: int) -> Optional[str]:
    extractor = get_image_extractor()
    return extractor.read_compound_html_from_id(compound_id)
