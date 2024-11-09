import abc
import requests

from typing import Optional

from is_api.attributes.attributes import Attributes
from is_api.utils.requestor import Requestor


class Scraper(metaclass=abc.ABCMeta):

    def __init__(self, requestor: Requestor):
        if not isinstance(requestor, Requestor):
            raise AttributeError("Credentials manager not in the correct format")

        self.__requestor: Requestor = requestor
        self.__last_content: Optional[requests.Response] = None
        self.__last_response: Optional[requests.Response] = None

    @abc.abstractmethod
    def request(self, attributes: Attributes):
        raise NotImplementedError

    @abc.abstractmethod
    def extract_information(self) -> int:
        raise NotImplementedError

    def _request(self, method: str, url: str, attributes: Attributes):
        self._last_response = self.requestor.request(method, url, data=attributes.data(), params=attributes.params())

    @property
    def requestor(self) -> Requestor:
        return self.__requestor

    @property
    def last_response(self):
        return self._last_response

    @property
    def _last_response(self):
        return self.__last_response

    @_last_response.setter
    def _last_response(self, response: Optional[requests.Response]):
        if response is None:
            self.__last_content = None
            self.__last_response = None
            return

        self.__last_content = response.content
        self.__last_response = response

    @property
    def _last_content(self):
        return self.__last_content