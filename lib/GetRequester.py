import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send a GET request to self.url and return the raw response body (bytes)."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Parse the response body into Python data (a list of dicts)."""
        return json.loads(self.get_response_body())
