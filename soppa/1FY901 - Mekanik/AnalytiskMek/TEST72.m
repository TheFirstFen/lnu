% Parametrar
g = 9.81;         % Tyngdacceleration (m/s^2)
l = 1.0;          % Pendellängd (meter)
a = 0.1;          % Amplitud för oscillationer i upphängningspunkt
v = ((1 / (2 * pi)) * sqrt(g / l)) * 10;          % Frekvensen hos de vertikala oscillationerna av upphängningspunkten

% Tidsintervall
tspan = [0 100];

% Initiala villkor för utslagsvinkel och vinkelhastighet
initial_p = pi;   % Justera utslagsvinkeln här
initial_dpdt = 0;  % Justera vinkelhastigheten här
y0 = [initial_p; initial_dpdt];

% Lösningsberäkningar med ode45
[t, y] = ode45(@(t, y) TEST71(t, y, g, l, a, v), tspan, y0);

% Plotta utslagsvinkeln över tid
figure;
plot(t, wrapToPi(y(:,1)), 'b');
xlabel('Tid (s)');
ylabel('Utslagsvinkel (p)');
title('Utslagsvinkel för pendeln');