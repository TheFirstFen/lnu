# note to whoever is correcting this, I am in 1DT903 but I got some extra time
# on my hands so I added the search by author/Title option to,
# because it felt uncompleted otherwise.
# I am fully acknowledge that you will correct that part
# as any other part and grade in the same way as in 1DV503 if you want to.

import os
import hashlib
from getpass import getpass
import re
from db_manager import Database
from gui import welcome_msg, print_invoice
from gui import standard_gui, print_book_information
from datetime import datetime, timedelta
import time


_CONFS = {"host": "localhost", "user": os.getenv("usr"),
          "password": os.getenv("pwd"),
          "database": "book_store"}


DB = Database(_CONFS)     # global so to make it easier
CURR_USR = None


class Registration:
    # checks if values are valid for the database
    @staticmethod
    def is_regex(regex, value, key):
        while not re.match(regex, value):
            if key == "phone" and value == "":
                return ""
            else:
                print(f"Invalid {key} try again")
                value = input(f"Enter {key}: ")
        return value

    # checks if the email exists already in the database
    @staticmethod
    def has_email(email):
        try:
            data = DB.fetch("""SELECT userid FROM members WHERE email = %s""",
                            (email,))
            return data == []
        except Exception as e:
            print(e)
            return False

    # main part of registration
    @staticmethod
    def register_member():
        clear()
        standard_gui("New member registration")

        # regx patterns
        name_patrn = r"^[a-öA-Ö]{2,50}$"
        pwd_patrn = r"^[A-Za-z\d@$!%*?&]{6,200}$"
        email_patrn = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,40}$"

        zip_patrn = r'^(\d+){4}$'
        phone_patrn = r"^(\+\d{10,15}|\d{10,15})$"
        street_patrn = r"\s*.{2,50}\s*"
        city_patrn = r"\s*.{2,30}\s*"

        regex_patterns = [name_patrn, name_patrn, street_patrn, city_patrn,
                          zip_patrn, phone_patrn, email_patrn, pwd_patrn]

        info = {"first name": "", "last name": "",
                "street address": "", "city": "",
                "zip": "", "phone": "",
                "email": "", "password": ""}

        # takes into account all the certain input types and cases
        for pattern, key in zip(regex_patterns, info.keys()):
            if key == "password":
                password = getpass(f"Enter your {key}: ")
                while not re.match(pwd_patrn, password):
                    print("Invalid password try again")
                    password = getpass(f"Enter your {key}: ")
                info[key] = hashlib.sha512(password.encode()).hexdigest()

            elif key == "email":
                value = input("Enter your email: ")
                value = Registration.is_regex(pattern, value, key)
                while not Registration.has_email(value):
                    print("Email already taken try again")
                    value = input(f"Enter your {key}: ")
                info[key] = value

            else:
                value = input(f"Enter your {key}: ")
                if value == "" and key == "phone":
                    info[key] = ""
                else:
                    info[key] = Registration.is_regex(pattern, value, key)

        Registration.add_member(info)
        clear()
        return True

    # add member to the database
    def add_member(info):
        global DB
        DB.insert_delete("""INSERT INTO members
                         (fname, lname, address, city, zip,
                         phone, email, password) VALUES
                       (%s, %s, %s, %s, %s, %s, %s, %s)""", (
                        info["first name"], info["last name"],
                        info["street address"], info["city"],
                        int(info["zip"]), info["phone"],
                        info["email"], info["password"]))




# To make it a nice gui interface i use a clear function
# To clear the gui at appropriate times
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# sends the isbn and qty to the cart table
def send_to_cart(isbn, qty):
    global CURR_USR

    status = DB.insert_delete("INSERT INTO cart (userid, isbn, qty) VALUES"
                              "(%s, %s, %s)", (CURR_USR["userid"], isbn, qty))
    if status:
        print("Book added to cart\n")


# makes it possible to add more of the same books
# if you realize that you wanted to add more of the same book
# also if you type a negative number for the quantity it takes that amount away
# as long as the number does not become negative
def add_if_cart(isbn, qty):
    isbn_in_cart = DB.fetch("""SELECT qty FROM cart
                            WHERE isbn=%s AND userid=%s""",
                            (isbn, CURR_USR["userid"]))

    time.sleep(2)
    if isbn_in_cart != []:
        new_qty = isbn_in_cart[0][0] + qty
        if new_qty >= 0:
            DB.insert_delete("""UPDATE cart SET qty = %s
                           WHERE isbn=%s AND userid=%s""",
                             (new_qty, isbn, CURR_USR["userid"]))

            # I have tried to delete a row without updateing it
            # when it becomes 0 but that does not work
            # but would not work so did this instead
            if new_qty == 0:
                DB.insert_delete("""DELETE FROM cart
                                    WHERE qty <= 0 AND userid=%s
                                    """, (CURR_USR["userid"], ))
            return True
        else:
            print("Invalid quantity this will result in a negative quantity")
            print("Try again")
            return False, False
    return False


