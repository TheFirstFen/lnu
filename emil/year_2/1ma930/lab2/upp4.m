format long 

clc

f = @(x) x - 4*sin(2*x) - 3 - 3/80;

df = @(x) 1 - 8*cos(2*x);

x0_1 = 6;
x0_2 = 8;

tolerance = 0.5e-8;

maxIterations = 1000;

x = x0_1;
iteration = 0;
errorEstimate = inf;

while abs(errorEstimate) > tolerance && iteration < maxIterations
    x_new = x - f(x) / df(x);
    
    errorEstimate = x_new - x;
    
    x = x_new;

    iteration = iteration + 1;
end

if iteration >= maxIterations
    disp("Maximum iterations reached without convergence for the first root.")
else
    disp(['First root found at x = ', num2str(x, '%.9f')])
end

x = x0_2;
iteration = 0;
errorEstimate = inf;

while abs(errorEstimate) > tolerance && iteration < maxIterations
    x_new = x - f(x) / df(x);
    
    errorEstimate = x_new - x;
    
    x = x_new;

    iteration = iteration + 1;
end

if iteration >= maxIterations
    disp("Maximum iterations reached without convergence for the second root.")
else
    disp(['Second root found at x = ', num2str(x, '%.9f')])
end
