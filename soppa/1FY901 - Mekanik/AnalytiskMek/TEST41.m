function inverted_pendulum_simulation()
    % Parametrar
    m = 1.0;   % Massa av pendelns ändpunkt (kg)
    g = 9.81;  % Tyngdacceleration (m/s^2)
    l = 1.0;   % Längden på pendelarmen (m)
    a = 0.1;   % Amplitud av den vertikala drivningskraften (m)
    omega = 1; % Frekvens av den vertikala drivningskraften (rad/s)

    % Initialvärden
    theta = pi / 4;         % Startvinkel (45 grader)
    theta_dot = 0;         % Startvinkelhastighet
    tspan = [0 10];         % Simuleringsintervall [Starttid, Sluttid]

    % Skapa en funktion för differentialekvationen
    pendulum_equation = @(t, y) pendulum_dynamics(t, y, m, g, l, a, omega);

    % Lösa differentialekvationen med ode45
    [time, results] = ode45(pendulum_equation, tspan, [theta, theta_dot]);

    % Extrahera vinklar från resultaten
    angles = results(:, 1);

    % Plotta resultatet
    figure;
    plot(time, angles);
    xlabel('Tid (s)');
    ylabel('Vinkel (rad)');
    title('Inverterad Pendel Simulering');
end

function dydt = pendulum_dynamics(t, y, m, g, l, a, omega)
    % State variables
    theta = y(1);
    theta_dot = y(2);

    % Rörelseekvationen
    theta_ddot = (-m * g * l * sin(theta)) / (m * l * (cos(theta) * theta_dot) + m * g * l * sin(theta));

    dydt = [theta_dot; theta_ddot];
end

% Anropa simuleringen

