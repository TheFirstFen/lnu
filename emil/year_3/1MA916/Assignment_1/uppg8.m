clc;
clear;

%% A
[x, y, z] = sphere();

x = 6 * x;
y = 6 * y;
z = 6 * z;

x = x - 2;
y = y + 1;
z = z + 3;

figure;
surf(x, y, z);
xlabel('x');
ylabel('y');
zlabel('z');
title('First part using sphere commmand');
axis equal;
grid on;

%% B

theta = linspace(0, 2 * pi, 50);
phi = linspace(0, pi, 50);

[Theta, Phi] = meshgrid(theta, phi);

r = 6;

X = r * cos(Theta) .* sin(Phi) + -2;
Y = r * sin(Theta) .* sin(Phi) + 1;
Z = r * cos(Phi) + 3;

figure;
surf(X, Y, Z);
xlabel('x');
ylabel('y');
zlabel('z');
title('Second part without sphere command');
axis equal;
grid on;
