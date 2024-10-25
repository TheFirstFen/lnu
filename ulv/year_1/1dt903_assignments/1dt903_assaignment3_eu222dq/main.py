# main.py

# Author: Emil Ulvagården
# Date: 2023-04-15

# Related files: book_store.sql, books.sql and schema.mwb

'''Description
    A functioning bookstore application.
    During my testing i get no faulty
    tasks and the program compleats
    its purpose without any errors.
    Using Flake8 for linting i have
    no visual warnings while using
    Python 3.11.2 64-bit.
'''

# Import modules:
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
from re import search, match
from hashlib import sha256
from getpass import getpass

# constant:
DATABASE = 'book_store'
HOST = 'localhost'
PORT = 3306
USER = 'root'
check_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
check_isbn = r'^\d+$'


def fetch_books():
    global conn
    global conn_cur

    # Fetch all book information from the database
    all_book_info = selectquery('SELECT * from books')
    return all_book_info


def mainmenu():
    global conn
    global conn_cur
    while True:
        # Showing the user the options they have and
        # prompting them to make a choice
        print('*' * 80)
        print('*' * 3 + ' ' * 74 + '*' * 3)
        print('***'+' '*18+'Welcome to the online Book Store'+' '*24+'***')
        print('*' * 3 + ' ' * 74 + '*' * 3)
        print('*' * 80)
        print(' '*25 + '1. Member Login')
        print(' '*25 + '2. New Member Registration')
        print(' '*25 + 'q. Quit')
        choice = input('Type in your choice: ', )
        if choice == '1':
            member_login()
        elif choice == '2':
            member_reg()
        elif choice == 'q':
            exit()
        else:
            print('type in one of the options to procied')


def member_reg():
    global conn
    global conn_cur
    # Inputs for member registration
    fname = input('Enter first name: ')
    lname = input('Enter last name: ')
    address = input('Enter address: ')
    city = input('Enter city: ')
    state = input('Enter state: ')
    zip = input('Enter zip: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')
    password = input('Enter password: ')

    # Checking if email is valid
    if not search(check_email, email):
        print('invalid email address, please enter a valid email')
        return

    # Checking if email exists in database
    existing_email = selectquery('SELECT * from members where email = %s',
                                 (email,), 'one')
    if existing_email:
        print('that email is already in use. Please try another valid email')
        return

    # hashing password
    hashed_password = sha256(password.encode()).hexdigest()

    # input user information in database
    try:
        query = '''INSERT INTO members
        (fname, lname, address, city, state, zip, phone, email, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        values = (fname, lname, address, city, state, int(zip),
                  phone, email, hashed_password)
        inputquery(query, values)
        print('You have registered successfully!')
        input('Press Enter to go back to Menu: ')
    except Error:
        print(f'failed to register user: {Error}')


def member_login():
    global conn
    global conn_cur
    email = input('enter email: ')
    password = input('enter password: ')

    if not search(check_email, email):
        print('Invalid email, please enter a valid email')
        return
    else:
        # Checking if user exists in database
        try:
            sql = '''SELECT * FROM members WHERE email=%s AND password=%s'''
            val = (email, sha256(password.encode()).hexdigest())
            myresult = selectquery(sql, val, 'one')

            if myresult:
                # If user exists, create user dictionary and login
                user_dict = user_dict_creation(email)
                print("Login successful.")
                stage2(user_dict)
            else:
                email_query = 'SELECT * FROM members WHERE email=%s'
                email_result = selectquery(email_query, (email,), 'one')
                if email_result:
                    # Email exists but invalid password
                    print("Invalid email/login credentials")
                    mainmenu()
                else:
                    # Email don't exist in database
                    print('Invalid email/login credentials')
                    mainmenu()
        except Error:
            print(f'failed to connect to database: {Error}')

        finally:
            disconnection(conn, conn_cur)


def disconnection(conn, conn_cur):
    # If connected to database, close the connection
    if (conn.is_connected()):
        print('closing database connection')
        conn_cur.close()
        conn.close()


def user_dict_creation(email):
    # Creates a dictionary with the information from the user
    global conn
    global conn_cur
    user_info = selectquery('SELECT * FROM members where email=%s',
                            (email,))
    user_dict = {
        'fname': user_info[0][0],
        'lname': user_info[0][1],
        'address': user_info[0][2],
        'city': user_info[0][3],
        'state': user_info[0][4],
        'zip': user_info[0][5],
        'phone': user_info[0][6],
        'email': user_info[0][7],
        'userid': user_info[0][8],
    }
    return user_dict


def stage2(user):
    global conn
    global conn_cur
    # Get user's cart and orders
    cart, orders = get_cart_and_orders(user)
    while True:
        print('*' * 80)
        print('*' * 3 + ' ' * 74 + '*' * 3)
        print('***'+' '*18+'Welcome to the online Book Store'+' '*24+'***')
        print('***' + ' ' * 26 + 'Member Menu' + ' ' * 37 + '***')
        print('*' * 3 + ' ' * 74 + '*' * 3)
        print('*' * 80)
        print(' '*25 + '1. Browse by subject')
        print(' '*25 + '2. Search by Author/Title')
        print(' '*25 + '3. check out')
        print(' '*25 + '4. logout')
        # Get input from user and send to the choosen menu
        choice = input('Enter your choice: ')
        if choice == '1':
            b_subject(user, cart)
        elif choice == '2':
            s_author_title(user, cart)
        elif choice == '3':
            check_out(user, cart, orders)
        elif choice == '4':
            logout(user, cart, orders)
        else:
            print('try another input')


def get_cart_and_orders(user, cart=None, orders=None):
    global conn
    global conn_cur

    # Clear user's cart and orders
    if cart is not None:
        cart.clear()
    if orders is not None:
        orders.clear()

    # Collect the user's cart and orders from database
    cart = selectquery('SELECT * FROM cart where userid = %s',
                       (user['userid'],))
    orders = selectquery('SELECT * FROM orders where userid = %s',
                         (user['userid'],))
    return cart, orders


def b_subject(user, cart):
    global conn
    global conn_cur

    # Collect a list from the database with all subjcts in ascending order
    query = ('SELECT DISTINCT subject FROM books ORDER BY subject ASC')
    subjects = selectquery(query)
    amount_sub = len(subjects)

    if amount_sub == 0:
        print('There are no subjects to view')
        return

    # Show the user all subjects
    print('subjects: ')
    for i in range(amount_sub):
        print(f'{i+1}. {subjects[i][0]}')

    # Ask for the user to chose a subject
    choice = input('Choose a subject: ')
    while not (choice.isnumeric() or int(choice) < 1 or
               int(choice) > amount_sub):
        print('Please enter a valid number for your chosen subject')
        choice = input('Choose a subject: ')
    choice = int(choice)

    # Asks the database for all books in the subject
    books = book_subject(subjects[choice-1])
    amount_books = len(books)

    # No books in the chosen subject
    if amount_books == 0:
        print('No books in this subject')
        return

    # Showing two books at a time from the chosen subject
    start = 0
    end = min(start + 2, amount_books)
    while True:
        print(f'\n{amount_books} books in this subject')
        if amount_books - end > 0:
            show_books_info(start, end, books)
        else:
            show_books_info(start, end, books)
            print('No books left to display in this subject')

        # prompt user to add books to cart, browse or return to previus menu
        choice = input('''\nEnter the ISBN to add to cart or
