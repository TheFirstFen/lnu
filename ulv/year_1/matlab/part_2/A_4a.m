load('batman.mat')
p = [1 0; 0 -1];
T = p * B;
plot(T(1, :), T(2, :), 'k.','MarkerSize', 1)