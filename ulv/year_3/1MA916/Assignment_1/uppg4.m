clc;
t = linspace(0, 2*pi, 1000);

x = sin(2*t);
y = cos(2*t);
z = sin(3*t);

figure;
plot3(x, y, z, 'b', 'LineWidth', 1);

xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
title('3D Curve: x = sin(2t), y = cos(2t), z = sin(3t)');

grid on;
axis equal;

view(3);
