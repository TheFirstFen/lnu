% Parametrar
g = 9.81;         % Tyngdacceleration (m/s^2)
l = 1.0;          % Pendellängd (meter)
a = 0.1;          % Amplitud för oscillationer i upphängningspunkt

v = 0.1;




% Tidsintervall
tspan = [0 100];

% Initiala villkor för utslagsvinkel och vinkelhastighet
initial_p = pi / 4;   % Justera utslagsvinkeln här
initial_dpdt = 0;  % Justera vinkelhastigheten här
y0 = [initial_p; initial_dpdt];

% Lösningsberäkningar med ode45

[t1, y1] = ode45(@(t, y) TEST71(t, y, g, l, a, v), tspan, y0);


    angles = y1(:, 1);

    % Analytisk lösning
    analytic_angles = y0(1) * cos(sqrt(g / l) * t1);

    % Plotta resultatet
    figure;
    plot(t1, y1(:,1), 'b', t1, analytic_angles, 'r--');
    xlabel('Tid (s)');
    ylabel('Vinkel (rad)');
    title('Pendel utan drivning');
    legend('Numerisk lösning', 'Analytisk lösning');
