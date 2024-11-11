function integral = compositeSimpsonsRule(f, a, b, n)
    % Check if n is even
    if mod(n, 2) ~= 0
        error('n must be even');
    end
    
    % Calculate the width of each subinterval
    h = (b - a) / n;
    
    % Initialization of the sum variables
    x = linspace(a, b, n+1); % Generates the points x0, x1, ..., xn
    y = f(x); % Function values at the points x0, x1, ..., xn
    
    % Simpson's coefficients: 1, 4, 2, 4, ..., 4, 2, 4, 1
    coefficients = 2 * ones(1, n+1); % Start with all 2s
    coefficients(2:2:n) = 4; % Set even indices (except the last) to 4
    coefficients(1) = 1; % First coefficient is 1
    coefficients(end) = 1; % Last coefficient is 1
    
    % Calculate the composite Simpson's integral
    integral = (h/3) * sum(coefficients .* y);
end
