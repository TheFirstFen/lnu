% Polar Plot of r = 1 - sin(4θ)
theta = linspace(0, 2*pi, 1000); % Create an array of angles from 0 to 2*pi
r = 1 - sin(4*theta);            % Calculate the radius r for each theta

polarplot(theta, r, 'r-', 'LineWidth', 2); % Plot the polar curve with red line and line width 2
title('Polar Plot of r = 1 - sin(4θ)')     % Add title to the plot
