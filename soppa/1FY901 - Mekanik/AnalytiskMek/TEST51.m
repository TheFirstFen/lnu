% Parametrar
g = 9.81;         % Tyngdacceleration (m/s^2)
l = 1.0;          % Pendellängd (meter)
a = 0.1;          % Amplitud för oscillationer i upphängningspunkt
omega = (1 / (2 * pi)) * sqrt(g / l);      % Egenfrekvens för pendeln (rad/s)

% Funktion för Lagrange-ekvationen
lagrange_eq = @(t, y) [y(2); -g/l*sin(y(1))];

% Funktion för given ekvation
given_eq = @(t, y) [y(2); -(g + a*omega^2*cos(omega*t))*sin(y(1))/l];

% Tidsintervall
tspan = [0 100];

% Initiala villkor för utslagsvinkel och vinkelhastighet
initial_p = pi / 4;   % Justera utslagsvinkeln här
initial_dpdt = 0;  % Justera vinkelhastigheten här
y0 = [initial_p; initial_dpdt];

% Lösningsberäkningar med ode45
[t_lagrange, y_lagrange] = ode45(lagrange_eq, tspan, y0);
[t_given, y_given] = ode45(given_eq, tspan, y0);

% Plotta utslagsvinkeln över tid
figure;
plot(t_lagrange, y_lagrange(:,1), 'b', t_given, y_given(:,1), '--r');
xlabel('Tid (s)');
ylabel('Utslagsvinkel (p)');
title('Utslagsvinkel för Lagrange och Given ekvation');

legend('Lagrange', 'Given ekvation');
