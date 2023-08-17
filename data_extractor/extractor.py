from datetime import datetime
from urllib.parse import urlencode
from uuid import uuid4

import requests


class Extractor:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        # simplest example of vcrpy usage
        response = requests.get(self.url)
        return response.text

    def get_data_with_loop(self) -> list:
        # example of vcrpy usage with loop which will record each request
        pages = []
        for page in range(3):
            response = requests.get(self.url + f"?{urlencode({'page': page})}")
            if response.status_code == 200:
                pages.append(response.text)
            else:
                print(f"Error: {response.status_code}")

        return pages

    def get_data_with_changing_query(self):
        # example of vcrpy usage with query parameters that change between runs (UUID and timestamp)
        # this illustrates a challenge in replaying recorded requests with dynamic parameters
        query_params = {
            "state": str(uuid4()),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        response = requests.get(self.url + f"?{urlencode(query_params)}")
        return response.text
