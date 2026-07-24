#Dependency Injection : We're injecting the APIClient into UserAPI instead of creating a new one inside it.
#from utils.api_client import APIClient

class UserAPI:

    def __init__(self, api_client):
        self.api_client = api_client
#"When you create a UserAPI, please give me an APIClient. 
# I won't create one myself."

    def get_users(self):
        return self.api_client.get("/users")

    def get_user(self,user_id):
        return self.api_client.get(f"/users/{user_id}")

    def create_user(self,body):
        return self.api_client.post("/users",body)
#"I know the endpoint, but I don't know how to send requests. I'll ask APIClient to do that."

    def update_user(self,user_id,body):
        return self.api_client.put(f"/users/{user_id}",body)
    
    def patch_user(self,user_id,body):
        return self.api_client.patch(f"/users/{user_id}",body)
    
    def delete_user(self,user_id):
        return self.api_client.delete(f"/users/{user_id}")