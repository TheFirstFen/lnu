%% A

% 1+2x+x^3=0


g = @(x) -((1 + x^3)/2);


x0 = 0;
max_iter = 100;


x = x0;
for i = 1:max_iter
    x_new = g(x);
    fprintf('Iteration %d: x = %.8f\n', i, x_new);

    x = x_new;
end
disp("****************************")
%% B

% x − 4 sin(2x) − 3 − 3/80


g = @(x) 4*sin(2*x) + 3 + (3/80);


x0 = 0;
max_iter = 100;


x = x0;
for i = 1:max_iter
    x_new = g(x);
    fprintf('Iteration %d: x = %.8f\n', i, x_new);


    x = x_new;
end

