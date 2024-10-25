f = [500 1000 2000 4600 4800 5000 5200 5400 10000 20000 40000];

dtms = [500 200 75 2 0 -2 -4 -5 -13 -10 -6];

dt = dtms.*10^-6;

T = 1./f;

fi = dt./T.*360

C = 10^-6;
L = 10^-3;
R = 18;
w = 2*pi*f;
RL = 10.3;

X_L = 2 * pi * f * L;
X_C = 1./ (2 * pi * f * C);

dtTeori = (1./(2*pi*f)) .*atan((X_L - X_C) / (R + RL));
fiTeori = -dtTeori./T.*360;


semilogx(f, fi, '.b');
hold on
semilogx(f, fiTeori, '-r');
hold off;
xlabel('angel');
ylabel('Frequency');
legend('Experimental','Teoretical');
