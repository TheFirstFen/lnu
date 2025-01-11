# this file contains list of subject, list of book, and add cart function

from database import Database

def get_user_choice(max_options):
    # this function is similar to check_option function in menu.py file
    # but i encountered problem when i tried to import that function to this file, which shows circular import
    # so i have to create a new one for this file
    while True:
        try:
            choice = input('Type in your option: ').strip()
            num_choice = int(choice)
            if 1 <= num_choice <= max_options:
                return num_choice
            print(f'Invalid input: please select between 1 and {max_options}')
        except ValueError:
            print('Invalid input: please enter a number')

def split_subject(compound_subject):
    # firstly, we need to split compound subjects into individual subjects, cuz the subjects in table is not the single one
    # split by '&' and then handle any additional separators
    subjects = []
    for part in compound_subject.split('&'):
        # use list comprehension to split by comma if present
        sub_parts = [s.strip() for s in part.split(',')]
        subjects.extend(sub_parts)  # use extend instead of append because we want to add each item individually, not as a nested list
    return [subject for subject in subjects if subject]  # use list comprehension to remove any empty strings

def list_of_subjects(db:Database, limit, offset):
    query = f"""SELECT DISTINCT subject from books ORDER BY subject ASC;"""
    compound_subjects = db.execute_with_fetchall(query)
    print(compound_subjects)
    # split and collect all unique individual subjects
    unique_subjects = set()  
    for subject_tuple in compound_subjects:
        individual_subjects = split_subject(subject_tuple[0])   # call function to split subjects
        for subject in individual_subjects:
            if subject:  # only add non-empty subjects
                print(subject)
                unique_subjects.add(subject)
    
    # sort subjects alphabetically
    options = sorted(list(unique_subjects)) # here option should be the list of subjects
    print(options)
    print('\nList of subjects')

    for i, subject in enumerate(options, 1):
        print(f'{i}. {subject}')  # print all subjects seperately and alphabetically, eg 1. sport..., then allows the user to choose one subject
    
    # user choose the subject they want
    choice = get_user_choice(len(options))

    # after choose show all the availble books 
    selected_subject = options[choice - 1]
    list_of_books(db, selected_subject)

    # so need the list of available books to show information


# list of available books
def list_of_books(db:Database, selected_subject, limit = 2):
     # query to search for books where the subject contains the selected subject
    query = f"""SELECT author,title,isbn,price,subject from books WHERE subject LIKE '%{selected_subject}%';"""
    books = db.execute_with_fetchall(query)

    print(f'\n{len(books)} books available on this Subject\n')

    offset = 0
    while offset < len(books):
        # display books two at a time
        for i in range(offset, min(offset + limit, len(books))):
            book = books[i]
            print(f'\nAuthor: {book[0]}')
            print(f'Title: {book[1]}')
            print(f'ISBN: {book[2]}')
            print(f'Price: ${book[3]:.2f}')
            print(f'Subject: {book[4]}\n')
        
        # get user input
        print('Enter ISBN to add to Cart')
        print('n Enter to browse')
        print('ENTER to go back to menu:', end=' ')
        
        choice = input().strip()
        
        if choice == '':  # empty input (just ENTER)
            return
        elif choice.lower() == 'n':
            offset += limit  # continue show the list
            if offset >= len(books):
                print('\nNo more books to display.')
                input('Press Enter to return to menu')
                return
        else:
            # try to add book to cart
            try:
                add_to_cart(db, choice)  # call add cart function
            except Exception as e:
                print(f'Error adding to cart: {e}')
                input('\nPress Enter to continue')


def add_to_cart(db: Database, isbn):
    # first we need to verify the book exists
    verify_query = f"""SELECT isbn FROM books WHERE isbn = '{isbn}';"""
    if not db.execute_with_fetchall(verify_query):
        print('Invalid ISBN. Book not found.')
        return
    
    # get quantity from user
    qty = input('Enter quantity: ').strip()
    try:
        qty = int(qty)
        if qty <= 0:
            raise ValueError('Quantity must be positive')
    except ValueError as e:
        print('Invalid quantity. Please enter a positive number.')
        return
    
    # check if book already in cart - if yes, update quantity, if no, insert new item
    check_query = f"""SELECT qty FROM cart WHERE isbn = '{isbn}';"""
    existing = db.execute_with_fetchall(check_query)
    
    try:
        if existing:
            # update existing cart item
            # use existing[0][0] to get the exact number, for instance,existing[0] get like(2,),existing[0][0] get 2
            new_qty = existing[0][0] + qty
            update_query = f"""UPDATE cart SET qty = {new_qty} WHERE isbn = '{isbn}';"""
            db.execute_with_commit(update_query)
        else:
            # insert new cart item  
            insert_query = f"""INSERT INTO cart (isbn, qty) VALUES ('{isbn}', {qty});"""
            db.execute_with_commit(insert_query)
        print("\nBook added to cart successfully!")
    except Exception as e:
        print(f"Error updating cart: {e}")
        raise e