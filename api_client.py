import requests

class APIClient:
    def __init__(self, base_url, length):
        self.url = base_url + "?length=" + str(length)

    def fetch(self):
        return requests.get(self.url).json()