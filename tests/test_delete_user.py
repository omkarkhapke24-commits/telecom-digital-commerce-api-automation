#from utils.api_client import APIClient

def test_delete_user(user_api):
    #api_client = APIClient()

    response = user_api.delete_user(2)
    print("Status code: " , response.status_code)
    print("Response:", response.text )

    assert response.status_code == 204
    assert response.text == ""