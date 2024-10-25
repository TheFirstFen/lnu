% 1

% Parametrar
g = 9.81;   % Tyngdacceleration (m/s^2)
l = 1.0;    % Pendellängd (m)
 
% Definition av differentialekvationen utan drivning
ode = @(t, y) [y(2); (-g/l)*sin(y(1))];

% Tidsintervall för lösningen
dt = 0.01;
t = 0:dt:10;

%tspan = [0 10]; % Tidsintervall att lösa ekvationen över
%y0 = [0; 0]; % Startvärden för vinkel och vinkelhastighet
 

% Initialvärden
phi0 = 0.1; % Initial vinkel
phi_dot0 = 0; % Initial vinkelhastighet

% Lös differentialekvationen numeriskt med ode45
%[t, y] = ode45(ode, tspan, y0);
[t, y] = ode45(ode, t, [phi0, phi_dot0]);

% Analytisk lösning för pendel utan drivning
% analytisk = y0(1)*cos(sqrt(g/l)*t);
 
% Plotta resultatet
plot(t, y(:, 1))
xlabel('Tid (s)')
ylabel('Vinkel (rad)')
title('Pendelns rörelse utan drivning')
grid on

% 2
% a) Långsam drivning, dvs då ν är lågt. Vad menas med "lågt" i detta sammanhang?

% Parametrar
l = 1.0; % Pendelns längd
a = 0.1; % Drivningsamplituden
g = 9.81; % Tyngdaccelerationen
nu = 0.1; % Låg frekvens för långsam drivning

% Definition av differentialekvationen med drivning
ode = @(t, y) [y(2); a*cos(nu*t) - g/l*sin(y(1))];

% Tidsintervall
tspan = [0 10]; % Tidsintervall att lösa ekvationen över
y0 = [0; 0]; % Startvärden för vinkel och vinkelhastighet

% Lösa diferentialekvationen
[t, y] = ode45(ode, tspan, y0);

% Plot av pendelns vinkel över tiden
figure;
plot(t, y(:, 1));
xlabel('Tid');
ylabel('Vinkel');
title('Pendelns vinkel över tiden (långsam drivning)');

% b) Drivning på resonansfrekvens

% Parametrar
l = 1.0; % Pendelns längd
a = 0.1; % Drivningsamplituden
g = 9.81; % Tyngdaccelerationen
omega0 = sqrt(g/l); % Pendelns egenfrekvens (resonansfrekvens)

% Definition av differentialekvationen med vertikal drivning på resonansfrekvensen
ode = @(t, y) [y(2); a*cos(omega0*t) - g/l*sin(y(1))];

% Tidsintervall
tspan = [0 10]; % Tidsintervall att lösa ekvationen över
y0 = [0; 0]; % Startvärden för vinkel och vinkelhastighet

% Lösa diferentialekvationen
[t, y] = ode45(ode, tspan, y0);

% Plot av pendelns vinkel över tiden
figure;
plot(t, y(:, 1));
xlabel('Tid');
ylabel('Vinkel');
title('Pendelns vinkel över tiden (drivning på resonansfrekvensen)');

% c) Snabb drivning, dvs d˚a ν ¨ar h¨ogt. Vad menas med ”h¨ogt” i detta sammanhang?

% Parametrar
l = 1.0; % Pendelns längd
a = 0.1; % Drivningsamplituden
nu = 10; % Frekvensen för snabb drivning
g = 9.81; % Tyngdaccelerationen

% Definition av differentialekvationen med snabb drivning
ode = @(t, y) [y(2); (a*cos(nu*t) - g/l*sin(y(1)))];

% Tidsintervall och initialvärden
tspan = [0 10]; % Tidsintervall att lösa ekvationen över
y0 = [0; 0]; % Startvärden för vinkel och vinkelhastighet

% Lösa differentialekvationen
[t, y] = ode45(ode, tspan, y0);

% Plot av pendelns vinkel över tiden
figure;
plot(t, y(:, 1));
xlabel('Tid');
ylabel('Vinkel');
title('Pendelns vinkel över tiden (snabb drivning)');

% d) Vid snabb drivning, sl¨app pendeln n¨ara ϕ = π. Vad h¨ander?

% Parametrar
l = 1.0; % Pendelns längd
a = 0.1; % Drivningsamplituden
g = 9.81; % Tyngdaccelerationen

% Definition av differentialekvationen med snabb drivning
ode = @(t, y) [y(2); (a*cos(y(1)) - g/l*sin(y(1)))];

% Tidsintervall och initialvärden
tspan = [0 10]; % Tidsintervall att lösa ekvationen över
y0 = [pi-0.01; 0]; % Startvärden för vinkel och vinkelhastighet

% Lösa differentialekvationen
[t, y] = ode45(ode, tspan, y0);

% Plot av pendelns vinkel över tiden
figure;
plot(t, y(:, 1));
xlabel('Tid');
ylabel('Vinkel');
title('Pendelns vinkel över tiden (snabb drivning ϕ nära π.)');
