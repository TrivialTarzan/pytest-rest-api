bearer = None


def test_delete_contact(api_client, endpoint_delete_contact, login_and_logout):
    headers = {
        'Authorization': f'Bearer {login_and_logout}'
    } 
    response_text = "Contact deleted"
    
    response = api_client.delete(endpoint_delete_contact, headers)
    print("Response Status Code:", response.status_code)
    assert response.status_code == 200
    assert response.text == response_text
      