% Load data
load('lab1_acceleration(1000värden).mat');
ax = Acceleration.(1);
ay = Acceleration.(2);
az = Acceleration.(3);

% Define N values for moving average
N_values = [3, 5, 10, 20, 100, 1000];

% Compute moving average for each N value
for i = 1:numel(N_values)
    syms k;
    N = N_values(i);
    AZ = movmean(az, N);
    %AZ = 1/N * sum(az(k), k, 1, N);
    Sd = std(Az);
    %Sd = sqrt(1/(N-1) * sum((Az - az(k)).^2, k, 1, N));
    Sm = Sd/sqrt(N);
    Azexakt = [AZ+Sm, AZ-Sm];
    
    % Plot histogram
    subplot(numel(N_values), 1, i)
    histogram(double(AZ), 'Normalization', 'pdf')
    hold on
    line([Azexakt(1), Azexakt(1)], ylim, 'LineWidth', 1, 'Color', 'r')
    line([Azexakt(2), Azexakt(2)], ylim, 'LineWidth', 1, 'Color', 'r')
    hold off
    title(sprintf('Moving average with N = %d', N))
    xlabel('Acceleration')
    ylabel('PDF')
end
