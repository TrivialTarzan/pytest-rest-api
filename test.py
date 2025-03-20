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
endpoint_delete = config.endpoint_delete_contact()
endpoint_post = config.endpoint_add_contact()
endpoint_update_user = config.endpoint_update_user()
email = config.email()
password = config.password()

payload_login = {
    "email": email, 
    "password": password
}
headers_login = {}

response_login = api_client.post(endpoint_login, headers_login, payload_login)
print("Response Status Code:", response_login.status_code)
print(response_login.json())
assert response_login.status_code == 200

token = response_login.json()['token']

payload_get_list = {}
headers_get_list = {
    'Authorization': f'Bearer {token}'
}
print(token)
response = api_client.get(endpoint_get_list, headers_get_list, payload_get_list)
print("Response Status Code:", response.status_code)
print(response.json())

id = response.json()[0]['_id']
print(id)
assert response.status_code == 200

new_creds1 = {
        "new_first_name": "Bogdan",
        "new_last_name": "Bogdanov",
        "new_email": "newmail@yahoo.edu",
        "new_password": "666"
}
    
default_creds = {
    "firstName": config.first_name(),
    "lastName": config.last_name(),
    "email": config.email(),
    "password": config.password()
}
    
payload_update = {
    "firstName": new_creds1["new_first_name"],
    "lastName": new_creds1["new_last_name"],
    "email": new_creds1["new_email"],
    "password": new_creds1["new_password"]
}

response_update = api_client.patch(f"{endpoint_update_user}", headers_get_list, payload_update)
print(response_update.json())

# response_delete = api_client.delete(f"{endpoint_delete}{id}", headers_get_list)
# assert response_delete.status_code == 200