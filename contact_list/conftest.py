import pytest
from config.config_loader import ConfigLoader
from api_client.api_client import ApiClient

'''
The fixtures are defined in the conftest.py file and can be used in any test file 
by passing them as arguments to the test functions.
'''

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
def endpoint_get_contact_list(config):
    return config.endpoint_get_contact_list()

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
        "_id": config.id()
    }

@pytest.fixture(scope="module")
def contact_details_1(config):
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
    
@pytest.fixture(scope="module")
def contact_details_2(config):
    return {
        "first_name": config.contact2_first_name(),
        "last_name": config.contact2_last_name(),
        "birthdate": config.contact2_birthdate(),
        "email": config.contact2_email(),
        "phone": config.contact2_phone(),
        "street1": config.contact2_street1(),
        "street2": config.contact2_street2(),
        "city": config.contact2_city(),
        "state": config.contact2_state(),
        "postal_code": config.contact2_postal_code(),
        "country": config.contact2_country()
    }    