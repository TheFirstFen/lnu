from database import Database
from getpass import getpass  # i cannot use getpass function in my codes, maybe cuz my IDE
import mysql.connector
from menu import main_menu

# check the database cridentials
def check_cridentials(username, password):
    try:
        mysql.connector.connect(
        host="localhost",
        user="root",
        password="Schroder13",
        database="book_store",
        charset="utf8mb4",  # Ensure utf8mb4 is used
        collation="utf8mb4_general_ci"
        )
        return True
    except:
        return False

valid_connection = False
username, password=(None, None)

while not valid_connection:
    username = "root" 
    password = "Schroder13"
 
    if check_cridentials(username, password):
        valid_connection = True
        print('Connection is successful.')
    else:
        print('Connection is failed. Please make sure your crientials are correct or MySQL Server is running.')

db = Database(username, password)
main_menu(db,['Member Login','New Member Registration','Quit'])