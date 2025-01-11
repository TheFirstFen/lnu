import printing_functions
import user_input as user_input
import check_out as check_out

MEMBER_HEADER = ['Welcome to the online Book Store', 'Member Menu']


def browse(db, books: list, userid: int, subject: str):
    # Display the books 2 by 2
    i = 0
    while i < len(books):
        printing_functions.print_header(MEMBER_HEADER, False)
        print(f'{len(books)} books found for: {subject}\n')
        printing_functions.print_book(books[i])  # Safely access books[i]
        print()

        # Check and print the next book if it exists
        if i + 1 < len(books) and books[i + 1] is not None:
            printing_functions.print_book(books[i + 1])

        user_choice = None
        qty = None
        while user_choice is None:
            user_choice = input('''\nEnter ISBN to add book to cart,
n for the next 2 books,
or press enter to return to member menu: ''')

            # Check the user's choice

            if user_choice == 'n':
                i += 2  # Move to the next pair of books
                break

            elif user_choice == '':
                print('Returning to member menu...')
                return

            # Check if the input is a valid ISBN
            elif len(user_choice) == 10 and user_choice.isdigit():
                isbn = user_choice
                # Get the quantity
                qty = user_input.get_int('Enter quantity: ')
                # Add the book to the cart
                check_out.insert_to_cart(db, userid, isbn, qty)
                break
            else:
                user_choice = None
                print('Invalid input, try again')


# brows by subject tab
def _by_subject(db, userid: int):
    printing_functions.print_header(MEMBER_HEADER, False)

    # Get all subjects from the database
    query = 'select distinct(subject) from books order by subject;'
    all_subjects = db.execute_and_fetchall(query)
    subject_option = [item[0] for item in all_subjects]

    # Print the subjects and get the user's choice
    printing_functions.print_options(subject_option)
    choice = user_input.check_choice(len(subject_option))

    # Get the books for the selected subject
    subject = subject_option[choice - 1]
    query = f"select * from books where subject='{subject}'"
    # List of books, books[i] is a tuple with the book's details
    books = db.execute_and_fetchall(query)
    # Display the books
    browse(db, books, userid, subject)
    return


# brows by author/title tab
def _by_author_Title(db, userid: int):
    while True:
        # Print the header and options
        printing_functions.print_header(MEMBER_HEADER, False)
        search_options = ['Author Search',
                          'Title Search',
                          'Go back to Members Menu']
        printing_functions.print_options(search_options)

        # Get the user's choice
        choice = user_input.check_choice(len(search_options))

        match choice:
            case 1:
                author = user_input.get_str("Enter author name: ")
                query = f"select * from books where author like '%{author}%'"
                # List of books, books[i] is a tuple with the book's details
                books = db.execute_and_fetchall(query)
                # Display the books
                if books:
                    browse(db, books, userid, author)
                else:
                    print(f"No books found for author: {author}")
                    input("Press Enter to return")
                return

            case 2:
                title = user_input.get_str("Enter title name: ")
                query = f"select * from books where title like '%{title}%'"
                # List of books, books[i] is a tuple with the book's details
                books = db.execute_and_fetchall(query)
                # Display the books
                if books:
                    browse(db, books, userid, title)
                else:
                    print(f"No books found for title: {title}")
                    input("Press Enter to return")
                return

            case 3:
                print('Returning to Member menu...')
                return
