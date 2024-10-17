% Define the function
clc
f = @(x) 1 + 2*x + x.^3;

x = linspace(-5, 5, 1000);
y = f(x);
plot(x, y);
grid on;
xlabel('x');
ylabel('y');
title('Plot of y = 1 + 2x + x^3');

coefficients = [1, 0, 2, 1];
roots_of_equation = roots(coefficients);

errors = zeros(size(roots_of_equation));
for i = 1:length(roots_of_equation)
    alpha = roots_of_equation(i);
    p_alpha = polyval(coefficients, alpha);
    p_prime_alpha = polyval(polyder(coefficients), alpha);
    errors(i) = abs(p_alpha / p_prime_alpha);
end

disp('Roots of the equation:');
disp(roots_of_equation);
disp('Method-independent error estimate (H):');
disp(errors);
