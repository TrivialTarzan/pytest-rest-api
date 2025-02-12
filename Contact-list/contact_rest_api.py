import pytest
import requests
from config.config_loader import load_config

@pytest.fixture
def base_url():
    return load_config['Contact List']['base_url']

@pytest.fixture
def token():
    return load_config['Contact List']['token']

@pytest.fixture
def endpoints():
    return load_config['Contact List']['endpoints']

def test_example(base_url, token, endpoints):
    print(f"Base URL: {base_url}")
    print(f"Token: {token}")
    print(f"Endpoints: {endpoints}")

    # Możesz teraz używać tych zmiennych w testach, np.:
    assert base_url == "https://thinking-tester-contact-list.herokuapp.com"
    assert endpoints['add_contact'] == "/contacts"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

body = {
    "firstName": "John",
    "lastName": "Doe",
    "birthdate": "1970-01-01",
    "email": "korwin-mikke@what.com",
    "phone": "666",
    "street1": "1 Hubris St.",
    "street2": "Apartment SS",
    "city": "Anytown",
    "stateProvince": "KS",
    "postalCode": "12345",
    "country": "PL"
}

def test_add_contact():
    response = requests.post(url, json=body, headers=headers)

    assert response.status_code == 201
    
    response_json = response.json()

    assert response_json["firstName"] == body["firstName"]
    assert response_json["lastName"] == body["lastName"]
    assert response_json["birthdate"] == body["birthdate"]
    assert response_json["email"] == body["email"]
    assert response_json["phone"] == body["phone"]
    assert response_json["street1"] == body["street1"]
    assert response_json["street2"] == body["street2"]
    assert response_json["city"] == body["city"]
    assert response_json["stateProvince"] == body["stateProvince"]
    assert response_json["postalCode"] == body["postalCode"]
    assert response_json["country"] == body["country"]

    assert "_id" in response_json
    assert "owner" in response_json
