# Function to get number abcd
def get_abcd(a, b, c, d):
    abcd = 1000*a+100*b+10*c+1*d
    return abcd


# Function to get number dcba
def get_dcba(a, b, c, d):
    dcba = 1000*d+100*c+10*b+1*a
    return dcba


# Start of program

# Loop to check all potential a, b, c, d values
for a in range(1, 10):  # a value between 1 and 9
    for b in range(0, 10):  # b value between 0 and 9
        for c in range(0, 10):  # c calue between 0 and 9
            for d in range(1, 10):  # d value between 1 and 9

                # Get values for
                abcd = get_abcd(a, b, c, d)
                dcba = get_dcba(a, b, c, d)
                if abcd * 4 == dcba:
                    num = abcd

# Result
print(f"ABCD = {num}")
