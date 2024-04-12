format long
% U 1
%% B
clc
[a, b] = sparsesetup(6);

afull = full(a)

%spy(a)

%% D
clc

x = jacobi(a, b, 1)

%% E
clc

[a, b] = sparsesetup(5000);

afull = full(a);
tic
x1 = jacobi(a, b, 6); % fast
toc

tic
x2 = jacobi(afull, b, 6); % slow
toc