# displays books
def display_books(data):
    amount_of_books = len(data)
    books_per_page = 2
    start_index = 0
    end_index = books_per_page
    user_input = "n"

    if amount_of_books > 0:
        while user_input.lower() != "" and start_index <= amount_of_books:
            clear()
            standard_gui("Book page")
            print_book_information(amount_of_books, data,
                                   start_index, end_index)
            user_input = get_user_input()

            if user_input != "" and user_input != "n":
                process_user_choice(user_input, data)

            elif user_input.lower() == "n" and start_index < amount_of_books:
                start_index, end_index = update_indices(books_per_page,
                                                        start_index, end_index)

            elif user_input == "":
                break

            print("\n" + "=" * 20)

    if amount_of_books == 0:
        print("No books found")
        input("Press any key to continue")

    clear()


def get_user_input():
    return str(input("\n>>> "))


def process_user_choice(user_input, data):
    try:
        check_for_book = DB.fetch("""
        SELECT isbn FROM books WHERE isbn=%s
        """, (user_input,))
        if check_for_book == []:
            print("Please enter a valid ISBN")
            display_books(data)

        quantity = get_quantity_input()

        is_in_cart = add_if_cart(user_input, quantity)
        if is_in_cart is False and is_in_cart is not tuple:
            send_to_cart(user_input, quantity)

    except ValueError:
        print("Please enter a number")
        display_books(data)


def get_quantity_input():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# updates the list split
def update_indices(books_per_page, start_index, end_index):
    start_index += books_per_page
    end_index += books_per_page
    return start_index, end_index


def subject_selection():
    clear()
    standard_gui("Subjects")
    data = DB.fetch("SELECT distinct subject FROM books order by subject")

    subjects = list()
    for index in range(len(data)):
        subjects.append(data[index][0])
        print(f"{index+1}. {data[index][0]}")

    try:
        subject_choice = int(input("\nEnter the number of the subject you wish"
                                   " to browse by: ")) - 1
    except ValueError:
        print("Please enter a number")
        return subject_selection()

    if subject_choice > len(subjects) or subject_choice < 0:
        print("Please enter a vaild subject number")
        return subject_selection()

    books_info = DB.fetch("""select count(*), author, title, isbn, price,
                          subject
                from books where subject = %s
                group by isbn, author, title, price, subject;""",
                          (subjects[subject_choice], ))
    clear()
    display_books(books_info)


def display_order(isbns, qtys, amounts, titles):
    global CURR_USR

    clear()
    created = datetime.now().date()

    DB.insert_delete("""
                INSERT INTO orders (userid, created, shipAddress,
                shipCity, shipZip)
                VALUES (%s, %s, %s, %s, %s)
            """, (CURR_USR['userid'], created, CURR_USR['address'],
                  CURR_USR['city'], CURR_USR['zip']))

    ono = DB.fetch("SELECT ono FROM orders WHERE userid = %s",
                   (CURR_USR['userid'], ), True)[-1][0]

    # I fetch all and set it to the last ono row,
    # as a person can have multiple orders
    # therefore if i only fetchone i get the first ono value
    # and not the last ono value
    # thus i fetch all and take the last ono value from there

    for isbn, qty, amount in zip(isbns, qtys, amounts):
        try:
            DB.insert_delete("INSERT INTO odetails VALUES (%s, %s, %s, %s)",
                             (ono, isbn, qty, amount))
        except Exception as e:
            print(e)
    standard_gui("Invoice")
    print(f"Invoice for order no.{ono}")
    print(f"Name: {CURR_USR['name']}")
    print(f"Address: {CURR_USR['address']}")
    print(f"City: {CURR_USR['city']}")
    print(f"Zip: {CURR_USR['zip']}")

    print_invoice("Order to be shipped", isbns, titles, amounts, qtys)
    print("Estimated delivery date:", created + timedelta(days=7))
    if input("Press enter to go back to Menu ") == "":
        clear()
        return True


