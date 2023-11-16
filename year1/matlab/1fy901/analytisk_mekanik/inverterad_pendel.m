% Konstanter
l = 1.0; % Pendelns längd
g = 9.81; % Tyngdaccelerationen
tspan = [0 30]; % Tidsintervall
y0 = [pi/2; 0]; % Startvärden för vinkel och vinkelhastighet

% 1.

a = 0; % Amplituden
f = 0; % Frekvensen

% Lösa differentialekvationen
ode = @(t, y) [y(2); -g/l*sin(y(1)) - (a*f^2)/l*sin(y(1))*cos(f*t)];
[t, y] = ode45(ode, tspan, y0);

% Analytisk lösning för pendeln utan drivning
analytical = y0(1)*cos(sqrt(g/l)*t);

% Plot
figure;
plot(t, y(:, 1), 'b', t, analytical, 'r');
xlabel('t[s]');
ylabel('θ(t)[rad]');
title('Pendelns vinkel över tid(utan drivning)');
legend('Laborativ lösning', 'Analytisk lösning');
grid on;

% 2.

% a) Långsam drivning, dvs då ν är lågt. Vad menas med "lågt" i detta sammanhang?

a = 0.1; % Amplituden
f = 0.3; % Frekvens

% Lösa differentialekvationen
ode = @(t, y) [y(2); -g/l*sin(y(1)) - (a*f^2)/l*sin(y(1))*cos(f*t)];
[t, y] = ode45(ode, tspan, y0);

% Plot
figure;
plot(t, y(:, 1));
xlabel('t[s]');
ylabel('θ(t)[rad]');
title('Pendelns vinkel över tid(långsam drivning)');
grid on;

% b) Drivning på resonansfrekvensen.

a = 0.1; % Amplituden
f = 1/(2*pi)*sqrt(g/l); % Frekvensen
tspan = [0 300]; % Tidsintervall

% Lösa differentialekvationen
ode = @(t, y) [y(2); -g/l*sin(y(1)) - (a*f^2)/l*sin(y(1))*cos(f*t)];
[t, y] = ode45(ode, tspan, y0);

% Plot
figure;
plot(t, y(:, 1));
xlabel('t[s]');
ylabel('θ(t)[rad]');
title('Pendelns vinkel över tid(resonansfrekvens drivning)');
grid on;

% c) Snabb drivning, dvs då ν är högt. Vad menas med "högt" i detta sammanhang?

a = 0.1; % Amplituden
f = 30; % Frekvensen
tspan = [0 30]; % Tidsintervall

% Lösa differentialekvationen
ode = @(t, y) [y(2); -g/l*sin(y(1)) - (a*f^2)/l*sin(y(1))*cos(f*t)];
[t, y] = ode45(ode, tspan, y0);

% Plot
figure;
plot(t, y(:, 1));
xlabel('t[s]');
ylabel('θ(t)[rad]');
title('Pendelns vinkel över tid(snabb drivning)');
grid on;

% d) Vid snabb drivning, släpp pendeln nära φ = π. Vad händer?

a = 0.1; % Amplituden
f = 5; % Frekvensen
tspan = [0 500]; % Tidsintervall
y0 = [pi; 0]; % Startvärden för vinkel och vinkelhastighet

% Lösa differentialekvationen
ode = @(t, y) [y(2); -g/l*sin(y(1)) - (a*f^2)/l*sin(y(1))*cos(f*t)];
[t, y] = ode45(ode, tspan, y0);

% Plot
figure;
plot(t, y(:, 1));
xlabel('t[s]');
ylabel('θ(t)[rad]');
title('Pendelns vinkel över tid(snabb drivning & startvinkel pi)');
grid on;