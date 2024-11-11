# bookstore.py
#
# Author: Samuel Berg
# Date: 2023-04-XX

import hashlib
import re
from getpass import getpass
from datetime import datetime, timedelta
from mysql.connector import Error, connect

# Constants
DB = 'book_store'
HOST = 'localhost'
PORT = 3306
USER = 'root'
REGEX = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'


def store_all_books():
    global conn
    global cur
    result = executeSelectQuery('SELECT * FROM books')
    return result


''' mainmenu()
This is the main function that handles the user interface
and provides options for logging in, registering, and quitting
'''


def mainmenu():
    global conn
    global cur
    while True:
        print('Welcome to the Online Book Store')
        print('\n1. Member Login')
        print('\n2. New Member Registration')
        print('\nq. Quit')
        opt = input('\nType in your option: ')
        if opt == '1':
            login()
        elif opt == '2':
            register()
        elif opt == 'q':
            print('Exiting...')
            break
        else:
            print('Invalid option, please try again')


def register():
    global conn
    global cur
    print('\nWelcome to the Online Book Store')
    print('\tNew Member Registrationn\n')

    # Taking input from user for registration
    fname = input('Enter first name: ')
    lname = input('Enter last name: ')
    address = input('Enter street address: ')
    city = input('Enter city: ')
    state = input('Enter state: ')
    zip_code = input('Enter zip: ')
    phone = input('Enter phone: ')
    email = input('Enter email address: ')
    password = input('Enter password: ')

    # Checking the validity of email
    if not re.search(REGEX, email):
        print('Invalid email address, please enter the valid email')
        return

    # Checking if the email already exists in the database
    cur.execute('SELECT * FROM members WHERE email =%s', (email,))
    result = cur.fetchone()
    if result:
        print('The user with such email exists. Please use another email for',
              'the username.')
        return

    # Hashing the password before storing it in the database
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Inserting user data into the database
    try:
        query = '''INSERT INTO members
        (fname, lname, address, city, state, zip, phone, email, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        values = (fname, lname, address, city, state, int(zip_code),
                  phone, email, hashed_password)
        cur.execute(query, values)
        conn.commit()
        print('\nYou have registered successfully!')
        input('Press Enter to go back to Menu')
    except Error as e:
        print(f'Failed to register user: {e}')


def login():
    global conn
    global cur
    email = input('Enter email: ')
    password = input('Enter password: ')

    if not re.search(REGEX, email):
        print('Invalid email address, please enter the valid email')
        return
    else:
        # Checking if the user exists in the database or not
        try:
            member_query = '''SELECT * FROM members WHERE
            email=%s AND password=%s'''
            values = (email, hashlib.sha256(password.encode()).hexdigest())
            cur.execute(member_query, values)
            result = cur.fetchone()

            if result:
                user_obj = user_obj_creation(email)
                print('Login successful!')
                member_screen(user_obj)
            else:
                email_query = 'SELECT * FROM members WHERE email=%s'
                cur.execute(email_query, (email,))
                email_result = cur.fetchone()
                if email_result:
                    # The email address exists in the database,
                    # but the password is incorrect
                    print('\nInvalid email/login credentials.\n')
                    mainmenu()
                else:
                    # The email address doesn't exist in the database
                    print('\nInvalid email/login credentials.\n')
                    mainmenu()

        except Error as e:
            print('\nFailed to connect to database: {}'.format(e))

        finally:
            if (conn.is_connected()):
                cur.close()
                conn.close()
                print('MySQL connection closed due to error.')


def user_obj_creation(email):
    global conn
    global cur
    details = executeSelectQuery('SELECT * FROM members WHERE email=%s',
                                 (email,))
    user_dict = {
        'fname': details[0][0],
        'lname': details[0][1],
        'address': details[0][2],
        'city': details[0][3],
        'state': details[0][4],
        'zip': details[0][5],
        'phone': details[0][6],
        'email': details[0][7],
        'userid': details[0][8],
        'creditcardtype': details[0][10],
        'creditcardnumber': details[0][11]
    }
    return user_dict


def member_screen(user):
    global conn
    global cur
    cart, orders = fetch_cart_orders(user)
    while True:
        print('\nWelcome to the Online Book Store')
        print('\tMember Menu')
        print('\n1. Browse by Subject')
        print('\n2. Search by Author/Title')
        print('\n3. Check Out')
        print('\n4. Logout')
        opt = input('\nType in your option: ')
        if opt == '1':
            browse_by_subject(user, cart)
        elif opt == '2':
            search_by_author_title(user, cart)
        elif opt == '3':
            checkout(user, cart, orders)
        elif opt == '4':
            logout(user, cart, orders)
        else:
            print('Invalid option, please try again')


def fetch_cart_orders(user, cart=None, orders=None):
    global conn
    global cur

    if cart is not None:
        cart.clear()
    if orders is not None:
        orders.clear()

    cart = executeSelectQuery('SELECT * FROM cart WHERE userid=%s',
                              (user['userid'],))
    orders = executeSelectQuery('SELECT * FROM orders WHERE userid=%s',
                                (user['userid'],))
    return cart, orders


def browse_by_subject(user, cart):
    global conn
    global cur
    subjcets_query = 'SELECT DISTINCT subject FROM books ORDER BY subject ASC'
    subjects = executeSelectQuery(subjcets_query)
    num_subjects = len(subjects)

    # check if there are any subjects
    if num_subjects == 0:
        print('There are no subjects to browse')
        return

    # print list of subjects
    for i in range(num_subjects):
        print(f'{i+1}. {subjects[i][0]}')

    # get user input for subject number
    subject_num = input('Enter your choice: ')
    while not (subject_num.isnumeric() or int(subject_num) < 1
               or int(subject_num) > num_subjects):
        print('Please enter a valid subject number, it should be',
              f'between 1 and {num_subjects}')
        subject_num = input('Enter your choice: ')
    subject_num = int(subject_num)

    # get books for selected subject
    books = get_books_by_subject(subjects[subject_num-1])
    num_books = len(books)

    # check if there are any books
    if num_books == 0:
        print('There are no books in this subject')
        return

    # display books, two at a time
    start_idx = 0
    end_idx = min(start_idx + 2, num_books)
    while True:
        print(f'\n{num_books} books available on this subject\n')
        if num_books - end_idx > 0:
            for i in range(start_idx, end_idx):
                print(f'Author:  {books[i][1]}')
                print(f'Title:   {books[i][2]}')
                print(f'ISBN:    {books[i][0]}')
                print(f'Price:   {books[i][3]}')
                print(f'Subject  {books[i][4]}\n')
        else:
            for i in range(start_idx, end_idx):
                print(f'Author:  {books[i][1]}')
                print(f'Title:   {books[i][2]}')
                print(f'ISBN:    {books[i][0]}')
                print(f'Price:   {books[i][3]}')
                print(f'Subject  {books[i][4]}\n')
            print('No more books available on this subject')

        # get user input for book choice
        choice = input('''\nEnter the ISBN to add to cart or
