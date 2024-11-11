%% A

A = rand(5, 5);
b = rand(5,1);
tic
x = A\b;
toc
r = b - A*x;

%% B
tic
[L, U] = lu(A);

z = L\b;
x1 = U\z;
toc
%% C
tic
inv(A);
toc
