% Circle Plot
clc
clear
theta = linspace(0, 2*pi, 100);
r = 3;
x = r * cos(theta);
y = r * sin(theta);

figure;
plot(x, y, 'b-', 'LineWidth', 2);
axis equal
grid on
xlabel('x')
ylabel('y')
title('Circle of Radius 3')