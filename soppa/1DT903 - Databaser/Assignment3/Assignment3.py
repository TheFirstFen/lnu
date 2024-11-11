##############################################################
# Assignment 3 - 1DT903
# jw223rn - Jesper Wingren
# NOTE! I have changed the datatype of password to VARCHAR(80)
##############################################################


from mysql.connector import connect, Error
from getpass import getpass
from datetime import date, timedelta
import re
import bcrypt


# Sorting functions list:
# A. Store all books and Hashing
# B. ExecuteQueries
# C. CheckFunctions
# D. Getinfo functions
# E. Homescreen
# F. Login and member menu
# G. Subject search
# H. Author and Title search
# I. Cart/Quantity
# J. Checkout
# K. Invoice
# L. NewMember
# M. MainPart


##############################################################
# A. Store all books and Hashing
def store_all_books():
    """
    Stores all isbns of books in book_store as a list
    """
    global connection
    global all_books
    with connection.cursor() as cursor:
        cursor.execute("SELECT isbn FROM books")
        all_books = cursor.fetchall()


def hashing(password):
    """
    Hashes the password using SALT
    """
    passwd = password.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed


def checkhash(password, hashed):
    """
    Decrypts password and checks if correct login details
    """
    password = password.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False


##############################################################
# B. ExecuteQueries
def executeInputQuery(query, info):
    global connection
    with connection.cursor() as cursor:
        cursor.execute(query, info)
        connection.commit()


def executeDisplayQuery(query):
    global connection
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)


def executeSelectQuery(query):
    global connection
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result


##############################################################
# C. CheckFunctions
def check_if_in_cart(loggedin_id, isbn, in_cart):
    """
    Checks if the book already exists in cart
    Compares the ISBN to all books in users cart
    Asks if user wants to change the quantity
    Returns True if book already exists in cart
    """
    global connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT isbn FROM cart WHERE userid=%s", (loggedin_id,))
        result = cursor.fetchall()
        result = result
    for books in result:
        if isbn == books[0]:
            print("Book already exists in cart!")
            with connection.cursor() as cursor:
                cursor.execute("""SELECT qty
                                  FROM cart
                                  WHERE isbn=%s
                                  AND userid=%s""", (isbn, loggedin_id))
                quantity = cursor.fetchone()
                quantity = quantity[0]
            answer = input(f"Current quantity is {quantity} would\
                             you like to change? (Y/N): ")
            change_quantity_input(answer, isbn, loggedin_id)
            return True


def check_if_input(x, temp):
    """
    For every Not NULLABLE value check if there is an input
    """
    C = ["phone", "fname", "lname", "address", "city", "state",
         "zip", "email", "password", "userid"]
    tx = x.strip()           # Removes if only whitespaces have been entered
    if not bool(tx):         # If string is not empty returns true
        x = input(f"Error! Please input new {C[temp]}: ")
        return check_if_input(x, temp)
    else:
        return x


def check_zip(Mzip):
    """
    Checks the users zip if contains only numbers
    Returns zip if Czip is True otherwise asks user for a valid input
    """
    Czip = False
    # Checks if zip contains digits
    for char in Mzip:
        if 48 <= ord(char) <= 57:
            Czip = True
    if Czip:
        return Mzip
    else:
        print("False zip, use digits!")
        Mzip = input("New zip: ")
        return check_zip(Mzip)


def check_duplicate_email(Mmail):
    """
    Checks if a user exists with the email that was inputed
    """
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*'
                       r'[A-Za-z0-9]+'
                       r'@[A-Za-z0-9-]+'
                       r'(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(regex, Mmail):
        print("Please provide a valid email!")
        Mmail = input("New mail: ")
        return check_duplicate_email(Mmail)
    query = "SELECT email FROM members"
    result = executeSelectQuery(query)
    for mail in result:
        if Mmail in mail:
            print("Email already taken!")
            Mmail = input("New mail: ")
            return check_duplicate_email(Mmail)
    return Mmail


