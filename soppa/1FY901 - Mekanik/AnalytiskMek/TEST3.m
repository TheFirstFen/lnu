function pendulum_with_high_frequency_driving()
    % Parametrar
    g = 9.81; % Tyngdacceleration (m/s^2)
    l = 1;    % Pendelns längd (m)
    a = 0.1;  % Amplitud för den vertikala drivningen (m)
    omega = (1 / (2 * pi)) * sqrt(g / l) * 10; % Pendlens egenfrekvens (rad/s)
    % Hög frekvens för den vertikala drivningen

    % Differentialekvation för pendeln med långsam vertikal drivning
    pendulum_equation_with_high_frequency_driving = @(t, phi) [phi(2); ...
        - (g + a * omega^2 * cos(omega * t)) * sin(phi(1)) / l];

    % Initialvärden
    initial_conditions = [pi / 4, 0]; % Startvinkel (180 grader), inledande vinkelhastighet

    % Simuleringsintervall
    tspan = [0, 100]; % [Starttid, Sluttid]

    % Anropa ode45 för att lösa differentialekvationen
    [time, results] = ode45(pendulum_equation_with_high_frequency_driving, tspan, initial_conditions);

    % Extrahera vinklar från resultaten
    angles = results(:, 1);

    % Plotta resultatet
    figure;
    plot(time, angles); % Använder wrapToPi för att säkerställa att vinklarna är i intervallet -pi till pi
    xlabel('Tid (s)');
    ylabel('Vinkel (rad)');
    title('Pendel med snabb vertikal drivning)');
end
