load('batman.mat')
a = [cos(2*pi/3) -sin(2*pi/3); sin(2*pi/3) cos(2*pi/3)];
T = a * B;
plot(T(1, :), T(2, :), 'k.','MarkerSize', 1)