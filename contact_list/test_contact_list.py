import pytest
import sys
import os
from config.config_loader import ConfigLoader
from api_client.api_client import ApiClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture(scope="module")
def config():
    return ConfigLoader()

@pytest.fixture(scope="module")
def api_client():
    return ApiClient()

@pytest.fixture(scope="module")
def endpoint_login(config):
    return config.endpoint_login()

@pytest.fixture(scope="module")
def endpoint_add_contact(config):
    return config.endpoint_add_contact()

@pytest.fixture(scope="module")
def endpoint_logout(config):
    return config.endpoint_logout()

@pytest.fixture(scope="module")
def user_credentials(config):
    return {
        "email": config.email(),
        "password": config.password(),
        "first_name": config.first_name(),
        "last_name": config.last_name(),
        "token": config.token(),
        "_id": config.id()
    }

@pytest.fixture(scope="module")
def contact_details(config):
    return {
        "first_name": config.contact1_first_name(),
        "last_name": config.contact1_last_name(),
        "birthdate": config.contact1_birthdate(),
        "email": config.contact1_email(),
        "phone": config.contact1_phone(),
        "street1": config.contact1_street1(),
        "street2": config.contact1_street2(),
        "city": config.contact1_city(),
        "state": config.contact1_state(),
        "postal_code": config.contact1_postal_code(),
        "country": config.contact1_country()
    }

def test_login(api_client, endpoint_login, user_credentials):
    global bearer
    
    payload = {
        "email": user_credentials["email"], 
        "password": user_credentials["password"]
    }
    headers = {}

    response = api_client.post(endpoint_login, headers, payload)
    print("Response Status Code:", response.status_code)
    assert response.status_code == 200
    
    data = response.json()['user']
    
    assert data['email'] == user_credentials["email"]
    assert data['firstName'] == user_credentials["first_name"]
    assert data['lastName'] == user_credentials["last_name"]
    assert data['_id'] == user_credentials["_id"]

def test_add_contact(api_client, endpoint_add_contact, contact_details, user_credentials):
    payload = {
        "firstName": contact_details["first_name"],
        "lastName": contact_details["last_name"],
        "birthdate": contact_details["birthdate"],
        "email": contact_details["email"],
        "phone": contact_details["phone"],
        "street1": contact_details["street1"],
        "street2": contact_details["street2"],
        "city": contact_details["city"],
        "stateProvince": contact_details["state"],
        "postalCode": contact_details["postal_code"],
        "country": contact_details["country"]
    }

    headers = {
        'Authorization': f'Bearer {user_credentials["token"]}'
    }
        
    response = api_client.post(endpoint_add_contact, headers, payload)
    
    response_json = response.json()

    assert response.status_code == 201
    assert response_json["firstName"] == contact_details["first_name"]
    assert response_json["lastName"] == contact_details["last_name"]
    assert response_json["birthdate"] == contact_details["birthdate"]
    assert response_json["email"] == contact_details["email"]
    assert response_json["phone"] == contact_details["phone"]
    assert response_json["street1"] == contact_details["street1"]
    assert response_json["street2"] == contact_details["street2"]
    assert response_json["city"] == contact_details["city"]
    assert response_json["stateProvince"] == contact_details["state"]
    assert response_json["postalCode"] == contact_details["postal_code"]
    assert response_json["country"] == contact_details["country"]

    assert "_id" in response_json
    assert "owner" in response_json

def test_logout(api_client, endpoint_logout, user_credentials):
    payload = {}
    headers = {
        'Authorization': f'Bearer {user_credentials["token"]}'
    }
    
    api_client.post(endpoint_logout, headers, payload)