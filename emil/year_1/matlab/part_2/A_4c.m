load('batman.mat')
a = [2 0; 0 1];
S = a * B;
plot(S(1, :), S(2, :), 'k.','MarkerSize', 1)