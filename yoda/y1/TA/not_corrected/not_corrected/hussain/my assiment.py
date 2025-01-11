import mysql.connector
from getpass import getpass

def connect_to_database():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="1764375a",
            database="book_store"
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

def register_member():
    # New member registration
    print("\nWelcome to the Online Book Store")
    print("New Member Registration\n")

    fname = input("Enter first name: ").strip()
    lname = input("Enter last name: ").strip()
    address = input("Enter street address: ").strip()
    city = input("Enter city: ").strip()
    zip_code = input("Enter zip: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email address: ").strip()
    password = getpass("Password: ").strip()

    connection = connect_to_database()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO members (fname, lname, address, city, zip, phone, email, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (fname, lname, address, city, zip_code, phone, email, password))
        connection.commit()
        print("\nRegistration successful!")
        input("Press Enter to return to the main menu...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def login_member():
    # Member login
    print("\nWelcome to the Online Book Store")
    print("Member Login\n")

    email = input("Enter email: ").strip()
    password = getpass("Enter password: ").strip()

    connection = connect_to_database()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        query = "SELECT userid FROM members WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        if result:
            print("\nLogin successful!")
            member_menu(connection, result[0])
        else:
            print("\nInvalid email or password.")
    except mysql.connector.Error as err:
        print(f"Error during login: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def member_menu(connection, user_id):
    # Display member menu options
    while True:
        print("\n" + "*" * 50)
        print("***               Member Menu                  ***")
        print("*" * 50)
        print("1. Browse by Subject")
        print("2. Search by Author/Title")
        print("3. Check Out")
        print("4. Logout")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            browse_by_subject(connection, user_id)
        elif choice == "2":
            search_books(connection, user_id)
        elif choice == "3":
            check_out(connection, user_id)
        elif choice == "4":
            print("\nYou have successfully logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def browse_by_subject(connection, user_id):
    # Browse books by subject
    print("\nBrowse by Subject\n")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT subject FROM books ORDER BY subject")
        subjects = cursor.fetchall()

        if not subjects:
            print("No subjects available.")
            return

        print("Available Subjects:")
        for idx, subject in enumerate(subjects, start=1):
            print(f"{idx}. {subject[0]}")

        choice = input("Enter subject number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(subjects):
            selected_subject = subjects[int(choice) - 1][0]
            display_books_by_subject(connection, user_id, selected_subject)
        else:
            print("Invalid selection. Returning to menu.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def display_books_by_subject(connection, user_id, subject):
    # Display books for the selected subject
    print(f"\nBooks under subject: {subject}\n")

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT isbn, title, author, price FROM books WHERE subject = %s",
            (subject,)
        )
        books = cursor.fetchall()

        if not books:
            print("No books found under this subject.")
            return

        index = 0
        while index < len(books):
            for book in books[index:index + 2]:
                print(f"ISBN: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nPrice: ${book[3]:.2f}\n")
            index += 2

            action = input("Enter ISBN to add to cart or 'n' to browse more, or press ENTER to return: ").strip()
            if action.lower() == 'n':
                continue
            elif action == "":
                break
            else:
                add_book_to_cart(connection, user_id, action)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def add_book_to_cart(connection, user_id, isbn):
    # Add book to cart
    quantity = input("Enter quantity: ").strip()
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity. Returning to menu.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO cart (userid, isbn, qty)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE qty = qty + VALUES(qty)
            """,
            (user_id, isbn, int(quantity))
        )
        connection.commit()
        print("Book added to cart.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def search_books(connection, user_id):
    # Search books by author or title
    print("\nSearch Books\n")
    print("1. Search by Author")
    print("2. Search by Title")

    choice = input("Enter your choice (1/2): ").strip()
    if choice not in ("1", "2"):
        print("Invalid choice. Returning to menu.")
        return

    keyword = input("Enter search keyword: ").strip()

    try:
        cursor = connection.cursor()
        if choice == "1":
            cursor.execute("SELECT isbn, title, author, price FROM books WHERE author LIKE %s", (f"%{keyword}%",))
        else:
            cursor.execute("SELECT isbn, title, author, price FROM books WHERE title LIKE %s", (f"%{keyword}%",))
        books = cursor.fetchall()

        if not books:
            print("No books found.")
            return

        index = 0
        while index < len(books):
            for book in books[index:index + 3]:
                print(f"ISBN: {book[0]}\nTitle: {book[1]}\nAuthor: {book[2]}\nPrice: ${book[3]:.2f}\n")
            index += 3

            action = input("Enter ISBN to add to cart or 'n' to browse more, or press ENTER to return: ").strip()
            if action.lower() == 'n':
                continue
            elif action == "":
                break
            else:
                add_book_to_cart(connection, user_id, action)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def check_out(connection, user_id):
    # Checkout process
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT b.isbn, b.title, c.qty, b.price, (c.qty * b.price) AS total
            FROM cart c
            JOIN books b ON c.isbn = b.isbn
            WHERE c.userid = %s
            """,
            (user_id,)
        )
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Your cart is empty.")
            return

        print("\nCart Summary:")
        total_price = 0
        for item in cart_items:
            print(f"ISBN: {item[0]}, Title: {item[1]}, Quantity: {item[2]}, Price: ${item[3]:.2f}, Total: ${item[4]:.2f}")
            total_price += item[4]

        print(f"\nTotal Price: ${total_price:.2f}")
        confirm = input("Do you want to proceed to checkout? (Y/N): ").strip().lower()
        if confirm != 'y':
            print("Checkout cancelled.")
            return

        cursor.execute(
            """
            INSERT INTO orders (userid, created, shipAddress, shipCity, shipZip)
            VALUES (%s, NOW(), %s, %s, %s)
            """,
            (user_id, cart_items[0][2], cart_items[0][3], cart_items[0][4])
        )
        order_id = cursor.lastrowid

        for item in cart_items:
            cursor.execute(
                """
                INSERT INTO orderdetails (orderid, isbn, qty, price)
                VALUES (%s, %s, %s, %s)
                """,
                (order_id, item[0], item[2], item[4])
            )

        cursor.execute("DELETE FROM cart WHERE userid = %s", (user_id,))
        connection.commit()

        print("\nCheckout complete. Your order has been placed.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def main_menu():
    # Main menu of the application
    while True:
        print("\n" + "*" * 50)
        print("***      Welcome to the Online Book Store      ***")
        print("*" * 50)
        print("1. Member Login")
        print("2. New Member Registration")
        print("q. Quit")

        option = input("Select an option: ").strip().lower()
        if option == "1":
            login_member()
        elif option == "2":
            register_member()
        elif option == "q":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()
