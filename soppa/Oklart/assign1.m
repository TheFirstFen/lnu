n = input("Enter the size of the matrix: ")

oness = ones(n);
v(1:n, 1) = 1;
C = oness + diag(v);
C(1, 1) = 1;
inv(C)

A = [1 1;1 2;1 3;1 4];
b = [0;3;5;6];



        
     