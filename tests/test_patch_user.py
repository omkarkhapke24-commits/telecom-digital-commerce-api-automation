#patch - selected part tb updated
#from utils.api_client import APIClient

def test_patch_user(user_api):
    #api_client = APIClient()

    body= {
        "job" : "QA ENGINEER"  #send only the changed field
    }

    response = user_api.patch_user(2,body)
    print("Status Code: ", response.status_code)

    response_data = response.json() #"Take the response body and convert it into a Python dictionary
    print("Response: " ,response_data)

    assert response.status_code == 200
    assert response_data["job"] == body["job"]
    assert "updatedAt" in response_data
