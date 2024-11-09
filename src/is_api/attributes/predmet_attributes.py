from dataclasses import dataclass
from typing import Optional, List

from src.is_api.attributes.attributes import Attributes
from src.is_api.data.combined_mark import CombinedMark
from src.is_api.data.mark import Mark
from src.is_api.data.operator import Operator


@dataclass
class PredmetAttributes(Attributes):
    predmet_id : int

    marks: Optional[List[Mark]] = None
    combined_marks: Optional[List[CombinedMark]] = None

    fields: Optional[List[int]] = None

    operator: Operator = Operator.AND

    finished: bool = True
    inactive: bool = True


    def params(self):
        return None

    def data(self):
        data = {
            "zuv_predmet": self.predmet_id,
            "operator": self.operator.value,
            "zmena_vybrdalomst": "Upřesnění omezení"
        }

        if self.marks or self.combined_marks:
            data["masedleznamka"] = 1

        if self.finished:
            data["masedlestav_ukonc"] = 1

        if self.inactive:
            data["masedlestav_neaktiv"] = 1

        if self.marks:
            data["xhodnomznamka"] = [f"kon:{mark.value}" for mark in self.marks]

        if self.combined_marks:
            data["xhodnomznamka"] = [f"{mark.value}" for mark in self.combined_marks]

        if self.fields:
            data["masedleobory"] = 1
            data["xhodnomobory"] = [f"{filed}" for filed in self.fields]

        return data