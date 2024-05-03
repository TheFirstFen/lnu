clc;
format long;

%% b

f = @(x) exp(x);

romberg(f, 0, 1, 3)

%% c
f = @(x) x^2;

romberg(f,0,1,3)

%% d
f = @(x) log(x);

romberg(f, 1, 2, 4)