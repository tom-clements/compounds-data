from typing import Optional

from chalicelib.data.base.base_image_extractor import ImageExtractor


# TODO: upload images into cloud bucket
class CompoundCloudImageExtractor(ImageExtractor):
    def read_compound_html_from_id(self, compound_id: int) -> str:
        raise NotImplementedError

    def read_compound_image_from_id(self, compound_id: int) -> Optional[bytes]:
        raise NotImplementedError
