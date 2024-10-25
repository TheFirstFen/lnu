n = input("Enter the number of columns and rows to print: ")
num = [0 ones(1, n-1)];
v = ones(n);
c = v + diag(num);
r = inv(c);
r