from abc import ABCMeta


class Credentials(metaclass=ABCMeta):

    def __init__(self, issesion: str, iscreds: str):
        self. __issession = None
        self.__iscreds = None

        if not isinstance(issesion, str) or not issesion:
            raise AttributeError("IS session must be a string")

        if not isinstance(iscreds, str) or not iscreds:
            raise AttributeError("IS credentials must be a string")

        self.__issession = issesion
        self.__iscreds = iscreds

    @property
    def creds(self) -> str:
        return self.__iscreds

    @property
    def session(self) -> str:
        return self.__issession
