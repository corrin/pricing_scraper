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

def list_suppliers():
    """
    Lists all configured suppliers by checking directories in scraper/suppliers.
    Exits if the directory is not found.
    """
    logging.info("Listing configured suppliers:")
    suppliers_dir = 'scraper/suppliers'

    supplier_dirs = [d for d in os.listdir(suppliers_dir) if os.path.isdir(os.path.join(suppliers_dir, d))]
    for supplier in supplier_dirs:
        logging.info(f"- {supplier}")


def start_scraping_process(supplier_name: str = None):
    """
    Initiates the main scraper process.
    This function is the entry point that would handle loading configurations,
    importing components, and running the scraper for the specified supplier(s).
    """
    if supplier_name:
        logging.info(f"Initiating scraper process for supplier: {supplier_name}")
        # In a real application, logic to load config and run scraper for
        # the specific supplier would be called here.
        logging.info(f"Simulating scraping for supplier: {supplier_name}") # Placeholder output
    else:
        logging.info("Initiating scraper process for all configured suppliers.")
        # In a real application, logic to load configs and run scraper for
        # all suppliers would be called here.
        logging.info("Simulating scraping for all suppliers.") # Placeholder output

def set_up_argparse():
    parser = argparse.ArgumentParser(description="Run the production pricing scraper.")
    parser.add_argument(
        "--supplier",
        type=str,
        help="Name of the specific supplier to scrape (e.g., 'steel_and_tube', 'wakefield_metals'). If not specified, all configured suppliers will be scraped.",
        # Removed 'choices' to avoid hardcoding the list of suppliers in main.py
    )
    parser.add_argument(
        "--list-suppliers",
        action="store_true",
        help="List all configured suppliers instead of scraping."
    )

    return parser

def main():
    logging.info("Starting pricing scraper production run...")

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