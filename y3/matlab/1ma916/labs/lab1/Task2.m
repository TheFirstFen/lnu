% Circle Plot
theta = linspace(0, 2*pi, 100); % Create an array of angles from 0 to 2*pi
radius = 3;                     % Define the radius of the circle
x = radius * cos(theta);        % Calculate the x-coordinates
y = radius * sin(theta);        % Calculate the y-coordinates

figure;                         % Create a new figure window
plot(x, y, 'b-', 'LineWidth', 2); % Plot the circle with blue line and line width 2
axis equal                      % Set equal scaling for x and y axes
grid on                         % Turn on the grid
xlabel('x')                     % Label x-axis
ylabel('y')                     % Label y-axis
title('Circle of Radius 3')     % Add title to the plot
