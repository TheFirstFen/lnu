% Parametrar
g = 9.81;         % Tyngdacceleration (m/s^2)
l = 1.0;          % Pendellängd (meter)
a = 0.1;          % Amplitud för oscillationer i upphängningspunkt

v = (1 / (2 * pi)) * sqrt(g / l) * 10;


% Funktion för given ekvation


% Tidsintervall
tspan = [0 2000];

% Initiala villkor för utslagsvinkel och vinkelhastighet
initial_p = pi;   % Justera utslagsvinkeln här
initial_dpdt = 0;  % Justera vinkelhastigheten här
y0 = [initial_p; initial_dpdt];

% Lösningsberäkningar med ode45

[t1, y1] = ode45(@(t, y) TEST71(t, y, g, l, a, v), tspan, y0);


% Plotta utslagsvinkeln över tid
figure;
plot( t1, wrapToPi(y1(:,1)), 'b');
xlabel('Tid (s)');
ylabel('Vinkel (rad)');
title('Pendelns rörelse med snabb vertikal drivning, Startvinkel=pi');

