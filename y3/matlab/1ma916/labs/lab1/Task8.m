% Parameters for the sphere
r = 6;                         % Radius of the sphere
center = [-2, 1, 3];          % Center of the sphere at (-2, 1, 3)

% Create a meshgrid for theta and phi
theta = linspace(0, 2*pi, 100); % Longitude (0 to 2π)
phi = linspace(0, pi, 100);     % Colatitude (0 to π)

% Create a grid of theta and phi values
[Theta, Phi] = meshgrid(theta, phi);

% Parametric equations for the sphere
X = r * sin(Phi) .* cos(Theta) + center(1); % X-coordinates
Y = r * sin(Phi) .* sin(Theta) + center(2); % Y-coordinates
Z = r * cos(Phi) + center(3);               % Z-coordinates

% Plot the sphere
figure;                                   % Create a new figure
surf(X, Y, Z, 'FaceColor', 'b', 'EdgeColor', 'none'); % Plot the surface
axis equal;                               % Set equal scaling for all axes
grid on;                                  % Turn on the grid
xlabel('X-axis');                         % Label for x-axis
ylabel('Y-axis');                         % Label for y-axis
zlabel('Z-axis');                         % Label for z-axis
title('Sphere with Radius 6 Centered at (-2, 1, 3)'); % Title for the plot
view(35, 35);                             % Set viewing angle
