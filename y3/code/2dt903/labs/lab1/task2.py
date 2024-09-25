# Variables
Vmin = 0.5
Vmax = 5.0
N = 4

step_size = (Vmax - Vmin)/(2**N - 1) # Correct

V = float(input("Provide the Voltage you want the bit representation of: "))

def compute(Vmin, Vmax, N, V):
    bit_str = ""

    for _ in range(N):
        Vx = (((Vmax - Vmin) / 2) + Vmin)
        print("Vmax:", Vmax, "V\tVmin:", Vmin, "V")
        if Vx > V:
            # -> 0 bit value
            bit_str += "0"
            Vmax = Vx
        else:
            # -> 1 bit value
            bit_str += "1"
            Vmin = Vx
        print("V:", V, "V , Vx:", Vx, "V\tBit representation:", bit_str)
    print("For", V, "V the bit representation is", bit_str, "\n")


compute(Vmin, Vmax, N, V)
