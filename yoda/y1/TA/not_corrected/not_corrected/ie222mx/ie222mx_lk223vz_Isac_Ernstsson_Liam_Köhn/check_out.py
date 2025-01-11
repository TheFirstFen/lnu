from mysql.connector import Error
import time
import datetime
import printing_functions
import user_input


# checkout functions
def insert_to_cart(db, userid: int, isbn: str, qty: int):
    # Query for entering a new member with placeholders
    query = '''insert into cart(userid, isbn, qty)
Values(%s, %s, %s);'''

    values = (userid, isbn, qty)

    try:
        # Use the execute_with_commit method to run the query with the values
        db.execute_with_commit(query, values)
        input('Press enter to return to continue browsing')
        print('Returning...')
        return
    except Error as e:
        if e.errno == 1062:
            print('Book already in cart')
            update_qty(db, userid, isbn, qty)


# get cart function
def get_cart(db, userid: int) -> list:
    # Query for entering a new member with placeholders
    query = f'''select * from cart where userid = {userid};'''

    try:
        cart = db.execute_and_fetchall(query)
        # geting the cart with the books title etc.
        books = []  # List of all books in the cart as tuples

        for _, isbn, qty in cart:
            book_details = get_book(db, isbn)
            for book in book_details:
                # Append the book tuple with qty
                books.append(book + (qty,))
                # books = [(isbn, author, title, price, subject, qty), ...]
        return books

    except Error as e:
        print("An error occurred in get cart:", e)
        input('Press enter to accept and return')


def get_book(db, isbn: str):
    query = f'''select * from books where isbn = {isbn};'''

    try:
        book = db.execute_and_fetchall(query)
        return book
    except Error as e:
        print("An error occurred in get_book:", e)
        input('Press enter to accept and return')


def clear_cart(db, userid: int):
    # Query to delete from the cart where userid matches, using placeholder
    query = f'''DELETE FROM cart WHERE userid = {userid};'''
    try:
        # Execute the query with the user ID as the value
        db.execute_with_commit(query)
        time.sleep(1)
        return
    except Error as e:
        print("An error occurred in clear_cart:", e)
        input('Press enter to accept and return')


def update_qty(db, userid: int, isbn: str, qty: int):
    old_qty = db.execute_and_fetchall(
        f'select qty from cart where userid = {userid} and isbn = "{isbn}";')[0][0]
    qty += old_qty
    # Query for entering a new member with placeholders
    query = '''update cart set qty = %s where userid = %s and isbn = %s;'''
    values = (qty, userid, isbn)
    try:
        # Use the execute_with_commit method to run the query with the values
        db.execute_with_commit(query, values)
        print('Total quantity:', qty)
        time.sleep(1)
        return
    except Error as e:
        print("An error occurred in update_cart:", e)
        input('Press enter to accept and return.')


def create_order(db, userid: int):
    try:
        # get time of order
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        # Get member details
        query = f'''select * from members where userid = {userid};'''
        member = db.execute_and_fetchall(query)

        query = '''INSERT INTO orders (userid, created, shipAddress, shipCity, shipZip)
        VALUES (%s, %s, %s, %s, %s);'''
        values = (userid, formatted_time, member[0][3], member[0][4], member[0][5])
        db.execute_with_commit(query, values)
        query = f'''SELECT ono FROM orders
        WHERE userid = {userid} and created = "{formatted_time}";'''

        ono = db.execute_and_fetchall(query)
        print(ono)
        return member, ono[0][0]
    except Error as e:
        print("An error occurred in create_order:", e)
        input('Press enter to accept and return')


def check_out(db, userid: int):
    books = get_cart(db, userid)
    # books = [(isbn, author, title, price, subject, qty), ...]
    if books:
        # Print the cart
        printing_functions.print_cart(books)

        # proceed to checkout?
        check_out = False
        while check_out is False:
            choice = user_input.get_str('Proceed to checkout? [y/n]: ')
            if  choice.lower() == 'y':
                check_out = True
                member, ono = create_order(db, userid)
                printing_functions.print_invoice(member, ono, books)
                try:
                    query = '''INSERT INTO odetails(ono, isbn, qty, amount)
                    VALUES (%s, %s, %s, %s);'''
                    for item in books:
                        isbn = item[0]
                        qty = item[5]
                        amount = qty * item[3]
                        values = (ono, isbn, qty, amount)
                        db.execute_with_commit(query, values)
                    clear_cart(db, userid)
                except Error as e:
                    print("An error occurred in check_out:", e)
                    input('Press enter to accept and return')
                return
            elif choice.lower() == 'n':
                print('Returning to main menu')
                return
            else:
                print('Wrong input, try again!')
    else:
        print('Your cart is empty!')
        print('You can brows our books by subject, author or title')
        input('Press enter to return to member menu')
        return
