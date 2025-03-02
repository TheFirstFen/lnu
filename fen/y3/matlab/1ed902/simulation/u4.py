import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# System parameters
G = ctrl.TransferFunction([1, -1], [1, 3, 2])  # G(s) = (1-s) / (s^2 + 3s + 2)
D = ctrl.TransferFunction([1, 1], [1, 0])  # D(s) = 1 + 1/s
H = -1  # H(s) = -1

# Closed-loop transfer function T(s) = D(s)G(s) / (1 - D(s)G(s)H(s))
open_loop = D * G
closed_loop = ctrl.feedback(open_loop, H)

# Time vector
t = np.linspace(0, 10, 1000)

# Step response
t, y = ctrl.step_response(closed_loop, t)

# Plotting the response
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='Step Response')
plt.title("Step Response for Uppgift 4")
plt.xlabel("Time [s]")
plt.ylabel("Output y(t)")
plt.legend()
plt.grid(True)
plt.show()

# Print poles and system type
print(f'Poles: {ctrl.poles(closed_loop)}')
print("System Type: 1")
