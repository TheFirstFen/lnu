load('batman.mat')
a = [-1 0; 0 1];
c = [cos(pi/3) -sin(pi/3); sin(pi/3) cos(pi/3)];
r = c * B;
R = a * r;
plot(R(1, :), R(2, :), 'k.','MarkerSize', 1)
