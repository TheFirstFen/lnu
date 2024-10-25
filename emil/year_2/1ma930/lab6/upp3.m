clc 
format short

f = @(t, y) t.*y + t.^3;

[t, w] = explicit_trapezoid_method(f,[0 1], 1, 0.1);
e = w - g10;

T10 = table(num2cell(t'), num2cell(w'), num2cell(g10'), num2cell(e'), 'VariableNames', {'t', 'w', 'g10', 'e'});
disp("Table for t10, y10:");
disp(T10);

function [t, y] = explicit_trapezoid_method(f, t, y0, h)
    % f: function handle representing the derivative function
    % tspan: [t0, tf] where t0 is the initial time and tf is the final time
    % y0: initial condition
    % h: step size
    % Returns:
    % t: time points
    % y: solution values at corresponding time points
    
    % Initialize variables
    t = t(1):h:t(2);
    N = length(t);
    y = zeros(size(t));
    y(1) = y0;
    
    % Perform Explicit Trapezoidal Method
    for i = 1:N-1
        % Predictor step
        y_pred = y(i) + h * f(t(i), y(i));
        
        % Corrector step
        y(i+1) = y(i) + 0.5 * h * (f(t(i), y(i)) + f(t(i+1), y_pred));
    end
end