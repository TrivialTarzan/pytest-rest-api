import logging
import pytest

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('test_log.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(file_handler)

@pytest.mark.run(order=1)
def test_add_contact(api_client, endpoint_add_contact, contact_details_1, login_and_logout):
    payload = {
        "firstName": contact_details_1["first_name"],
        "lastName": contact_details_1["last_name"],
        "birthdate": contact_details_1["birthdate"],
        "email": contact_details_1["email"],
        "phone": contact_details_1["phone"],
        "street1": contact_details_1["street1"],
        "street2": contact_details_1["street2"],
        "city": contact_details_1["city"],
        "stateProvince": contact_details_1["state"],
        "postalCode": contact_details_1["postal_code"],
        "country": contact_details_1["country"]
    }

    headers = {
        'Authorization': f'Bearer {login_and_logout}'
    }
        
    response = api_client.post(endpoint_add_contact, headers, payload)
    
    response_json = response.json()

    logger.info("Response Status Code: %s", response.status_code)
    assert response.status_code == 201
    logger.info("Assertion passed: response.status_code == 201")
    assert response_json["firstName"] == contact_details_1["first_name"]
    logger.info(f"Assertion passed: {response_json['firstName']} == {contact_details_1['first_name']}")
    assert response_json["lastName"] == contact_details_1["last_name"]
    logger.info(f"Assertion passed: {response_json['lastName']} == {contact_details_1['last_name']}")
    assert response_json["birthdate"] == contact_details_1["birthdate"]
    logger.info(f"Assertion passed: {response_json['birthdate']} == {contact_details_1['birthdate']}")
    assert response_json["email"] == contact_details_1["email"]
    logger.info(f"Assertion passed: {response_json['email']} == {contact_details_1['email']}")
    assert response_json["phone"] == contact_details_1["phone"]
    logger.info(f"Assertion passed: {response_json['phone']} == {contact_details_1['phone']}")
    assert response_json["street1"] == contact_details_1["street1"]
    logger.info(f"Assertion passed: {response_json['street1']} == {contact_details_1['street1']}")
    assert response_json["street2"] == contact_details_1["street2"]
    logger.info(f"Assertion passed: {response_json['street2']} == {contact_details_1['street2']}")
    assert response_json["city"] == contact_details_1["city"]
    logger.info(f"Assertion passed: {response_json['city']} == {contact_details_1['city']}")
    assert response_json["stateProvince"] == contact_details_1["state"]
    logger.info(f"Assertion passed: {response_json['stateProvince']} == {contact_details_1['state']}")
    assert response_json["postalCode"] == contact_details_1["postal_code"]
    logger.info(f"Assertion passed: {response_json['postalCode']} == {contact_details_1['postal_code']}")
    assert response_json["country"] == contact_details_1["country"]
    logger.info(f"Assertion passed: {response_json['country']} == {contact_details_1['country']}")
    assert "_id" in response_json
    logger.info("Assertion passed: '_id' in response_json")
    assert "owner" in response_json
    logger.info("Assertion passed: 'owner' in response_json")