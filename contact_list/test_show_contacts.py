def test_get_contact_list(api_client, endpoint_get_contact_list, login_and_logout):
    payload = {}
    headers = {
        'Authorization': f'Bearer {login_and_logout}'
    }
    
    response = api_client.get(endpoint_get_contact_list, headers, payload)
    data = response.json()
    
    assert isinstance(data, list), "Response is not a list"
    assert data[0]['firstName'] == 'Carlos', f"Expected first name 'Carlos', but got {data[0]['firstName']}"
    assert data[0]['lastName'].startswith('Gonz'), f"Expected last name to start with 'Gonz', but got {data[0]['lastName']}"
