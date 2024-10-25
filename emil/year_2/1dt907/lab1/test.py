import numpy as np
import matplotlib.pyplot as plt

# Function for the fitted curve: a * x^b
def fitted_curve(x, a, b):
    return a * x**b

# Function for the computed curve: (x * 2^(aC / bC))^bC
def computed_curve(x, aC, bC):
    return (x * 2**(aC / bC))**bC

# Given parameters for the fitted curve
a_fitted = 9.620923278880196e-11
b_fitted = 3.156849570357424

# Given parameters for the computed curve
aC_computed = -27.930453063895982
bC_computed = 2.7555222203420464

# Generate x values for plotting
x_values = np.linspace(1, 10, 100)

# Calculate y values for the fitted and computed curves
y_fitted = fitted_curve(x_values, a_fitted, b_fitted)
y_computed = computed_curve(x_values, aC_computed, bC_computed)

# Plot the curves
plt.plot(x_values, y_fitted, label='Fitted Curve')
plt.plot(x_values, y_computed, label='Computed Curve')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.show()

