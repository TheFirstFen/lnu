format long

%% C

clc

f = @(x) exp(x);

a = 0;
b = 1;

m_val = [1, 2, 4];

for i = 1:length(m_val)
    m = m_val(i);
    h = (b - a) / m;
    
    x = a:h:b;
    
    approx = (h / 3) * (f(x(1)) + 4*sum(f(x(2:2:end-1))) + 2*sum(f(x(3:2:end-2))) + f(x(end)));
    
    fprintf('Approximation with %d panels: %f\n', m, approx);
end

%% A

clc 

f = @(x) x.^2;

a = 0;
b = 1;

m_val = [1, 2, 4];

for i = 1:length(m_val)
    m = m_val(i);
    h = (b - a) / m;
    
    x = a:h:b;
    
    approx = (h / 3) * (f(x(1)) + 4*sum(f(x(2:2:end-1))) + 2*sum(f(x(3:2:end-2))) + f(x(end)));
    
    fprintf('Approximation with %d panels: %f\n', m, approx);
end

