% Task 9
%% (1) z = 2x^2 + 2y^2
x = linspace(-2, 2, 50);
y = linspace(-2, 2, 50);
[X, Y] = meshgrid(x, y);

Z1 = 2 * X.^2 + 2 * Y.^2;

figure;
% Plotting the surface
subplot(1, 2, 1);
surf(X, Y, Z1);
title('Surface');
xlabel('X'); 
ylabel('Y'); 
zlabel('Z');

% Plotting the contour
subplot(1, 2, 2);
contour(X, Y, Z1, 20);
title('Level Curves');
xlabel('X'); ylabel('Y');
axis equal;
sgtitle('(1) z = 2x^2 + 2y^2');
%% (2) z = sin(x) + cos(5y)
x = linspace(-pi, pi, 50);
y = linspace(-pi, pi, 50);
[X, Y] = meshgrid(x, y);

Z2 = sin(X) + cos(5 * Y);

figure;
% Plotting the surface
subplot(1, 2, 1);
surf(X, Y, Z2);
title('Surface');
xlabel('X'); 
ylabel('Y'); 
zlabel('Z');

% Plotting the contour
subplot(1, 2, 2);
contour(X, Y, Z2, 20);
title('Level Curves');
xlabel('X'); ylabel('Y');
axis equal;
sgtitle('(2) z = sin(x) + cos(5y)');
%% (3) z = 1 / (x^2 + y^2)
x = linspace(-2, 2, 50);
y = linspace(-2, 2, 50);
[X, Y] = meshgrid(x, y);

Z3 = 1 ./ (X.^2 + Y.^2);


figure;
% Plotting the surface
subplot(1, 2, 1);
surf(X, Y, Z3);
title('Surface');
xlabel('X'); 
ylabel('Y'); 
zlabel('Z');

% Plotting the contour
subplot(1, 2, 2);
contour(X, Y, Z3, 20);
title('Level Curves');
xlabel('X'); ylabel('Y');
axis equal;
sgtitle('(3) z = 1 / (x^2 + y^2)');
%% (4) z = sqrt(6 - x^2 - y^2)
x = linspace(-2, 2, 50);
y = linspace(-2, 2, 50);
[X, Y] = meshgrid(x, y);

Z4 = sqrt(6 - X.^2 - Y.^2);
Z4(imag(Z4) ~= 0) = NaN; % Removing complex values


figure;
% Plotting the surface
subplot(1, 2, 1);
surf(X, Y, Z4);
title('Surface');
xlabel('X'); 
ylabel('Y'); 
zlabel('Z');

% Plotting the contour
subplot(1, 2, 2);
contour(X, Y, Z4, 20);
title('Level Curves');
xlabel('X'); ylabel('Y');
axis equal;
sgtitle('(4) z = sqrt(6 - x^2 - y^2)');
