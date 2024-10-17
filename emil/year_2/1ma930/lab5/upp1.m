clc 
format long;

% A
f = @(x) sin(x) - cos(x);
h = 10.^(-1:-1:-12);

f_prime = @(x) cos(x) + sin(x);

central_diff = @(x,h) (f(x+h)-f(x-h))/(2*h);

errors = zeros(size(h));
for i = 1:length(h)
    errors(i) = abs(centered_difference(0, h(i)) - f_prime(0));
end

loglog(h, errors, 'o-')
hold on
title('Error of Three-Point Centered-Difference Formula for f''(0)')
xlabel('h')
ylabel('Error')
grid on

table_data = [h' errors'];

disp('Table of Errors for Different h Values:')
disp('   h                   Error')
disp(table_data)

%B

forward_diff = @(x, h) (f(x+h) - f(x))/h;

errors = zeros(size(h));
for i = 1:length(h)
    errors(i) = abs(forward_diff(0, h(i)) - f_prime(0));
end

loglog(h, errors, 'r-')
title('Error of Forward Difference Formula for f''(0)')

table_data = [h' errors'];

disp('Table of Errors for Different h Values (Forward Finite Difference D+):')
disp('   h                   Error')
disp(table_data)