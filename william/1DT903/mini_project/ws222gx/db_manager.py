from mysql.connector import connect, Error


class Database:
    def __init__(self, settings):
        self.conn = None
        self.prefs = settings

    def connect_to_db(self):
        try:
            self.conn = connect(
                host=self.prefs["host"],
                user=self.prefs["user"],
                password=self.prefs["password"],
                database=self.prefs["database"]
            )
            return True
        except Error as e:
            print(e)

    def insert_delete(self, query, data):
        try:
            self.connect_to_db()
            if self.conn is not None:
                with self.conn.cursor() as cursor:
                    cursor.execute(query, data)
                self.conn.commit()
                self.conn.close()
                return True
        except Error as e:
            print(e)

    def fetch(self, query, data=None, fetch_all=True):
        try:
            self.connect_to_db()
            if self.conn is not None:
                with self.conn.cursor() as cursor:
                    if data is not None:
                        cursor.execute(query, data)
                    else:
                        cursor.execute(query)
                    if fetch_all:
                        result = cursor.fetchall()
                    else:
                        result = cursor.fetchone()
                    self.conn.close()
                return result
        except Error as e:
            print(e)

    def test_connect_to_db(self):
        return self.connect_to_db()
