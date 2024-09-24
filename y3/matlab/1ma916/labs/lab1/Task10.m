% Define the function to integrate
f = @(x) 1 ./ (1 + x).^2;

% Calculate the integral from 0 to 1
result = integral(f, 0, 1);

% Display the result
disp(['The integral from 0 to 1 of 1/(1+x)^2 dx is: ', num2str(result)]);
