f= [500 1000 2000 4600 4800 5000 5200 5400 10000 20000 40000];

u2 = [0.06 0.1125 0.225 0.60 0.65 0.68 0.65 0.60 0.325 0.1563 0.078];

u1 = 1;

C = 10^-6;
L = 10^-3;
R = 18;
w = 2*pi*f;
RL = 10.3;

u2calc = (u1 * R) ./ sqrt(R^2 + (w * L - 1 ./ (w * C)).^2);
u2withRL = (u1 * R) ./ sqrt((R + RL)^2 + (w * L - 1 ./ (w * C)).^2);

y = u2./u1;


semilogx(f, u2calc, '-b');
hold on
semilogx(f, u2withRL, '-g');
hold on
semilogx(f, y, '*r');
xlabel('Frequency');
ylabel('u(V)');
legend('U with out RL', 'U with RL', 'U2/U1')

