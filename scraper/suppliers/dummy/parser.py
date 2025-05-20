from __future__ import annotations
from typing import List
from scraper.interfaces.parser import Parser
from scraper.models.product import ProductData
import logging


class DummyParser(Parser):
    """
    Dummy parser for demonstration purposes.
    """

    def __init__(self: DummyParser, config: dict) -> None:
        """
        Initializes the DummyParser with configuration.
        """
        self.config = config
        logging.info(f"DummyParser: Initialized with config: {config.get('name')}")

    def parse(self: DummyParser, html_content: str) -> List[ProductData]:
        """
        Simulates parsing HTML content and returns dummy ProductData objects.
        """
        logging.info(f"DummyParser: Simulating parsing content: {html_content[:50]}...")
        # Return a list of dummy ProductData objects
        return [
            ProductData(name="Dummy Product 1", sku="DP001", price=10.0),
            ProductData(name="Dummy Product 2", sku="DP002", price=20.0, stock=5),
        ]
