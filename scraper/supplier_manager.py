# scraper/supplier_manager.py

import importlib
import os
import logging
import yaml # Import the yaml library

# Dictionary to store loaded supplier run functions and their configurations
_loaded_suppliers = {}
# Dictionary to store the loaded configuration from the YAML file
_supplier_configs = {}

def load_all_suppliers():
    """
    Loads configuration from suppliers.yaml and dynamically finds and loads
    the 'run' function from the 'scrape.py' module in each configured supplier directory.
    """
    logging.info("Loading all configured suppliers...")

    # Load configuration from YAML file
    config_path = "config/suppliers.yaml"
    with open(config_path, 'r') as f:
        global _supplier_configs
        _supplier_configs = yaml.safe_load(f) or {} # Load config, handle empty file
    logging.info(f"Successfully loaded configuration from {config_path}")

    suppliers_dir = "scraper/suppliers"

    # Get list of potential supplier directories
    supplier_dirs = [
        d
        for d in os.listdir(suppliers_dir)
        if os.path.isdir(os.path.join(suppliers_dir, d)) and not d.startswith('__') # Exclude __pycache__ etc.
    ]

    for supplier_name in supplier_dirs:
        # Construct the module path for the supplier's scrape module
        module_path = f"scraper.suppliers.{supplier_name}.scrape"

        # Dynamically import the module
        supplier_scrape_module = importlib.import_module(module_path)

        # Get the 'run' function from the module
        run_function = getattr(supplier_scrape_module, 'run')

        # Store the run function and its configuration
        _loaded_suppliers[supplier_name] = {
            'run_function': run_function,
            'config': _supplier_configs.get(supplier_name, {}) # Get config for this supplier
        }
        logging.info(f"Successfully loaded scraper for supplier: {supplier_name}")


def get_available_suppliers():
    """
    Returns a list of names of successfully loaded suppliers.
    """
    return list(_loaded_suppliers.keys())


def run_supplier(supplier_name: str):
    """
    Runs the scraper for the specified supplier if it has been loaded.
    Passes the supplier's configuration to the run function.
    """
    if supplier_name in _loaded_suppliers:
        logging.info(f"Running scraper for supplier: {supplier_name}")
        supplier_info = _loaded_suppliers[supplier_name]
        run_function = supplier_info['run_function']
        config = supplier_info['config']
        run_function(config) # Call the loaded run function with config
    else:
        logging.warning(f"Scraper for supplier '{supplier_name}' is not available.")