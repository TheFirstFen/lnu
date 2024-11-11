% Extract z-component of acceleration
z_acceleration = Acceleration.Z(:);

time = (datenum(Acceleration.Timestamp)-datenum(Acceleration.Timestamp(1)))*86400;
% Define constants
mass = 90; % kg

% Calculate velocity, displacement, and force in z-axis
velocity = [0; cumsum(diff(z_acceleration) ./ diff(time))];
displacement = 0.5 * cumtrapz(time, velocity) + Acceleration.Z(1) * time(:);
force = mass * z_acceleration;

% Plot results
figure;
hold on;
plot(time, velocity, 'b');
plot(time, displacement, 'r');
plot(time, force, 'g');
xlabel('Time');
ylabel('Velocity (m/s), Displacement (m), Force (N)');
legend('Velocity', 'Displacement', 'Force');

max(velocity)
max(az)
max(force)