n ENTER to browse or
ENTER to go back to menu:\n''')
        if choice == '':
            return
        elif choice == 'n':
            start_idx = end_idx
            end_idx = min(start_idx + 2, num_books)
        else:
            if not re.match('^\d+$', choice):
                print('\nInvalid ISBN, it should contain only numbers')
                continue

            # Check if book exists in database
            isbn_query = 'SELECT * FROM books WHERE isbn=%s'
            book = executeSelectQuery(isbn_query, (choice,))
            if not book:
                print('\nInvalid book ISBN or Entered book ISBN does',
                      'not exist in our Book Shop, please enter the',
                      'correct ISBN')
                continue

            # get user input for quantity
            qty = input('Enter the quantity: ')
            while not qty.isnumeric():
                print('Invalid quantity, please enter a number')
                qty = input('Enter the quantity: ')
            qty = int(qty)

            # get book details
            book_isbn = book[0][0]

            update_cart(user, cart, book_isbn, qty)


def get_books_by_subject(subject):
    global conn
    global cur
    books = executeSelectQuery('SELECT * FROM books WHERE subject=%s',
                               subject)
    return books


def update_cart(user, cart, book_isbn, qty):
    # check if book already exists in cart
    for item in cart:
        if item[1] == book_isbn:
            new_item = item[:2] + (qty,) + item[2+1:]
            idx = cart.index(item)
            cart[idx] = new_item
            qty_update_query = '''UPDATE cart SET qty=%s WHERE isbn=%s
            AND userid=%s'''
            executeInputQuery(qty_update_query,
                              (qty, book_isbn, user['userid'],))
            return

    cart.append((user['userid'], book_isbn, qty))
    insert_cart_query = '''INSERT INTO cart (userid, isbn, qty)
    VALUES (%s, %s, %s)'''
    executeInputQuery(insert_cart_query,
                      (user['userid'], book_isbn, qty))


def search_by_author_title(user, cart):
    global conn
    global cur
    while True:
        print('\n1. Author Search')
        print('2. Title Search')
        print('3. Go Back to Main Menu')
        choice = input('\nType in your option: ')
        if choice == '1':
            search(user, cart, 'author')
        elif choice == '2':
            search(user, cart, 'title')
        elif choice == '3':
            return
        else:
            print('Invalid option, please try again')


def search(user, cart, search_type):
    if search_type == 'author':
        search_str = input('\nEnter author or partial author name: ')
        search_matching_books = get_books_by_author(search_str)
        if len(search_matching_books) == 0:
            print('0 books found')

        display_books(search_matching_books, user, cart)

    elif search_type == 'title':
        search_str = input('\nEnter title or part of the title: ')
        search_matching_books = get_books_by_title(search_str)
        if len(search_matching_books) == 0:
            print('0 books found')

        display_books(search_matching_books, user, cart)


def get_books_by_author(search_string):
    global conn
    global cur
    global books
    matching_books = []
    for book in books:
        if search_string.lower() in book[1].lower():
            matching_books.append(book)

    return matching_books


def get_books_by_title(search_string):
    global conn
    global cur
    global books
    matching_books = []
    for book in books:
        if search_string.lower() in book[2].lower():
            matching_books.append(book)

    return matching_books


def display_books(search_matching_books, user, cart):
    # display books, three at a time
    num_books = len(search_matching_books)

    start_idx = 0
    end_idx = min(start_idx + 3, num_books)
    while True:
        print(f'\n{num_books} books found\n')
        if num_books - end_idx > 0:
            for i in range(start_idx, end_idx):
                print(f'Author:  {search_matching_books[i][1]}')
                print(f'Title:   {search_matching_books[i][2]}')
                print(f'ISBN:    {search_matching_books[i][0]}')
                print(f'Price:   {search_matching_books[i][3]}')
                print(f'Subject  {search_matching_books[i][4]}\n')
        else:
            for i in range(start_idx, end_idx):
                print(f'Author:  {search_matching_books[i][1]}')
                print(f'Title:   {search_matching_books[i][2]}')
                print(f'ISBN:    {search_matching_books[i][0]}')
                print(f'Price:   {search_matching_books[i][3]}')
                print(f'Subject  {search_matching_books[i][4]}\n')
            print('No more books matching search criteria')

        # get user input for book choice
        choice = input('''\nEnter the ISBN to add to cart or
