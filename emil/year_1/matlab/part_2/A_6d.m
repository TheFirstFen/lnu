u = [3, 3,-1]
v = [2, 4,-1]
w = cross(u,v)
origin = [0,0,0]
hold on
plot3([origin(1) u(1)], [origin(2) u(2)], [origin(3) u(3)], 'star', ...
    [origin(1) v(1)], [origin(2) v(2)], [origin(3) v(3)], '-diamond', ...
    [origin(1) w(1)], [origin(2) w(2)], [origin(3) w(3)], '-square', 'MarkerSize', 10)

 
X = [6; 6; -6; -6]
Y = [6; -6; -6; 6]
Z = [-2; 0; 2; 0]
fill3(X, Y, Z, 'r', 'facealpha', 0.4)
hold off
xlabel('x'), ylabel('y'), zlabel('Z')
grid on
box on
axis equal
set(gca,'fontsize',16) 
