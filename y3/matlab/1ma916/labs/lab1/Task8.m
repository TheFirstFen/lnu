clc
clear
[x, y, z] = sphere();
r = 6;

x = 6 * x - 2;
y = 6 * y + 1;
z = 6 * z + 3;

figure;
surf(x, y, z);
xlabel('x');
ylabel('y');
zlabel('z');
title('Made using sphere function');
axis equal;
grid on;
view(35, 35);

theta = linspace(0, 2*pi, 100);
phi = linspace(0, pi, 100);
[Theta, Phi] = meshgrid(theta, phi);

X = r * sin(Phi) .* cos(Theta) - 2;
Y = r * sin(Phi) .* sin(Theta) + 1;
Z = r * cos(Phi) + 3;

figure;
surf(X, Y, Z);
axis equal;
grid on;
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
title('Made without using sphere function');
view(35, 35);