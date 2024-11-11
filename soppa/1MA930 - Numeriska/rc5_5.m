x = @(t) 0.5 + 0.3*t + 3.9*t.^2 - 4.7*t.^3;
y = @(t) 1.5 + 0.3*t + 0.9*t.^2 - 2.7*t.^3;

t_vals = linspace(0, 1, 100);

x_vals = arrayfun(x, t_vals);
y_vals = arrayfun(y, t_vals);

figure;
plot(x_vals, y_vals, 'r-', 'LineWidth', 1.5);
xlabel('x');
ylabel('y');
axis([0 1.4 0 1.7])
hold on;

p = plot(x_vals(1), y_vals(1), 'bo', 'MarkerFaceColor', 'b');

for k = 2:length(x_vals)
    p.XData = x_vals(k);
    p.YData = y_vals(k);
    drawnow;
    pause(0.05); % This is used to slow down the animation making it easier to examine
end

s_vals = linspace(0, 1, 100);

t_stars = zeros(1, length(s_vals));

for i = 1:length(s_vals)
    t_stars(i) = find_t_s(s_vals(i));
end

x_star_vals = arrayfun(x, t_stars);
y_star_vals = arrayfun(y, t_stars);

figure;
plot(x_vals, y_vals, 'r-', 'LineWidth', 1.5);
xlabel('x');
ylabel('y');
axis([0 1.4 0 1.7])
hold on;

p_star = plot(x_star_vals(1), y_star_vals(1), 'go', 'MarkerFaceColor', 'g');

for k = 2:length(x_star_vals)
    p_star.XData = x_star_vals(k);
    p_star.YData = y_star_vals(k);
    drawnow;
    pause(0.05); % This is used to slow down the animation making it easier to examine
end
