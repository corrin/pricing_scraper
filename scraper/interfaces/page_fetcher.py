import abc
import requests
from typing import List

class PageFetcher(abc.ABC):
    """
    Abstract base class for page fetchers.
    Defines the interface for fetching content from a supplier's website.
    """
    @abc.abstractmethod
    def fetch_pages(self, session: requests.Session) -> List[str]:
        """
        Fetches pages from the supplier's website using the provided session.
        Returns a list of raw page contents (e.g., HTML).
        """
        pass