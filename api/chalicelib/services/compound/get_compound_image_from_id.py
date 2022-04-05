from typing import Optional

from chalicelib.data.images.image_extractor import CompoundImageExtractor


def get_compound_image_from_id(compound_id: int) -> Optional[bytes]:
    extractor = CompoundImageExtractor()
    return extractor.read_compound_image_from_id(compound_id)


def get_compound_image_html_from_id(compound_id: int) -> Optional[str]:
    extractor = CompoundImageExtractor()
    return extractor.read_compound_html_from_id(compound_id)
