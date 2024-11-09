from is_api.utils.credentials import Credentials


class ValueCredentials(Credentials):
    def __init__(self, issession: str, iscreds: str):

        super().__init__(issesion=issession, iscreds=iscreds)