n ENTER to browse or ENTER to go back to menu:\n''')
        if choice == '':
            return
        elif choice == 'n':
            start = end
            end = min(start + 2, amount_books)
        else:
            # Verify the ISBN and query the database for the book with the
            # entered ISBN
            if not match(check_isbn, choice):
                print('\n Invalid ISBN, it should contain only numbers')
                continue

            isbn_query = 'SELECT * FROM books WHERE isbn = %s'
            book = selectquery(isbn_query, (choice,))

            # ISBN not found
            if not book:
                print('\nInvalid ISBN')
                continue
            else:
                # Asks the user for the quantity of the selected book
                qty = input('Enter the quantity: ')
                while not qty.isnumeric():
                    print('Invalid quantity, please enter a number')
                    qty = input('Enter the quantity: ')
                qty = int(qty)

                # Add book and quantity to cart
                isbn_book = book[0][0]
                refresh_cart(user, cart, isbn_book, qty)


def show_books_info(start, end, books):
    for i in range(start, end):
        print(f'Author: {books[i][1]}')
        print(f'Title: {books[i][2]}')
        print(f'ISBN: {books[i][0]}')
        print(f'Price: {books[i][3]}')
        print(f'Subject: {books[i][4]}\n')


def book_subject(subject):
    global conn
    global conn_cur
    # Select alll books with the given subject
    books = selectquery('SELECT * FROM books WHERE subject=%s',
                        subject)
    return books


def refresh_cart(user, cart, isbn_book, qty):
    # Search the cart for the given ISBN
    for item in cart:
        if item[1] == isbn_book:
            # If the book is in the cart, update the quantity
            new_item = item[:2] + (qty,) + item[2+1:]
            idx = cart.index(item)
            cart[idx] = new_item
            # Update the cart in the database
            qty_update_query = '''UPDATE cart SET qty=%s WHERE isbn=%s
            AND userid=%s'''
            inputquery(qty_update_query,
                       (qty, isbn_book, user['userid'],))
            return

    # If the book is not in cart, add it and its quantity
    cart.append((user['userid'], isbn_book, qty))
    # Add the book to the cart in the databas
    insert_cart_query = '''INSERT INTO cart (userid, isbn, qty)
    VALUES (%s, %s, %s)'''
    inputquery(insert_cart_query,
               (user['userid'], isbn_book, qty))


def s_author_title(user, cart):
    global conn
    global conn_cur
    while True:
        # Asks user what they want to do
        print('\nSearch by Author/Title: ')
        print('1. Author Search')
        print('2. Title Search')
        print('3. Go back to main menu')
        choice = input('Enter your choice: ')
        if choice == '1':
            s_author(user, cart)
        elif choice == '2':
            s_title(user, cart)
        elif choice == '3':
            return
        else:
            print('Invalid input, Please try again')


def s_author(user, cart):
    # Get list of books by the user's given author
    author_name = input('Enter authors name: ')
    matching_books = authors_books(author_name)
    if len(matching_books) == 0:
        print('No books found by that author')

    show_three_books(matching_books, user, cart)


def authors_books(author_name):
    global conn
    global conn_cur
    global books
    # Create list with all books that has the author thats inputed
    matching_books = []
    for book in books:
        if author_name.lower() in book[1].lower():
            matching_books.append(book)

    return matching_books


def s_title(user, cart):
    # Get list of books with the given title
    title_name = input('Enter titles name: ')
    matching_books = title_books(title_name)
    if len(matching_books) == 0:
        print('No books found with that title')

    show_three_books(matching_books, user, cart)


def title_books(title_name):
    global conn
    global conn_cur
    global books
    # Create list with all books with the given title
    matching_books = []
    for book in books:
        if title_name.lower() in book[2].lower():
            matching_books.append(book)

    return matching_books


def show_three_books(matching_books, user, cart):
    amount_books = len(matching_books)
    # Start and stop index for displaying books
    start = 0
    end = min(start + 3, amount_books)
    # Loop to display the books
    while True:
        print(f'{amount_books} books found')
        if amount_books - end > 0:
            show_books_info(start, end, matching_books)
        else:
            show_books_info(start, end, matching_books)
            print('No more books')

        # Asks user what they want to do
        choice = input('''Enter the ISBN to add to cart or
