n = 500;
a = floor(10*rand(n));
b = sum(a')';
z = ones(n, 1);
x = a\b;
y  = inv(a) * b;
max(abs(x-z))
max(abs(y-z))

n = 1000;
a = floor(10*rand(n));
b = sum(a')';
z = ones(n, 1);
x = a\b;
y  = inv(a) * b;
max(abs(x-z))
max(abs(y-z))