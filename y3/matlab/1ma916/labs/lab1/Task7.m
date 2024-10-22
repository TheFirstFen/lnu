clc
clear
figure(1)
clf
hold on
grid on

x = -2:0.1:2;
y = -2:0.1:2;
[X, Y] = meshgrid(x, y);

Z1 = -X - Y;
Z2 = -X - Y + 2;

surf(X, Y, Z1)
surf(X, Y, Z2)

view(35, 35)
hold off


xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
title('Two Parallel Planes');