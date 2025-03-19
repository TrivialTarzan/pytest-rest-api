import pytest

contact_id = None

@pytest.mark.run(order=2)
def test_get_contact_list(api_client, endpoint_get_contact_list, login_and_logout):
    global contact_id
    
    payload = {}
    headers = {
        'Authorization': f'Bearer {login_and_logout}'
    }
    
    response = api_client.get(endpoint_get_contact_list, headers, payload)
    contact_id = response.json()[0]['_id']

@pytest.mark.run(order=3)
def test_delete_contact(api_client, endpoint_delete_contact, login_and_logout):
    headers = {
        'Authorization': f'Bearer {login_and_logout}'
    } 
    response_text = "Contact deleted"
    
    response = api_client.delete(f'{endpoint_delete_contact}{contact_id}', headers)
    print("Response Status Code:", response.status_code)
    assert response.status_code == 200
      