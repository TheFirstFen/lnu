function pendulum_with_slow_driving_updated()
    % Parametrar
    g = 9.81; % Tyngdacceleration (m/s^2)
    l = 1;    % Pendelns längd (m)
    a = 0.1;  % Amplitud för den vertikala drivningen (m)
    v = ((1 / (2 * pi)) * sqrt(g / l)) * 10;  % Frekvens för den vertikala drivningen (rad/s)

    % Differentialekvation för pendeln med långsam vertikal drivning inklusive v
    pendulum_equation_with_slow_driving_updated = @(t, y) [y(2); ...
        - (g / l) * sin(y(1)) - a * sin(v * t) - (y(2)^2) * sin(y(1)) * cos(y(1))];

    % Initialvärden
    initial_conditions = [pi, 0]; % Startvinkel (45 grader), inledande vinkelhastighet

    % Simuleringsintervall
    tspan = [0, 50]; % [Starttid, Sluttid]

    % Anropa ode45 för att lösa differentialekvationen
    [time, results] = ode45(pendulum_equation_with_slow_driving_updated, tspan, initial_conditions);

    % Extrahera vinklar från resultaten
    angles = results(:, 1);

    % Plotta resultatet
    figure;
    plot(time, wrapToPi(angles));
    xlabel('Tid (s)');
    ylabel('Vinkel (rad)');
    title('Pendelns rörelse med långsam drivning inklusive v');
end
