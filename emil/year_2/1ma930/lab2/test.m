format long 

clc

f = @(x) x - 4*sin(2*x) - 3 - 3/80;
df = @(x) 1 - 8*cos(2*x);
initialGuess = [6 8];
tolerance = 1e-6;
for x = initialGuess
    root = newtonRaphson(f, df, x, tolerance);
    root
end

function root = newtonRaphson(func, deriv, guess, tolerance)
    root = guess;
    while abs(func(root)) > tolerance
        root = root - func(root)/deriv(root);
    end
end
