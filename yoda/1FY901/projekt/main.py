import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from pendulum import pendulum


def pend_parms(t, y):
    return pendulum(t, y, A, f)


phi0 = 1
phi_dot0 = 0
t = 100
A = 0.1
f = np.pi

tspan = [0, t]
y0 = [phi0, phi_dot0]

sol = solve_ivp(pend_parms, tspan, y0)
t_eval = np.linspace(tspan[0], tspan[1], 1000)

plt.plot(sol.t, sol.y[0])
plt.ylabel("Vinkel (radianer)")
plt.xlabel("Tid (s)")
plt.grid(True)
plt.show()