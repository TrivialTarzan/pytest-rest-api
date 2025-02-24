import requests
from requests import Response
from config.config_loader import ConfigLoader


class ApiClient:
    def __init__(self, client: str = 'ContactList'):
        self.client = client
        self.config = ConfigLoader.load()
        self.BASE_URL = self.config[self.client]['base_url']
    
    def set_client(self, client: str):
        self.client = client
        self.BASE_URL = self.config[self.client]['base_url']
        
    def get(self, endpoint: str, params: dict = None) -> Response:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"GET request failed: {e}")
            raise
        return response

    def post(self, endpoint: str, headers: dict = {}, payload: dict = {}) -> Response:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"POST request failed: {e}")
            raise
        return response

    def put(self, endpoint: str, data: dict = None) -> Response:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.put(url, json=data)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"PUT request failed: {e}")
            raise
        return response

    def delete(self, endpoint: str) -> Response:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"DELETE request failed: {e}")
            raise
        return response