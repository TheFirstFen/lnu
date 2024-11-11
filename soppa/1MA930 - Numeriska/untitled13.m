clear
clc
close all

% Define the parametric path functions
x = @(t) 0.5 + 0.3*t + 3.9*t.^2 - 4.7*t.^3;
y = @(t) 1.5 + 0.3*t + 0.9*t.^2 - 2.7*t.^3;

% Loop over the values of n
for n = [4, 20]
    s = linspace(0, 1, n + 1); % Generate s values from 0 to 1
    
    % Compute t* values using find_t_s_newton
    t_stars_newton = arrayfun(@find_t_s_newton, s(2:end)); % Exclude the first value (0)

    % Compute t* values using find_t_s
    t_stars = arrayfun(@find_t_s, s(2:end)); % Exclude the first value (0)
    
    % Compute x and y values for the path using t_stars_newton
    x_vec_newton = arrayfun(x, t_stars_newton);
    y_vec_newton = arrayfun(y, t_stars_newton);
    
    % Compute x and y values for the path using t_stars
    x_vec = arrayfun(x, t_stars);
    y_vec = arrayfun(y, t_stars);
    
    % Plot the results
    figure;
    hold on;
    plot(x_vec_newton, y_vec_newton, 'bx-', 'DisplayName', 'find\_t\_s\_newton');
    plot(x_vec, y_vec, 'ro-', 'DisplayName', 'find\_t\_s');
    xlabel('x');
    ylabel('y');
    title(['Number of points = ', num2str(n)]);
    axis([0 1.4 0 1.7]);
    legend('Location', 'best');
    hold off;
end
