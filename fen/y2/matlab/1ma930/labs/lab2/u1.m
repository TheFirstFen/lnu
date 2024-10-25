format long;

clc

x = -2:1/1000:8;

f = @(x) x - 4 * sin(2 * x) - 3 - 3 / 80;
y = f(x);

plot(x, y, 'b', 'LineWidth', 2);
hold on;
grid on;
plot(xlim, [0 0], 'r', 'LineWidth', 2);
hold on;
x_z = [];

for x_g = x
    zero = fzero(f, x_g);
    x_z = [x_z zero];
end

plot(x_z, zeros(size(x_z)), 'ro', 'MarkerSize', 50);

hold off;