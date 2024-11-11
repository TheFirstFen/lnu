function pendulum_simulation_ode45()
    % Parametrar
    g = 9.81; % Tyngdacceleration (m/s^2)
    l = 1;    % Pendelns längd (m)

    % Differentialekvation för pendeln
    pendulum_equation = @(t, y) [y(2); (-g / l) * sin(y(1))];

    % Initialvärden
    initial_conditions = [pi / 4, 0]; % Startvinkel (45 grader), inledande vinkelhastighet

    % Simuleringsintervall
    tspan = [0, 30]; % [Starttid, Sluttid]

    % Anropa ode45 för att lösa differentialekvationen
    [time, results] = ode45(pendulum_equation, tspan, initial_conditions);

    % Extrahera vinklar från resultaten
    angles = results(:, 1);

    % Analytisk lösning
    analytic_angles = initial_conditions(1) * cos(sqrt(g / l) * time);

    % Plotta resultatet
    figure;
    plot(time, angles, 'b', time, analytic_angles, 'r--');
    xlabel('Tid (s)');
    ylabel('Vinkel (rad)');
    title('Pendel utan drivning');
    legend('Numerisk lösning', 'Analytisk lösning');
end
