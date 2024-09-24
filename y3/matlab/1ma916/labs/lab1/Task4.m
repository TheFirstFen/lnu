% 3D Curve Plot
t = linspace(0, 10, 1000);  % Create an array of 1000 points for t from 0 to 10
x = sin(2*t);               % Calculate x-coordinates
y = cos(2*t);               % Calculate y-coordinates
z = sin(3*t);               % Calculate z-coordinates

plot3(x, y, z, 'b-', 'LineWidth', 2); % Plot the 3D curve with blue line and line width 2
grid on                             % Turn on the grid
xlabel('x')                         % Label x-axis
ylabel('y')                         % Label y-axis
zlabel('z')                         % Label z-axis
title('3D Curve: x = sin(2t), y = cos(2t), z = sin(3t)') % Add title to the plot
