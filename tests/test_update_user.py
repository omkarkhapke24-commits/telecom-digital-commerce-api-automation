#put method 
#should verify:
#Request succeeded (200)
# Name is correct
#job is updated
#API returned an updatedAt timestamp
#from utils.api_client import APIClient

def test_update_user(user_api):
    #api_client = APIClient()

    body = {
        "name" : "OMKAR",
        "job" : "Senior QA"
    }
    
    response = user_api.update_user("/users/2",body) #put
    print("Status Code:", response.status_code)

    response_data = response.json() #RHS converts json response into python dictationairy
    print("Response:", response_data)

    assert response.status_code == 200
    assert response_data["name"] == body["name"]
    assert response_data["job"] == body["job"]
    assert "updatedAt" in response_data