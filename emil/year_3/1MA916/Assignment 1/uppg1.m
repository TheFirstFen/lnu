t = 0:0.01:5;
x = 4 +t.^3;
y = 1 + 5 * 5.^2;

plot(x, y);
xlabel('X');
ylabel('Y');
title('Plot the Parametric Curve x = 4 + t^3, y = 1 + 5^2')
grid on
