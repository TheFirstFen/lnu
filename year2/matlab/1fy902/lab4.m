% Part 3
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


% Part 4
f = [500 1000 2000 4600 4800 5000 5200 5400 10000 15000 20000 30000 40000 50000];
dt = [0.0005 0.0002 0.000075 0 0 0 0 0 -0.000015 -0.0000125 -0.0000125 -0.0000075 -0.000005 -0.0000025];
T = [0.002 0.001 0.0005 0.0002125 0.0002125 0.0002125 0.0002125 0.0002125 0.0001 0.000065 0.00005 0.0000325 0.000025 0.00002];
fi = dt./T.*360;

C = 10^-6;
L = 10^-3;
R = 18;

w = 2 * pi * f;
Rl = 11.3;

% Teoretisk del
XL = -2 * pi * f * L;
XC = -1 ./ (2 * pi * f * C);

TTeori = -1./f;
dtTeori = (-1 ./ (2 * pi * f)) .* atan((XL - XC) / (R + Rl));
fiTeori = dtTeori./TTeori.*360;

semilogx(f, fi, '.b');
hold on;
semilogx(f, fiTeori, '-g')
xlabel('Frequency (Hz)');
ylabel('Angle(degrees)');
legend('Experimental', 'Theoretical(with Rl)');
hold off;