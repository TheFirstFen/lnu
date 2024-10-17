theta = linspace(0, 2*pi, 1000);

r = 1 - sin(4*theta);

figure;
polarplot(theta, r, 'r', 'LineWidth', 2);

title('Polar Plot of r = 1 - sin(4\theta)');

grid on;
