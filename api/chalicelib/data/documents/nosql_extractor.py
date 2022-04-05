from typing import List, Optional

from chalicelib.data.base.base_document_extractor import DocumentExtractor
from chalicelib.models.compound import Compound


class CompoundNoSQLExtractor(DocumentExtractor):
    def read_compounds(self) -> List[Compound]:
        raise NotImplementedError

    def read_compound_ids(self) -> List[int]:
        raise NotImplementedError

    def read_compound_from_id(self, compound_id: int) -> Optional[Compound]:
        raise NotImplementedError
