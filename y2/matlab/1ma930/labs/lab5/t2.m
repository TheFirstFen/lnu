clc;
format long;

%% b
m1 = 16;
m2 = 32;
a = 0;
b = 4;
f = @(x) x ./ sqrt(x.^2 + 9);
F = integral(f,a,b);

function result = composite_trapezoid_rule(f, a, b, m)
    h = (b - a) / m;
    x = a:h:b;
    fx = f(x);
    result = h * (sum(fx) - (fx(1) + fx(end)) / 2);
end

approx1 = composite_trapezoid_rule(f, a, b, m1);
approx2 = composite_trapezoid_rule(f, a, b, m2);

error1 = abs(F - approx1);
error2 = abs(F - approx2);

fprintf('Approximation with %d panels: %.8f\n', m1, approximation1);
fprintf('Error: %.8f\n\n', error1);

fprintf('Approximation with %d panels: %.8f\n', m2, approximation2);
fprintf('Error: %.8f\n', error2);