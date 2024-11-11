%% A
format long

clc
A = 2;
f = @(x) x^3 - A;
opts.TOL = 10^-6;
[x, k] = bisection_method(f, 1, 2, opts)


A = 3;
f = @(x) x^3 - A;
opts.TOL = 10^-6;
[x, k] = bisection_method(f, 1, 2, opts)

A = 5;
f = @(x) x^3 - A;
opts.TOL = 10^-6;
[x, k] = bisection_method(f, 1, 2, opts)

%% B

f = @(x) det([1 2 3 x; 4 5 x 6; 7 x 8 9; x 10 11 12]) - 1000;


a = -100;
b = 100;
opts.TOL = 10^-7;


[x, k] = bisection_method(f, a, b, opts);



det_value = det([1 2 3 x; 4 5 x 6; 7 x 8 9; x 10 11 12]);
fprintf('Determinant at x = %.6f is approximately %.6f\n', x, det_value);


backward_error = abs(det_value - 1000);
fprintf('Backward error: %.6f\n', backward_error);

%% C

R = 0.0820578;
T = 320;
P = 15;
n = 1;
a = 1.36;
b = 0.003183;

V_ideal = (n * R * T) / P;

f = @(V) (P + a / V^2) * (V - b) - n * R * T;

df = @(V) (P + a / V^2) - 2 * a * (V - b) / V^3;

V = V_ideal;
tolerance = 1e-6;
max_iter = 100;
fprintf("\n");
fprintf('Initial guess: %.3f L\n', V_ideal);
for i = 1:max_iter
    V_next = V - f(V) / df(V);
    if abs(V_next - V) < tolerance
        fprintf('Converged to %.3f after %d iterations\n', V_next, i);
        break;
    end
    V = V_next;
end

fprintf('Final estimated volume: %.3f L\n', V);

actual_determinant = (P + a / V^2) * (V - b) - n * R * T;
fprintf('Determinant check: %.3f\n', actual_determinant);

%% D
% Root is computed to 3/4

f = @(x) (1 - 3./(4*x)).^(1/3);
df = @(x) -(1./(4*x.^2)).*(1 - 3./(4*x)).^(-2/3);
df(3/4);

x0 = 0.70;
iterates = zeros(1, 50);
iterates(1) = x0;

for k = 2:50
    x0 = x0 - f(x0) / df(x0);
    iterates(k) = x0;
end

figure;
plot(1:50, iterates, 'o-');
xlabel('Iteration');
ylabel('x');
grid on;





