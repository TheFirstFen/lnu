import numpy as np

def pendulum(t, y, A, f):
    
    g = 9.82
    
    phi = y[0]
    phi_dot = y[1]
    
    phi_ddot = -np.sin(phi) * (A * t**2 * np.cos(f * t) + g)
    
    dydt = [phi_dot, phi_ddot]
    return dydt


