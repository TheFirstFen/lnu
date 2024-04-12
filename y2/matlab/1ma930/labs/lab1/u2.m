format long;

clc

x = [-1:1/1000:1];

y = sin(2*x);

plot(x, y, 'b', 'LineWidth', 2);
grid on;