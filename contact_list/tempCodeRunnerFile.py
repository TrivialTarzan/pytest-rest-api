def test_logout(api_client, endpoint_logout):
    payload = {}
    headers = {
        'Authorization': f'Bearer {bearer}'
    }
    
    api_client.post(endpoint_logout, headers, payload)  