def check_if_user_exists(Imail, Ipassword):
    """
    Checks if the mail used when logging in is connected to a member
    """
    query = "SELECT email FROM members"
    result = executeSelectQuery(query)
    for mail in result:
        if Imail in mail:
            return check_password(Imail, Ipassword)
    return False


def check_password(Imail, Ipassword):
    """
    Checks if the password used is correct for the email
    """
    global connection
    query = "SELECT password FROM members WHERE email=%s"
    with connection.cursor() as cursor:
        cursor.execute(query, (Imail,))
        result = cursor.fetchone()
    if checkhash(Ipassword, result[0]):
        return True


##############################################################
# D. Getinfo functions
def get_bookinfo(isbn):
    """
    Gets the info about the book using ISBN
    Returns a list of the book info
    """
    book_info = []
    book_info.append(isbn)
    with connection.cursor() as cursor:
        cursor.execute("""SELECT title, author, price, subject
                          FROM books
                          WHERE isbn=%s""", (isbn,))
        book = cursor.fetchall()
        for info in book[0]:
            book_info.append(info)
        return book_info


def get_user_info(loggedin_id):
    """
    Gets the info about a user using the userid
    Returns a list of the users info
    """
    user_info = []
    user_info.append(loggedin_id)
    with connection.cursor() as cursor:
        cursor.execute("""SELECT fname,lname,address,city,state,zip,phone
                          FROM members
                          WHERE userid=%s""", (loggedin_id,))
        user = cursor.fetchall()
        for info in user[0]:
            user_info.append(info)
        return user_info


##############################################################
# E. Homescreen
def homescreen():
    """
    Prints the homescreen which is displayed when accessing the book store
    """
    print("*" * 70 + "")
    print("***" + " " * 64 + "***")
    print("***" + "Welcome to the Online Book Store!".center(64) + "***")
    print("***" + " " * 64 + "***")
    print("*" * 70)
    print(" " * 25 + "1. Member Login\n")
    print(" " * 25 + "2. New Member Registration\n")
    print(" " * 25 + "q. Quit\n")
    option = input("Type in your option: ")
    homescreen_input(option)


def homescreen_input(option):
    """
    Error checking function that forces the user to input a correct value
    Uses recursive function if input is false
    """
    if option == "1":
        login_screen()
    elif option == "2":
        newMember()
    elif option == "q":
        quit()
    else:
        print("False Input!")
        NewInput = input("Try again: ")
        homescreen_input(NewInput)


##############################################################
# F. Login and member menu
def login_screen():
    """
    Displays the log-in screen
    Uses help functions to login the user if the credentials are correct
    """
    global connection
    Lmail = input("\nEnter email: ")
    Lpassword = getpass("Enter password: ")
    if check_if_user_exists(Lmail, Lpassword):
        query = "SELECT userid FROM members WHERE email=%s"
        with connection.cursor() as cursor:
            cursor.execute(query, (Lmail,))
            result = cursor.fetchone()
        member_menu(result[0])
    else:
        print("Incorrect user details")
        login_screen()


def member_menu(loggedin_id):
    """
    Displays the member menu for the logged in user
    """
    print("*" * 70 + "")
    print("***" + " " * 64 + "***")
    print("***" + "Welcome to the Online Book Store!".center(64) + "***")
    print("***" + "Member Menu".center(64) + "***")
    print("***" + " " * 64 + "***")
    print("*" * 70)
    print(" " * 25 + "1. Browse by subject\n")
    print(" " * 25 + "2. Search by authour/title\n")
    print(" " * 25 + "3. Checkout\n")
    print(" " * 25 + "4. Logout\n")
    Moption = input("Type in your option: ")
    member_menu_input(Moption, loggedin_id)


