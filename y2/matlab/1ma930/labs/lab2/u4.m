format long

clc

x = -2:1/10000:8;

f = @(x) x - 4 * sin(2 * x) - 3 - 3 / 80;
df = @(x) 1 - 8 * cos(2 * x);

x0 = [6 8];

tol = 0.5 * 10^-8;

for x = x0
    maxItr = 1000;
    itr = 0;
    errEst = inf;

    while abs(errEst) > tol && itr < maxItr
        x_new = x - f(x)/df(x);
        errEst = x_new - x;
        x = x_new;
        itr = itr + 1;
    end
    x
end