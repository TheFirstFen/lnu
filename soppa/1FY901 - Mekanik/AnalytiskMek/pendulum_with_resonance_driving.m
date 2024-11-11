function pendulum_with_resonance_driving()
    % Parametrar
    g = 9.81; % Tyngdacceleration (m/s^2)
    l = 1;    % Pendelns längd (m)
    a = 0.1;  % Amplitud för den vertikala drivningen (m)
    w = (1 / (2 * pi)) * sqrt(g / l); % Pendlens egenfrekvens (rad/s)
    v = (1 / (2 * pi)) * sqrt(g / l);    % Frekvens för den vertikala drivningen (resonansfrekvensen)

    % Differentialekvation för pendeln med långsam vertikal drivning
    pendulum_equation_with_resonance_driving = @(t, y) [y(2); ...
        - (g / l) * sin(y(1)) - a * w^2 * cos(w*t) * sin(y(1)) - a * v^2 * cos(v*t)];

    % Initialvärden
    initial_conditions = [pi / 4, 0]; % Startvinkel (45 grader), inledande vinkelhastighet

    % Simuleringsintervall
    tspan = [0, 100]; % [Starttid, Sluttid]

    % Anropa ode45 för att lösa differentialekvationen
    [time, results] = ode45(pendulum_equation_with_resonance_driving, tspan, initial_conditions);

    % Extrahera vinklar från resultaten
    angles = results(:, 1);

    % Plotta resultatet
    figure;
    plot(time, angles);
    xlabel('Tid (s)');
    ylabel('Vinkel (rad)');
    title('Pendel med drivning på resonansfrekvensen');
end
