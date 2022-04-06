from chalicelib.data.base.base_image_extractor import ImageExtractor
from chalicelib.data.images.local_image_extractor import CompoundLocalImageExtractor


def get_image_extractor() -> ImageExtractor:
    return CompoundLocalImageExtractor()
