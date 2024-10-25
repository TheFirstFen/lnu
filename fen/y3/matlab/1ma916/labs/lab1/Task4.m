% 3D Curve Plot
clc
clear
t = linspace(0, 10, 1000); 
x = sin(2*t);
y = cos(2*t);
z = sin(3*t);

plot3(x, y, z, 'b-', 'LineWidth', 2);
grid on
xlabel('x')
ylabel('y')
zlabel('z')
title('3D Curve: x = sin(2t), y = cos(2t), z = sin(3t)')
