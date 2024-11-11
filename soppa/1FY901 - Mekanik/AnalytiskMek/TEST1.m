function pendulum_with_slow_drivingggg()
    % Parameters
    g = 9.81; % Acceleration due to gravity (m/s^2)
    l = 1;    % Length of the pendulum (m)
    a = 0.1;  % Amplitude of the vertical driving (m)
    omega = ((1 / (2 * pi)) * sqrt(g / l)) / 10; % Natural frequency of the pendulum (rad/s)


    % Differential equation for the pendulum with slow vertical driving
    pendulum_equation_with_slow_driving = @(t, phi) [phi(2); ...
        - (g + a * omega^2 * cos(omega * t)) * sin(phi(1)) / l];

    % Initial conditions
    initial_conditions = [pi / 4, 0]; % Initial angle (45 degrees), initial angular velocity

    % Simulation time span
    tspan = [0, 100]; % [Start time, End time]
    
    % Call ode45 to solve the differential equation
    [time, results] = ode45(pendulum_equation_with_slow_driving, tspan, initial_conditions);

    % Extract angles from the results
    angles = results(:, 1);

    % Plotta resultatet
    figure;
    plot(time, angles);
    xlabel('Tid (s)');
    ylabel('Vinkel (rad)');
    title('Pendel med låg drivning');
end
