from database import Database
from getpass import getpass 
import mysql.connector
from menu import *
from member_options import member_login,register_member,list_books,list_subjects
from author_options import author_search,title_search


def main_menu(db:Database,options):
    while True:
        print_header("Welcome to the Book Store database!....")
        print_options(menu_options)
        choice = user_choice(len(menu_options))

        if choice == "1":
            userid = member_login(db)  #redirecting to external python file
            if userid:
                member_menu(db,options,userid)
        if choice == "2":
            register_member(db)
        if choice == "3":
            quit() #Quits the program

def member_menu(db:Database,options,userid):
    while True:
        print_header("Welcome to the Online Book Store \n"
                     "Member Menu")
        print_options(member_options)
        choice = user_choice(len(member_options))

        if choice == "1":
            chosen_subject = list_subjects(db)
            if chosen_subject:
                list_books(db,chosen_subject,2,0,userid)
        if choice == "2":
            chosen_author = author_title_menu(db,userid)
            if chosen_author:
                author_search(db,3,0,userid)

        if choice == "3":
            checkout(db,userid)
        if choice == "4":
            return False # logs out the user

def author_title_menu(db:Database,userid):

    while True:
        menu_options = ["Author Search","Title Search","Go back to Main Menu"]
        print_options(menu_options)
        selected_choice = user_choice(len(menu_options))

        if selected_choice == "1":
            user_author = input("Enter name of author: ")
            author_search(db,3,0,userid,user_author)
        
        elif selected_choice == "2":
            user_title = input("Enter title or part of the title: ")
            title_search(db,3,0,userid,user_title)
            
        elif selected_choice == "3":
            return  
        
def checkout(db: Database, userid):
    try:
        cart_query = f"""
            SELECT c.isbn, b.title, b.price, c.qty FROM cart c JOIN books b ON c.isbn = b.isbn WHERE c.userid = '{userid}'; """ # joins the cart table onto the book table
        cart_items = db.execute_fetchall(cart_query)                                                                            # so that the correct books can be displayed
                                                                                                                                # according to the user's cart
        if not cart_items:
            print("Your cart is empty.")
            return #takes back to main menu

        total_price = 0
        print("\n--- Invoice ---")
        for isbn, title, price, quantity in cart_items:
            item_total = price * quantity
            total_price += item_total
            print(f"ISBN: {isbn}, Title: {title}, Price: {price}, Quantity: {quantity}, Total: {item_total}") # prints the invoice

        print(f"\nOverall Total: {total_price}")

        proceed = input("Proceed to check out (Y/N)?: ").strip().upper()
        if proceed == "Y":

            from datetime import datetime, timedelta
            created = datetime.now().date() # takes the current time
            shipment_date = created + timedelta(weeks=1) # adds 1 week to the current time


            user_query = f""" SELECT address,city,zip FROM members WHERE userid = '{userid}'; """ 
            user_address = db.execute_fetchall(user_query)

            order_query = f""" INSERT INTO orders (userid, created, shipaddress, shipCity, shipZip) VALUES ('{userid}', '{created}', '{user_address[0][0]}', '{user_address[0][1]}',{user_address[0][2]}); """
            db.execute_commit(order_query) # inserts the addresses into the orders, which i fetched from the lines aboves, using a tuple list

            order_id_query = "SELECT LAST_INSERT_ID();" # takes the last inserted id so that we know what the order number is
            order_id = db.execute_fetchone(order_id_query)[0]

            for isbn, title, price, quantity in cart_items:
                amount = price * quantity
                order_detail_query = f""" INSERT INTO odetails (ono, isbn, qty, amount) VALUES ('{order_id}','{isbn}', {quantity}, {amount}); """# inserts the order details in odetails
                db.execute_commit(order_detail_query)

            print("Order has been placed successfully!\n")
        else:
            print("Checkout cancelled.")
    except Exception as err:
        print(f"Error: {err}")

def check_credentials(username,password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Schroder13",
        database="book_store",
        charset="utf8mb4",  # Ensure utf8mb4 is used
        collation="utf8mb4_general_ci"
    )
    return True


valid_connection = False
username,password = (None, None)


username = "root"
password = "Schroder13"
if check_credentials(username,password):
    valid_connection = True #if the check_credentials function is passed successfully, valid_connection becomes true and logs thbe user in
    db = Database(username,password)

    main_menu(db,menu_options)
else:
    print("Connection to SQL server has failed, please make sure your credentials are correct")



