from dataclasses import dataclass

from src.is_api.attributes.attributes import Attributes

@dataclass
class OdborIdsAttributes(Attributes):
    predmet_id : int

    def params(self):
        return None

    def data(self):
        data = {
            "zuv_predmet": self.predmet_id,
            "masedlestav_ukonc": 1,
            "masedlestav_neaktiv": 1,
            "masedleobory": 1
        }

        return data