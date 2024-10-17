format long;

f = @(x) x-4*sin(2*x)-3-3/80;

x = linspace(6, 8, 1000);

y = f(x);
zero = 0;

plot(x, y, 'b', 'LineWidth', 2);
hold on;

plot(xlim, [0 0], 'k--');
title('Graph of f(x) = x - 4*sin(2*x) - 3 - 3/80');
xlabel('x');
ylabel('f(x)');
grid on;
x_guesses = x;
x_zeros = [];

for guess = x_guesses
    zero = fzero(f, guess);
    x_zeros = [x_zeros zero]
end

plot(x_zeros, zeros(size(x_zeros)), 'ro', 'MarkerSize', 100);

hold off;
