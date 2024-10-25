format long 

% U 1
%% B
clc
[a, b] = sparsesetup(6);

afull = full(a)
spy(a)

%% D
clc
k = 1;
x = jacobi(a, b, k);
x

%% E
clc

[a,b] = sparsesetup(1000);
afull = full(a);

tic
x1 = jacobi(a, b, 6);
toc
tic
x2 = jacobi(afull, b, 6);
toc