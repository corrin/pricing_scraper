from __future__ import annotations
import requests
from scraper.interfaces.authenticator import Authenticator
import logging


class DummyAuthenticator(Authenticator):
    """
    Dummy authenticator for demonstration purposes.
    """

    def __init__(self: DummyAuthenticator, config: dict) -> None:
        """
        Initializes the DummyAuthenticator with configuration.
        """
        self.config = config
        logging.info(
            "DummyAuthenticator: Initialized with config: %s", config.get("name")
        )

    def login(self: DummyAuthenticator) -> requests.Session:
        """
        Simulates a login process.
        """
        logging.info("DummyAuthenticator: Simulating login...")
        # Return a mock session object or None
        return requests.Session()

    def get_session(self: DummyAuthenticator) -> requests.Session:
        """
        Returns a mock session object.
        """
        logging.info("DummyAuthenticator: Providing dummy session.")
        # Return the current session or None
        return requests.Session()  # Or return None if no session is active
