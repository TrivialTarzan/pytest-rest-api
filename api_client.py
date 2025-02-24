import requests
import pytest
from config.config_loader import ConfigLoader

# def base_url():
#     return load_config['Contact List']['base_url']

class ApiClient:
    def __init__(self):
        self.client = ''
        self.config = ConfigLoader.load()
        self.BASE_URL = self.config['Mocky' if self.client == 'Mocky' else 'ContactList']['base_url']
    
    def set_client(self, client):
        self.client = client     
        
    def get(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, headers={}, payload={}):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.post(url, headers=headers, json=payload)
        return response

    def put(self, endpoint, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.delete(url)
        return response