def get_number(A, B, C, D):
    # Converts digits A, B, C, and D into a four-digit integer ABCD
    return A * 1000 + B * 100 + C * 10 + D

# Quadruple nested loop to iterate through all possible combinations
for A in range(1, 10):
    for B in range(10):
        for C in range(10):
            for D in range(1, 10):
                # Ensure that A, B, C, and D are all different
                if len(set([A, B, C, D])) == 4:
                    # Calculate DCBA and ABCD
                    DCBA = get_number(D, C, B, A)
                    ABCD = get_number(A, B, C, D)

                    # Check if DCBA is equal to 4 times ABCD
                    if DCBA == 4 * ABCD:
                        print(f"A = {A}, B = {B}, C = {C}, D = {D}")
