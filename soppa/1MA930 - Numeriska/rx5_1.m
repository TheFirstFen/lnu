function rx5_1(T)

% x = @(t) 0.5 + 0.3*t + 3.9*t^2 - 4.7*t^3;
% y = @(t) 1.5 + 0.3*t + 0.9*t^2 - 2.7*t^3;

dx = @(t) 0.3 + 7.8*t - 42.3*t^2;
dy = @(t) 0.3 + 1.8*t - 8.1*t^2;

integrand = @(t) sqrt((dx(t))^2 + (dy(t))^2);

adapquad(integrand, 0, T, 1e-6)
end