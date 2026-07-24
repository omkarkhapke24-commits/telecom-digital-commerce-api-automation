#from utils.api_client import APIClient

def test_get_users_with_custom_headers(api_client):
    #api_client = APIClient()
    response = api_client.get("/users", headers = {  #object me method call krte ho toh self automatic pass ho jata hai.
        "X-Correlation-ID": "12345"  #self parameter is automatically passed by Python when you call a method on an object.
    })

    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"])> 0