import requests
from config.config_loader import ConfigLoader


class ApiClient:
    def __init__(self, client = 'ContactList'):
        self.client = client
        self.config = ConfigLoader.load()
        self.BASE_URL = self.config[self.client]['base_url']
    
    def set_client(self, client: str):
        self.client = client
        self.BASE_URL = self.config[self.client]['base_url']
        
    def get(self, endpoint: str, headers = {}, payload = {}):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, headers=headers, data=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"GET request failed: {e}")
            raise
        return response

    def post(self, endpoint: str, headers = {}, payload = {}):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"POST request failed: {e}")
            raise
        return response
    
    def patch(self, endpoint: str, headers = {}, payload = {}):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.patch(url, headers=headers, json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"PATCH request failed: {e}")    

    def put(self, endpoint: str, data: dict = None):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.put(url, json=data)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"PUT request failed: {e}")
            raise
        return response

    def delete(self, endpoint: str, headers = {}):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"DELETE request failed: {e}")
            raise
        return response