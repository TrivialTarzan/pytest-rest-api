import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config_loader import load
from api_client import ApiClient

config = load()
bearer = None

def endpoint():
    return config['ContactList']['endpoints']['login_user']
def email():
    return config['ContactList']['first_user']['email']
def password():
    return config['ContactList']['first_user']['password']
def first_name():
    return config['ContactList']['first_user']['first_name']
def last_name():
    return config['ContactList']['first_user']['last_name']
def id():
    return config['ContactList']['first_user']['id']    


def test_login(api_client, endpoint, email, password, first_name, last_name, id):
    global bearer
    
    payload = {
        "email": email, 
        "password": password
    }
    headers = {}

    response = api_client.post(endpoint, headers, payload)
    print("Response Status Code:", response.status_code)
    assert response.status_code == 200
    
    data = response.json()['user']
    bearer = response.json()['token']
    
    assert data['email'] == email
    assert data['firstName'] == first_name
    assert data['lastName'] == last_name
    assert data['_id'] == id
 
   
def test_logout(api_client, endpoint, token):
    payload = {}
    headers = {
    'Authorization': f'Bearer {token}'
    }
    
    response = api_client.post(endpoint, headers, payload)
    
    
api_client = ApiClient()
endpoint = endpoint()
email = email()
password = password()
first_name = first_name()
last_name = last_name()
id = id() 
    
test_login(api_client, endpoint, email, password, first_name, last_name, id)
test_logout(api_client, endpoint, bearer)    