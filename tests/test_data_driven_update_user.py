import pytest
from test_data.update_user_data import UPDATE_USER_DATA

@pytest.mark.parametrize(
"name,job,expected_status",
UPDATE_USER_DATA,
)

def test_data_driven_update_user(
    user_api,
    name,
    job,
    expected_status
):
    body ={
        "name" : name,
        "job" : job,
    }

    response = user_api.update_user(2,body)

    print("Response Code: ", response.status_code)
    print("Response:",response.json())

    assert response.status_code == expected_status
