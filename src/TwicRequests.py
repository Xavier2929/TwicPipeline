import requests


class TwicRequests:

    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36",
            "Accept": "application/json,text/html;q=0.9,*/*;q=0.8"
        }

    def get(self, request_url):
        response = requests.get(request_url, headers=self.headers)
        is_response_valid = self.is_request_200Ok_result(response)
        if is_response_valid == False:
            raise Exception(f"the response from the request to {request_url} ")
        return response

    def is_request_200Ok_result(self, response):
        if response is not None and response.status_code == 200:
            return True
        return False
