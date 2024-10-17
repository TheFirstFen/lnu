radius = 3;

theta = linspace(0, 2*pi, 100);

x = radius * cos(theta);
y = radius * sin(theta);

figure;
plot(x, y, 'b', 'LineWidth', 2);
axis equal;
grid on;

xlabel('X-axis');
ylabel('Y-axis');
title('Circle with radius 3');

hold off;
