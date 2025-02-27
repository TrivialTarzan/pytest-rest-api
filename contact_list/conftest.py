import pytest
import logging
from config.config_loader import ConfigLoader
from api_client.api_client import ApiClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def login(api_client, endpoint_login, user_credentials):
    logger.info("Logging in with user credentials: %s", user_credentials["email"])
    payload = {
        "email": user_credentials["email"],
        "password": user_credentials["password"]
    }
    headers = {}

    response = api_client.post(endpoint_login, headers, payload)
    logger.info("Login response status code: %s", response.status_code)
    assert response.status_code == 200
    logger.info("Assertion passed: response.status_code == 200")

    token = response.json()['token']
    logger.info("Received bearer token")
    return token

def logout(api_client, endpoint_logout, bearer_token):
    logger.info("Logging out")
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    response = api_client.post(endpoint_logout, headers, {})
    logger.info("Logout response status code: %s", response.status_code)
    assert response.status_code == 200
    logger.info("Assertion passed: response.status_code == 200")

@pytest.fixture(scope="module", autouse=True)
def login_and_logout(api_client, endpoint_login, endpoint_logout, user_credentials):
    bearer_token = login(api_client, endpoint_login, user_credentials)

    yield bearer_token

    logout(api_client, endpoint_logout, bearer_token)

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
def endpoint_delete_contact(config):
    return config.endpoint_delete_contact()

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