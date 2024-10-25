% Task1
clc
clear
t = 0 : 0.01 : 5;
x = 4 + t.^3;
y = 1 + 5 * t.^2;
plot(x, y)
xlabel('x')
ylabel('y')
title('Plot of x = 4 + t^3 and y = 1 + 5t^2')
grid on