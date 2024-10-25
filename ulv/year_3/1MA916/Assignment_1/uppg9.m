clc;
clear;

[x, y] = meshgrid(linspace(-3, 3, 100));

z1 = 2 * x.^2 + 2 * y.^2;
z2 = sin(x) + cos(5 * y);
z3 = 1 ./ (x.^2 + y.^2);
z4 = 6 - x.^2 - y.^2;

figure;

% Surface for z1 = 2x² + 2y²
subplot(2, 4, 1);
surf(x, y, z1);
shading interp;
title('Surface: z = 2x^2 + 2y^2');
xlabel('x');
ylabel('y');
zlabel('z');
colormap('jet');

% Contour for z1
subplot(2, 4, 5);
contour(x, y, z1);
title('Contour: z = 2x^2 + 2y^2');
xlabel('x');
ylabel('y');

% Surface for z2 = sin(x) + cos(5y)
subplot(2, 4, 2);
surf(x, y, z2);
shading interp;
title('Surface: z = sin(x) + cos(5y)');
xlabel('x');
ylabel('y');
zlabel('z');
colormap('jet');

% Contour for z2
subplot(2, 4, 6);
contour(x, y, z2);
title('Contour: z = sin(x) + cos(5y)');
xlabel('x');
ylabel('y');

% Surface for z3 = 1 / (x^2 + y^2)
subplot(2, 4, 3);
surf(x, y, z3);
shading interp;
title('Surface: z = 1 / (x^2 + y^2)');
xlabel('x');
ylabel('y');
zlabel('z');
colormap('jet');

% Contour for z3
subplot(2, 4, 7);
contour(x, y, z3);
title('Contour: z = 1 / (x^2 + y^2)');
xlabel('x');
ylabel('y');

% Surface for z4 = 6 - x^2 - y^2
subplot(2, 4, 4);
surf(x, y, z4);
shading interp;
title('Surface: z = 6 - x^2 - y^2');
xlabel('x');
ylabel('y');
zlabel('z');
colormap('jet');

% Contour for z4
subplot(2, 4, 8);
contour(x, y, z4);
title('Contour: z = 6 - x^2 - y^2');
xlabel('x');
ylabel('y');

