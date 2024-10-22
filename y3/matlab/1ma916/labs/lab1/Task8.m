% Parameters for the sphere
clc
clear
r = 6;
center = [-2, 1, 3];

theta = linspace(0, 2*pi, 100);
phi = linspace(0, pi, 100);

[Theta, Phi] = meshgrid(theta, phi);

X = r * sin(Phi) .* cos(Theta) + center(1);
Y = r * sin(Phi) .* sin(Theta) + center(2);
Z = r * cos(Phi) + center(3);

figure;
surf(X, Y, Z, 'FaceColor', 'b', 'EdgeColor', 'none');
axis equal;
grid on;
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
title('Sphere with Radius 6 Centered at (-2, 1, 3)');
view(35, 35);