n enter to browse or enter to go back to menu: ''')
        if choice == '':
            return
        elif choice == 'n':
            start = end
            end = min(start + 3, amount_books)
        else:
            # Validating ISBN
            if not match(check_isbn, choice):
                print('Invalid ISBN, please try again')
                continue
            else:
                # Asking for the quantity and validationg it
                qty = input('Enter the quantity: ')
                while not qty.isnumeric():
                    print('Invalid quantity')
                    qty = input('Enter the quantity: ')
                qty = int(qty)
                # Getting ISBN of first book and then updating cart
                isbn_book = books[0][0]
                refresh_cart(user, cart, isbn_book, qty)


def check_out(user, cart, orders):
    global conn
    global conn_cur
    global books

    # Check if cart is empty
    if len(cart) != 0:
        cart_contains(cart, books)

        while True:
            option = input('Continue to checkout? (y/n): ')
            if option.lower() == 'y':
                now = datetime.now()

                # generate delivery date
                delivery_date = now + timedelta(days=7)

                # save details from order in database
                ono = save_orders(user, delivery_date)

                # Calculate total price of books in cart
                total_price = 0
                new_orders = []
                for item in cart:
                    book_index = get_book(item[1], books)
                    price = books[book_index][3]
                    total_price_book = price * item[2]
                    total_price += total_price_book
                    new_orders.append((ono[0][0], item[1], item[2],
                                      total_price_book))

                order_database(new_orders)

                # Generate invoice
                invoice(user, cart, ono, delivery_date, total_price)

                # Clear the cart
                clear_cart(user)

                # Update cart and orders
                get_cart_and_orders(user, cart, orders)

                input('Press enter to go back to menu: ')
                return
            elif option.lower() == 'n':
                return
            else:
                print('Invalid input')
    # If cart is empy, propt user to add books
    print('Cart is empty, please add some books to your cart')
    return


def cart_contains(cart, books):
    # showing info from the books in the cart and the total price
    print('Your cart contains: ')
    print('ISBN\tTitel\t\t\t\t\t\t\t$   Qty\tTotal')
    print('-' * 80)
    total_price = 0
    for item in cart:
        book_index = get_book(item[1], books)
        price = books[book_index][3]
        total = price * item[2]
        total_price += total
        space = 65 - (len(books[book_index][0]) + len(books[book_index][2])+4)
        print(f'{books[book_index][0]}  {books[book_index][2]}{" " * space}',
              f'{books[book_index][3]}  {item[2]}  {total}')
        print('-' * 80)
    print(f'Total{" " * 65}${total_price:.2f}')
    print('-' * 80)


def invoice(user, cart, ono, delivery_date, total_price):
    # showing info from user
    print(f'{"-"*80}\n{" "*20}Invoce for order no.{ono[0][0]}\n{"-"*80}')
    print('Shipping Address & Billing Address')
    print(f'Name: {user["fname"]} {user["lname"]}')
    print(f'Address: {user["address"]}')
    print(f'\t{user["city"]}')
    print(f'\t{user["state"]} {user["zip"]}')

    print('\nISBN\tTitle\t\t\t\t\t\t\t$   Qty\tTotal')
    print('-' * 80)
    total_price = 0
    # Show info from books in cart and calculate total price
    for item in cart:
        book_index = get_book(item[1], books)
        if book_index is not None:
            title = books[book_index][2]
            price = books[book_index][3]
            total_book_price = price * item[2]
            space = 65 - (len(books[book_index][0]) + len(title) + 4)
            print(f'{books[book_index][0]}  {title}{" " * space}',
                  f'{price}  {item[2]}  {total_book_price}')
            print('-' * 80)
            total_price += total_book_price
    print(f'Total{" "*65}${total_price:.2f}')
    print('-' * 80)
    print('Estimated delivery date:', f'{delivery_date.strftime("%Y-%m-%d")}')
    print('-' * 80)


def save_orders(user, delivery_date):
    global conn
    global conn_cur
    # Save order information in database
    save_query = '''INSERT INTO orders (userid, received,
    shipAddress, shipCity, shipState, shipZip) VALUES
    (%s, %s, %s, %s, %s, %s)'''
    values = (user['userid'], delivery_date.strftime('%Y-%m-%d'),
              user['address'], user['city'], user['state'], user['zip'])
    inputquery(save_query, values)

    # retrieve the maximum order number from database
    ono_query = '''SELECT MAX(ono) FROM orders WHERE userid = %s AND
    received = %s AND shipAddress = %s AND shipCity = %s AND shipState = %s
    AND shipZip = %s'''
    new_ono = selectquery(ono_query, values)
    return new_ono


def get_book(isbn_book, books):
    global conn
    global conn_cur
    # Gets index of the book from books based on ISBN
    for book in books:
        if book[0] == isbn_book:
            index = books.index(book)
            return index
    return None


def clear_cart(user):
    # Delets all items from the cart in the database
    query = '''DELETE FROM cart WHERE userid = %s'''
    inputquery(query, (user['userid'],))


def order_database(new_orders):
    global conn
    global conn_cur
    # statement for inserting new orders
    save_query = '''INSERT INTO odetails (ono, isbn, qty, price)
    VALUES (%s, %s, %s, %s)'''
    # Looping through each order in the list of new orders
    for order in new_orders:
        values = (order[0], order[1], order[2], order[3])
        # Insert new order into odetails in the database
        inputquery(save_query, values)


def logout(user, cart, orders):
    global conn
    global conn_cur
    # Clears cart, orders, user and returns to mainmenu
    cart.clear()
    orders.clear()

    user.clear()

    print('Logging out')
    mainmenu()


def selectquery(query, val=None, fetch='all'):
    global conn
    global conn_cur
    # Executes an select query depending on values and the fetch
    conn_cur.execute(query, val)
    if fetch == 'one':
        result = conn_cur.fetchone()
    elif fetch == 'all':
        result = conn_cur.fetchall()
    else:
        print('Invalid fetch')
        return
    return result


def inputquery(query, val):
    global conn
    global conn_cur
    # Executes an insert, update or delete query
    conn_cur.execute(query, val)
    conn.commit()


while True:
    # Connecting to database
    try:
        with mysql.connector.connect(
            user=USER,
            password=getpass('Input database password: '),
            host=HOST,
            port=PORT,
            database=DATABASE
        ) as conn:
            conn_cur = conn.cursor()
            books = fetch_books()
            mainmenu()
    except Error as e:
        print(f'Failed to connect to database: {e}')
    finally:
        disconnection(conn, conn_cur)
