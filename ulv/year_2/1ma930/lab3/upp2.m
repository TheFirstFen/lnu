format long

clc

%% A
H = hilb(7);
b = 10* ones(7,1);

%% B
x = H\b
xexact = invhilb(7)*b

%% C
norm(b, 'inf')
max(b)
cond(H, 'inf')