# main.py

# This file is the entry point for the production pricing scraper.
# It handles command-line arguments and initiates the scraping process.

import logging
import argparse
import os
import sys

# Configure basic logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Import functions from the supplier manager
from scraper.supplier_manager import load_all_suppliers, get_available_suppliers, run_supplier


def list_suppliers():
    """
    Lists all configured suppliers by checking directories in scraper/suppliers.
    """
    logging.info("Listing configured suppliers:")
    available_suppliers = get_available_suppliers()
    for supplier in available_suppliers:
        logging.info(f"- {supplier}")


def start_scraping_process(supplier_name: str = None):
    """
    Initiates the main scraper process for the specified supplier(s).
    """
    if supplier_name:
        logging.info(f"Initiating scraper process for supplier: {supplier_name}")
        run_supplier(supplier_name)
        logging.info(f"Scraping process finished for {supplier_name}.")
    else:
        logging.info("Initiating scraper process for all configured suppliers.")
        available_suppliers = get_available_suppliers()

        logging.info(f"Scraping {len(available_suppliers)} suppliers: {', '.join(available_suppliers)}")
        for supplier in available_suppliers:
            run_supplier(supplier)
        logging.info("Scraping process finished for all configured suppliers.")


def set_up_argparse():
    parser = argparse.ArgumentParser(description="Run the production pricing scraper.")
    parser.add_argument(
        "--supplier",
        type=str,
        help="Name of the specific supplier to scrape (e.g., 'steel_and_tube', 'wakefield_metals'). If not specified, all configured suppliers will be scraped.",
    )
    parser.add_argument(
        "--list-suppliers",
        action="store_true",
        help="List all configured suppliers instead of scraping.",
    )

    return parser


def main():
    logging.info("Starting pricing scraper production run...")

    # Load all suppliers at the start
    load_all_suppliers()

    parser = set_up_argparse()
    args = parser.parse_args()

    if args.list_suppliers:
        list_suppliers()
    else:
        # Call the main process function with the parsed supplier name
        start_scraping_process(args.supplier)

    logging.info("Pricing scraper production script finished.")


if __name__ == "__main__":
    main()
