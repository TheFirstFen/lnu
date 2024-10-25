format long;

x = linspace(-1, 1, 1000);

f = sin(2*x);

plot(x, f, 'b', 'Linewidth', 2);
title('Plot of f(x) = sin(2x)');
xlabel('x');
ylabel('f(x)');
grid on;