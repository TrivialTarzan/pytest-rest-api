import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('test_log.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(file_handler)

def test_get_contact_list(api_client, endpoint_get_contact_list, login_and_logout):
    payload = {}
    headers = {
        'Authorization': f'Bearer {login_and_logout}'
    }
    
    response = api_client.get(endpoint_get_contact_list, headers, payload)
    data = response.json()
    
    for i in range(0, len(data)):
        logger.info(f"Contact {i+1}:")
        for detail in data[i]:
            logger.info(f"\t{detail}: {data[i][detail]}")
    
    assert isinstance(data, list), "Response is not a list"
    logger.info("Assertion passed: Response is a list")

    assert data[0]['firstName'] == 'Carlos', f"Expected first name 'Carlos', but got {data[0]['firstName']}"
    logger.info(f"Assertion passed: {data[0]['firstName']} == 'Carlos'")

    assert data[0]['lastName'].startswith('Gonz'), f"Expected last name to start with 'Gonz', but got {data[0]['lastName']}"
    logger.info(f"Assertion passed: data[0]['lastName'].startswith('Gonz')")