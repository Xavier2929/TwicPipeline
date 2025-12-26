from bs4 import BeautifulSoup
from TwicRequests import TwicRequests
import re


class GetLatestTwic:
    def __init__(self, mainTwicUrl):
        self.url = mainTwicUrl

    def get(self):
        twicRequest = TwicRequests()

        response = twicRequest.get(self.url)
        twic_number = self.get_twic_number(response)
        return twic_number

    def get_twic_number(self, response):

        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(" ", strip=True)
        match = re.search(r"The Week in Chess\s+(\d+)", text)
        if match:
            return (match.group(1))

        else:
            raise Exception("No se pudo encontrar el latest issue")
