% Task 8
theta = linspace(0, 2*pi, 50);
phi = linspace(0, pi, 50);

[Theta, Phi] = meshgrid(theta, phi);

X = cos(Theta) .* sin(Phi);
Y = sin(Theta) .* sin(Phi);
Z = cos(Phi);

X = 6 * X;
Y = 6 * Y;
Z = 6 * Z;

X = X - 2;
Y = Y + 1;
Z = Z + 3;

figure;
surf(X, Y, Z);

axis equal;

