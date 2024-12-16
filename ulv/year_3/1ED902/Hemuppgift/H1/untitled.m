clc
clear

syms x1 x2 u

f1 = x2;
f2 = -(x2^6 / x1^2 - x1 - sqrt(u+1));
x = [x1; x2];
A = jacobian([f1, f2], x);
B = jacobian([f1, f2], u);
C = jacobian(x1^3 + u^2, x);
D = jacobian(x1^3 + u^2, u);

equilibrium_x = [-3;0];
equilibrium_u = 8;

A_eq = double(subs(A, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));
B_eq = double(subs(B, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));
C_eq = double(subs(C, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));
D_eq = double(subs(D, {x1, x2, u}, {equilibrium_x(1), equilibrium_x(2), equilibrium_u}));

disp(A_eq)
disp(B_eq)
disp(C_eq)
disp(D_eq)


% Define the initial house as a matrix of 2D points
house = [
    0, 0;  % Bottom-left
    2, 0;  % Bottom-right
    2, 3;  % Top-right
    1, 4;  % Roof peak
    0, 3;  % Top-left
    0, 0   % Back to bottom-left to close the shape
];

% Transformation parameters
rotation_angle = 45; % in degrees
translation_vector = [3, 1]; % Translation along x and y

% Define the rotation matrix
theta = deg2rad(rotation_angle); % Convert degrees to radians
rotation_matrix = [
    cos(theta), -sin(theta);
    sin(theta),  cos(theta)
];

% Apply translation and rotation transformations
translated_house = house + translation_vector; % Translate the house
transformed_house = (rotation_matrix * translated_house')'; % Rotate the translated house

% Plot the original and transformed house
figure;
hold on;
axis equal;
grid on;

% Plot the original house
plot(house(:, 1), house(:, 2), '--o', 'DisplayName', 'Original House');

% Plot the transformed house
plot(transformed_house(:, 1), transformed_house(:, 2), '-o', 'DisplayName', 'Transformed House');

% Add labels and legend
title('House Transformation: Rotation + Translation');
xlabel('X');
ylabel('Y');
legend;