def member_menu_input(option, loggedin_id):
    """
    Error checking function that forces the user to input a correct option
    """
    invoice = False
    if option == "1":
        subjectB(loggedin_id)
    elif option == "2":
        author_titleB(loggedin_id)
    elif option == "3":
        print("\nCurrent Cart Contents:\n")
        checkout(loggedin_id, invoice)
    elif option == "4":
        loggedin_id = ""
        homescreen()
    else:
        print("False Input!")
        NewInput = input("Try again: ")
        member_menu_input(NewInput, loggedin_id)


##############################################################
# G. Subject search
def subjectB(loggedin_id):
    """
    Prints all available subjects in book store
    Using distinct query it collects all existing subjects and assigns
    a number to it
    Using indexes it checks if the number is a correct input
    """
    query = ("SELECT DISTINCT subject FROM books ORDER BY subject")
    result = executeSelectQuery(query)
    for i, sub in enumerate(result):
        print(f"{i + 1} {(sub[0])}")
    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print(f"Please input an integer between 1 and {len(result)}")
        option = int(input("Enter your choice: "))
    while not 0 < option < len(result):
        print("False Input!")
        option = input("Try again: ")
    subject = result[option - 1]
    for sub in subject:
        Msubject = sub
    display_books_subject(Msubject, loggedin_id)


def display_books_subject(subject, loggedin_id):
    """
    Stores all books within the subject and counts hwo many of them exists
    """
    global connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT isbn FROM books WHERE subject=%s", (subject,))
        result = cursor.fetchall()
        cursor.execute("""SELECT COUNT(isbn)
                          FROM books
                          WHERE subject=%s""", (subject,))
        count = cursor.fetchall()
        count = count[0]  # To print the result in a pure string
        print("-" * 70)
        print("-" * 70)
        print(f"{count[0]} books available in this subject")
    option = "n"
    temp = 0
    page = 1
    display_books_input(result, loggedin_id, option, temp, page)


##############################################################
# H. Author and Title search
def author_titleB(loggedin_id):
    """
    Displays the options the user has when searching by author or title
    """
    print("1. Author Search")
    print("2. Title Search")
    print("3. Go back to member Menu")
    option = input("\nType in your option: ")
    author_titleB_input(loggedin_id, option)


def author_titleB_input(loggedin_id, option):
    """
    Error checking the input
    """
    if option == "1":
        authorB(loggedin_id)
    elif option == "2":
        titleB(loggedin_id)
    elif option == "3":
        member_menu(loggedin_id)
    else:
        print("False Input!")
        option = input("Try again: ")
        author_titleB_input(loggedin_id, option)


def authorB(loggedin_id):
    """
    Returns books with an author containing the string searched for by the user
    """
    global connection
    search = input("\nEnter authors name or part of authors name: ")
    corrsearch = "%"
    for char in search:
        corrsearch = corrsearch + char
    corrsearch = corrsearch + "%"
    with connection.cursor() as cursor:
        cursor.execute("""SELECT isbn
                          FROM books
                          WHERE author LIKE %s""", (corrsearch,))
        result = cursor.fetchall()
        cursor.execute("""SELECT COUNT(isbn)
                          FROM books
                          WHERE author LIKE %s""", (corrsearch,))
        count = cursor.fetchall()
        count = count[0]
        print("-" * 70)
        print("-" * 70)
        print(f"{count[0]} books available with this authors name")
    option = "n"
    temp = 0
    page = 1
    if len(result) == 0:
        authorB(loggedin_id)
    else:
        display_books_input(result, loggedin_id, option, temp, page)


def titleB(loggedin_id):
    """
    Returns books with an author containing the string searched for by the user
    """
    global connection
    search = input("\nEnter title or part of title: ")
    corrsearch = "%"
    for char in search:
        corrsearch = corrsearch + char
    corrsearch = corrsearch + "%"
    with connection.cursor() as cursor:
        cursor.execute("""SELECT isbn
                          FROM books
                          WHERE title LIKE %s""", (corrsearch,))
        result = cursor.fetchall()
        cursor.execute("""SELECT COUNT(isbn)
                          FROM books
                          WHERE title LIKE %s""", (corrsearch,))
        count = cursor.fetchall()
        count = count[0]
        print("-" * 70)
        print("-" * 70)
        print(f"{count[0]} books available with this title")
    option = "n"
    temp = 0
    page = 1
    if len(result) == 0:
        titleB(loggedin_id)
    else:
        display_books_input(result, loggedin_id, option, temp, page)


