format long;

x = -2:1/1000:8;

y = x - (4 * sin(2 * x)) - 3 - (3/80);


figure;
plot(x, y, 'b-');
hold on;
plot(xlim, [0 0], 'r-');

func = @(x) x - (4 * sin(2 * x)) - 3 - (3/80);


x_z = [];

for i = x
    root = fzero(func, i);
    x_z = [x_z root];
end

plot(x_z, zeros(size(x_z)), 'ro', 'MarkerSize', 10)
hold off;


