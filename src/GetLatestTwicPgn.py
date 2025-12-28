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
            pgn_name = zip_file.filelist[0].filename
            pgn_bytes = zip_file.read(pgn_name)
            return pgn_bytes
