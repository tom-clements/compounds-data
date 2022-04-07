from typing import Optional

from chalicelib.data.base.base_image_extractor import CompoundImageExtractor


# TODO: upload images into cloud bucket
class CompoundCloudImageExtractor(CompoundImageExtractor):
    def read_compound_html_from_id(self, compound_id: int) -> str:
        raise NotImplementedError

    def read_compound_image_from_id(self, compound_id: int) -> Optional[bytes]:
        raise NotImplementedError
