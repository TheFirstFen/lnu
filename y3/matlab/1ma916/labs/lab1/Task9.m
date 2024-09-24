% Define the range for x and y
x = -3:0.1:3; % Range for x
y = -3:0.1:3; % Range for y
[X, Y] = meshgrid(x, y); % Create a meshgrid for x and y

% (1) z = 2x^2 + 2y^2
Z1 = 2*X.^2 + 2*Y.^2;
figure(1); % Create figure 1
surf(X, Y, Z1); % Plot the surface
title('Surface: z = 2x^2 + 2y^2');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(2); % Create figure 2 for contour
contour(X, Y, Z1, 20); % Plot the level curves
title('Level Curves: z = 2x^2 + 2y^2');
xlabel('X-axis');
ylabel('Y-axis');
grid on;

% (2) z = sin(x) + cos(5y)
Z2 = sin(X) + cos(5*Y);
figure(3); % Create figure 3
surf(X, Y, Z2); % Plot the surface
title('Surface: z = sin(x) + cos(5y)');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(4); % Create figure 4 for contour
contour(X, Y, Z2, 20); % Plot the level curves
title('Level Curves: z = sin(x) + cos(5y)');
xlabel('X-axis');
ylabel('Y-axis');
grid on;

% (3) z = 1/(x^2 + y^2)
Z3 = 1 ./ (X.^2 + Y.^2 + eps); % Add eps to avoid division by zero
figure(5); % Create figure 5
surf(X, Y, Z3); % Plot the surface
title('Surface: z = 1/(x^2 + y^2)');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(6); % Create figure 6 for contour
contour(X, Y, Z3, 20); % Plot the level curves
title('Level Curves: z = 1/(x^2 + y^2)');
xlabel('X-axis');
ylabel('Y-axis');
grid on;

% (4) z = sqrt(6 - x^2 - y^2)
Z4 = sqrt(6 - X.^2 - Y.^2);
Z4(Z4 < 0) = NaN; % Set negative values to NaN for proper plotting
figure(7); % Create figure 7
surf(X, Y, Z4); % Plot the surface
title('Surface: z = sqrt(6 - x^2 - y^2)');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
grid on;
figure(8); % Create figure 8 for contour
contour(X, Y, Z4, 20); % Plot the level curves
title('Level Curves: z = sqrt(6 - x^2 - y^2)');
xlabel('X-axis');
ylabel('Y-axis');
grid on;
