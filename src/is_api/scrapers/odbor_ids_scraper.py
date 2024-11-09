from bs4 import BeautifulSoup

from is_api.attributes.odbor_ids_attributes import OdborIdsAttributes
from is_api.scrapers.scraper import Scraper
from is_api.utils.requestor import Requestor


class OdborIdsScraper(Scraper):
    URL = "https://is.muni.cz/auth/ucitel/statistika_kreditu"

    def __init__(self, requestor: Requestor):
        super().__init__(requestor)

    def request(self, request_attributes: OdborIdsAttributes):

        return super()._request("POST", self.URL, request_attributes)

    def extract_information(self) -> dict[int, str]:
        if self._last_content is None:
            raise ValueError("This call must be preceded by a request() call")

        soup = BeautifulSoup(self._last_content, "html.parser")

        ## div(radio-group-box)
        odbor_id_div = soup.find("div", {"class": "radio-group-box"})
        if not odbor_id_div:
            try:
                # no fields were found
                soup.find("main", {"id": "app_content"}).select("div > h3")[0].get_text()
                return {}
            except IndexError:
                raise ValueError("Scraped data not in predicted format. Are credentials correct? Is subject name correct?")

        odbor_ids = {}

        try:
            for odbor_input in odbor_id_div.select("label"):
                name = odbor_input.get_text()
                odbor_id = odbor_input.select("input")[0].attrs["value"]
                odbor_ids[odbor_id] = name

        except (IndexError, ValueError) as e:
            raise ValueError("Cannot find the requested value. Are credentials correct?") from e

        return odbor_ids