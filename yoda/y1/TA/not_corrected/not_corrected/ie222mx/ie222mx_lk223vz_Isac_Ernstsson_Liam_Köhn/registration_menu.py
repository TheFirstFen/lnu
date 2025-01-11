import user_input as usr_input
from mysql.connector import Error


def registration_menu(db):

    info = {}
    # Enter all the information about user
    print("\nNew member registration: ")
    print("* = Mandatory")
    info["fname"] = usr_input.get_str("Enter your first name *: ")
    info["lname"] = usr_input.get_str("Enter your last name *: ")
    info["address"] = usr_input.get_str("Enter your street address *: ")
    info["city"] = usr_input.get_str("Enter your city *: ")
    info["zip"] = usr_input.get_int("Enter zip code *: ")
    info["phone"] = usr_input.get_phone("Enter phone: ")
    info["email"] = usr_input.get_email("Enter your email *: ")
    info["password"] = usr_input.get_pass()

    insert_new_customer(db, info)


def insert_new_customer(db, info: dict):
    # Query for entering a new member with placeholders
    query = """INSERT INTO members (fname, lname,
               address, city, zip, phone, email, password)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

    # Create a tuple of values to pass into the query
    values = (
        info['fname'],
        info['lname'],
        info['address'],
        info['city'],
        info['zip'],
        info['phone'],
        info['email'],
        info['password']
    )

    try:
        # Use the execute_with_commit method to run the query with the values
        db.execute_with_commit(query, values)
        print('Registration succesfull!')
        input('Press enter to return to main menu')
        return print('Returning to main menu...')
    except Error as e:
        if e.errno == 1062:
            print("An error occurred!")
            print('Email already exists, try again')
            registration_menu(db)
        print("An error occurred:", e)
        print('Registration failed!')
        input('Press enter to accept and return to main menu.')
