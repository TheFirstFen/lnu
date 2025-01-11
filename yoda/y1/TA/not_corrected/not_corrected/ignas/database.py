import mysql.connector 

class Database:
    
    def __init__(self,username,password) -> None: #establishes connection between python file and the database on the MySQL server
        self.connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Schroder13",
        database="book_store",
        charset="utf8mb4",  # Ensure utf8mb4 is used
        collation="utf8mb4_general_ci"
        )
    
    def __get_cursor__(self):
        return self.connection.cursor()
    
    def execute_fetchall(self,query,): #function to fetch information
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        
    def execute_commit(self,query, params = None):#function to change information
        with self.__get_cursor__() as cursor:
            cursor.execute(query, params)
            self.connection.commit()
    
    def execute_fetchone(self,query, params = None):#retrieves next row
        with self.__get_cursor__() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()
            