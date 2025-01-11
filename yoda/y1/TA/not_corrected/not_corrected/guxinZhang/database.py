# to connect python with the database

import mysql.connector

class Database:
    # establish the connection to the database in MySQL server
    def __init__(self, username, password) -> None:
        self.connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Schroder13",
        database="book_store",
        charset="utf8mb4",  # Ensure utf8mb4 is used
        collation="utf8mb4_general_ci"
        )
    
    # get cursor
    def __get_cursor__(self):
        return self.connection.cursor()
    
    # execute and ferch all results
    def execute_with_fetchall(self,query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        
    # exextute with commit
    def execute_with_commit(self, query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            self.connection.commit()