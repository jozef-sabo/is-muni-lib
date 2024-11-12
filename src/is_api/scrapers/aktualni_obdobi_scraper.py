from bs4 import BeautifulSoup

from is_api.attributes.empty_attributes import EmptyAttributes
from is_api.attributes.predmet_attributes import PredmetAttributes
from is_api.scrapers.scraper import Scraper
from is_api.utils.requestor import Requestor


class AktualniObdobiScraper(Scraper):
    URL = "https://is.muni.cz/auth/ucitel/statistika_kreditu"

    def __init__(self, requestor: Requestor):
        super().__init__(requestor)

    def request(self, request_attributes: EmptyAttributes = None):
        request_attributes = EmptyAttributes()

        return super()._request("POST", self.URL, request_attributes)

    def extract_information(self) -> int:
        if self._last_content is None:
            raise ValueError("This call must be preceded by a request() call")

        soup = BeautifulSoup(self._last_content, "html.parser")

        button_obdobi = soup.find("button", {"class": "obd-minus button clear isi-zobacek-vlevo-bold"})
        if not button_obdobi:
            raise ValueError("Scraped data not in predicted format. Are credentials correct?")

        try:
            value = int(button_obdobi.get("data-obd"))
        except (IndexError, ValueError) as e:
            raise ValueError("Cannot find the requested value. Are credentials correct?", e)

        return value
