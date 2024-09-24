figure(1)                % Create or activate a figure with number 1
clf                      % Clear the figure
hold on                  % The following plots will be superposed in the same figure
grid on                  % Visible grid lines

x = -2:0.1:2;           % Plotting interval in x-direction
y = -2:0.1:2;           % Plotting interval in y-direction
[X, Y] = meshgrid(x, y); % Create a mesh of (x, y)-coordinate points in the xy-plane

Z1 = -X - Y;            % Define z-values for the first plane
Z2 = -X - Y + 2;        % Define z-values for the second parallel plane

surf(X, Y, Z1)          % Plots the first surface
surf(X, Y, Z2)          % Plots the second surface

view(35, 35)            % Choose the viewing angle
hold off                 % Inactivate the figure

% Add labels and title for better understanding
xlabel('X-axis');       % Label for x-axis
ylabel('Y-axis');       % Label for y-axis
zlabel('Z-axis');       % Label for z-axis
title('Two Parallel Planes'); % Title for the plot
