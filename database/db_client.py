import mysql.connector
import time
from config.logger_config import logger

class DatabaseClient: #this class handles db communication

    def __init__(self):
        self.connection =mysql.connector.connect( #self.connection: stores a live connection to MySQL.
            #mysql.connector.connect = creates communication with MySQL.
            host="localhost",
            user="root",
            password="Password",
            database="telecom_db"
        )

    def execute_query(self,query): #execute any SELECT query
        cursor = self.connection.cursor(dictionary=True) #LHS=created a cursor

        logger.info(f"Executing SQL Query: {query}")
        start_time = time.time()

        try:
            cursor.execute(query)
            result=cursor.fetchone()

            execution_time = time.time()-start_time
            logger.info(f"SQL Query executed successfully in {execution_time:.2f}seconds")

            return result

        except Exception as error:
            logger.error(f"Database query failed: {error}")
            raise

        finally:
            cursor.close()

    def close_connection(self):#close the db connection
        if self.connection.is_connected():
           self.connection.close()
           logger.info("Database connection closed.")
