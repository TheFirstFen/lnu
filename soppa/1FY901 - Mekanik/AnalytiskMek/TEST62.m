% Ange värden för de konstanta parametrarna
g = 9.81;   % Tyngdaccelerationen
l = 1.0;    % Pendelns längd
a = 0.1;    % Amplituden för oscillationerna i upphängningspunkten
v = 1.0;    % Frekvensen hos de vertikala oscillationerna av upphängningspunkten

% Ange initiala villkor
p0 = 0.1;   % Initial utslagsvinkel i radianer
dp0dt = 0;  % Initialt derivata dp/dt

% Skapa en tidsvektor
tspan = [0 10];  % Tidsintervall för simuleringen

% Anropa ode45 för att lösa differentialekvationen
[t, y] = ode45(@(t, y) TEST61(t, y, g, l, a, v), tspan, [p0; dp0dt]);

% Plotta resultatet
plot(t, y(:, 1))
xlabel('Tid (s)')
ylabel('Utslagsvinkel (rad)')
title('Pendelns rörelse')