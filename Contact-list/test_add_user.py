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


def add_user():
    