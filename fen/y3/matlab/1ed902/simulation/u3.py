import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# System parameters
num = [1]
den = [1, 7, 2, 4]  # s^3 + 7s^2 + 2s + 4
G = ctrl.TransferFunction(num, den)

# Proportional gains to test
K_values = [-3, 0.1, 5, 9, 11]

# Time vector
t = np.linspace(0, 10, 1000)

plt.figure(figsize=(10, 6))

for K in K_values:
    # Closed-loop system: T(s) = KG(s) / (1 + KG(s))
    system = ctrl.feedback(K * G, 1)
    t, y = ctrl.step_response(system, t)

    plt.plot(t, y, label=f'K = {K}')
    print(f'K = {K}, Poles: {ctrl.poles(system)}')

plt.title("Step Response for Different K values")
plt.xlabel("Time [s]")
plt.ylabel("Output y(t)")
plt.legend()
plt.grid(True)
plt.show()

