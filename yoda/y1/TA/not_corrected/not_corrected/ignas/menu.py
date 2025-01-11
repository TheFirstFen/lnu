from database import Database


menu_options = (["Member Login", "New Member Registration", "Quit"])
member_options = (["Browse by Subject","Search by Author/Title","Check Out","Logout"])


def print_header(title):
    print("------------------------------------------------------------------")
    print("-----                                                        -----")
    print("-----                     "+ title +"                        -----")
    print("-----                                                        -----")
    print("------------------------------------------------------------------")


def print_options(options):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    
def user_choice(max_options):
    selected_option = None

    while selected_option == None:
        choice = input("Enter Choice:")
        try:
            if int(choice) in [y for y in range(1,max_options+1)]: #checks to see if the input is an integer
                selected_option = choice
            else:
                print("Invalid input detected, please enter an available option...")
        except Exception:
            selected_option = None
            print("Invalid input detected, please enter a number...") #if there's an error, selected_option is none and the while loop runs until a correct input.
    
    return selected_option

