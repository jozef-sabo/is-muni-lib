from abc import ABC, abstractmethod


class Attributes(ABC):

    @abstractmethod
    def data(self):
        raise NotImplementedError

    @abstractmethod
    def params(self):
        raise NotImplementedError