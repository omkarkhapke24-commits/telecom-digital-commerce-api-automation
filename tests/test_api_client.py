#from utils.api_client import APIClient (irrelavent with introduction of fixtures)

def test_get_users(user_api):
    #api_client = APIClient() #created an object of APIClient() 
    response = user_api.get_users()
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    assert "data" in response.json()  #data in json is not empty
    assert len(response.json()["data"]) > 0  #users info are actually returned
    
def test_create_user(user_api):  #post method
   # api_client = APIClient()    #we need an object to call our post method
    body = {
        "name" : "OMKAR",
        "job" : "IFS"
    }
    response = user_api.create_user(body)
    print("Status Code:",response.status_code)
    response_data = response.json()
    print("Response:",response_data)

    assert response.status_code ==201
    assert response_data["name"] == body["name"]
    assert response_data["job"] == body["job"]
    assert "id" in response_data
   # assert "id" in response_data > 0
    assert "createdAt" in response_data