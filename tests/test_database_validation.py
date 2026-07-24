from utils.api_client import APIClient
from database.db_client import DatabaseClient

def test_validate_user_data_with_database(authenticated_api_client):
    response = authenticated_api_client.get("/users/2")
    api_data = response.json()["data"]

    db = DatabaseClient()
    db_data = db.execute_query("SELECT * FROM users WHERE id =2")

    assert api_data["id"] == db_data["id"]
    assert api_data["email"] == db_data["email"]
    assert api_data["first_name"] == db_data["first_name"]
    assert api_data["last_name"] == db_data["last_name"]

    db.close_connection()