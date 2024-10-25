% U3
format long
clear
clc
n = 5;

%% A
A = rand(n,n);
b = rand(n,1);

tic
x = A\b;
toc

r = b - A*x;

%% B & C & D
tic
LUfactor(A, b)
toc