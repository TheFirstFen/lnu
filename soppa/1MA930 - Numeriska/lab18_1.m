format long;

f = @(x) sin(x) - cos(x);


df = @(x) cos(x) + sin(x);

h_values = logspace(-1, -12, 12);

correct_der = df(0);

errors = zeros(size(h_values));
errors2 = zeros(size(h_values));
errors3 = zeros(size(h_values));

for i = 1:length(h_values)
    h = h_values(i);
    formula_der = (f(h) - f(-h)) / (2*h);
    errors(i) = abs(formula_der - correct_der);
    
    
    der5_4 = (f(h)-f(0))/h;
    errors2(i) = abs(der5_4 - correct_der);
    
    der5_16 = (f(-h) - 8*f(-h/2) + 8*f(h/2) - f(h)) / (6*h);
    errors3(i) = abs(der5_16 - correct_der);
    
    
    
    disp([h, formula_der, errors(i), der5_4, errors2(i), der5_16, errors3(i)]);
end

% Plotting the errors
figure;
loglog(h_values, errors, '-o');
xlabel('h');
ylabel('Error');
grid on;
hold on
loglog(h_values, errors2, '-o');
xlabel('h');
ylabel('Error');
hold on
loglog(h_values, errors3, '-o');
xlabel('h');
ylabel('Error');


