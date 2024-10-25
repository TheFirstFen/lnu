format long;

x = linspace(-1, 1, 1000);

f = sin(2*x);
g = exp(-x.^2);

plot(x, f, 'b', 'LineWidth', 2);
hold on;
plot(x, g, 'r', 'Linewidth', 2);
hold off;

title('Plot of f(x) = sin(2x) and g(x) = e^{-x^2}');
xlabel('x');
ylabel('y');
legend('f(x) = sin(2x)', 'g(x) = e^{-x^2}', 'Location', 'best');
grid on;