import mysql.connector
from datetime import date, timedelta

conn = mysql.connector.connect(user="root", password="Schroder13", database="book_store",    charset="utf8mb4",  # Ensure utf8mb4 is used
    collation="utf8mb4_unicode_ci")

cursor = conn.cursor(buffered=True)


# Function to register new members
def member_registration():
    print("Welcome to the online book store")
    print("New member registration\n")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    address = input("Enter street address: ")
    city = input("Enter city: ")
    zip = input("Enter zip: ")
    phone = input("Enter phone: ")
    email = input("Enter email address: ")
    password = input("\nPassword: ")

    # Adding new member into the database
    insert_members = f'''INSERT INTO members
    (fname, lname, address, city, zip, phone, email, password)
    VALUES (('{fname}'), ('{lname}'), ('{address}'), ('{city}'),
    ('{zip}'), ('{phone}'), ('{email}'), ('{password}'))'''

    cursor.execute(insert_members)
    conn.commit()

    print("\nYou have registered succesfully!")
    _ = input("Press Enter to go back to Menu")
    main_menu()


def member_login():
    # Login and checking that the user is registered and email and password match
    while True:
        email = input("\nEnter email: ")
        password = input("Enter password: ")
        try:
            cursor.execute(f"SELECT email FROM members WHERE email LIKE '{email}'")
            compare_email = cursor.fetchone()[0]

            cursor.execute(f"SELECT password FROM members WHERE email LIKE '{email}'")
            compare_password = cursor.fetchone()[0]
        except TypeError:
            print("\nIncorrect email or password")
            continue
        else:
            break

    if email == compare_email and password == compare_password:
        member_menu(email)
    else:
        print("\nIncorrect email or password")
        member_login()


def member_menu(email):
    print("\nWelcome to the online book store")
    print("Member Menu")
    print("\n1. Browse by subject")
    print("2. Search by author/title")
    print("3. Check out")
    print("4. Logout")

    # Choice for where to go
    choice = input("\nType in your option: ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Not a valid option")
        choice = input("\nType in your option: ")
    if choice == "1":
        browse(email)
    elif choice == "2":
        at_search_choice(email)
    elif choice == "3":
        check_out(email)
    else:
        main_menu()


def browse(email):
    # Getting the subjects for the books and turning it into a set to avoid duplicates
    cursor.execute("SELECT subject FROM books")
    subject = set(cursor.fetchall())
    subject = list(subject)
    subject.sort()

    temp = 1
    for i in subject:
        print(f"{temp}. {i[0]}")
        temp += 1

    choice = int(input("Type in your choice: "))

    print(subject[choice - 1][0])

    # Getting all the books with the subject of choice
    cursor.execute(f"SELECT * FROM books WHERE subject LIKE '{subject[choice - 1][0]}'")
    book_subject = cursor.fetchall()

    choice_browse = None
    index1 = 0
    index2 = 1
    # Printing out the books aslong when the user doesnt just press enter
    while choice_browse != "":
        print(f"{len(book_subject)} books on this subject\n")
        print(f"Author: {book_subject[index1][1]}")
        print(f"Title: {book_subject[index1][2]}")
        print(f"ISBN: {book_subject[index1][0]}")
        print(f"Price: {book_subject[index1][3]}")
        print(f"Subject: {book_subject[index1][4]}\n")

        print(f"Author: {book_subject[index2][1]}")
        print(f"Title: {book_subject[index2][2]}")
        print(f"ISBN: {book_subject[index2][0]}")
        print(f"Price: {book_subject[index2][3]}")
        print(f"Subject: {book_subject[index2][4]}")

        print("\nEnter ISBN to enter to cart or")
        print("'n' to browse or")
        choice_browse = input("ENTER to go back to menu: ")
        if choice_browse == "n":
            index1 += 2
            index2 += 2
        # Checking if the user typed in either if the isbns
        elif choice_browse == book_subject[index1][0] or choice_browse == book_subject[index2][0]:
            qty = int(input("Enter quantity: "))
            cursor.execute(f"SELECT userid FROM members WHERE email LIKE '{email}'")
            userid = cursor.fetchone()[0]

            cursor.execute(f"SELECT qty FROM cart WHERE userid LIKE '{userid}' AND isbn LIKE '{choice_browse}'")
            # Checking if the book has already been added to cart
            try:
                qty_check = cursor.fetchone()[0]
            except TypeError:
                # If given this error it means the book has not yet been added so we assign a empty variable
                qty_check = 0
                pass
            if qty_check > 0:
                insert_cart = f'''UPDATE cart
                SET qty = '{qty + qty_check}'
                WHERE userid LIKE '{userid}' AND isbn LIKE '{choice_browse}'
                '''
            else:
                insert_cart = f'''INSERT INTO cart
                (userid, isbn, qty)
                VALUES (('{userid}'), ('{choice_browse}'), ('{qty}'))
                '''
            cursor.execute(insert_cart)
            conn.commit()
            print("\nSuccesfully added to cart\n")
            _ = input("Press enter to keep browsing")
        else:
            member_menu(email)


