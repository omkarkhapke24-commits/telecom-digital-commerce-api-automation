import pytest
from test_data.login_data import LOGIN_SUCCESS_DATA

@pytest.mark.parametrize(
        "email,password,expected_status",
        LOGIN_SUCCESS_DATA
)


def test_data_driven_login(
    api_client,
    email,
    password,
    expected_status
):

    
    body ={
            "email" :email ,
            "password" :password ,
        }

    response = api_client.login(body)

    print("Status Code: ",response.status_code)
    print("Response:", response.json())

    assert response.status_code == expected_status
    assert api_client.token is not None
