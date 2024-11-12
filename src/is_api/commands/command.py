import abc
from abc import ABC


class Command(ABC):

    @abc.abstractmethod
    def url(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def method(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def data(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def params(self) -> dict:
        raise NotImplementedError