def display_books_input(result, loggedin_id, option, temp, page):
    """
    Displays the books from the tuple containing ISBNs
    that is collected using other functions
    Also checks the users input, if its valid, and if
    it supposed to add the book to cart
    """
    global all_books
    bookaddedtocart = False
    while option == "n":
        if temp == (len(result) - 1):
            print("-" * 70)
            display_book_info(result[temp][0])
            print("-" * 70)
            print(f"Current page {page}")
            temp = 0
            page = 1
            option = input("\nEnter ISBN to add to cart\nEnter n then\
 ENTER to browse\nEnter ENTER to go back to menu:\n")
        elif temp == len(result):
            print("-" * 70)
            temp = 0
            page = 1
            display_book_info(result[temp][0])
            display_book_info(result[temp + 1][0])
            print("-" * 70)
            print(f"Current page {page}")
            temp += 2
            page += 1
            option = input("\nEnter ISBN to add to cart\nEnter n then\
 ENTER to browse\nEnter ENTER to go back to menu:\n")
        else:
            print("-" * 70)
            display_book_info(result[temp][0])
            display_book_info(result[temp + 1][0])
            print("-" * 70)
            print(f"Current page {page}")
            temp += 2
            page += 1
            option = input("\nEnter ISBN to add to cart\nEnter n then\
 ENTER to browse\nEnter ENTER to go back to menu:\n")

    for isbn in all_books:
        if option == isbn[0]:
            book_to_cart = option
            quantity = input("Enter quantity: ")
            add_to_cart(book_to_cart, quantity, loggedin_id)
            bookaddedtocart = True
            option = input("\nEnter ISBN to add to cart\nEnter n then\
 ENTER to browse\nEnter ENTER to go back to menu:\n")
    if option == "":
        member_menu(loggedin_id)
    elif not bookaddedtocart:
        print("False input!")
        option = input("Please provide a correct input: ")
        display_books_input(result, loggedin_id, option, temp, page)
    else:
        display_books_input(result, loggedin_id, option, temp, page)


def display_book_info(isbn):
    """
    Displays the information about the book that is supposed to be displayed
    """
    global connection
    with connection.cursor() as cursor:
        cursor.execute("""SELECT author, title, price, subject
                          FROM books
                          WHERE isbn=%s""", (isbn,))
        result = cursor.fetchall()
        result = result[0]
    print("-" * 70)
    print(f"Author: {result[0]}")
    print(f"Title: {result[1]}")
    print(f"ISBN: {isbn}")
    print(f"Price: {result[2]}")
    print(f"Subject: {result[3]}")


##############################################################
# I. Cart/Quantity
def add_to_cart(isbn, quantity, loggedin_id):
    in_cart = False
    in_cart = check_if_in_cart(loggedin_id, isbn, in_cart)
    if not in_cart:
        C = (loggedin_id, isbn, quantity)
        executeInputQuery("""
        INSERT INTO cart
        (userid, isbn, qty)
        VALUES ( %s, %s, %s)
        """, C)
        book_info = get_bookinfo(isbn)
        print(f"Successfully added {book_info[1]} to cart!")


def change_quantity_input(answer, isbn, loggedin_id):
    if answer == "Y" or answer == "y":
        change_quantity(isbn, loggedin_id)
    elif answer != "N" and answer != "n":
        print("False input!")
        answer = input("Please answer Y or N: ")
        change_quantity_input(answer, isbn, loggedin_id)


