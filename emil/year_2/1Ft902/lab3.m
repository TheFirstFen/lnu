v = [0 10 20 30 40 50 60 70 80];
vneg = [-80 -70 -60 -50 -40 -30 -20 -10 0];


i = [0 3.0 8.6 15.6 24.9 36.2 52.1 87.2 180];
ineg = [-220 -98.1 -58.7 -41.8 -29.1 -20.7 -14.1 -6.4 0];

i2 = i ./ 1000;
ineg2 = ineg ./ 1000;


vtot = [vneg, v];
itot = [ineg2, i2];


x = tan(vtot);
const = (4 * pi * 10^(-7) * 154) / (2 * 0.20);
y = const * itot(1, :);


mdl = fitlm(x, y);
disp(mdl);


plot(v, i2, 'r.', 'DisplayName', 'Positiva mÃ¤tvÃ¤rde');
hold on
plot(vneg, ineg2, 'b.', 'DisplayName', 'Negativa mÃ¤tvÃ¤rden');

xlabel('Vinkel');
ylabel('StrÃ¶m(A)');

x_range = linspace(min(vtot), max(vtot), 100);
y_range = predict(mdl, x_range');
plot(x_range, y_range, 'k-', 'DisplayName', 'LinjÃ¤r regressionsmodell');

legend('Location', 'best');