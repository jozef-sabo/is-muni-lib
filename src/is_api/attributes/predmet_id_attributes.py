from dataclasses import dataclass

from is_api.attributes.attributes import Attributes
from is_api.data.faculty import Faculty
from is_api.data.term import Term


@dataclass
class PredmetIdAttributes(Attributes):
    predmet_name : str
    faculty: Faculty
    term: Term

    def params(self):
        return None

    def data(self):
        data = {
            "skpm_kt": self.predmet_name,
            "skpm_vt": "Vybrat",
            "obdobi": self.term.value,
            "fakulta": self.faculty.value
        }


        return data