
def test_get_users_by_pagr(api_client):

    response = api_client.get(
        "/users",
        params = {"page": "2"}
    )

    response_data = response.json()

    print("Status Code: ", response.status_code)
    print("Response:" , response_data)

    assert response.status_code == 200
    assert response_data["page"] == 2
    assert "data" in response_data
    assert len(response_data["data"])>0