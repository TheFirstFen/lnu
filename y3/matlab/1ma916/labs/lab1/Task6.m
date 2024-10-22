% Define the matrices and vectors
clc
clear
A = [1 0 3; 0 4 5; 1 2 -1];
B = [1 3 1; 2 2 2; 3 1 3];
a = [2; 3; 0];
b = [1; 1; 1];

% Calculations
AB = A * B;
Aa = A * a;
% BbT = B * b.';     % Error
% aA = a * A;        % Error
bTB = b.' * B;
aTb = a.' * b;
abT = a * b.';
adotb = a .* b;
A_dot_B = A .* B;

% Comments:
