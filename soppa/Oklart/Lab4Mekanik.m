f = [500 1000 2000 4600 4800 5000 5200 5400 10000 15000 20000 30000 40000 50000];

u2 = [0.056 0.11 0.24 0.60 0.65 0.70 0.65 0.60 0.34 0.20 0.15 0.10 0.08 0.06];

u1 = 1;
C = 10^-6;
L = 10^-3;
R = 18;
w = 2 * pi * f;
Rl = 11.3;


u2calc = (u1 * R) ./ sqrt(R^2 + (w * L - 1 ./ (w * C)).^2);
u2calcWithRl = (u1 * R) ./ sqrt((R + Rl)^2 + (w * L - 1 ./ (w * C)).^2);


y = u2./1;


semilogx(f, u2calc, '-b')
hold on;
semilogx(f, u2calcWithRl, '-g');
hold on;
semilogx(f, y, '.r');
xlabel('Frequency (Hz)');
ylabel('u(V)');
legend('Theoretical', 'Theoretical(with Rl)', 'Experimental');
hold off;


