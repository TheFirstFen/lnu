from database import Database
from getpass import getpass
from menu import print_options,user_choice

def register_member(db:Database):

    print("\n--- Register Member ---")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    address = input("Address: ")
    city = input("City: ")
    zip = input("Zip Code: ")
    phone = input("Phone: ")
    email = input("Email (must be unique): ")
    password = getpass("Password: ")

    try:
        insert_query = f""" INSERT INTO members (fname,lname,address,city,zip,phone,email,password) VALUES("{fname}","{lname}","{address}","{city}","{zip}","{phone}","{email}","{password}")"""
        db.execute_commit(insert_query)
        print("You have successfully registered!...")

        

    except Exception as e:
        print("Member registration has failed!...")
        print(e)
    
    input("\nPress ENTER to go back to the main menu...")


def member_login(db:Database):
    print("\n--- Member Login ---")
    username = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        # Query to check for matching email and password
        query = "SELECT userid, fname, lname FROM members WHERE email = %s AND password = %s"
        params  = (username, password)
        result = db.execute_fetchone(query, params)

        if result:
            userid, fname, lname = result
            print(f"\nWelcome back, {fname} {lname}!")
            return userid  # Return the member's userid to track their session
        else:
            print("\nInvalid email or password. Please try again.")
            return None
    except Exception as e:
        print("An error occurred while logging in:")
        print(e)
        return None
    
def list_subjects(db:Database):
    i = 0
    query = f"""SELECT DISTINCT subject FROM books ORDER BY subject ; """
    subjects = db.execute_fetchall(query)
    print("\nList of subjects")

    for subject in subjects:
        i += 1
        print(f"{i} {subject[0]}")
    
    selected_option = input("\nEnter which subject you'd like to select, or enter Q to go back to the menu: \n")

    if selected_option.upper() == "Q":
        return
    
    elif selected_option.isdigit():
        selected_index = int(selected_option) - 1
        if 0 <= selected_index < len(subjects):
            selected_subject = subjects[selected_index][0]
            print(f"You selected: {selected_subject}")
            return selected_subject

        else:
            print("Invalid selection. Please try again.")
            list_subjects(db)
    else:
        print("Invalid input. Please enter a number or 'Q'.")
        list_subjects(db)

def list_books(db:Database,subject,limit,offset,userid):

    query = f"""SELECT title, isbn, author, price FROM books WHERE subject = '{subject}' LIMIT {limit} OFFSET {offset} ; """
    amount_query = f"""SELECT title, isbn, author, price FROM books WHERE subject = '{subject}' ; """

    results = db.execute_fetchall(query)
    amount = db.execute_fetchall(amount_query)

    print(f'\nThere are {len(amount)} books in the selected subject\n')

    for title, isbn, author, price in results:
        print(f'Title: {title},\n ISBN: {isbn},\n Author: {author},\n Price: {price}\n')

    books_options = ["Enter ISBN","Previous Page", "Next Page", "Return to Menu"]

    print_options(books_options)

    selected_option = user_choice(len(books_options))

    if selected_option == "1":
        chosen_isbn = input("Enter the ISBN of the book you'd like: ")
        qty = int(input("Enter the quanity: "))
        isbn_query = f"""INSERT into cart (userid, isbn, qty) VALUES("{userid}","{chosen_isbn}","{qty}") ON DUPLICATE KEY UPDATE qty = qty + {qty} ; """

        db.execute_commit(isbn_query)

        print("Books added to cart successfully!...\n")        
    
    elif selected_option == "2":
        list_books(db,subject, limit, offset-limit,userid)
    
    elif selected_option == "3":
        list_books(db, subject, limit, offset+limit,userid)

    elif selected_option == "4":
        return




    


