import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config_loader import ConfigLoader
from api_client.api_client import ApiClient

config = ConfigLoader()


def test_login(api_client, endpoint, email, password, first_name, last_name, id):
    payload = {
        "email": email, 
        "password": password
    }
    headers = {}

    response = api_client.post(endpoint, headers, payload)
    print("Response Status Code:", response.status_code)
    assert response.status_code == 200
    
    data = response.json()['user']
    
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
endpoint = config.endpoint()
email = config.email()
password = config.password()
first_name = config.first_name()
last_name = config.last_name()
id = config.id()
token = config.token() 
    
test_login(api_client, endpoint, email, password, first_name, last_name, id)
test_logout(api_client, endpoint, token)    