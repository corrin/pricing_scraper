# scraper/core/scraper.py

from typing import List, Dict, Any

# Assuming interfaces and models are in these paths relative to the project root
from scraper.interfaces.authenticator import Authenticator
from scraper.interfaces.page_fetcher import PageFetcher
from scraper.interfaces.parser import Parser
from scraper.models.product import ProductData

class Scraper:
    """
    Core orchestration logic for scraping a specific supplier.

    This class is responsible for coordinating the steps of authentication,
    page fetching, and parsing using the provided interface implementations
    based on the supplier configuration.
    """

    def scrape_supplier(self, config: Dict[str, Any]) -> List[ProductData]:
        """
        Orchestrates the scraping process for a single supplier.

        Args:
            config: A dictionary containing configuration for the supplier,
                    including the classes to use for Authenticator,
                    PageFetcher, and Parser, and any specific parameters
                    they might need. Expected keys:
                    - 'authenticator_class': The concrete Authenticator class.
                    - 'page_fetcher_class': The concrete PageFetcher class.
                    - 'parser_class': The concrete Parser class.
                    - Additional keys for specific implementation parameters.

        Returns:
            A list of ProductData objects extracted from the supplier's pages.
        """
        authenticator_class = config.get('authenticator_class')
        page_fetcher_class = config.get('page_fetcher_class')
        parser_class = config.get('parser_class')

        if not all([authenticator_class, page_fetcher_class, parser_class]):
            raise ValueError("Supplier configuration must include 'authenticator_class', 'page_fetcher_class', and 'parser_class'")

        # Instantiate components based on configuration
        # Assuming config contains necessary args for instantiation
        authenticator: Authenticator = authenticator_class(config)
        page_fetcher: PageFetcher = page_fetcher_class(config)
        parser: Parser = parser_class(config)

        # 1. Authenticate
        # The login method is expected to handle session management internally
        # and potentially return a session object or modify the fetcher/parser
        # to use the authenticated session. For simplicity here, we assume
        # the authenticator modifies the state of the fetcher/parser or
        # provides a session object that the fetcher/parser can use.
        # A common pattern is for login to return a session object.
        session = authenticator.login()

        # Pass the session to the page fetcher if needed
        # This is a common pattern, but depends on interface design.
        # Assuming PageFetcher's fetch_pages method can accept a session.
        # If the session is managed internally by the fetcher after login,
        # this step might be different or not needed.
        # Let's assume fetch_pages takes the session as an argument.
        # If the session is managed internally by the fetcher, the fetcher
        # instance itself would need to be passed to the authenticator
        # or the authenticator would need access to the fetcher instance.
        # A simpler approach for core logic is that login returns the session
        # and fetch_pages accepts it.
        # If login doesn't return a session, the authenticator might
        # configure the fetcher directly. Let's stick to login returning session.

        # 2. Fetch pages
        # fetch_pages is expected to handle pagination and yield page contents
        all_product_data: List[ProductData] = []
        for page_content in page_fetcher.fetch_pages(session=session):
            # 3. Parse page content
            # parse is expected to return a list of ProductData objects for the page
            product_data_on_page: List[ProductData] = parser.parse(page_content)
            all_product_data.extend(product_data_on_page)

        # 4. Return collected data
        return all_product_data

# Example Usage (for demonstration, not part of core logic)
# from scraper.interfaces.authenticator import DummyAuthenticator
# from scraper.interfaces.page_fetcher import DummyPageFetcher
# from scraper.interfaces.parser import DummyParser
#
# if __name__ == "__main__":
#     # Example configuration for a dummy supplier
#     dummy_config = {
#         'authenticator_class': DummyAuthenticator,
#         'page_fetcher_class': DummyPageFetcher,
#         'parser_class': DummyParser,
#         # Add any specific parameters needed by dummy implementations
#         'dummy_auth_param': 'auth_value',
#         'dummy_fetch_param': 'fetch_value',
#         'dummy_parse_param': 'parse_value',
#     }
#
#     scraper = Scraper()
#     try:
#         scraped_data = scraper.scrape_supplier(dummy_config)
#         print(f"Scraped {len(scraped_data)} product(s).")
#         for product in scraped_data:
#             print(product)
#     except ValueError as e:
#         print(f"Error during scraping: {e}")