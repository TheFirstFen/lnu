format long
clear
clc
%% A
A = rand(5,5);
b = rand(5,1);
tic
x = A\b;
toc
r = b-A*x;

%% B
tic
[L,U] = lu(A);
z = L\b;
x1 = U\z;
toc

%% D
clear
clc

% Define array of n values
n_values = 100:100:1000;

% Initialize arrays to store average times
t0_avg = zeros(size(n_values));
t1_avg = zeros(size(n_values));
t2_avg = zeros(size(n_values));
t3_avg = zeros(size(n_values));

% Number of simulations for each n
num_simulations = 1;

for idx = 1:numel(n_values);
    n = n_values(idx);
    times_t0 = zeros(num_simulations, 1);
    times_t1 = zeros(num_simulations, 1);
    times_t2 = zeros(num_simulations, 1);
    times_t3 = zeros(num_simulations, 1);
    
    for sim = 1:num_simulations;
        % Generate random matrix A and vector b
        A = rand(n, n);
        b = rand(n, 1);
        
        % Time for solving Ax=b using built-in MATLAB operator
        tic;
        x = A\b;
        times_t0(sim) = toc;
        
        % Time for LU factorization
        tic;
        [L, U] = lu(A);
        times_t1(sim) = toc;
        
        % Time for forward and backward substitution
        tic;
        y = L\b;
        x_lu = U\y;
        times_t2(sim) = toc;
        
        % Calculate residual
        r = b - A*x_lu;
        
        % Time for LUfactor function
        tic;
        LUfactor(A, b);
        times_t3(sim) = toc;
    end
    
    % Calculate average times
    t0_avg(idx) = mean(times_t0);
    t1_avg(idx) = mean(times_t1);
    t2_avg(idx) = mean(times_t2);
    t3_avg(idx) = mean(times_t3);
end

% Plotting
figure;
plot(n_values, t0_avg, '-o', n_values, t1_avg, '-o', n_values, t2_avg, '-o', n_values, t3_avg, '-o');
xlabel('Matrix size (n)');
ylabel('Average time (s)');
legend('Built-in operator', 'LU factorization', 'Back-substitution', 'LUfactor function');
title('Average Execution Times vs Matrix Size');