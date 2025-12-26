from TwicRequests import TwicRequests
import zipfile
from io import BytesIO


class GetLatestTwicPgn:
    def __init__(self, url):
        self.url = url

    def get(self):
        twic_request = TwicRequests()
        response = twic_request.get(self.url)

        zip_bytes = BytesIO(response.content)
        with zipfile.ZipFile(zip_bytes) as zip_file:
            return zip_file.filelist[0]
