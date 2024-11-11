% Task 6
A = [1 0 3; 0 4 5; 1 2 -1];
B = [1 3 1; 2 2 2; 3 1 3];

a = [2; 3; 0];
b = [1; 1; 1];

result_1 = A * B % Works

result_2 = A * a % Works

result_3 = B * b % Works

% result_4 = a * A % Does not work, beacuse you cannot multiply vector 
% a(3x1) with matrix A(3x3) using matrix multiiplication due to how matrix 
% multiplication is calculated.

result_5 = b' * B % Works

result_6 = a' * b % Works

result_7 = a * b' % Works

result_8 = a .* b % Works

result_9 = A .* B % Works

