function TEST31()
    % Define the differential equations function
    function dydt = inverted_pendulum(t, y)
        % State variables
        theta = y(1);
        theta_dot = y(2);

        % Constants
        g = 9.81;  % Acceleration due to gravity (m/s^2)
        l = 1.0;   % Length of the pendulum arm (m)
        a = 0.1;   % Amplitude of the driving force (m)
        omega = (1 / (2 * pi)) * sqrt(g / l) * 10; % Frequency of the driving force (rad/s)

        % Differential equations
        theta_ddot = (a * omega^2 * cos(omega * t) - g * sin(theta)) / l;


        dydt = [theta_dot; theta_ddot];
    end

    % Initial values and time span
    initial_angle = pi / 4;
    initial_ang_vel = 0;
    tspan = [0 100]; % Start and end times

    % Solve the differential equations using ode45
    [t, y] = ode45(@inverted_pendulum, tspan, [initial_angle, initial_ang_vel]);

    % Plot the results
    figure;
    plot(t, y(:,1)); % Plot θ over time
    xlabel('Time (s)');
    ylabel('Angle θ (rad)');
    title('Inverted Pendulum Angle Over Time');


end
