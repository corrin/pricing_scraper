from __future__ import annotations
import requests
from typing import Generator
from scraper.interfaces.page_fetcher import PageFetcher
import logging


class DummyPageFetcher(PageFetcher):
    """
    Dummy page fetcher for demonstration purposes.
    """

    def __init__(self: DummyPageFetcher, config: dict) -> None:
        """
        Initializes the DummyPageFetcher with configuration.
        """
        self.config = config
        logging.info(
            "DummyPageFetcher: Initialized with config: %s", config.get("name")
        )

    def fetch_pages(
        self: DummyPageFetcher, session: requests.Session
    ) -> Generator[str, None, None]:
        """
        Simulates fetching pages and yields dummy HTML content.
        """
        logging.info("DummyPageFetcher: Simulating fetching pages.")
        # Yield some dummy HTML content once for the test
        yield "<html><body><h1>Dummy Page 1</h1></body></html>"
