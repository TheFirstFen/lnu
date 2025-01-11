import mysql.connector
from getpass import getpass

def connect_to_database():
    """连接到数据库"""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Schroder13",
        database="book_store",
        charset="utf8mb4",  # Ensure utf8mb4 is used
        collation="utf8mb4_general_ci"
    )

def register_member():
    """处理会员注册"""
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

    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = """
        INSERT INTO members (fname, lname, address, city, zip, phone, email, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (fname, lname, address, city, zip_code, phone, email, password))
        connection.commit()
        print("\nYou have registered successfully!")
        input("Press Enter to go back to Menu...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def login_member():
    
    print("\nWelcome to the Online Book Store")
    print("Member Login\n")

    email = input("Enter email: ")
    password = getpass("Enter password: ")

    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "SELECT userid FROM members WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        if result:
            print("\nLogin successful!")
            member_menu(connection, result[0])  # 传递用户ID到会员菜单
        else:
            print("\nInvalid email or password.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def member_menu(connection, user_id):
    while True:
        print("\n" + "*" * 50)
        print("***                                            ***")
        print("***               Member Menu                  ***")
        print("***                                            ***")
        print("*" * 50)
        print("1. Browse by Subject")
        print("2. Search by Author/Title")
        print("3. Check Out")
        print("4. Logout")

        option = input("Enter your choice: ").strip()
        if option == "1":
            browse_by_subject(connection, user_id)
        elif option == "2":
            search_books(connection,user_id)
        elif option == "3":
            check_out(connection,user_id)
        elif option == "4":
            print("\nLogged out successfully!")
            break
        else:
            print("Invalid option. Please try again.")


def browse_by_subject(connection,user_id):
    """Browse books by subject and allow adding to cart."""
    print("\nBrowse by Subject\n")
    
    try:
        cursor = connection.cursor()
        # 获取所有主题并按字母排序
        cursor.execute("SELECT DISTINCT subject FROM books ORDER BY subject;")
        subjects = cursor.fetchall()
        
        if not subjects:
            print("No subjects available.")
            return
        
        # 显示主题列表
        print("Subjects:")
        for i, subject in enumerate(subjects, start=1):
            print(f"{i}. {subject[0]}")
        
        # 用户输入选择
        choice = input("Enter your choice (number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(subjects):
            selected_subject = subjects[int(choice) - 1][0]
            print(f"\nYou selected: {selected_subject}")
            
            # 显示选定主题的书籍
            cursor.execute(
                "SELECT isbn, title, author, price FROM books WHERE subject = %s",
                (selected_subject,)
            )
            books = cursor.fetchall()
            
            if not books:
                print(f"No books available under {selected_subject}.")
            else:
                print(f"\n{len(books)} books available on this Subject:")
                for book in books:
                    print(f"Author: {book[2]}\nTitle: {book[1]}\nISBN: {book[0]}\nPrice: ${book[3]:.2f}\nSubject {selected_subject}\n")
                
                while True:
                    isbn = input("Enter ISBN to add to Cart or 'n' to browse or press ENTER to go back to menu: ").strip()
                    if isbn.lower() == "n":
                        break
                    elif isbn == "":
                        print("Returning to menu...")
                        return
                    else:
                        quantity = input("Enter quantity: ").strip()
                        if not quantity.isdigit() or int(quantity) <= 0:
                            print("Invalid quantity. Please try again.")
                        else:
                            # 添加书籍到购物车
                            cursor.execute(
                                """
                                INSERT INTO cart (userid, isbn, qty)
                                VALUES (%s, %s, %s)
                                ON DUPLICATE KEY UPDATE qty = qty + VALUES(qty)
                                """,
                                (user_id, isbn, int(quantity))
                            )
                            connection.commit()
                            print("Book added to cart successfully!")
        else:
            print("Invalid choice. Please try again.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()



def search_books(connection,user_id):
    """Search books by author or title."""
    print("\nSearch Books\n")
    print("1. Search by Author")
    print("2. Search by Title")
    
    choice = input("Enter your choice (1/2): ").strip()
    
    if choice not in ("1", "2"):
        print("Invalid choice.")
        return
    
    keyword = input("Enter search keyword: ").strip()
    
    try:
        cursor = connection.cursor()
        if choice == "1":  # 按作者搜索
            query = "SELECT isbn, title, author, price FROM books WHERE author LIKE %s"
        else:  # 按标题搜索
            query = "SELECT isbn, title, author, price FROM books WHERE title LIKE %s"
        
        cursor.execute(query, (f"%{keyword}%",))
        results = cursor.fetchall()
        
        if not results:
            print("No books found.")
        else:
            print("\nSearch Results:")
            for book in results:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: ${book[3]:.2f}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def add_to_cart(connection, user_id):
    """Add a book to the cart."""
    isbn = input("Enter ISBN of the book to add to the cart: ").strip()
    quantity = int(input("Enter quantity: ").strip())
    
    try:
        cursor = connection.cursor()
        # 检查书籍是否存在
        cursor.execute("SELECT price FROM books WHERE isbn = %s", (isbn,))
        book = cursor.fetchone()
        
        if not book:
            print("Book not found.")
            return
        
        price = book[0]
        # 添加到购物车
        cursor.execute(
            """
            INSERT INTO cart (userid, isbn, qty)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE qty = qty + VALUES(qty)
            """,
            (user_id, isbn, quantity)
        )
        connection.commit()
        print("Book added to cart successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def check_out(connection, user_id):
    """Checkout the cart and print invoice."""
    
    cursor = connection.cursor()

    # 获取购物车内容
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

    # 获取用户地址信息
    cursor.execute(
        """
        SELECT fname, lname, address, city, zip
        FROM members
        WHERE userid = %s
        """,
        (user_id,)
    )
    user_info = cursor.fetchone()
    if not user_info:
        print("Error retrieving user information.")
        return

    # 显示购物车内容
    print("\nCurrent Cart Contents:")
    total_price = 0
    for item in cart_items:
        print(f"ISBN: {item[0]}, Title: {item[1]}, Quantity: {item[2]}, Price: ${item[3]:.2f}, Total: ${item[4]:.2f}")
        total_price += item[4]

    print(f"\nTotal Price: ${total_price:.2f}")

    # 确认结账
    confirm = input("Proceed to checkout (Y/N)? ").strip().lower()
    if confirm != "y":
        print("Checkout cancelled.")
        return

    # 创建订单
    cursor.execute(
        """
        INSERT INTO orders (userid, created, shipAddress, shipCity, shipZip)
        VALUES (%s, NOW(), %s, %s, %s)
        """,
        (user_id, user_info[2], user_info[3], user_info[4])
    )
    order_id = cursor.lastrowid

    # 保存订单明细
    for item in cart_items:
        cursor.execute(
            """
            INSERT INTO odetails (ono, isbn, qty, amount)
            VALUES (%s, %s, %s, %s)
            """,
            (order_id, item[0], item[2], item[4])
        )

    # 清空购物车
    cursor.execute("DELETE FROM cart WHERE userid = %s", (user_id,))
    connection.commit()

    # 打印发票
    print("\nInvoice for Order no.{}".format(order_id))
    print("Shipping Address:")
    print(f"                Name: {user_info[0]} {user_info[1]}")
    print(f"                Address: {user_info[2]}")
    print(f"{user_info[3]} {user_info[4]}")
    print("-" * 80)
    print("{:<15} {:<40} {:<10} {:<10}".format("ISBN", "Title", "Qty", "Total"))
    print("-" * 80)
    for item in cart_items:
        print("{:<15} {:<40} {:<10} ${:<10.2f}".format(item[0], item[1], item[2], item[4]))
    print("-" * 80)
    print(f"Total = ${total_price:.2f}")
    print("-" * 80)
    input("Press enter to go back to Menu...")


    cursor.close()


def main_menu():
    while True:
        print("\n" + "*" * 50)
        print("***                                            ***")
        print("***      Welcome to the Online Book Store      ***")
        print("***                                            ***")
        print("*" * 50)
        print("1. Member Login")
        print("2. New Member Registration")
        print("q. Quit")

        option = input("Type in your option: ").strip().lower()
        if option == "1":
            login_member()
        elif option == "2":
            register_member()
        elif option == "q":
            print("Thank you for visiting the Online Book Store. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()

