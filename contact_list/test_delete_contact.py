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
    
def test_delete_contact(api_client, endpoint_delete_contact):
    headers = {
    'Authorization': 'Bearer {{token}}'
    }    
    response_text = "Contact deleted"
    
    response = api_client.delete(endpoint_delete_contact, headers)
    print("Response Status Code:", response.status_code)
    assert response.status_code == 200
    assert response.text == response_text
    
def test_logout(api_client, endpoint_logout):
    payload = {}
    headers = {
        'Authorization': f'Bearer {bearer}'
    }
    
    api_client.post(endpoint_logout, headers, payload)      