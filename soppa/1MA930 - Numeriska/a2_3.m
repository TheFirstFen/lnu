format long

clc

x = -10:0.00001:10;

y = @(x) x.^3 + 0*x.^2 + 2*x + 1;
y1 = @(x) 3*x.^2 + 2;

plot(x, y(x));
grid on;

p = [1 0 2 1];
p1 = [3 0 2];

p_roots = roots(p)

errors = zeros(size(p_roots));
for i = 1:length(p_roots)
    alpha = p_roots(i);
    p_alpha = polyval(p, alpha);
    prime_alpha = polyval(polyder(p), alpha);
    errors(i) = abs(p_alpha/prime_alpha);
end

errors
