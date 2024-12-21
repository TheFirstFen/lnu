import math

# A)

epsilon_0 = 8.854E-12
epsilon_r = 1

# ändra dessa
radien = 3
distance = 4
read_C = 10E-11
# -----------

area = (radien**2) * math.pi
theory_C = epsilon_0 * epsilon_r * (area / distance)

deviation = ((abs(read_C - theory_C)) / theory_C) * 100

print(f"Teori: {theory_C}")
print(f"Avvikelse: {round(deviation, 3)}%")

# B)
# ändra dessa
optimal_area = 10
optimal_distans = 5
C = 6.64E-12
# ---------

epsilon_0_calc = (C*optimal_distans) / optimal_area
print(f"\nUträknat epsilon 0 {epsilon_0_calc:.3}")

# C)
# ändra dessa

C_plexi = 8.0E-12
C_luft = 4.0E-12
# ----------

epsilon_r = C_plexi / C_luft
print("\nBeräknat epsilon för plexi", epsilon_r)
