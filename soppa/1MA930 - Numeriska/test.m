% Define the function p(x)
p = @(x) x^3 + 2*x + 1;

% Use fzero to find a root starting from an initial guess
root = fzero(p, -2); % Start from an initial guess close to where the sign changes
root = root * 2
% Display the found root
fprintf('The root found using fzero is: %.8f\n', root);