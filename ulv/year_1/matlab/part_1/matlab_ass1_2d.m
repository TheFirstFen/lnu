n = 100;
a = floor(10*rand(n));
b = sum(a')';
z = ones(n, 1);
C = sym(a);
x = C\b
y = inv(C) * b
max(abs(x-z))
max(abs(y-z))
tic,x=C\b;toc
tic,y =inv(C)*b;toc