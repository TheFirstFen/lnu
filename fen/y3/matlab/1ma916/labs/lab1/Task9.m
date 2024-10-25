clc
clear
x = -3:0.1:3;
y = -3:0.1:3;
[X, Y] = meshgrid(x, y);

% (1) z = 2x^2 + 2y^2
Z1 = 2*X.^2 + 2*Y.^2;
figure(1);
surf(X, Y, Z1);
title('Surface: z = 2x^2 + 2y^2');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(2);
contour(X, Y, Z1, 20);
title('Level Curves: z = 2x^2 + 2y^2');
xlabel('X-axis');
ylabel('Y-axis');
grid on;

% (2) z = sin(x) + cos(5y)
Z2 = sin(X) + cos(5*Y);
figure(3);
surf(X, Y, Z2);
title('Surface: z = sin(x) + cos(5y)');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(4)
contour(X, Y, Z2, 20);
title('Level Curves: z = sin(x) + cos(5y)');
xlabel('X-axis');
ylabel('Y-axis');
grid on;

% (3) z = 1/(x^2 + y^2)
Z3 = 1 ./ (X.^2 + Y.^2 + eps);
figure(5);
surf(X, Y, Z3);
title('Surface: z = 1/(x^2 + y^2)');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(6);
contour(X, Y, Z3, 20);
title('Level Curves: z = 1/(x^2 + y^2)');
xlabel('X-axis');
ylabel('Y-axis');
grid on;

% (4) z = sqrt(6 - x^2 - y^2)
Z4 = sqrt(6 - X.^2 - Y.^2);
Z4(imag(Z4) ~= 0) = NaN;
Z4(Z4 < 0) = NaN; 
figure(7);
surf(X, Y, Z4);
title('Surface: z = sqrt(6 - x^2 - y^2)');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(8);
contour(X, Y, Z4, 20);
title('Level Curves: z = sqrt(6 - x^2 - y^2)');
xlabel('X-axis');
ylabel('Y-axis');
grid on;
