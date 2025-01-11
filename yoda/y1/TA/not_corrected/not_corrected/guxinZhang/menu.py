# this file contains menu function and helper function

from database import Database
from member import login_member, add_member
from list_of_subjects import list_of_subjects
from searchAndCheckout import search_books, checkout

# create main menu
def main_menu(db:Database,options):
    while True:
        print_header('Welcome to the Online Book Store')  # function to print header
        print_option(options)  # function to print option
        
        # check the user choice
        choice = check_choice(len(options))

        
        if choice == 1:  # show login menu
            member_details = login_member(db)  # store member details so that we can use it later
            if member_details:   # and after login show the member menu
                member_menu(db,['Browse by Subject', 'Search by Author/Title', 'Check Out', 'Logout'],member_details)
        
        elif choice == 2:   # show registration and add member to table
            add_member(db)
        else:
            print("\nThank you for visiting the Online Book Store!")
            quit()

# member menu
def member_menu(db:Database,options, member_details):
    while True:
        print_header('Welcome to the Member Menu')  # function to print header
        print_option(options)  # function to print option
        
        # check the user choice
        choice = check_choice(len(options))

        
        if choice == 1:  # show list of subjects alphabetically, then allows the user to choose one subject
            list_of_subjects(db, 10, 0)
        elif choice == 2:   # show search function
            search_books(db)
        elif choice == 3:
            checkout(db, member_details)   # check out
        else:   
            # clear any items in cart when logging out
            try:
                db.execute_with_commit('DELETE FROM cart')
            except Exception:
                pass  # ignore any errors during cart cleanup
            break


def print_header(title):
    border = '*' * 71
    print(border)
    print(f'{title.center(63)}')
    print(border)


def print_option(options):   # options is a list
    # print numbered options from the given list, use enumerate function to start from 1 instead of 0
    for i, option in enumerate(options, 1):
        print(f'{i}. {option}')
    print()


def check_choice(maxOptions):  # function to check if the option user make is valid
    selectedOption = None
    while selectedOption is None:
        choice = input('Type in your option:')
        try:
            if int(choice) in [x for x in range(1, maxOptions + 1)]:
                selectedOption = int(choice)
            else:
                print('Invalid input: please select the available options.')

        except Exception:
            selectedOption = None
            print('Invalid input: it should be a number.')
    
    return selectedOption