# scraper/suppliers/steel_and_tube/scrape.py

import logging
from scraper.core.scraper import Scraper
from scraper.suppliers.steel_and_tube.authenticator import SteelAndTubeAuthenticator
from scraper.suppliers.steel_and_tube.page_fetcher import SteelAndTubePageFetcher
from scraper.suppliers.steel_and_tube.parser import SteelAndTubeParser

def run(config):
    """
    Runs the scraper specifically for Steel and Tube using the provided configuration.
    This function serves as the main entry point for the Steel and Tube scraper.
    """
    logging.info("Running Steel and Tube scraper...")

    # Use the provided configuration to instantiate components
    # The config dictionary should contain 'authenticator_class', 'page_fetcher_class',
    # and 'parser_class', as well as any supplier-specific parameters like credentials.
    # We assume these class references are added to the config by the supplier_manager
    # before calling this run function. However, based on the supplier_manager code,
    # it passes the config from the YAML, which does NOT contain class references.
    # This means the supplier's run function is responsible for getting the classes
    # and instantiating them with the config.

    # Re-instantiate components using the config passed from supplier_manager
    authenticator = SteelAndTubeAuthenticator(config)
    page_fetcher = SteelAndTubePageFetcher(config)
    parser = SteelAndTubeParser(config)

    # Configure the scraper for Steel and Tube using the instantiated components
    steel_and_tube_config = {
        'authenticator_class': authenticator.__class__, # Pass the class reference
        'page_fetcher_class': page_fetcher.__class__,   # Pass the class reference
        'parser_class': parser.__class__,       # Pass the class reference
        'name': config.get('name', 'steel_and_tube'), # Get name from config if available
        **config # Include all other config parameters
    }


    scraper = Scraper()
    scraped_data = scraper.scrape_supplier(steel_and_tube_config)

    logging.info(f"Steel and Tube scraper finished. Scraped {len(scraped_data)} product(s).")
    # Here you would typically export the data
    # For now, just log the scraped data (or a summary)
    # for product in scraped_data:
    #     logging.info(product)