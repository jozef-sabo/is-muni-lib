from typing import Optional

class Headers:
    DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
    DEFAULT_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    DEFAULT_ACCEPT_ENCODING = "gzip, deflate, br, zstd"
    DEFAULT_ORIGIN = "https://is.muni.cz"

    def __init__(self, user_agent: Optional[str] = None, accept: Optional[str] = None,
                 accept_encoding: Optional[str] = None, origin: Optional[str] = None, **kwargs):

        if user_agent is not None and not isinstance(user_agent, str):
            raise ValueError("User Agent must be string or None")

        if accept is not None and not isinstance(accept, str):
            raise ValueError("Accept must be string or None")

        if accept_encoding is not None and not isinstance(accept_encoding, str):
            raise ValueError("Accept Encoding must be string or None")

        if origin is not None and not isinstance(origin, str):
            raise ValueError("Origin must be string or None")

        headers = {}
        if kwargs is not None:
            headers = kwargs.copy()

        own_headers = {
            "User-Agent": user_agent if user_agent is not None else self.DEFAULT_USER_AGENT,
            "Accept": accept if accept is not None else self.DEFAULT_ACCEPT,
            "Accept-Encoding": accept_encoding if accept_encoding is not None else self.DEFAULT_ACCEPT_ENCODING,
            "Origin": origin if origin is not None else self.DEFAULT_ORIGIN
        }

        headers.update(own_headers)

        self.__headers = headers

    @property
    def headers_dict(self) -> dict:
        return self.__headers.copy()
