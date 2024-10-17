%a)
n = 200;
a = floor(10*rand(n));
b = sum(a')';
z = ones(n, 1);
tic,x=a\b;toc
tic,y =inv(a)*b;toc

%b)
max(abs(x-z))
max(abs(y-z))
