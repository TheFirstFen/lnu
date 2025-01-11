# this file contains search and checkout function

from database import Database
from datetime import datetime  # import datetime module for date handling in orders
from list_of_subjects import add_to_cart

def search_books(db: Database):
    while True:
        print('\nSearch Options:')  # here still i tried to import function in menu but show circular import again
        print('1. Author Search')
        print('2. Title Search')
        print('3. Go Back to Member Menu')

        choice = input('\nType in your option: ').strip()
        
        if choice == '1':
            search_by_author(db)
        elif choice == '2':
            search_by_title(db)
        elif choice == '3':
            break
        else:
            print('Invalid option. Please try again.')

def search_by_author(db: Database, limit=3): # search function by author
    author = input('\nEnter author or part of the author name: ')
    query = f"""SELECT author, title, isbn, price, subject FROM books WHERE author LIKE '%{author}%';"""
    display_search_results(db, query, limit)

def search_by_title(db: Database, limit=3):  # search function by title
    title = input('\nEnter title or part of the title: ')
    query = f"""SELECT author, title, isbn, price, subject FROM books WHERE title LIKE '%{title}%';"""
    display_search_results(db, query, limit)

def display_search_results(db: Database, query, limit):   # function to display the search results
    books = db.execute_with_fetchall(query)
    print(f'\n{len(books)} books found\n')
    
    offset = 0  # start from first book
    while offset < len(books):
        # display books three at a time
        for i in range(offset, min(offset + limit, len(books))):
            book = books[i]
            print(f'\nAuthor: {book[0]}')  # print details
            print(f'Title: {book[1]}')
            print(f'ISBN: {book[2]}')
            print(f'Price: ${book[3]:.2f}')
            print(f'Subject: {book[4]}\n')
        
        if not books:  # if no books found just return to menu
            input('Press Enter to return to menu')
            return

        # show options    
        print('Enter ISBN to add to Cart or')
        print('n Enter to browse or')
        print('ENTER to go back to menu:', end=' ')
        
        choice = input().strip()
        
        if choice == '':
            return
        elif choice.lower() == 'n':  # show next set of books
            offset += limit
            if offset >= len(books):  # check if no more books to display
                print('\nNo more books to display.')
                input('Press Enter to return to menu')
                return
        else:   # add books to cart
            try:
                add_to_cart(db, choice)
            except Exception as e:
                print(f'Error adding to cart: {e}')
                input('\nPress Enter to continue')

def checkout(db: Database, member_details):
    # get cart contents and calculate
    query = """SELECT c.isbn, b.title, b.price, c.qty, (b.price * c.qty) as total FROM cart c JOIN books b ON c.isbn = b.isbn;"""
    cart_items = db.execute_with_fetchall(query)
    
    if not cart_items:  # check if the cart is empty
        print('\nYour cart is empty!')
        input('\nPress Enter to continue')
        return
    
    # display cart contents and total
    print('\nCurrent Cart Contents:\n')
    print('ISBN          Title                                          $ Qty    Total')
    print('-' * 75)
    
    cart_total = 0
    for item in cart_items:
        isbn, title, price, qty, total = item
        # truncate title if it's too long
        # ljust function to add spaces to the right until the total length is 40 characters
        display_title = title[:37] + '...' if len(title) > 40 else title.ljust(40)
        print(f'{isbn}  {display_title}  ${price:8.2f} {qty:3d}  ${total:8.2f}')
        cart_total += total
    
    print('-' * 75)
    print(f'{' '*60}Total    ${cart_total:<8.2f}')
    
    # confirm checkout
    proceed = input('\nProceed to check out (Y/N)?: ').strip().upper()
    
    if proceed == 'Y':
        try:
            # get member details and prepare dates for order
            userid, fname, lname, address, city, zip = member_details
            current_date = datetime.now().strftime('%Y-%m-%d')  # use datetime to get the current date for 'created' attribute
            
            # insert order in our database
            order_query = f"""INSERT INTO orders (userid, created, shipAddress, shipCity) VALUES ({userid}, '{current_date}', '{address}', '{city}');"""
            db.execute_with_commit(order_query)
            
            # get the order number (last inserted id)
            order_no = db.execute_with_fetchall('SELECT LAST_INSERT_ID()')[0][0]
            
            # insert order details
            for item in cart_items:
                isbn, _, price, qty, total = item
                detail_query = f"""INSERT INTO odetails (ono, isbn, qty, amount) VALUES ({order_no}, '{isbn}', {qty}, {total});"""
                db.execute_with_commit(detail_query)
            
            # clear cart
            db.execute_with_commit('DELETE FROM cart')
            
            # print invoice with format
            print(f'\nInvoice for Order no.{order_no}')
            print('\nShipping Address')
            print(f'Name:     {fname} {lname}')
            print(f'Address:  {address}')
            print(f'          {city}')
            print(f'          {zip}')
            print('\n' + '-' * 75)
            print('ISBN          Title                                          $ Qty    Total')
            print('-' * 75)
            
            for item in cart_items:
                isbn, title, price, qty, total = item
                display_title = title[:37] + '...' if len(title) > 40 else title.ljust(40)
                print(f'{isbn}  {display_title}  ${price:8.2f} {qty:3d}  ${total:8.2f}')
            
            print('-' * 75)
            print(f'{' '*60}Total    ${cart_total:<8.2f}')
            
            input('\nPress Enter to go back to Menu')
            return True
            
        except Exception as e:
            print(f'\nError processing checkout: {e}')
            input('\nPress Enter to continue')
            return False
            
    return False