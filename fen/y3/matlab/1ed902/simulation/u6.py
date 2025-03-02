import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# System parameters
A = np.array([[0, 1], [1, -1]])  # System matrix
B = np.array([[0], [2]])        # Input matrix
C = np.array([[1, 0]])          # Output matrix
D = np.array([[0]])             # Direct transmission matrix

# State-space system
sys = ctrl.ss(A, B, C, D)

# Full state feedback parameters
l1, l2 = 5/2, 3/2
L = np.array([[l1, l2]])
lr = 2

# Closed-loop system with full state feedback
Acl = A - B @ L
Bcl = B * lr
Ccl = C
Dcl = D
sys_cl = ctrl.ss(Acl, Bcl, Ccl, Dcl)

# Time vector
t = np.linspace(0, 10, 1000)

# Step response
t, y = ctrl.step_response(sys_cl, t)

plt.figure(figsize=(10, 6))
plt.plot(t, y, label='Full State Feedback')
plt.title("Step Response for Uppgift 6")
plt.xlabel("Time [s]")
plt.ylabel("Output y(t)")
plt.legend()
plt.grid(True)
plt.show()

# Poles
print(f'Poles: {ctrl.poles(sys_cl)}')
