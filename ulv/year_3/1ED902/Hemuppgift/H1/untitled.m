clc

syms x1 x2 u

f1 = x2;
f2 = -(x2^6 / x1^2 - x1 - sqrt(u+1));
x = [x1; x2];
A = jacobian([f1, f2], x);
B = jacobian([f1, f2], u);
C = jacobian(x1^3 + u^2, x);
D = jacobian(x1^3 + u^2, u);

equilibrium_x = [-3;0];
equilibrium_u = 8;

A_eq = double(subs(A, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));
B_eq = double(subs(B, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));
C_eq = double(subs(C, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));
D_eq = double(subs(D, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));

disp(A_eq)
disp(B_eq)
disp(C_eq)
disp(D_eq)

