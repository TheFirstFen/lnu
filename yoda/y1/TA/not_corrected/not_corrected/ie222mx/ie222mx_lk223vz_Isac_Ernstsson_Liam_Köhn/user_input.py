from getpass import getpass
import re


def get_str(prompt) -> str:
    # Get a non-empty string from the user
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Invalid input! Please enter a non-empty string.")


def get_int(prompt) -> int:
    # Get an integer from the user
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.\n")


def get_phone(prompt) -> str:
    # Get a phone number from the user
    # but is not required
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return None  # Return None if the input is empty
        elif user_input and len(user_input) <= 15:
            return user_input
        else:
            print("Invalid input! Please enter a valid value.\n")


def get_pass() -> str:
    password = None
    # Ensure the password are entered correct
    # then return to main menu
    while password is None:
        password = getpass('Enter a password *: ')
        temp_password = getpass('Reenter your password *: ')
        if password == temp_password:
            return password
        else:
            print('Passwords dont match, try again\n')
        password = None


def get_email(prompt) -> str:
    # Get an email address from the user
    while True:
        user_input = input(prompt).strip()
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                         user_input)

        if valid:
            return user_input
        else:
            print('Invalid email address!\n')


def check_choice(nr_of_options: int):
    selected_option = None

    # while a wrong option is selected
    while selected_option is None:
        choice = input('Enter choice: ')
        try:
            if int(choice) in [x for x in range(1, nr_of_options + 1)]:
                selected_option = int(choice)
            else:
                print(
                    f'Invalid input, must be between 1 and {nr_of_options}\n'
                )

        except ValueError:
            # wrong input, try again
            selected_option = None
            print('invalid input, must be a number\n')
    return selected_option
