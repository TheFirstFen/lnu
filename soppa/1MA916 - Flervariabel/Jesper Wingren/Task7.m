% Task 7
figure(1) % create or activate a figure with number 1
clf % clear the figure
hold on % the following plots will be superposed in the same figure
grid on % visible grid lines
x = -2 : 0.1 : 2; % plotting intervall in x-direction
y = -2 : 0.1 : 2; % plotting intervall in y-direction
[X, Y ] = meshgrid(x, y); % create a mesh of (x, y)-coordinate points in the xy-plane
Z = -X - Y;% define a z-value for each (x, y)-coordinate
Z1 = -X - Y - 2; % different z-value for second plane
surf(X, Y, Z) % plots a surface
surf(X, Y, Z1) % plots a second paralel surface
view(35, 35) % choose the viewing angle
% can be changed with the rotation arrow in the figure
hold off % inactivate the figure