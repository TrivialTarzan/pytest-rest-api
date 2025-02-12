import requests
import pytest
from config.config_loader import load_config

# def base_url():
#     return load_config['Contact List']['base_url']

class ApiClient:
    def __init__(self):
        self.base_url = "https://thinking-tester-contact-list.herokuapp.com"
        
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, headers={}, payload={}):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=headers, json=payload)
        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        return response