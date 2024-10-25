def welcome_msg():
    print("*"*50)
    print("*"*3 + " "*44 + "*"*3)
    print("*"*3 + " "*6 + "Welcome to the Online Book Store" + " "*6 + "*"*3)
    print("*"*3 + " "*44 + "*"*3)
    print("*"*50)


def members_gui():
    print("*"*50)
    print("*"*3 + " "*44 + "*"*3)
    print("*"*3 + " "*6 + "Welcome to the Online Book Store" + " "*6 + "*"*3)
    print("*"*3 + " "*16 + "Member Menu" + " "*17 + "*"*3)
    print("*"*3 + " "*44 + "*"*3)
    print("*"*50)


def standard_gui(second_word):
    total_length = 50  # Total length of the line
    word_length = len(second_word)

    # Calculate left and right empty spaces
    left_empty = (total_length - word_length - 6) // 2
    right_empty = total_length - word_length - left_empty - 6

    print("*" * total_length)
    print("*" * 3 + " " * (total_length - 6) + "*" * 3)
    print("*" * 3 + " " * 15 + "Online Book Store" + " " * 12 + "*" * 3)
    print("*" * 3 + " " * left_empty + second_word + " " * right_empty +
          "*" * 3)
    print("*" * 3 + " " * (total_length - 6) + "*" * 3)
    print("*" * total_length + "\n")


def print_invoice(text, isbns, titles, costs, quantitys):
    multiplier_const = 150
    total_cost = 0
    # Print header
    print("="*multiplier_const)
    print(f"      {text}")
    print("="*multiplier_const)
    for isbn, cost, title, qty in zip(isbns, costs, titles, quantitys):
        total_book_cost = cost * qty
        total_cost += total_book_cost

        # Print details
        print(f"ISBN:              {isbn:<10}")
        print(f"Title:             {title:<20}")
        print(f"Cost per unit:    ${cost:<10}")
        print(f"Quantity:          {qty:<10}")
        print(f"Total Cost:       ${total_book_cost:<10}")
        print("="*multiplier_const)

    print(f"Total Cost: ${total_cost:<10}")
    print("="*multiplier_const)


def print_book_information(books_found, books, start_index, end_index):
    multiplier_const = 150
    print(f"Found {books_found} book(s)")
    array_split = books[start_index:end_index]

    for row in array_split:
        print("="*multiplier_const)
        print(f"\nAuthor: {row[1]}")
        print(f"Title: {row[2]}")
        print(f"ISBN: {row[3]}")
        print(f"Price: {row[4]}")
        print(f"Subject: {row[5]}\n")
        print("\n" + "=" * multiplier_const)
    print("Enter ISBN to add to Cart or n Enter to browse or" +
          " ENTER to go back to menu:")
