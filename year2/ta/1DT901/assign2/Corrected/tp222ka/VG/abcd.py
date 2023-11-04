
# Function 'get_number' that takes four digits (a, b, c, d)
def get_number(a, b, c, d):
    # Calculate to their size
    thousand = a * 1000
    hundred = b * 100
    ten = c * 10
    one = d
    # Returns a four-digit number.
    return thousand + hundred + ten + one


# Function 'simulate' to find the solution.
def simulate():
    # Iterate through all four-digit number combinations
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(1, 10):
                    # Using the digits from get_number(a, b, c, d)
                    # Call the function with the current digits
                    abcd = get_number(a, b, c, d)
                    # Reverse the order of the digits
                    dcba = get_number(d, c, b, a)

                    # Check if the number abcd multiplied by 4 equals dcba.
                    if abcd * 4 == dcba:
                        print(f"A = {a}, B = {b}, C = {c}, D = {d}")
                        print(f"{abcd} * 4 = {dcba}")
                        # Found a solution return
                        return


# Call the 'simulate'
simulate()
