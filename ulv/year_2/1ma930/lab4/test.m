format long
clc

x0=[0 0.5 1 1.5];
 y0=[0 0.479425538604203 0.841470984807897 0.997494986604054];
 c=newtdd(x0,y0,4);
 x=-pi:.01:pi;
 y=nest(3,c,x,x0);
 plot(x0,y0,'r.',x,y)
 hold on
 xlabel('x value');
 ylabel('y value');
 s = -4:.01:4;
 plot(s, sin(s))
 
 p = @(x) 0 + 0.958851077208406.* (x-0) -0.234760184801018.* (x-0).*(x-0.5) -0.118188469342704.* (x-0).*(x-0.5).*(x-1);
 f = p(x);
%plot (x, f, '.b')
legend('Original Points', 'Interpolated Curve', 'sin(x)')

true_error = abs(sin(0.75) - p(0.75))
x = 1;
worst_error = (((x-0).*(x-0.5)*(x-1)*(x-1.5))/24)*sin(max(c))