# Choice for either searching for author or title
def at_search_choice(email):
    print("\n1. Author search")
    print("2. Title search")
    print("3. Go back to main menu")
    choice = input("\nType in your option: ")
    while choice != "1" and choice != "2" and choice != "3":
        print("Not a valid choice")
        choice = input("Type in your option: ")
    if choice == "1":
        author_search(email)
    elif choice == "2":
        title_search(email)
    else:
        member_menu(email)


def author_search(email):
    check = 0
    while check == 0:
        search = input("Enter author name or part of author name: ")
        cursor.execute(f"SELECT * FROM books WHERE author LIKE '{search}%'")
        books = cursor.fetchall()
        check = len(books)
        # Checking if the search yielded results
        if check == 0:
            print("No author by that name")
            author_search(email)

    choice_browse = None
    index1 = 0
    index2 = 1
    index3 = 3
    while choice_browse != "":
        print(f"{len(books)} books by this author\n")
        print(f"Author: {books[index1][1]}")
        print(f"Title: {books[index1][2]}")
        print(f"ISBN: {books[index1][0]}")
        print(f"Price: {books[index1][3]}")
        print(f"Subject: {books[index1][4]}\n")

        # Making sure that it only tries to print out more than one result if
        # There are more than 1 result
        if len(books) >= 2:
            print(f"Author: {books[index2][1]}")
            print(f"Title: {books[index2][2]}")
            print(f"ISBN: {books[index2][0]}")
            print(f"Price: {books[index2][3]}")
            print(f"Subject: {books[index2][4]}\n")

        if len(books >= 3):
            print(f"Author: {books[index3][1]}")
            print(f"Title: {books[index3][2]}")
            print(f"ISBN: {books[index3][0]}")
            print(f"Price: {books[index3][3]}")
            print(f"Subject: {books[index3][4]}")

        print("\nEnter ISBN to enter to cart or")
        print("'n' to browse or")
        choice_browse = input("ENTER to go back to menu: ")
        if choice_browse == "":
            member_menu(email)
        elif choice_browse == "n":
            index1 += 3
            index2 += 3
            index3 += 3
        elif choice_browse == books[index1][0] or choice_browse == books[index2][0] or choice_browse == books[index3][0]:
            qty = int(input("Enter quantity: "))
            cursor.execute(f"SELECT userid FROM members WHERE email LIKE '{email}'")
            userid = cursor.fetchone()[0]

            cursor.execute(f"SELECT qty FROM cart WHERE userid LIKE '{userid}' AND isbn LIKE '{choice_browse}'")
            try:
                qty_check = cursor.fetchone()[0]
            except TypeError:
                qty_check = 0
                pass
            if qty_check > 0:
                insert_cart = f'''UPDATE cart
                SET qty = '{qty + qty_check}'
                WHERE userid LIKE '{userid}' AND isbn LIKE '{choice_browse}'
                '''
            else:
                insert_cart = f'''INSERT INTO cart
                (userid, isbn, qty)
                VALUES (('{userid}'), ('{choice_browse}'), ('{qty}'))
                '''
            cursor.execute(insert_cart)
            conn.commit()
            print("\nSuccesfully added to cart\n")
            _ = input("Press enter to keep browsing")


# Pretty much same as author search except looks for title now
def title_search(email):
    check = 0
    while check == 0:
        search = input("Enter title or part of title: ")
        cursor.execute(f"SELECT * FROM books WHERE title LIKE '{search}%'")
        books = cursor.fetchall()
        check = len(books)
        if check == 0:
            print("No title with that name")
            title_search(email)

    choice_browse = None
    index1 = 0
    index2 = 1
    index3 = 3
    while choice_browse != "":
        print(f"{len(books)} with this title\n")
        print(f"Author: {books[index1][1]}")
        print(f"Title: {books[index1][2]}")
        print(f"ISBN: {books[index1][0]}")
        print(f"Price: {books[index1][3]}")
        print(f"Subject: {books[index1][4]}\n")

        if len(books) >= 2:
            print(f"Author: {books[index2][1]}")
            print(f"Title: {books[index2][2]}")
            print(f"ISBN: {books[index2][0]}")
            print(f"Price: {books[index2][3]}")
            print(f"Subject: {books[index2][4]}\n")

        if len(books) >= 3:
            print(f"Author: {books[index3][1]}")
            print(f"Title: {books[index3][2]}")
            print(f"ISBN: {books[index3][0]}")
            print(f"Price: {books[index3][3]}")
            print(f"Subject: {books[index3][4]}")

        print("\nEnter ISBN to enter to cart or")
        print("'n' to browse or")
        choice_browse = input("ENTER to go back to menu: ")
        if choice_browse == "":
            member_menu(email)
        elif choice_browse == "n":
            index1 += 3
            index2 += 3
            index3 += 3
        elif choice_browse == books[index1][0] or choice_browse == books[index2][0] or choice_browse == books[index3][0]:
            qty = int(input("Enter quantity: "))
            cursor.execute(f"SELECT userid FROM members WHERE email LIKE '{email}'")
            userid = cursor.fetchone()[0]

            cursor.execute(f"SELECT qty FROM cart WHERE userid LIKE '{userid}' AND isbn LIKE '{choice_browse}'")
            try:
                qty_check = cursor.fetchone()[0]
            except TypeError:
                qty_check = 0
                pass
            if qty_check > 0:
                insert_cart = f'''UPDATE cart
                SET qty = '{qty + qty_check}'
                WHERE userid LIKE '{userid}' AND isbn LIKE '{choice_browse}'
                '''
            else:
                insert_cart = f'''INSERT INTO cart
                (userid, isbn, qty)
                VALUES (('{userid}'), ('{choice_browse}'), ('{qty}'))
                '''
            cursor.execute(insert_cart)
            conn.commit()
            print("\nSuccesfully added to cart\n")
            _ = input("Press enter to keep browsing")