n ENTER to browse or
ENTER to go back to menu:\n''')
        if choice == '':
            return
        elif choice == 'n':
            start_idx = end_idx
            end_idx = min(start_idx + 3, num_books)
        else:
            if not re.match('^\d+$', choice):
                print('Invalid ISBN, it should contain only numbers')
                continue

            # Check if book exists in database
            isbn_query = 'SELECT * FROM books WHERE isbn=%s'
            book = executeSelectQuery(isbn_query, (choice,))
            if not book:
                print('Invalid book ISBN or Entered book ISBN does',
                      'not exist in our Book Shop, please enter the',
                      'correct ISBN')
                continue

            # get user input for quantity
            qty = input('Enter the quantity: ')
            while not qty.isnumeric():
                print('Invalid quantity, please enter a number')
                qty = input('Enter the quantity: ')
            qty = int(qty)

            # get book details
            book_isbn = book[0][0]

            update_cart(user, cart, book_isbn, qty)


def checkout(user, cart, orders):
    global conn
    global cur
    global books

    if cart is not None:
        # Current cart contents
        print('\nYour current cart contents:')
        print('\nISBN\t\tTitle\t\t\t\t\t\t\t\t$ Qty\tTotal')
        print('-' * 80)
        final_price = 0
        for item in cart:
            book_idx = get_book_by_isbn(item[1], books)
            total = books[book_idx][3] * int(item[2])
            final_price += total
            print(f'{books[book_idx][0]}  {books[book_idx][2]}\t\t',
                  f'{books[book_idx][3]} {item[2]} {total}')
            print('-' * 80)
        print(f'Total{" "*70}${final_price}')
        print('-' * 80)

        while True:
            checkout_option = input('Proceed to checkout? (y/n)?: ')
            if checkout_option.lower() == 'y':
                # Get current datetime
                now = datetime.now()

                # Generate estimated date for delivery (one week ahead)
                estimated_delivery_date = now + timedelta(days=7)

                # Save the order to the Order table with generated estimated
                # delivery date and null shipment date
                ono = save_order_to_database(user, estimated_delivery_date)

                # Save the order details to the 'odetails' table with quantity
                # and total price
                total_price = 0
                new_orders = []
                for item in cart:
                    book_idx = get_book_by_isbn(item[1], books)
                    price = books[book_idx][3]
                    total_price_per_isbn = price * item[2]
                    total_price += total_price_per_isbn
                    new_orders.append((ono[0][0], item[1], item[2],
                                       total_price_per_isbn))
                save_order_details_to_database(new_orders)

                # Print the invoice
                print(f'\n{"="*20}\n{" "*10}Invoice for Order no.{ono}\n',
                      f'{"="*20}')
                print('\nShipping Address & Billing Address')
                print(f'Name: {user["name"]}')
                print(f'Address: {user["address"]}')
                print(f'\t\t{user["city"]}')
                print(f'\t\t{user["state"]} {user["zip"]}')

                print('\nISBN\t\tTitle\t\t\t\t\t\t\t\t$ Qty\tTotal')
                print('-' * 80)
                for item in cart:
                    book_idx = get_book_by_isbn(item[1], books)
                    if book_idx is not None:
                        title = books[book_idx][2]
                        price = books[book_idx][3]
                        total_price_per_isbn = price * item[2]
                        print(f'{books[book_idx][0]}  {title}\t\t',
                              f'{price} {item[2]} {total_price_per_isbn}')
                print(f'Total{" "*70}${total_price}')
                print('-' * 80)
                print(f'{estimated_delivery_date.strftime("%Y-%m-%d")}\n',
                      f'{"-"*20}')

                # Clear the cart
                clean_db_cart(user)
                fetch_cart_orders(user, cart, orders)
                input('Press enter to go back to Menu')
                return
            elif checkout_option.lower() == 'n':
                return
            else:
                print('\nInvalid option, please try again')


def save_order_to_database(user, received_date):
    global conn
    global cur
    save_order_query = '''INSERT INTO orders (userid, received,
    shipAddress, shipCity, shipState, shipZip) VALUES
    (%s, %s, %s, %s, %s, %s)'''
    values = (user['userid'], received_date.strftime('%Y-%m-%d'),
              user['address'], user['city'], user['state'], user['zip'])
    executeInputQuery(save_order_query, values)

    get_ono_query = '''SELECT MAX(ono) FROM orders WHERE userid = %s AND
    received = %s AND shipAddress = %s AND shipCity = %s AND
    shipState = %s AND shipZip = %s'''
    new_orders_ono = executeSelectQuery(get_ono_query, values)
    return new_orders_ono


def get_book_by_isbn(book_isbn, books):
    global conn
    global cur
    for book in books:
        if book[0] == book_isbn:
            idx = books.index(book)
            return idx
    return None


def clean_db_cart(user):
    clear_cart_query = '''DELETE FROM cart WHERE userid = %s'''
    executeInputQuery(clear_cart_query, (user['userid'],))


def save_order_details_to_database(new_orders):
    global conn
    global cur
    save_order_details_query = '''INSERT INTO odetails (ono, isbn, qty, price)
    VALUES (%s, %s, %s, %s)'''
    for order in new_orders:
        values = (order[0], order[1], order[2], order[3])
        executeInputQuery(save_order_details_query, values)


def logout(user, cart, orders):   # ?? WORKING ON THIS !!
    global conn
    global cur
    # Clear the cart and orders
    cart.clear()
    orders.clear()

    # Clears the user details
    user.clear()

    # Log out the user
    print('Logging out...')
    mainmenu()


''' executeInputQuery()
This function executes a SQL query that modifies the database
'''


def executeInputQuery(query, val):
    global conn
    global cur
    cur.execute(query, val)
    conn.commit()


''' executeSelectQuery()
This function executes a SQL query that selects data from the
database and returns the results
'''


def executeSelectQuery(query, val=None):
    global conn
    global cur
    cur.execute(query, val)
    result = cur.fetchall()
    return result


# Connecting to the database
try:
    with connect(
        user=USER,
        password=getpass('Input database password: '),
        host=HOST,
        port=PORT,
        database=DB
    ) as conn:
        cur = conn.cursor()
        books = store_all_books()
        mainmenu()
        # ?? print(f'Connected to {DB} database') for DEBUGGING
except Error as e:
    print(f'Failed to connect to database: {e}')
finally:
    print('Thank you for using our Book Shop')
    print('Closing database connection')
    cur.close()
    conn.close()