%A
u = [3, 3,-1]
v = [2, 4,-1]
w = cross(u,v)

% equation of plane
% x + y + 6z = 0
% P1 = (6, 6, -2)
% P2 = (6, -6, 0)
% P3 = (-6, -6, 2)
% P4 = (-6, 6, 0)
%B
origin = [0,0,0];
plot3([origin(1) u(1)], [origin(2) u(2)], [origin(3) u(3)], 'o', ...
    [origin(1) v(1)], [origin(2) v(2)], [origin(3) v(3)], '-diamond', ...
    [origin(1) w(1)], [origin(2) w(2)], [origin(3) w(3)], '-square', 'MarkerSize', 10)
grid on
xlabel('x'), ylabel('y'), zlabel('z')

%C
X = [6; 6; -6; -6]
Y = [6; -6; -6; 6]
Z = [-2; 0; 2; 0]
fill3(X, Y, Z, 'r', 'facealpha', 0.4)
grid on


