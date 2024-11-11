format long;

x = linspace(-1, 1, 1000);
y = sin(2*x);
g = exp(-x.^2);


plot(x,y,'b-')
hold on
plot(x, g,'r-')
hold off