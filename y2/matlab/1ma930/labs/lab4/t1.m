%% B
clc
clear
format long

x0 = [];
y0 = [];
for i = 1:4
   val = (((pi/2)/4) - 0.1) * i;
   x0 = [x0 (val)];
   y0 = [y0 (sin(val))];
end

c=newtdd(x0,y0,4);
x=-pi:.01:pi;
y=nest(3,c,x,x0);
plot(x0,y0,'or',x,y, 'LineWidth',2);
hold on
f = @(x) sin(x);
f = f(x);

plot(x, f, 'g', 'LineWidth', 2)
legend('coords', 'p(x)', 'f(x)');


p = @(x) c(1) + c(2).*(x - x0(1)) + c(3).*(x-x0(1)).*(x-x0(2)) + c(4).*(x-x0(1)).*(x-x0(2)).*(x-x0(3));
%p = p(x);
%plot(x, p, '--b', 'LineWidth',2)
hold off
xlabel('steps');
ylabel('steps');

%% E
x=1;
est_err = abs((((x-x0(1))*(x-x0(2))*(x-x0(3))*(x-x0(4)))/factorial(4))*sin(max(c)))
trur_err = abs(sin(1) - p(1))

