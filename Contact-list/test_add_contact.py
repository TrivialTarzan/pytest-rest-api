import pytest
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config_loader import load_config
from api_client import ApiClient

config = load_config()

@pytest.fixture
def endpoint():
    return config['ContactList']['endpoints']['login_user']

@pytest.fixture
def email():
    return config['ContactList']['first_user']['first_name']

@pytest.fixture
def password():
    return config['ContactList']['first_user']['password']

@pytest.fixture
def api():
    return ApiClient()


def test_log_in(api, endpoint, email, password):
    payload = { "email": email, "password": password}
    headers = {}
    response = api.post(endpoint, headers, payload)
    data = response.json()
    
    print(data)