clc;
format long;

%% a
f = @(x) sin(x) - cos(x);
h = [];
for k=1:12
    h = [h 10^-k];
end

f_prime = @(x) cos(x) + sin(x);

central_diff = @(x, h) (f(x+h) - f(x-h))/(2*h);

central_err = zeros(size(h));
for i=1:length(h)
    central_err(i) = abs(central_diff(0, h(i)) - f_prime(0));
end

loglog(h, central_err, 'o-')

for i=1:length(h)
    disp(['h: ', num2str(h(i)), ', x: ', num2str(central_err(i))])
end

%% b
clc

forward_diff = @(x, h) (f(x + h) - f(x)) / h;

forward_err = zeros(size(h));
for i=1:length(h)
    forward_err(i) = abs(central_diff(0,h(i)) - f_prime(0));
end



