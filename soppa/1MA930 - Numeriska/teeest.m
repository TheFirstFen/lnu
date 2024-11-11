

x = @(t) 0.5 + 0.3*t + 3.9*t^2 - 4.7*t^3;
y = @(t) 1.5 + 0.3*t + 0.9*t^2 - 2.7*t^3;

% Test for n = 4 and n = 20
n_values = [4, 20];

for n = n_values
    % Define the s values
    s = (0:n) / n;
    
    % Compute the t_star values for each s
    t_stars = arrayfun(@(si) find_t_s(si), s);
    
    % Compute the x and y coordinates for each t_star
    x_vec = arrayfun(x, t_stars);
    y_vec = arrayfun(y, t_stars);

    % Plot the points
    figure
    hold on
    plot(x_vec, y_vec, 'bx', 'LineWidth', 1.5)
    xlabel('x')
    ylabel('y')
    title(['Number of points = ', num2str(n)])
    axis([0 1.4 0 1.7])
    hold off
end




