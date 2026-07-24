from database.db_client import DatabaseClient

def test_database_connection():
    db = DatabaseClient()

    result = db.execute_query(
        "SELECT * FROM users where id =2"
    )
    print(result)