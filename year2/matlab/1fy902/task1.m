U = [15.98 15.51 15.43 15.35 15.23 15.06 14.82 14.43 13.72 11.94 0];
I = [0 0.34 0.38 0.43 0.50 0.60 0.73 0.95 1.36 2.38 9.14];
I = I *10^-3;

Rx = 1725;
Ux = linspace(0, 15.98, 100);
Ix = (-1/Rx) * Ux + (15.98/Rx);

plot(U, I, '-r', 'LineWidth', 1.0);
hold on;
plot(Ux, Ix, '-b', 'LineWidth', 1.0);

xlabel('Volt (V)');
ylabel('Ström (A)');
hold off;
legend('Mätdata', 'Rxfunc');
