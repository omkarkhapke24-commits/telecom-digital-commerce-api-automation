#from utils.api_client import APIClient

def test_login_success(api_client):
        #api_client = APIClient()

        body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        response = api_client.login(body)
        
        print("Status Code: ", response.status_code)
        print("Response:", response.json())

        assert response.status_code == 200
        assert api_client.token is not None


def test_login_failure(api_client):
        #api_client = APIClient()

        body = {
            "email": "eve.holt@reqres.in"
        }

        try:
            api_client.login(body)
            assert False, "Expected login to fail"

        except Exception as error:
            assert "Login failed" in str(error)

