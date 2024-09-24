% Helix Plot
t = linspace(0, 10*pi, 1000);  % Create an array of points for t from 0 to 10*pi
radius = 2;                    % Define the radius of the helix
x = radius * cos(t);           % Calculate x-coordinates of the helix
y = radius * sin(t);           % Calculate y-coordinates of the helix
z = t / (2*pi);                % Calculate z-coordinates (1 unit per revolution)

plot3(x, y, z, 'r-', 'LineWidth', 2); % Plot the helix with red line and line width 2
grid on                              % Turn on the grid
xlabel('x')                          % Label x-axis
ylabel('y')                          % Label y-axis
zlabel('z')                          % Label z-axis
title('Helix with Radius 2')         % Add title to the plot
axis equal                           % Set equal scaling for all axes
