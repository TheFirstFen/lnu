% Parametrar
l = 1.0; % Pendelns längd
g = 9.81; % Tyngdaccelerationen
a = 0.1; % Drivningsamplitud
nu_resonance = sqrt(g / l); % Resonansfrekvens

% Differentialekvationssystem för resonansfrekvens
ode_resonance = @(t, y) [y(2); (-g/l) * sin(y(1)) + a^2 * nu_resonance^2 * cos(nu_resonance * t) * sin(y(1))];

% Tidssteg
dt = 0.01;
t = 0:dt:20; % Tidsintervall

% Initialvärden
phi0 = 0.1; % Initial vinkel
phi_dot0 = 0; % Initial vinkelhastighet

% Lös differentialekvationssystemet numeriskt för resonansfrekvens
[t_resonance, y_resonance] = ode45(ode_resonance, t, [phi0, phi_dot0]);

% Plotta resultatet
subplot(2, 1, 1)
plot(t_resonance, y_resonance(:, 1))
xlabel('Tid (s)')
ylabel('Vinkel (rad)')
title('Pendelns rörelse med vertikal drivning på resonansfrekvensen')
grid on

subplot(2, 1, 2)
plot(t_resonance, a * cos(nu_resonance * t_resonance))
xlabel('Tid (s)')
ylabel('Amplitud')
title('Vertikal drivningsamplitud')
grid on

sgtitle('Pendelns rörelse med vertikal drivning på resonansfrekvensen')
