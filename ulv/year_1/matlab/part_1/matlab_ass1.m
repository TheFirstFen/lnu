%1e)
n = input("Enter the number of columns and rows to print: ")
num = [0 ones(1, n-1)];
v = ones(n);
c = v + diag(num);
r = inv(c);
r


%2a)
n = 200;
a = floor(10*rand(n));
b = sum(a);
z = ones(n, 1);
tic,x=a\b;toc
tic,y =inv(a)*b;toc

%2b)
max(abs(x-z))
max(abs(y-z))

%2c)
n = 500;
a = floor(10*rand(n));
b = sum(a');
z = ones(n, 1);
x = a\b;
y  = inv(a) * b;
max(abs(x-z))
max(abs(y-z))

n = 1000;
a = floor(10*rand(n));
b = sum(a');
z = ones(n, 1);
x = a\b;
y  = inv(a) * b;
max(abs(x-z))
max(abs(y-z))

%2d)
n = 100;
a = floor(10*rand(n));
b = sum(a');
z = ones(n, 1);
C = sym(a);
x = c\b
y = inv(c) * b
max(abs(x-z));
max(abs(y-z));

% 3a)
underdetermined