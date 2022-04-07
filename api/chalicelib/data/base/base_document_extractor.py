from abc import abstractmethod
from typing import Optional, List

from chalicelib.data.base.base_extractor import CompoundExtractor
from chalicelib.models.compound import Compound


class CompoundDocumentExtractor(CompoundExtractor):
    """
    Extracts compound data from document stores

    ...

    Methods
    -------
    read_compounds()
        Reads and returns data for all compounds

    read_compound_ids()
        Reads and returns IDs for all compounds

    read_compound_from_id(compound_id)
        Reads and returns data for one compound
    """

    @abstractmethod
    def read_compounds(self) -> List[Compound]:
        """
        Reads and returns data for all compounds

        Parameters
        ----------
        None

        Returns
        -------
        list
            List of Compounds
        """
        pass

    @abstractmethod
    def read_compound_ids(self) -> List[int]:
        """
        Reads and returns IDs for all compounds

        Parameters
        ----------
        None

        Returns
        -------
        list
            List of Compound IDs
        """
        pass

    @abstractmethod
    def read_compound_from_id(self, compound_id: int) -> Optional[Compound]:
        """
        Reads and returns data for one compound

        Parameters
        ----------
        compound_id (int): ID of compound to retrieve data of

        Returns
        -------
        dict
            Data for a single compound
        """
        pass
