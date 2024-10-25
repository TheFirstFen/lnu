clc;
clear;

A = [1 0 1; 0 4 2; 3 5 -1];
B = [1 2 3; 1 3 2; 1 2 3];
a = [2; 3; 0];
b = [1; 1; 1];

C1 = A * B;
C2 = A * a;
%C3 = B * b';    Incorrect dimensions for matrix multiplication.
%C4 = a * A;     Incorrect dimensions for matrix multiplication.
C5 = b' * B;
C6 = a' * b;
C7 = a * b';
C8 = a .* b;
C9 = A .* B;

disp('A * B ='), disp(C1)
disp('A * a ='), disp(C2)
%disp('B * b' ='), disp(C3)
%disp('a * A ='), disp(C4)
disp('b'' * B ='), disp(C5)
disp('a'' * b ='), disp(C6)
disp('a * b'' ='), disp(C7)
disp('a .* b ='), disp(C8)
disp('A .* B ='), disp(C9)