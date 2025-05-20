# scraper/suppliers/dummy/scrape.py

import logging
from scraper.core.scraper import Scraper
from scraper.suppliers.dummy.authenticator import DummyAuthenticator
from scraper.suppliers.dummy.page_fetcher import DummyPageFetcher
from scraper.suppliers.dummy.parser import DummyParser

def run(config):
    """
    Runs the scraper specifically for the Dummy supplier using the provided configuration.
    This function serves as the main entry point for the Dummy scraper.
    """
    logging.info("Running Dummy supplier scraper...")

    # Use the provided configuration to instantiate components
    # The config dictionary should contain 'authenticator_class', 'page_fetcher_class',
    # and 'parser_class', as well as any supplier-specific parameters.
    # We assume these class references are added to the config by the supplier_manager
    # before calling this run function. However, based on the supplier_manager code,
    # it passes the config from the YAML, which does NOT contain class references.
    # This means the supplier's run function is responsible for getting the classes
    # and instantiating them with the config.

    # Instantiate components using the config passed from supplier_manager
    authenticator = DummyAuthenticator(config)
    page_fetcher = DummyPageFetcher(config)
    parser = DummyParser(config)

    # Configure the scraper for Dummy using the instantiated components
    dummy_config = {
        'authenticator_class': authenticator.__class__, # Pass the class reference
        'page_fetcher_class': page_fetcher.__class__,   # Pass the class reference
        'parser_class': parser.__class__,       # Pass the class reference
        'name': config.get('name'), # Get name from config if available
        **config # Include all other config parameters
    }


    scraper = Scraper()
    scraped_data = scraper.scrape_supplier(dummy_config)

    logging.info(f"Dummy supplier scraper finished. Scraped {len(scraped_data)} product(s).")
    # Here you would typically export the data
    # For now, just log the scraped data (or a summary)
    # for product in scraped_data:
    #     logging.info(product)