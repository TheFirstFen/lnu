from database import Database
from getpass import getpass
from menu import print_options,user_choice


def author_search(db:Database,limit,offset,userid,user_author):#very similar to the subject search

    query = f"""SELECT author, title, isbn, price FROM books WHERE author LIKE '%{user_author}%' LIMIT {limit} OFFSET {offset} ; """ 
    amount_query = f"""SELECT title, isbn, author, price FROM books WHERE author LIKE '%{user_author}%' ; """ #query for amount of books

    results = db.execute_fetchall(query)
    amount = db.execute_fetchall(amount_query)
        
    print(f'\n{len(amount)} books found.')

    for author, title, isbn, price in results:
        print(f'Title: {title},\n ISBN: {isbn},\n Author: {author},\n Price: {price}\n')

    books_options = ["Enter ISBN","Previous Page", "Next Page", "Return to Menu"]

    print_options(books_options)

    selected_option = user_choice(len(books_options))

    if selected_option == "1":
        chosen_isbn = input("Enter the ISBN of the book you'd like: ")
        qty = int(input("Enter the quanity: "))
        isbn_query = f"""INSERT into cart (userid, isbn, qty) VALUES("{userid}","{chosen_isbn}","{qty}") ON DUPLICATE KEY UPDATE qty = qty + {qty} ; """ # allows for duplicate entries

        db.execute_commit(isbn_query)

        print("Books added to cart successfully!...\n")
    
    elif selected_option == "2":
        author_search(db, limit, offset-limit,userid,user_author) #previous page
    
    elif selected_option == "3":
        author_search(db, limit, offset+limit,userid,user_author) #next page

    elif selected_option == "4":
        return
    
def title_search(db:Database,limit,offset,userid,user_title): # author search and title search is basically the same


    query = f"""SELECT author, title, isbn, price FROM books WHERE title LIKE '%{user_title}%' LIMIT {limit} OFFSET {offset} ; """
    amount_query = f"""SELECT title, isbn, author, price FROM books WHERE title LIKE '%{user_title}%' ; """

    results = db.execute_fetchall(query)
    amount = db.execute_fetchall(amount_query)
        
    print(f'\n{len(amount)} books found.')

    for author, title, isbn, price in results:
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
        author_search(db, limit, offset-limit,userid,user_title) #previous page
    
    elif selected_option == "3":
        author_search(db, limit, offset+limit,userid,user_title) #next page

    elif selected_option == "4":
        return