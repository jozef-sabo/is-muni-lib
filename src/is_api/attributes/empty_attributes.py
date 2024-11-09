from dataclasses import dataclass

from is_api.attributes.attributes import Attributes


@dataclass
class EmptyAttributes(Attributes):
    def params(self):
        return None

    def data(self):
        return None
