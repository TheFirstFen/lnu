format long;

x = linspace(-10, 10, 500);
x1 = linspace(6.9, 7.1, 500);
y = x - (4 * sin(2*x)) - 3 - (3/80);
y1 = x1 - (4 * sin(2*x1)) - 3 - (3/80);


subplot(2,1,1)
plot(x,y,'b-')
hold on
plot(xlim, [0 0], 'r-')


subplot(2,1,2)
plot(x1,y1,'b-')
hold on
plot(xlim, [0 0], 'r-')
hold off
