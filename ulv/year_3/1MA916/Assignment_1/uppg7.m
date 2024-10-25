clc;
clear;

hold on 
grid on

x = -2: 0.1: 2;
y = -2: 0.1: 2;
[X, Y] = meshgrid(x, y);

Z1 = -X - Y;
surf(X , Y, Z1)

Z2 = 2 - X - Y;
surf(X, Y, Z2)

view(35, 35)
hold off