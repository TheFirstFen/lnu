% Define the matrices and vectors
A = [1 0 3; 0 4 5; 1 2 -1]; % Matrix A
B = [1 3 1; 2 2 2; 3 1 3];  % Matrix B
a = [2; 3; 0];              % Column vector a
b = [1; 1; 1];              % Column vector b

% Calculations
AB = A * B;        % Matrix multiplication A * B
Aa = A * a;        % Matrix multiplication A * a
BbT = B * b.';     % Error: Dimensions must agree
aA = a * A;        % Error: Dimensions must agree
bTB = b.' * B;     % Row vector b' multiplied by matrix B
aTb = a.' * b;     % Dot product (scalar multiplication) of a and b
abT = a * b.';     % Outer product (matrix multiplication) of a and b'
adotb = a .* b;    % Element-wise multiplication of vectors a and b
A_dot_B = A .* B;  % Element-wise multiplication of matrices A and B

% Comments:
% 1. aA = a * A; 
%    Error: Inner matrix dimensions must agree.
%    a is a (3x1) vector, and A is a (3x3) matrix.
%    To multiply, the number of columns in a must match the number of rows in A.
%    This condition is not satisfied, so the operation fails.

% 2. BbT = B * b.'; 
%    This works because B is (3x3) and b' is (1x3).
%    The resulting matrix will be (3x3).

% 3. bTB = b.' * B; 
%    This works because b' is (1x3) and B is (3x3).
%    The resulting row vector will be (1x3).

% 4. aTb = a.' * b; 
%    This is a scalar (dot product) as a.' is (1x3) and b is (3x1).

% 5. abT = a * b.'; 
%    This results in a (3x3) matrix as a is (3x1) and b' is (1x3).

% 6. adotb = a .* b; 
%    This is element-wise multiplication of vectors a and b.
%    Both a and b are (3x1), so it results in a (3x1) vector.

% 7. A_dot_B = A .* B; 
%    This is element-wise multiplication of matrices A and B.
%    Both A and B are (3x3), so it results in a (3x3) matrix.
