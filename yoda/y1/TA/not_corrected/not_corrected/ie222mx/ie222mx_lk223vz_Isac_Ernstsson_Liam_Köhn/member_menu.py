import browsing as brows
import printing_functions
import user_input as user_input
import check_out as check_out
from getpass import getpass
from mysql.connector import Error


MEMBER_HEADER = ['Welcome to the online Book Store', 'Member Menu']


# Member menu
def member_menu(db):

    # login phase for the member
    access = False
    while not access:
        print()
        email = input('Enter email or type "x" to return: ')
        if email.lower() == 'x':
            return
        password = getpass('Enter password: ')

        try:
            # SQL query to fetch password based on email
            query = f'''SELECT password, userid FROM members WHERE email='{email}';'''
            answer = db.execute_and_fetchall(query)

            # Check if no results are returned (member does not exist)
            if not answer:
                print('The member does not exist, try again')
            else:
                # Check if the password matches
                for item in answer:
                    if item[0] == password:
                        userid = item[1]  # Get the user id
                        access = True
                        print('Access granted! Welcome!')
                    else:
                        print('Wrong password, try again!')
        except Error as e:
            # Catching database errors
            print(f'An error occurred: {e}')

    # Options for the member menu
    options = ['Browse by Subject',
               'Search by Author/Title',
               'Check out',
               'Logout']

    # Member menu
    while True:
        # Print Member title
        printing_functions.print_header(MEMBER_HEADER)

        # Print options
        printing_functions.print_options(options)

        # Get user choice
        choice = user_input.check_choice(len(options))
        match choice:
            case 1:  # Browse by subject
                brows._by_subject(db, userid)

            case 2:  # Search by author/title
                brows._by_author_Title(db, userid)

            case 3:  # Check out
                check_out.check_out(db, userid)

            case 4:  # Logout
                print('Logging out...')
                return
