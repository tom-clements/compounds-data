from abc import abstractmethod
from typing import Optional

from chalicelib.data.base.base_extractor import CompoundExtractor


class CompoundImageExtractor(CompoundExtractor):
    """
    Extracts compound image data from image stores

    ...

    Methods
    -------
    read_compound_html_from_id(compound_id)
        Reads image data for one compound and returns a HTML page displaying the compound image

    read_compound_image_from_id(compound_id)
        Reads image data for one compound and returns a png image of the compound
    """

    @abstractmethod
    def read_compound_html_from_id(self, compound_id: int) -> str:
        """
        Reads image data for one compound and returns a HTML page displaying the compound image

        Parameters
        ----------
        compound_id (int): ID of compound to retrieve data of

        Returns
        -------
        str
            HTML string containing the image of the compound
        """
        pass

    @abstractmethod
    def read_compound_image_from_id(self, compound_id: int) -> Optional[bytes]:
        """
        Reads image data for one compound and returns a HTML page displaying the compound image

        Parameters
        ----------
        compound_id (int): ID of compound to retrieve data of

        Returns
        -------
        bytes
            bytes of png data for the compound image
        """
        pass
