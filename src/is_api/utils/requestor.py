import requests

from typing import Optional, Union, Any

from src.is_api.utils.creadentials_manager import CredentialsManager
from src.is_api.utils.headers import Headers

class Requestor:

    def __init__(self, credentials: CredentialsManager, headers: Optional[Headers]):
        if headers is None:
            headers = Headers()

        self.__headers = headers
        self.__creds = credentials

    def request(self, method: str, url: Union[str, bytes], params: Any = None, data: Any = None):
        return requests.request(method=method, url=url, params=params, data=data, headers=self.__get_headers())

    def get(self, url: Union[str, bytes], params: Any):
        return self.request("GET", url=url, params=params)

    def post(self, url: Union[str, bytes], data: Any = None):
        return self.request("POST", url, data=data)

    def __get_headers(self):
        headers = self.__headers.headers_dict.copy()
        headers["Cookie"] = self.__creds.cookie

        return headers
