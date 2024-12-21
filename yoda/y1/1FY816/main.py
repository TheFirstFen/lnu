import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import math

my = 4 * math.pi * 10**-7
r = 2  # meter
N = 10
angles = np.array([5, 10, 15, -5, -10, -15])  # Vinklar i grader
currents = np.array([0.1, 0.2, 0.3, -0.1, -0.2, -0.3])  # Ström i ampere

# Beräkning av tan(α) för varje vinkel
tan_alpha = np.tan(np.radians(angles))
Be = [(my * N * I) / r for I in currents]
Bj_h = [B / np.tan(np.radians(angle)) for B, angle in zip(Be, angles)]

slope, intercept, r_value, p_value, std_err = linregress(tan_alpha, Be)

plt.scatter(tan_alpha, Be, label="Mätdata")
plt.plot(tan_alpha, slope * tan_alpha + intercept, color='red', label=f"Linjär regression (lutning = {slope:.2e})")
plt.xlabel("tan(α)")
plt.ylabel("B_e (proportionell mot ström)")
plt.legend()
plt.title("Beräkning av B_jH från tan(α) och B_e")
plt.grid()
plt.show()

# Skriv ut resultat för B_jH från linjär regression
print(f"Horisontell komponent av jordens magnetfält (B_jH) från regression: {slope:.3e} T")

# Skriv ut B_jH för varje mätning
print("\nB_jH för varje mätning:")
for angle, B_j in zip(angles, Bj_h):
    print(f"Vinkel: {angle}°, B_jH: {B_j:.3e} T")
