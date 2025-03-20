import logging
import pytest

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('test_log.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(file_handler)

@pytest.mark.run(order=5)
def test_update_user(api_client, endpoint_update_user, login_and_logout, config):
    
    new_creds1 = {
        "new_first_name": "Bogdan",
        "new_last_name": "Bogdanov",
        "new_email": "newmail@yahoo.edu",
        "new_password": "666"
    }
    
    default_creds = {
        "firstName": config.first_name(),
        "lastName": config.last_name(),
        "email": config.email(),
        "password": config.password()
    }
    
    payload1 = {
        "firstName": new_creds1["new_first_name"],
        "lastName": new_creds1["new_last_name"],
        "email": new_creds1["new_email"],
        "password": new_creds1["new_password"]
    }

    headers = {
        'Authorization': f'Bearer {login_and_logout}'
    }

    logger.info(f"Payload for PATCH request: {payload1}")
    logger.info(f"Headers for PATCH request: {headers}")
        
    response = api_client.patch(endpoint_update_user, headers, payload1)
    response_json = response.json()

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response_json}")
    
    assert response.status_code == 200
    if response.status_code == 200:
        logger.info(f"Assertion passed: response.status_code == 200")
    else:
        logger.error(f"Assertion failed: response.status_code != 200")    
    assert response_json["firstName"] == new_creds1["new_first_name"]
    if response_json["firstName"] == new_creds1["new_first_name"]:
        logger.info(f"Assertion passed: {response_json['firstName']} == {new_creds1['new_first_name']}")
    else:
        logger.error(f"Assertion failed: {response_json['firstName']} != {new_creds1['new_first_name']}")    
    assert response_json["lastName"] == new_creds1["new_last_name"]
    if response_json["lastName"] == new_creds1["new_last_name"]:
        logger.info(f"Assertion passed: {response_json['lastName']} == {new_creds1['new_last_name']}")
    else:
        logger.error(f"Assertion failed: {response_json['lastName']} != {new_creds1['new_last_name']}")
    assert response_json["email"] == new_creds1["new_email"]
    if response_json["email"] == new_creds1["new_email"]:
        logger.info(f"Assertion passed: {response_json['email']} == {new_creds1['new_email']}")
    else:
        logger.error(f"Assertion failed: {response_json['email']} != {new_creds1['new_email']}")
    assert response_json["password"] == new_creds1["new_password"]
    if response_json["password"] == new_creds1["new_password"]:
        logger.info(f"Assertion passed: {response_json['password']} == {new_creds1['new_password']}")
    else:
        logger.error(f"Assertion failed: {response_json['password']} != {new_creds1['new_password']}")
    
    payload2 = {
        "firstName": default_creds["firstName"],
        "lastName": default_creds["lastName"],
        "email": default_creds["email"],
        "password": default_creds["password"]
    }

    logger.info(f"Payload for POST request: {payload2}")
    logger.info(f"Headers for POST request: {headers}")
    
    response = api_client.post(endpoint_update_user, headers, payload2)
    response_json = response.json()
    
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response JSON: {response_json}")
    
    assert response.status_code == 200
    assert response_json["firstName"] == default_creds["firstName"]
    assert response_json["lastName"] == default_creds["lastName"]
    assert response_json["email"] == default_creds["email"]