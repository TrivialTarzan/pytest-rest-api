import pytest

bearer = None


def test_login(api_client, endpoint_login, user_credentials):
    global bearer
    
    payload = {
        "email": user_credentials["email"], 
        "password": user_credentials["password"]
    }
    headers = {}

    response = api_client.post(endpoint_login, headers, payload)
    print("Response Status Code:", response.status_code)
    assert response.status_code == 200
    
    data = response.json()['user']
    print(data)
    bearer = response.json()['token']
    
    assert data['email'] == user_credentials["email"]
    assert data['firstName'] == user_credentials["first_name"]
    assert data['lastName'] == user_credentials["last_name"]
    assert data['_id'] == user_credentials["_id"]


def test_get_contact_list(api_client, endpoint_get_contact_list, user_credentials):
    payload = {}
    headers = {
        'Authorization': f'Bearer {bearer}'
    }
    
    response = api_client.get(endpoint_get_contact_list, headers, payload)
    data = response.json()
    
    assert isinstance(data, list), "Response is not a list"
    assert data[0]['firstName'] == 'Carlos', f"Expected first name 'Carlos', but got {data[0]['firstName']}"
    assert data[0]['lastName'].startswith('Gonz'), f"Expected last name to start with 'Gonz', but got {data[0]['lastName']}"


def test_logout(api_client, endpoint_logout, user_credentials):
    payload = {}
    headers = {
        'Authorization': f'Bearer {bearer}'
    }
    
    api_client.post(endpoint_logout, headers, payload)