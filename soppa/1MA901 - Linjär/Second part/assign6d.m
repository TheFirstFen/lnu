u = [3;3;-1];
v = [2;4;-1];
w = cross(u, v);

x1 = 6;
y1 = 6;
z1 = (-x1 - y1)/6;

x2 = 6;
y2 = -6;
z2 = (-x2 - y2)/6;

x3 = -6;
y3 = -6;
z3 = (-x3 - y3)/6;

x4 = -6;
y4 = 6;
z4 = (-x4 - y4)/6;

plot3([0 u(1)],[0 u(2)],[0 u(3)], 'g', 'LineWidth', 2)
hold on
plot3([0 v(1)],[0 v(2)],[0 v(3)], 'r', 'LineWidth', 2)
plot3([0 w(1)],[0 w(2)],[0 w(3)], 'b', 'LineWidth', 2)
hold on

plot3([0 u(1)],[0 u(2)],[0 u(3)],'g-o', 'MarkerSize', 10)
plot3([0 v(1)],[0 v(2)],[0 v(3)],'r-s', 'MarkerSize', 10)
plot3([0 w(1)],[0 w(2)],[0 w(3)],'b-*', 'MarkerSize', 10)
hold on

x = [x1;x2;x3;x4];
y = [y1;y2;y3;y4];
z = [z1;z2;z3;z4];
fill3(x, y, z, 'b', 'facealpha', 0.4)
hold off

xlabel("x")
ylabel("y")
zlabel("z")
grid on
box on
set(gca,'fontsize',16)
axis equal
