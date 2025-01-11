import mysql.connector as mysql


class Database:
    def __init__(self, username, password):
        self.connection = mysql.connect(host="localhost",
        user="root",
        password="Schroder13",
        database="book_store",
        charset="utf8mb4",  # Ensure utf8mb4 is used
        collation="utf8mb4_general_ci"
            )

    # get cursor
    def __get_cursor__(self):
        return self.connection.cursor()

    # execute and fetch result
    def execute_and_fetchall(self, query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    # execute with commit
    def execute_with_commit(self, query, parameters=None):
        with self.__get_cursor__() as cursor:
            # Pass the parameters as a second argument
            cursor.execute(query, parameters)
            self.connection.commit()