def display_cart_content():
    global CURR_USR
    clear()
    isbn_qty = DB.fetch("""
                        select isbn, qty
                        from cart where userid = %s
                        """, (CURR_USR["userid"], ))

    isbns = [key[0] for key in isbn_qty]
    qtys = [key[1] for key in isbn_qty]

    book_info = []
    for isbn in isbns:
        book_info.append(DB.fetch("""select title, price
                                    from books
                                    where isbn = %s
                            """, (isbn, )))
    if book_info is not None:
        titles = [title for item in book_info for title, _ in item]
        prices = [price for item in book_info for _, price in item]
    else:
        return 0

    standard_gui("Cart")
    if isbn_qty != []:
        print_invoice(f"Cart Contents{chr(128722)}: ",
                      isbns, titles, prices, qtys)

        try:
            proceed = str(input("\nProceed to check out (Y/N)?: "))
            while proceed.upper() != "Y" and proceed.upper() != "N":
                print("Invalid option try again:")
                proceed = input("\nProceed to check out (Y/N)?: ")

            if proceed.upper() == "Y":
                DB.insert_delete("""delete from cart where userid=%s""",
                                 (CURR_USR["userid"],))
                print("here")
                return display_order(isbns, qtys, prices, titles)
            else:
                clear()
                return
        except Exception:
            print("invalid input")
            return display_cart_content()
    else:
        print_invoice(f"Cart Contents{chr(128722)}: ",
                      isbns, titles, prices, qtys)
        getpass("Press enter to go back to Menu ")
        clear()
        return True


def check_out():
    global CURR_USR
    isbn_qty = DB.fetch("""
                        select isbn, qty
                        from cart where userid = %s
                        """, (CURR_USR["userid"], ))
    isbns = [key[0] for key in isbn_qty]
    qtys = [key[1] for key in isbn_qty]
    books_info = {}

    for isbn, index in enumerate(isbns):
        book_info = DB.fetch("""
                            select author, title, price
                            from books where isbn in %s
                            """, (isbn, ))
        books_info[isbn] = [i for i in book_info[0]]
        books_info[isbn].append(qtys[index])
    return display_cart_content(books_info)


def logout():
    global CURR_USR
    clear()
    CURR_USR = None  # terminates the user session


def searching_by(regx, key):
    value = input(f"Enter {key} or part of the {key}: ")
    while not re.match(regx, value):
        print("\nInvalid charachters try again: ")
        value = input(f"Enter {key} or part of the {key}: ")

    books = DB.fetch(f"""
                     SELECT COUNT(DISTINCT isbn), author, title,
                     isbn, price, subject
                     FROM books
                     WHERE {key} LIKE %s
                     GROUP BY isbn, author, title, price, subject""",
                     ('%' + value + '%', ))
    display_books(books)
    search_by()


def search_by():
    clear()
    standard_gui("Search by")
    print("""
        1. Author search
        2. Title search
        3. Go back to member menu
        """)
    try:
        option = int(input("\nEnter your option: "))
        if option > 0 and option < 4:
            match option:
                case 1:
                    searching_by(r"^[a-zA-Z]{2,50}", "author")
                case 2:
                    searching_by(r"^[a-zA-Z 0-9]{2,50}$", "title")
                case 3:
                    return members_menu()
        else:
            invalid = True
            print("Invalid option")
            while invalid:
                option = int(input("\nEnter your option: "))
    except Exception:
        return search_by()


def members_menu():
    clear()
    while True:
        standard_gui("Members Menu")
        options = {"1": subject_selection, "2": search_by, "3":
                   display_cart_content, "4": logout}

        invalid_option = True
        while invalid_option:
            print("\n1 Browse by Subject")
            print("\n2 Search by author/Title")
            print("\n3 Check Out")
            print("\n4 Logout")
            choice = str(input("\nType in your option: "))
            if choice in options:
                invalid_option = False
            else:
                print("Invalid option\n")
        options[choice]()
        if CURR_USR is None:
            break


def login():
    global CURR_USR

    pwd_patrn: str = r"^[A-Za-z\d@$!%*?&]{8,}$"
    email_patrn = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    data = None

    while data is None:
        print()
        email = str(input("Enter email: "))
        while not re.match(email_patrn, email):
            print("Invalid email try again")
            email = str(input("\nEnter email: "))

        password = getpass("Enter password: ")
        while not re.match(pwd_patrn, password):
            print("Invalid password try again")
            password = getpass("\nEnter password: ")

        crypted = hashlib.sha512(password.encode()).hexdigest()

        data = DB.fetch("""SELECT userid, fname, lname, address, city, zip
                        FROM members
                        WHERE email = %s
                        AND password = %s""", (email, crypted), False)

        if data is None:
            print("Either your email is incorrect"
                  " or your password is incorrect")
        else:
            CURR_USR = {"userid": data[0], "name": data[1] + " " + data[2],
                        "address": data[3], "city": data[4],
                        "zip": data[5]}
            clear()
            break

    members_menu()


def main():
    # start
    while True:
        clear()
        welcome_msg()
        print("\n1. Member Login")
        print("\n2. New Member Registration")
        print("\nq. quit")

        option = str(input("\nType in your option: "))

        if option == "1":
            login()
        elif option == "2":
            sucess = Registration.register_member()
            if sucess:
                standard_gui("Successfully registered")
                time.sleep(1.5)
        elif option == "q":
            print("\nGood Bye!")
            break
        else:
            print("Invalid option")


main()
