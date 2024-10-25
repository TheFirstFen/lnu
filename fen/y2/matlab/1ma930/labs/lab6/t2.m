t1
format default
clc
%% a
[t5, wi5] = euler_IVP([0 1], 1, 5);
[t10, wi10] = euler_IVP([0 1], 1, 10);

g = @(t) 3*exp(t.^2/2) - t.^2 - 2;
yi5 = g(0:0.2:1);
yi10 = g(0:0.1:1);

ei5 = yi5 - wi5;
ei10 = yi10 - wi10;

%% b
hold on
[tE, yE] = euler_IVP([0 1], 1, 5);
plot(tE, yE)