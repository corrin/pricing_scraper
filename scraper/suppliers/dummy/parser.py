from typing import List
from scraper.interfaces.parser import Parser
from scraper.models.product import ProductData

class DummyParser(Parser):
    """
    Dummy parser for demonstration purposes.
    """
    def parse(self, html_content: str) -> List[ProductData]:
        """
        Simulates parsing HTML content and returns dummy ProductData objects.
        """
        print(f"DummyParser: Simulating parsing content: {html_content[:50]}...")
        # Return a list of dummy ProductData objects
        return [
            ProductData(name="Dummy Product 1", sku="DP001", price=10.0),
            ProductData(name="Dummy Product 2", sku="DP002", price=20.0, stock=5),
        ]