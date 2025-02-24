import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config_loader import ConfigLoader
from api_client import ApiClient

config = ConfigLoader()
api_client = ApiClient()
endpoint = config.endpoint()
email = config.email()
password = config.password()
first_name = config.first_name()
last_name = config.last_name()
token = config.token()
id = config.id()
contact_first_name = config.contact1_first_name()
contact_last_name = config.contact1_last_name()
contact_birthdate = config.contact1_birthdate()
contact_email = config.contact1_email()
contact_phone = config.contact1_phone()
contact_street1 = config.contact1_street1()
contact_street2 = config.contact1_street2()
contact_city = config.contact1_city()
contact_state = config.contact1_state()
contact_postal_code = config.contact1_postal_code()
contact_country = config.contact1_country()


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
    

def test_add_contact(endpoint, first_name, last_name, birthdate, email, phone, street1, street2, city, state, postal_code, country, token):
    payload = {
        "firstName": f"{first_name}",
        "lastName": f"{last_name}",
        "birthdate": f"{birthdate}",
        "email": f"{email}",
        "phone": f"{phone}",
        "street1": f"{street1}",
        "street2": f"{street2}",
        "city": f"{city}",
        "stateProvince": f"{state}",
        "postalCode": f"{postal_code}",
        "country": f"{country}"
    }

    headers = {
    'Authorization': f'Bearer {token}'
    }
        
    response = api_client.post(endpoint, headers, payload)
    
    response_json = response.json()

    assert response.status_code == 201
    assert response_json["firstName"] == first_name
    assert response_json["lastName"] == last_name
    assert response_json["birthdate"] == birthdate
    assert response_json["email"] == email
    assert response_json["phone"] == phone
    assert response_json["street1"] == street1
    assert response_json["street2"] == street2
    assert response_json["city"] == city
    assert response_json["stateProvince"] == state
    assert response_json["postalCode"] == postal_code
    assert response_json["country"] == country

    assert "_id" in response_json
    assert "owner" in response_json

def test_logout(api_client, endpoint, token):
    payload = {}
    headers = {
    'Authorization': f'Bearer {token}'
    }
    
    api_client.post(endpoint, headers, payload)