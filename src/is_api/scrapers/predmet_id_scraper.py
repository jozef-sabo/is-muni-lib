from typing import Optional
from bs4 import BeautifulSoup

from is_api.attributes.predmet_id_attributes import PredmetIdAttributes
from is_api.scrapers.scraper import Scraper
from is_api.utils.requestor import Requestor


class PredmetIdScraper(Scraper):
    URL = "https://is.muni.cz/auth/ucitel/statistika_kreditu"

    def __init__(self, requestor: Requestor):
        super().__init__(requestor)

    def request(self, request_attributes: PredmetIdAttributes):

        return super()._request("POST", self.URL, request_attributes)

    def extract_information(self) -> Optional[int]:
        if self._last_content is None:
            raise ValueError("This call must be preceded by a request() call")

        soup = BeautifulSoup(self._last_content, "html.parser")

        ## *input(name=predmet)
        input_predmet_id = soup.find("input", {"name": "predmet"})
        if not input_predmet_id:
            try:
                # subject not found, but correct privileges
                soup.find("main", {"id": "app_content"}).select("div > h3")[0].get_text()
                return None
            except IndexError:
                raise ValueError("Scraped data not in predicted format. Are credentials correct? Is subject name correct?")

        try:
            value = int(input_predmet_id.attrs["value"])
        except (IndexError, ValueError) as e:
            raise ValueError("Cannot find the requested value. Are credentials correct?", e)

        return value