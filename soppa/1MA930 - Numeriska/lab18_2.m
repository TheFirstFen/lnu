% Define the function
f = @(x) e^x;

% Define the interval and number of subintervals
a = 0;
b = 1;
n = 10; % Number of subintervals (must be even)

% Compute the integral using the Composite Simpson's Rule
integral_value = compositeSimpsonsRule(f, a, b, n);

% Display the result
disp(['The integral of sin(x) from 0 to pi is approximately ', num2str(integral_value)]);
