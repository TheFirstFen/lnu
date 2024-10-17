% Parametrar
l = 1.0; % Pendelns längd
g = 9.81; % Tyngdaccelerationen
a = 0.1; % Drivningsamplitud
nu_low = 0.1; % Låg frekvens

% Differentialekvationssystem för låg frekvens
ode_low = @(t, y) [y(2); (-g/l) * sin(y(1)) + a^2 * nu_low^2 * cos(nu_low * t) * sin(y(1))];

% Tidssteg
dt = 0.01;
t = 0:dt:20; % Tidsintervall

% Initialvärden
phi0 = 0.1; % Initial vinkel
phi_dot0 = 0; % Initial vinkelhastighet

% Lös differentialekvationssystemet numeriskt för låg frekvens
[t_low, y_low] = ode45(ode_low, t, [phi0, phi_dot0]);

% Plotta resultatet
subplot(2, 1, 1)
plot(t_low, y_low(:, 1))
xlabel('Tid (s)')
ylabel('Vinkel (rad)')
title('Pendelns rörelse med långsam drivning')
grid on

subplot(2, 1, 2)
plot(t_low, a * sin(nu_low * t_low))
xlabel('Tid (s)')
ylabel('Amplitud')
title('Vertikal drivningsamplitud')
grid on

sgtitle('Pendelns rörelse med långsam vertikal drivning')
