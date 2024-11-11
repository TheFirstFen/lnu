v = [0 10 20 30 40 50 60 70 80];
vneg = [-80 -70 -60 -50 -40 -30 -20 -10];

i = [0 3.0 8.6 15.6 24.9 36.2 52.1 87.2 180];
i2 = i./1000;
ineg = [-220 -98.1 -58.7 -41.8 -29.1 -20.7 -14.1 -6.4];
ineg2 = ineg./1000;

vtot = [vneg, v];
itot = [ineg2, i2];
vtotRad = deg2rad(vtot);

% Initialize x with the correct dimensions
x = zeros(1, length(vtot));

for i = 1 : length(vtotRad)
    xi = tan(vtotRad(i));
    x(1, i) = xi;
end

disp(x)

y = ((4 * pi * 10^(-7)) * itot(1, :) * 154)/(2 * 0.20);

mdl = fitlm(x, y);
disp(mdl);


plot(v, i2, 'r.', 'DisplayName', 'Positiva mätvärde');
hold on
plot(vneg, ineg2, 'b.', 'DisplayName', 'Negativa mätvärden');
xlabel('Angle');
ylabel('Current(A)');

figure;
x_range = linspace(min(x), max(x), 100);
y_range = predict(mdl, x_range');
plot(x_range, y_range, 'k-', 'DisplayName', 'Linear regressionmodel');
legend('Location', 'best');
xlabel('tan(θ)')
ylabel('Be')


1.6748 * 10^(-5) / cos(deg2rad(70))