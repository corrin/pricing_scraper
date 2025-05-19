import abc
import requests
from typing import List, Generator
from scraper.interfaces.page_fetcher import PageFetcher

class DummyPageFetcher(PageFetcher):
    """
    Dummy page fetcher for demonstration purposes.
    """
    def fetch_pages(self, session: requests.Session) -> Generator[str, None, None]:
        """
        Simulates fetching pages and yields dummy HTML content.
        """
        print("DummyPageFetcher: Simulating fetching pages.")
        # Yield some dummy HTML content a few times
        yield "<html><body><h1>Dummy Page 1</h1></body></html>"
        yield "<html><body><h1>Dummy Page 2</h1></body></html>"
        yield "<html><body><h1>Dummy Page 3</h1></body></html>"