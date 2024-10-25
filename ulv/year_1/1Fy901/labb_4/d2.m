% Parametrar
l = 1.0; % Pendelns längd
g = 9.81; % Tyngdaccelerationen
a = 0.1; % Drivningsamplitud
nu_high = 10; % Hög frekvens

% Differentialekvationssystem för hög frekvens
ode_high = @(t, y) [y(2); (-g/l) * sin(y(1)) + a^2 * nu_high^2 * cos(nu_high * t) * sin(y(1))];

% Tidssteg
dt = 0.001;
t = 0:dt:10; % Tidsintervall

% Initialvärden
phi0 = pi - 0.01; % Nära ϕ = π
phi_dot0 = 0; % Initial vinkelhastighet

% Lös differentialekvationssystemet numeriskt för hög frekvens
[t_high, y_high] = ode45(ode_high, t, [phi0, phi_dot0]);

% Plotta resultatet
subplot(2, 1, 1)
plot(t_high, y_high(:, 1))
xlabel('Tid (s)')
ylabel('Vinkel (rad)')
title('Pendelns rörelse vid snabb drivning nära ϕ = π')
grid on

subplot(2, 1, 2)
plot(t_high, a * sin(nu_high * t_high))
xlabel('Tid (s)')
ylabel('Amplitud')
title('Vertikal drivningsamplitud')
grid on

sgtitle('Pendelns rörelse vid snabb drivning nära ϕ = π')
