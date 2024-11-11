format long


[a, b] = sparsesetup(1000);

afull = full(a);

%spy(a)

tic
x = jacobi(a, b, 6);
toc

tic
xfull = jacobi(afull, b, 6);
toc