def change_quantity(isbn, loggedin_id):
    n_qty = input("Please provide new quantity: ")
    B = (n_qty, isbn, loggedin_id)
    with connection.cursor() as cursor:
        cursor.execute("""UPDATE cart
                        SET qty=%s
                        WHERE isbn=%s AND userid=%s""", B)
        connection.commit()
    print(f"Successfully updated quantity to {n_qty}")


##############################################################
# J. Checkout
def checkout(loggedin_id, invoice):
    """
    Prints the current cart contents and the total price
    Asks if the user wants to checkout
    """
    totalprice = float(0)
    with connection.cursor() as cursor:
        cursor.execute("""SELECT isbn,qty
                          FROM cart
                          WHERE userid=%s""", (loggedin_id,))
        books_incart = cursor.fetchall()
        if books_incart == []:
            print("Empty cart!")
            option = input("Choose a new option: ")
            member_menu_input(option, loggedin_id)
    print("ISBN" + " " * 8, end="")
    print("Title" + " " * 40, end="")
    print("Price" + " " * 2, end="")
    print("Qty" + " " * 4, end="")
    print("Total")
    print("-" * 76)
    for i in range(len(books_incart)):
        book = books_incart[i][0]
        Current_book = get_bookinfo(book)
        quantity_book = books_incart[i][1]
        print(Current_book[0] + " " * (12 - len(Current_book[0])), end="")
        if len(Current_book[1]) >= 40:
            title = ""
            for i, char in enumerate(Current_book[1]):
                if i <= 40:
                    title += char
            title += "..."
        else:
            title = Current_book[1]
        print(title + " " * (45 - len(title)), end="")
        print(str(Current_book[3]) + " " * (7 - len(str(Current_book[3]))),
              end="")
        print(str(quantity_book) + (" " * (7 - len(str(quantity_book)))),
              end="")
        price_t_qty = Current_book[3] * quantity_book
        price_t_qty = round(price_t_qty, 2)
        print(str(price_t_qty) + " " * (5 - len(str(price_t_qty))))
        totalprice += price_t_qty
        totalprice = round(totalprice, 2)
    print("-" * 76)
    print("Total" + " " * 65 + "$" + str(totalprice))
    print("-" * 76)
    if invoice:
        clearcart(loggedin_id)
        input("Press enter to go back to menu")
        member_menu(loggedin_id)
    else:
        option = input("\nProceed to checkout (Y/N)?: ")
        checkout_option(option, loggedin_id)


def checkout_option(option, loggedin_id):
    """
    Error handling function to get the correct user input
    """
    if option == "Y" or option == "y":
        create_invoice(loggedin_id)
        invoice = True
        checkout(loggedin_id, invoice)
    elif option != "N" and option != "n":
        print("False input!")
        option = input("Please answer Y or N: ")
        checkout_option(option, loggedin_id)
    else:
        member_menu(loggedin_id)


##############################################################
# K. Invoice
def create_invoice(loggedin_id):
    """
    Creates an innvoice and an order in the database
    """
    global connection
    user_info = get_user_info(loggedin_id)
    current_date = date.today()
    invoi = [loggedin_id, current_date, user_info[3],
             user_info[4], user_info[5], user_info[6]]
    with connection.cursor() as cursor:
        cursor.execute("""
    INSERT INTO orders
    (userid, ono, received, shipped, shipAdress, shipCity, shipState, shipZip)
    VALUES (%s, 0, %s, NULL, %s, %s, %s, %s)
    """, invoi)
        connection.commit()
    invoice_info(loggedin_id, current_date)
    create_odetails(loggedin_id, current_date)


