import abc
import requests

class Authenticator(abc.ABC):
    """
    Abstract base class for authenticators.
    Defines the interface for handling supplier login and sessions.
    """
    @abc.abstractmethod
    def login(self) -> requests.Session:
        """
        Performs the login process and returns an authenticated requests session.
        """
        pass

    @abc.abstractmethod
    def get_session(self) -> requests.Session:
        """
        Returns the current authenticated requests session.
        """
        pass