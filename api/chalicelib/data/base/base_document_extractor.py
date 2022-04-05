from abc import abstractmethod
from typing import Optional, List

from chalicelib.data.base.base_extractor import Extractor
from chalicelib.models.compound import Compound


class DocumentExtractor(Extractor):
    @abstractmethod
    def read_compounds(self) -> List[Compound]:
        pass

    @abstractmethod
    def read_compound_ids(self) -> List[int]:
        pass

    @abstractmethod
    def read_compound_from_id(self, compound_id: int) -> Optional[Compound]:
        pass
