from __future__ import annotations
import requests
from scraper.interfaces.authenticator import Authenticator
import logging


class SteelAndTubeAuthenticator(Authenticator):
    """
    Authenticator for Steel and Tube.
    """

    def __init__(self: SteelAndTubeAuthenticator, config: dict) -> None:
        """
        Initializes the SteelAndTubeAuthenticator with configuration.
        """
        self.config = config
        self._session = requests.Session()
        logging.info(
            "SteelAndTubeAuthenticator: Initialized with config for %s",
            config.get("name"),
        )

    def login(self: SteelAndTubeAuthenticator) -> requests.Session:
        """
        Performs the login process for Steel and Tube.
        """
        login_url = self.config.get("login_url")
        username = self.config.get("username")
        password = self.config.get("password")

        if not login_url or not username or not password:
            logging.error("SteelAndTubeAuthenticator: Missing login configuration.")
            raise ValueError # Always terminate immediately on any error
            # In a real scenario, this would raise an exception or handle the error appropriately.
            # For now, we return the session without attempting login.
            return self._session

        logging.info(
            f"SteelAndTubeAuthenticator: Attempting login to {login_url} with user {username}..."
        )

        # Actual form-based login logic
        login_data = {
            'username': username, # Assuming 'username' is the form field name
            'password': password  # Assuming 'password' is the form field name
        }

        try:
            response = self._session.post(login_url, data=login_data)
            response.raise_for_status() # Raise an exception for bad status codes

            logging.info("SteelAndTubeAuthenticator: Login successful.")

        except requests.exceptions.RequestException as e:
            logging.error(f"SteelAndTubeAuthenticator: Login failed: {e}")
            raise ValueError # ALWAYS FAIL IMMEDIATELY ON ANY ERROR
            # Handle login failure
            # Removed the return self._session here as it would be unreachable after raising

        return self._session

    def get_session(self: SteelAndTubeAuthenticator) -> requests.Session:
        """
        Returns the current authenticated requests session.
        """
        if self._session is None:
            self._session = (
                requests.Session()
            )  # Ensure session exists even if login wasn't called
        return self._session
