import requests


class Client:
    def __init__(self):
        self.base_url = "https://my-json-server.typicode.com/michael446-github/transformerseducationbot"

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}{endpoint}")
        return response.json().dict()
