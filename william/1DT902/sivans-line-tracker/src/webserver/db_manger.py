import sqlite3
import os
from datetime import datetime


def utc_to_cet(utc_time):
    cet_time = utc_time[0:11]
    add_hour = str(int(utc_time[11:13]) + 1)
    cet_time += add_hour + utc_time[13::]
    return cet_time


def get_time():
    now = datetime.now()
    time_right_now = now.strftime('%Y-%m-%d %H:%M:%S')
    return utc_to_cet(time_right_now)


class DBManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = None

    # creates the connection to the database
    def connect_to_db(self):
        try:
            db_path = os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                f"{self.database_name}.db"
                )
            self.conn = sqlite3.connect(db_path)
            self.conn.row_factory = sqlite3.Row
            print("Connected to database")

        except Exception as e:
            print(f'Connection to database failed: {e}')

    # closes the connection to the database
    def close_connection(self):
        self.conn.commit()
        self.conn.close()
        print("Closed connection to database")

    # creates table for database
    def create_table(self):
        self.connect_to_db()
        script_path = os.path.join(os.path.dirname(__file__), 'main.sql')
        with open(script_path) as f:
            self.conn.executescript(f.read())

        self.close_connection()
        print('Created table')

    # fetches data from database
    def fetch(self, from_date=None, to_date=None):
        try:
            self.connect_to_db()
            if from_date is None and to_date is None:
                cur = self.conn.execute('SELECT length, date FROM ' +
                                        self.database_name +
                                        ' ORDER BY id DESC LIMIT 1')
                data = cur.fetchone()
            else:
                cur = self.conn.execute('SELECT length, date FROM ' +
                                        self.database_name + ' WHERE date ' +
                                        f'BETWEEN "{from_date}" AND "{to_date}"')

                data = cur.fetchall()

                if data:
                    data_list = []
                    for row in data:
                        data_list.append({'length': row['length'],
                                        'date': row['date']})
                    self.conn.close()
                    return data_list
            if data:
                return dict(data)

            else:
                return [{'error': 'data not found'}]

        except Exception as e:
            print(f'Error fetching data: {e}')
        finally:
            self.conn.close()

    # insert values from database
    def insert_data(self, data):
        try:
            self.connect_to_db()
            if not isinstance(data, (int, float)):
                raise ValueError("Data must be a number")
            self.conn.execute('INSERT INTO ' + self.database_name +
                              ' (length) VALUES (?)', (data,))
        except Exception as e:
            print(f'Error inserting data: {e}')
        finally:
            self.close_connection()

    # removes data in a range
    def remove_range(self, full_boot=False, start_id=None, end_id=None):
        try:
            if full_boot:
                self.connect_to_db()
                self.conn.execute('DELETE FROM sivans')

            else:
                if start_id and end_id is not None:
                    self.connect_to_db()
                    self.conn.execute(
                        'DELETE FROM ' + self.database_name +
                        f' WHERE id BETWEEN {start_id} AND {end_id}')
        except Exception as e:
            print(f'Error removing data: {e}')
        finally:
            self.close_connection()
