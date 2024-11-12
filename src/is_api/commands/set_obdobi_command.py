from typing import Union

from is_api.commands.command import Command
from is_api.data.term import Term


class SetObdobiCommand(Command):
    URL = "https://is.muni.cz/auth/ucitel/statistika_kreditu"
    METHOD = "GET"

    def __init__(self, obdobi: Union[int, Term], save_preference: bool):

        self.__obdobi: Term = obdobi
        self.__save_preference: bool = save_preference

    @property
    def obdobi(self):
        return self.__obdobi

    @obdobi.setter
    def obdobi(self, obdobi: Union[int, Term]):
        try:
            obdobi = Term(obdobi)
        except ValueError as e:
            raise ValueError("Given Term value is unknown") from e

        self.__obdobi = obdobi

    @property
    def save_preference(self):
        return self.__save_preference

    @save_preference.setter
    def save_preference(self, save_preference: bool):
        self.__save_preference = save_preference

    def url(self):
        return self.URL

    def method(self):
        return self.METHOD

    def params(self) -> dict:
        return  {
            "save_obd_pref": 1 if self.save_preference else 0,
            "obdobi": self.obdobi.value
        }

    def data(self) -> dict:
        return {}
