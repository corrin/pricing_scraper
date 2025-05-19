import abc
from typing import List
from ..models.product import ProductData

class Exporter(abc.ABC):
    """
    Abstract base class for exporters.
    Defines the interface for exporting product data.
    """
    @abc.abstractmethod
    def export_data(self, product_data: List[ProductData]):
        """
        Exports the list of ProductData objects to a specified destination.
        """
        pass