def check_out(email):
    # Grabbing all the values needed for the invoice and order
    # Then assigning it to variables for use
    cursor.execute(f"SELECT userid FROM members WHERE email LIKE '{email}'")
    userid = cursor.fetchone()[0]
    cursor.execute(f"SELECT isbn FROM cart WHERE userid LIKE '{userid}'")
    isbn = cursor.fetchall()
    print("Curret cart contents:")
    total = 0
    for book in isbn:
        cursor.execute(f"SELECT qty FROM cart WHERE isbn LIKE '{book[0]}'")
        qty = cursor.fetchone()
        cursor.execute(f"SELECT price FROM books WHERE isbn LIKE '{book[0]}'")
        price = cursor.fetchone()
        cursor.execute(f"SELECT title FROM books WHERE isbn LIKE '{book[0]}'")
        title = cursor.fetchone()
        print(f"Title: {title[0]}")
        print(f"ISBN: {book}")
        print(f"Price: {price[0]}")
        print(f"Quantity: {qty[0]}")
        print(f"Total price: {price[0] * qty[0]}")
        print("-"*40)
        total += price[0] * qty[0]
    print(f"Total: {total}")

    choice = input("\nProceed to check out y/n?: ")
    while choice != "y" and choice != "n":  # Making sure the input is valid
        print("Not a valid input")
        choice = input("Proceed to check out y/n?: ")

    if choice == "y":
        cursor.execute(f"SELECT fname FROM members WHERE email LIKE '{email}'")
        fname = cursor.fetchone()
        cursor.execute(f"SELECT lname FROM members WHERE email LIKE '{email}'")
        lname = cursor.fetchone()
        cursor.execute(f"SELECT address FROM members WHERE email LIKE '{email}'")
        address = cursor.fetchone()
        cursor.execute(f"SELECT city FROM members WHERE email LIKE '{email}'")
        city = cursor.fetchone()
        cursor.execute(f"SELECT zip FROM members WHERE email LIKE '{email}'")
        zip = cursor.fetchone()
        print("\nInvoice")
        print("\nShipping address")
        print(f"Name: {fname[0]} {lname[0]}")
        print(f'''Address: {address[0]}
            {city[0]}
            {zip[0]}
        ''')
        for book in isbn:
            cursor.execute(f"SELECT qty FROM cart WHERE isbn LIKE '{book[0]}'")
            qty = cursor.fetchone()
            cursor.execute(f"SELECT price FROM books WHERE isbn LIKE '{book[0]}'")
            price = cursor.fetchone()
            cursor.execute(f"SELECT title FROM books WHERE isbn LIKE '{book[0]}'")
            title = cursor.fetchone()
            print(f"Title: {title[0]}")
            print(f"ISBN: {book}")
            print(f"Price: {price[0]}")
            print(f"Quantity: {qty[0]}")
            print(f"Total price: {price[0] * qty[0]}")
            print("-"*40)
        print(f"Total: {total}")
        today_date = date.today()  # Getting todays date

        # Adding all the information into the database
        order_insert = f'''INSERT INTO orders
        (userid, created, shipAddress, shipCity, shipZip)
        VALUES (('{userid}'), ('{today_date}'), ('{address[0]}'), ('{city[0]}'), ('{zip[0]}'))'''
        cursor.execute(order_insert)
        cursor.execute(f"SELECT ono FROM orders WHERE userid LIKE '{userid}'")
        ono = cursor.fetchone()
        for book in isbn:
            odetails_insert = f'''INSERT INTO odetails
            (ono, isbn, qty, amount)
            VALUES (('{ono[0]}'), ('{book[0]}'), ('{qty[0]}'), ('{price[0] * qty[0]}'))'''
            cursor.execute(odetails_insert)
        conn.commit()
        print("Thank you for your purchase!")
    else:
        member_menu(email)


# Just the main menu
def main_menu():
    print("\nWelcome to the online book store\n")
    print("1. Member Login")
    print("2. Member Registration")
    print("q. Quit")
    choice = input("\nType in your option: ")
    if choice != "1" and choice != "2" and choice != "q":
        print("Not a valid choice")
    elif choice == "1":
        member_login()
    elif choice == "2":
        member_registration()
    else:
        pass


main_menu()
