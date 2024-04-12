format long

clc

f = @(x) x - 4 * sin(2 * x) - 3 - 3 / 80;

opts.TOL = 10^-6;

[x, k] = bisection_method(f, 1, 2, opts);
%% A
k
%% B
x
%% C
bisect(f, 1, 2, 0.000001)


