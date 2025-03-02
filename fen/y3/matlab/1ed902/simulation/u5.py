import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# System parameters
G = ctrl.TransferFunction([1], [1, 2, 0])  # G(s) = 1 / (s(s+2))

# PD regulator parameters
kp_values = [12.96]
kd_values = [2.25]

# Time vector
t = np.linspace(0, 10, 1000)

plt.figure(figsize=(10, 6))

for kp, kd in zip(kp_values, kd_values):
    # PD regulator
    D = ctrl.TransferFunction([kd, kp], [1])

    # Closed-loop system: T(s) = D(s)G(s) / (1 + D(s)G(s))
    open_loop = D * G
    closed_loop = ctrl.feedback(open_loop, 1)

    # Step response
    t, y = ctrl.step_response(closed_loop, t)
    plt.plot(t, y, label=f'kp={kp}, kd={kd}')
    print(f'kp={kp}, kd={kd}, Poles: {ctrl.poles(closed_loop)}')

plt.title("Step Response for Uppgift 5")
plt.xlabel("Time [s]")
plt.ylabel("Output y(t)")
plt.legend()
plt.grid(True)
plt.show()
