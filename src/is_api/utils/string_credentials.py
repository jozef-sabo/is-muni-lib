import re

from src.is_api.utils.credentials import Credentials


class StringCredentials(Credentials):
    COOKIE_FORMAT = r"^__Host-issession=([A-Za-z0-9]+); __Host-iscreds=([A-Za-z0-9]+)$"
    COOKIE_RE = re.compile(COOKIE_FORMAT)

    def __init__(self, cookie: str):

        match = self.COOKIE_RE.match(cookie)

        if not match or len(match.groups()) != 2:
            raise ValueError("Cookie string is not matching a pattern")

        session, creds = match.groups()

        super().__init__(issesion=session, iscreds=creds)
