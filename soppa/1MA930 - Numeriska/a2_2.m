format long

clc

f = @(x) x - 4 * sin(2 * x) - 3 - 3 / 80;

opts.TOL = 10^-6;

[x, k] = bisection_method(f, 1, 2, opts);
%% A
% Mellan [1, 2]
% c1 = 1,5
% f(c1) ≈ -2.102
% Vilket ger ett uppdaterat interval på [1.5, 2]
% c2 = 1,75
% f(c2) ≈ 0.116
% Vilket ger ett uppdaterat interval på [1.5, 1.75]
% c = 1,625
% f(c) ≈ -0.980
% Vilket ger ett uppdaterat interval på [1.625, 75]
% Ungefärligt fel på 0.25

%% B
disp(['iterationer ', num2str(k)])
disp(['Svar ', sprintf('%.16f', x)])

%% C
val = bisect(f, 1, 2, 0.000001);
disp(['Från boken ', sprintf('%.16f', val)])


