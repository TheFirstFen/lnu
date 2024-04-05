format long;

clc

x = [-1:1/1000:1];

y = sin(2*x);
y1 = exp(-x.^2);

plot(x, y, 'b', 'LineWidth', 2);
grid on;

hold on;

plot(x, y1, 'r', 'LineWidth', 2);
hold off;
