plot3([0, u(1)], [0, u(2)], [0, u(3)], 'b', 'LineWidth', 2);
hold on;
plot3(u(1), u(2), u(3), 'bo', 'MarkerSize', 8); 

plot3([0, v(1)], [0, v(2)], [0, v(3)], 'g', 'LineWidth', 2);
plot3(v(1), v(2), v(3), 'g*', 'MarkerSize', 8);


plot3([0, w(1)], [0, w(2)], [0, w(3)], 'r', 'LineWidth', 2);
plot3(w(1), w(2), w(3), 'rs', 'MarkerSize', 8);


grid on;
axis equal;
title('Plott av vektorer');

X_cordinates = [P1(1); P2(1); P3(1); P4(1)];
Y_cordinates = [P1(2); P2(2); P3(2); P4(2)];
Z_cordinates = [P1(3); P2(3); P3(3); P4(3)];

fill3(X_cordinates, Y_cordinates, Z_cordinates, 'b', 'FaceAlpha', 0.4)
grid on;
axis equal;
title('Plan')