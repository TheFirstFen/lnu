% Helix Plot
clc
clear
t = linspace(0, 10*pi, 1000);
r = 2;
x = r * cos(t);
y = r * sin(t);
z = t / (2*pi);

plot3(x, y, z, 'r-', 'LineWidth', 2);
grid on
xlabel('x')
ylabel('y')
zlabel('z')
title('Helix with Radius 2')
axis equal