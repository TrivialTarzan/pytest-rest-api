"""
This file serves as a testing ground for experimenting with different functions and classes 
before integrating them into the actual test files
"""
import sys
import os
from config.config_loader import ConfigLoader
from api_client.api_client import ApiClient
# import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

config = ConfigLoader()


api_client = ApiClient()
url = "https://thinking-tester-contact-list.herokuapp.com"
endpoint_login = config.endpoint_login()
endpoint_get_list = config.endpoint_get_contact_list()
email = config.email()
password = config.password()
token = config.token()

payload_login = {
    "email": email, 
    "password": password
}
headers_login = {}

response_login = api_client.post(endpoint_login, headers_login, payload_login)
print("Response Status Code:", response_login.status_code)
print(response_login.json())
assert response_login.status_code == 200

payload_get_list = {}
headers_get_list = {
    'Authorization': f'Bearer {token}'
}
print(token)
response = api_client.get(endpoint_get_list, headers_get_list, payload_get_list)
print("Response Status Code:", response.status_code)
print(response.json())
assert response.status_code == 200