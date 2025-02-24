"""
This file serves as a testing ground for experimenting with different functions and classes 
before integrating them into the actual test files
"""


from config.config_loader import load
from api_client import ApiClient
import requests

config = load()

def endpoint1():
    return config['ContactList']['endpoints']['login_user']

def endpoint2():
    return config['ContactList']['endpoints']['get_contact_list']

def email():
    return config['ContactList']['first_user']['first_name']

def password():
    return config['ContactList']['first_user']['password']

def base_url():
    return config['ContactList']['base_url']

print(endpoint1())
print(email())
print(password())
print(base_url())

test = ApiClient()
url = base_url()
end = endpoint1()
end2 = endpoint2()

response = test.get(end2)
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
print("Response Text:", response.text) 