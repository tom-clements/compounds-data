from chalicelib.data.base.base_image_extractor import CompoundImageExtractor
from chalicelib.data.images.local_image_extractor import CompoundLocalImageExtractor


def get_image_extractor() -> CompoundImageExtractor:
    return CompoundLocalImageExtractor()
