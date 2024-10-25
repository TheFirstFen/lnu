clc;
clear;

t = 0:0.01:10*pi;
x = 2 * cos(t);
y = 2 * sin(t);
z = t / (2*pi);

plot3(x, y , z)
xlabel('X')
ylabel('Y')
zlabel('Z')
title('3D Helix with radius 2')
grid on
