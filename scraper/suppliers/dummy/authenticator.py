import requests
from scraper.interfaces.authenticator import Authenticator

class DummyAuthenticator(Authenticator):
    """
    Dummy authenticator for demonstration purposes.
    """
    def login(self) -> requests.Session:
        """
        Simulates a login process.
        """
        print("DummyAuthenticator: Simulating login...")
        # Return a mock session object or None
        return requests.Session()

    def get_session(self) -> requests.Session:
        """
        Returns a mock session object.
        """
        print("DummyAuthenticator: Providing dummy session.")
        # Return the current session or None
        return requests.Session() # Or return None if no session is active