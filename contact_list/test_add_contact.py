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
    bearer = response.json()['token']
    print(data)
    
    assert data['email'] == user_credentials["email"]
    assert data['firstName'] == user_credentials["first_name"]
    assert data['lastName'] == user_credentials["last_name"]
    assert data['_id'] == user_credentials["_id"]

def test_add_contact(api_client, endpoint_add_contact, contact_details_1):
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
        'Authorization': f'Bearer {bearer}'
    }
        
    response = api_client.post(endpoint_add_contact, headers, payload)
    
    response_json = response.json()

    assert response.status_code == 201
    assert response_json["firstName"] == contact_details_1["first_name"]
    assert response_json["lastName"] == contact_details_1["last_name"]
    assert response_json["birthdate"] == contact_details_1["birthdate"]
    assert response_json["email"] == contact_details_1["email"]
    assert response_json["phone"] == contact_details_1["phone"]
    assert response_json["street1"] == contact_details_1["street1"]
    assert response_json["street2"] == contact_details_1["street2"]
    assert response_json["city"] == contact_details_1["city"]
    assert response_json["stateProvince"] == contact_details_1["state"]
    assert response_json["postalCode"] == contact_details_1["postal_code"]
    assert response_json["country"] == contact_details_1["country"]

    assert "_id" in response_json
    assert "owner" in response_json

  
def test_logout(api_client, endpoint_logout):
    payload = {}
    headers = {
        'Authorization': f'Bearer {bearer}'
    }
    
    api_client.post(endpoint_logout, headers, payload)        