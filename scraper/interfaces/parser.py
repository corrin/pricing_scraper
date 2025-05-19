import abc
from typing import List
from ..models.product import ProductData

class Parser(abc.ABC):
    """
    Abstract base class for parsers.
    Defines the interface for parsing raw page content into product data.
    """
    @abc.abstractmethod
    def parse(self, html_content: str) -> List[ProductData]:
        """
        Parses the raw HTML content and returns a list of ProductData objects.
        """
        pass