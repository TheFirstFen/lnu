% Task1
clear
t = 0 : 0.01 : 5; % Define the range of t from 0 to 5 with a step size of 0.01
x = 4 + t.^3;     % Calculate x as a function of t
y = 1 + 5 * t.^2; % Calculate y as a function of t
plot(x, y)        % Plot x vs. y
xlabel('x')       % Label x-axis
ylabel('y')       % Label y-axis
title('Plot of x = 4 + t^3 and y = 1 + 5t^2') % Title of the plot
grid on           % Add grid to the plot