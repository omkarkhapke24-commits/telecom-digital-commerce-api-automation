def test_authenticated_api_client_has_token(authenticated_api_client):
    assert authenticated_api_client.token is not None
    