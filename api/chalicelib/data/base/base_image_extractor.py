from abc import abstractmethod
from typing import Optional

from chalicelib.data.base.base_extractor import Extractor


class ImageExtractor(Extractor):
    @abstractmethod
    def read_compound_html_from_id(self, compound_id: int) -> str:
        pass

    @abstractmethod
    def read_compound_image_from_id(self, compound_id: int) -> Optional[bytes]:
        pass
