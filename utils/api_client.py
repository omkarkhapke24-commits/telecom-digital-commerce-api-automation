import requests
import time 
from config.config import BASE_URL, REQUEST_TIMEOUT
from config.headers import COMMON_HEADERS
from config.auth import AUTH_HEADERS
from config.logger_config import logger 


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.token = None

    def _request(self, method, endpoint, body=None, headers = None, params = None):
        try:
            url = f"{self.base_url}{endpoint}"
  
            request_headers = {
                    **COMMON_HEADERS,
                    **AUTH_HEADERS  
                }
            if self.token is not None:
                request_headers["Authorization"] = f"Bearer {self.token}"
              
            if headers is not None:
                request_headers = {
                    **request_headers,
                    **headers
                }

            logger.info(f"Sending {method} request to {url}")

            start_time = time.time()

            response = requests.request(
                method = method,
                url = url,
                headers= request_headers,
                json= body,
                params = params,
                timeout = REQUEST_TIMEOUT,
            )

            end_time = time.time()

            execution_time = end_time - start_time

            logger.info(f"Response Status Code: {response.status_code}")
            logger.info(f"Execution Time: {execution_time:.2f}seconds")

            return response
        
        except Exception as error:
            logger.error(f"{method} request failed: {error}")
            raise

    
    def login(self, body):
        response = self._request("POST", "/login",body)
        response_data = response.json()
        if "token" in response_data:
            self.token = response_data["token"]
        else:
            raise Exception("error" ,"Login failed")

        return response

    def get(self, endpoint,params = None, headers = None):
       return self._request("GET", endpoint,params = params, headers=headers )

    def post(self,endpoint, body, headers = None):   
        return self._request("POST",endpoint,body, headers)
    
    def patch(self,endpoint,body, headers = None):
        return self._request("PATCH", endpoint, body, headers)
    
    def put(self,endpoint,body, headers = None):  # is used to completely replace an existing resource or create a new resource if it does not already exist.
        return self._request("PUT",endpoint,body, headers)
    
    def delete(self, endpoint, headers = None):
        return self._request("DELETE",endpoint, headers=headers)