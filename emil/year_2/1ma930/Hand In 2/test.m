clc

A = [
 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0
 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0
 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0
 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0
 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0
 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0
 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0
 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1
 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0];
q = 0.15;

% Calculate the size of matrix A
[rows, cols] = size(A);

% Initialize matrix G
G = zeros(rows, cols);

% Calculate G matrix
for i = 1:rows
    % Calculate ni (sum of row i)
    ni = sum(A(i, :));
    for j = 1:cols
        % Calculate Gij using the provided formula
        G(i, j) = q/15 + (1 - q) * A(i, j) / ni;
    end
end

% Display the result
disp('Matrix G:');
disp(G);

