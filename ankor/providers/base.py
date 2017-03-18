from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """ Abstract class for shortener providers. """

    @abstractmethod
    def short(cls, url):
        """ short method should be implemented for each child. """
        ...
