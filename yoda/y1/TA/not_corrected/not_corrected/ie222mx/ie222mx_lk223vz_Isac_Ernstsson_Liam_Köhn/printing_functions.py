import os
import time

WIDTH = 110


# Different functions for creating the view
def print_header(title: list, pause=True):
    # provide a list for each row of text you want in the header
    # Max 90 characters
    # Clearing terminal
    if pause:
        time.sleep(1)
    clear_screen()

    inner_width = WIDTH - 10
    # Printing out the header
    box = ('*' * WIDTH) + '\n'
    box += f'{"*" * 5}{" " * inner_width}{"*" * 5}\n'
    box += f'{"*" * 5}{" " * inner_width}{"*" * 5}\n'
    for text in title:
        title_width = len(text)
        remaining_space = WIDTH - 10 - title_width
        space = (inner_width - title_width) // 2
        right_space = remaining_space - space
        box += f'{"*" * 5}{" " * space}{text}{" " * right_space}{"*" * 5}\n'
    box += f'{"*" * 5}{" " * inner_width}{"*" * 5}\n'
    box += f'{"*" * 5}{" " * inner_width}{"*" * 5}\n'
    box += ('*' * WIDTH) + '\n'

    print(box)


# print out the different options for the user
def print_options(options: list):
    space = (WIDTH // 6) * 2
    for i in range(len(options)):
        print(f'{" " * space}{i + 1}.   {options[i]}{" " * space}')
        print()


# Print out the book details
def print_book(item: tuple):
    print('Author:', item[1])
    print('Title:', item[2])
    print('ISBN', item[0])
    print('Price', item[3])
    print('Subject', item[4])


# Clear the terminal
def clear_screen():
    # Clearing terminal For Linux
    if os.name == 'posix':
        os.system('clear')
    # Clearing terminal For Windows
    elif os.name == 'nt':
        os.system('cls')  # clears the terminal of text


# Print out the cart
def print_cart(cart: list):
    # Calculate column widths dynamically
    isbn_width = int(WIDTH * 0.15)
    title_width = int(WIDTH * 0.5)
    price_width = int(WIDTH * 0.1)
    qty_width = int(WIDTH * 0.1)
    total_width = WIDTH - (isbn_width + title_width + price_width + qty_width)

    divider = '-' * WIDTH

    # Header
    header = (
        f"{'ISBN':<{isbn_width}}"
        f"{'Title':<{title_width}}"
        f"{'$':>{price_width}}"
        f"{'Qty':>{qty_width}}"
        f"{'Total':>{total_width}}"
    )

    # Display the table
    print(divider)
    print(header)
    print(divider)

    grand_total = 0
    for isbn, author, title, price, category, qty in cart:
        total = price * qty
        grand_total += total
        # Print each row
        print(
            f"{isbn:<{isbn_width}}"
            f"{title[:title_width]:<{title_width}}"
            f"{price:>{price_width}.2f}"
            f"{qty:>{qty_width}}"
            f"{total:>{total_width}.2f}"
        )

    print(divider)
    print(f"{'Total':>{WIDTH - 15}}{f'${grand_total:,.2f}':>15}")
    print(divider)


def print_invoice(member: list, ono: int, books: list):
    print_header(["Welcome to the online Book Store", "Check out"], False)
    print(f'Invoice for order with order number: {ono}')
    print(f'Name: {member[0][0]} {member[0][1]}')
    print(f'''Address: {member[0][2]}
          {member[0][3]}
          {member[0][4]}''')
    print_cart(books)
    input('''Thank you for shopping at online books store,
    press enter to return to member menu''')
