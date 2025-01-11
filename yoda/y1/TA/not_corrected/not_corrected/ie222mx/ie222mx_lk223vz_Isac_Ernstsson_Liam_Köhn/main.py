from mysql.connector import connect, Error
from getpass import getpass
import time


# file import
from database import Database
import printing_functions
from registration_menu import registration_menu
from member_menu import member_menu
import user_input as user_input


# Main menu
def main_menu(db):
    # main menu
    while True:
        MAIN_OPTIONS = ['Member Login', 'New Member Registration', 'Quit']
        # Print header
        printing_functions.print_header(["Welcome to the online Book Store"])
        # Print Options
        printing_functions.print_options(MAIN_OPTIONS)
        # Check user choice
        choice = user_input.check_choice(len(MAIN_OPTIONS))
        match choice:
            case 1:
                member_menu(db)

            case 2:
                # Going to registation_menu
                registration_menu(db)

            case 3:
                print('Exiting program...')
                quit()


# check in credentials to sql sever is correct before
# login in to sever
def check_credentials(username, password):

    try:
        connect(host='localhost',
                user=username,
                password=password,
                database='book_store')
        return True

    except Error:
        return False


def main():
    # log in to sql sever
    valid_connection = False
    username, password = None, None

    # Trying to access the database and create a database object
    # if the credentials are not correct you will try again
    username = "root"
    password = "Schroder13"

    print('Connecting to sql server...\n')
    db = Database(username, password)
    time.sleep(1)
    print('Connection established')
    main_menu(db)


if __name__ == "__main__":
    main()
