"""
This file serves as a testing ground for experimenting with different functions and classes 
before integrating them into the actual test files
"""
import sys
import os
from config.config_loader import ConfigLoader
from api_client.api_client import ApiClient
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

config = ConfigLoader()


api_client = ApiClient()
url = "https://thinking-tester-contact-list.herokuapp.com"
endpoint = config.endpoint_login()
email = config.email()
password = config.password()

payload = {
    "email": email, 
    "password": password
}
headers = {}

response = api_client.post(endpoint, headers, payload)
print("Response Status Code:", response.status_code)
assert response.status_code == 200