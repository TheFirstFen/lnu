% Standard symbol

plot(B(1, :), B(2, :), 'k.','MarkerSize', 1)
%%

% Reflect in x-axis:
A = [1 0;0 -1];
C = A * B;
plot(C(1, :), C(2, :), 'k.','MarkerSize', 1)
axis equal
%%

% Counter-clockwise rotation by 120 degrees:
theta = 120*pi/180;
rot = [cos(theta) -sin(theta);sin(theta) cos(theta)];
E = rot * B;
plot(E(1, :), E(2, :), 'k.','MarkerSize', 1)
axis equal
%%

% Stretch image by 2 in x-axis:
stretch = [2 0;0 1];
G = stretch * B;
plot(G(1, :), G(2, :), 'k.','MarkerSize', 1)
axis equal
%%

% Counter-clockwise rotation by 60 degrees then reflect in y-axis:
theta = 60*pi/180;
rot = [cos(theta) -sin(theta);sin(theta) cos(theta)];
refl_y = [-1 0;0 1];
C = rot * B;
C = refl_y * C;
plot(C(1, :), C(2, :), 'k.','MarkerSize', 1)
axis equal