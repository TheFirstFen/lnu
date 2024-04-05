format long

clc

a = 1;
b = 3;
c = -8^(-14);

y1 = -b/2;
y2 = sqrt((b/2)^2 + c);

x1 = (-2*c)/(b + sqrt(b^2 - 4*a*c));
x2 = y1 - y2;

fprintf('%.3d\n', x1)
fprintf('%.3d\n', x2)