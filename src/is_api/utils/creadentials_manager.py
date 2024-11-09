from src.is_api.utils.credentials import Credentials


class CredentialsManager:

    def __init__(self, creds: Credentials):
        self.__creds = creds

    @property
    def cookie(self):
        return f"__Host-issession={self.__creds.session}; __Host-iscreds={self.__creds.creds}"
