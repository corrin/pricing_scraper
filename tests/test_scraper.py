from scraper.core.scraper import Scraper
from scraper.suppliers.dummy.authenticator import DummyAuthenticator
from scraper.suppliers.dummy.page_fetcher import DummyPageFetcher
from scraper.suppliers.dummy.parser import DummyParser


# Define a configuration dictionary for the dummy supplier for testing
dummy_supplier_config = {
    "name": "dummy_supplier",
    "authenticator_class": DummyAuthenticator,
    "page_fetcher_class": DummyPageFetcher,
    "parser_class": DummyParser,
}


def test_dummy_scraper_returns_list() -> None:
    """
    Test that the scraper with the dummy supplier returns a list.
    """
    scraper = Scraper()
    product_data_list = scraper.scrape_supplier(config=dummy_supplier_config)

    assert isinstance(product_data_list, list)


def test_dummy_scraper_returns_expected_number_of_products() -> None:
    """
    Test that the scraper with the dummy supplier returns the expected
    number of products.
    (Assuming the dummy parser is expected to return a specific number of items)
    """
    # You would need to know the expected output of your DummyParser
    # For this example, let's assume the DummyParser always returns 2 products
    expected_product_count = 2

    scraper = Scraper()
    product_data_list = scraper.scrape_supplier(config=dummy_supplier_config)

    assert len(product_data_list) == expected_product_count


# Add more tests here to cover different aspects of the dummy scraper,
# or tests for other components/suppliers as you add them.
