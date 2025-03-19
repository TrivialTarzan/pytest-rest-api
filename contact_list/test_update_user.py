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
        
    response = api_client.post(f"{endpoint_update_user}{default_creds['firstName']}", headers, payload1)
    response_json = response.json()
    
    assert response.status_code == 200
    assert response_json["firstName"] == new_creds1["new_first_name"]
    assert response_json["lastName"] == new_creds1["new_last_name"]
    assert response_json["email"] == new_creds1["new_email"]
    assert response_json["password"] == new_creds1["new_password"]
    
    payload2 = {
        "firstName": default_creds["firstName"],
        "lastName": default_creds["lastName"],
        "email": default_creds["email"],
        "password": default_creds["password"]
    }
    
    response = api_client.post(f"{endpoint_update_user}{default_creds['firstName']}", headers, payload2)
    response_json = response.json()
    
    assert response.status_code == 200
    assert response_json["firstName"] == default_creds["firstName"]
    assert response_json["lastName"] == default_creds["lastName"]
    assert response_json["email"] == default_creds["email"]