def create_odetails(loggedin_id, date):
    """
    Inserts values to odetails table in database
    """
    global connection
    with connection.cursor() as cursor:
        cursor.execute("""SELECT ono
                          FROM orders
                          WHERE userid=%s AND received=%s
                          ORDER BY ono DESC""", (loggedin_id, date,))
        ono = cursor.fetchall()
        ono = ono[0][0]
        cursor.execute("""SELECT isbn,qty
                          FROM cart
                          WHERE userid=%s""", (loggedin_id,))
        books_incart = cursor.fetchall()
        for i in range(len(books_incart)):
            tot_price = 0
            book = books_incart[i][0]
            current_book = get_bookinfo(book)
            quantity_book = books_incart[i][1]
            tot_price = current_book[3] * quantity_book
            book_order = [ono, book, quantity_book, tot_price]
            cursor.execute("""INSERT INTO odetails (ono, isbn, qty, price)
                              VALUES (%s, %s, %s, %s)""", book_order)
            connection.commit()


def invoice_info(loggedin_id, date):
    """
    Displays the users shipping and billing address
    """
    global connection
    with connection.cursor() as cursor:
        cursor.execute("""SELECT ono
                          FROM orders
                          WHERE userid=%s AND received=%s
                          ORDER BY ono DESC""", (loggedin_id, date,))
        ono = cursor.fetchall()
        ono = ono[0][0]
        user_info = get_user_info(loggedin_id)
    name = user_info[1] + " " + user_info[2]
    print(f"Invoice for order no.{ono}".center(76))
    print()
    print(" " * 6 + "Shipping address" + " " * 25 + "Billing address")
    print(" " * 6 + f"Name:     {name}" + " " * (31 - len(name)), end="")
    print(f"Name:     {name}")
    print(" " * 6 + f"Address:  {user_info[3]}" +
          " " * (31 - len(user_info[3])), end="")
    print(f"Address:  {user_info[3]}")
    print(" " * 16 + f"{user_info[4]}" + " " * (41 - len(user_info[3])),
          end="")
    print(f"{user_info[4]}")
    print(" " * 16 + f"{user_info[5]} {user_info[6]}" +
          " " * (40 - ((len(user_info[5])) + len(str(user_info[6])))), end="")
    print(f"{user_info[5]} {user_info[6]}\n")
    ship_date = date - timedelta(days=7)
    print(f"\nEstimated delivery day: {ship_date}\n")


def clearcart(loggedin_id):
    """
    Removes the cart of the user whom created an order
    """
    global connection
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM cart WHERE userid=%s", (loggedin_id,))
        connection.commit()


##############################################################
# L. NewMember
def newMember():
    """
    Creates a new member
    Takes the input from user
    Checks that all inputs are correct
    Inputs details into members table
    """
    print("Welcome to the online book store!")
    print("New member registration")
    Mfname = input("Enter first name: ")
    Mlname = input("Enter last name: ")
    Maddress = input("Enter street address: ")
    Mcity = input("Enter city: ")
    Mstate = input("Enter state: ")
    Mzip = input("Enter zip: ")
    Mphone = input("Enter phone: ")
    Mmail = input("Enter email: ")
    Mpass = getpass("Enter password: ")
    Mpass = hashing(Mpass)
    M = [Mphone, Mfname, Mlname, Maddress, Mcity, Mstate, Mzip, Mmail, Mpass]
    temp = 0                            # To not get an error if phone is NULL
    for x in M:
        if temp != 0:              # Check if a NOT NULLABLE objects are NULL
            nx = check_if_input(x, temp)
            M[temp] = nx
        temp += 1
    Nmail = check_duplicate_email(Mmail)  # Check if the given email is taken
    M[7] = Nmail
    Nzip = check_zip(Mzip)
    M[6] = Nzip
    executeInputQuery("""
    INSERT INTO members
    (phone, fname, lname, address, city, state, zip, email, password, userid)
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)
    """, M)
    print("You have registered successfully!")
    input("Press Enter to go back to Menu\n")
    homescreen()


##############################################################
# M. MainPart
try:
    with connect(
        user='root',
        password=getpass("Input database password: "),
        host='localhost',
        database='book_store'
    ) as connection:
        store_all_books()
        homescreen()
        print("Connected to database successfully!")
except Error as e:
    print(f"Failed to connect to database: {e}")
