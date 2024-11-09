from bs4 import BeautifulSoup

from src.is_api.attributes.predmet_attributes import PredmetAttributes
from src.is_api.scrapers.scraper import Scraper
from src.is_api.utils.requestor import Requestor


class StatistikaKredituScraper(Scraper):
    URL = "https://is.muni.cz/auth/ucitel/statistika_kreditu"

    def __init__(self, requestor: Requestor):
        super().__init__(requestor)

    def request(self, request_attributes: PredmetAttributes):
        if not isinstance(request_attributes, PredmetAttributes):
            raise AttributeError("Request Attributes must be of a class PredmetAttributes")

        return super()._request("POST", self.URL, request_attributes)

    def extract_information(self) -> int:
        if self._last_content is None:
            raise ValueError("This call must be preceded by a request() call")

        soup = BeautifulSoup(self._last_content, "html.parser")

        ## students covered
        ## div(zu_pocty) -> b - first
        class_pocty = soup.find("div", {"class": "zu_pocty"})
        if not class_pocty:
            raise ValueError("Scraped data not in predicted format. Are credentials correct? Is subject id correct?")

        if int(class_pocty.select("b:nth-of-type(1)")[0].get_text()) == 0:
            return 0

        ## table(data1) -> 3x TR - last -> 3x TD - middle
        class_data1 = soup.find("table", {"class": "data1"})

        try:
            value = int(class_data1.select("tr:nth-of-type(3) > td:nth-of-type(2)")[0].get_text())
        except (IndexError, ValueError) as e:
            raise ValueError("Cannot find the requested value. Are credentials correct?", e)

        return value