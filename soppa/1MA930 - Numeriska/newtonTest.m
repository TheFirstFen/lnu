format long

x0=[0 0.5 1 1.5];
 y0=[0 0.479425538604203 0.841470984807897 0.997494986604054];
 c=newtdd(x0,y0,4);
 x=-pi:.01:pi;
 y=nest(3,c,x,x0);
 plot(x0,y0,'r.',x,y, 'DisplayName', 'Interpolation')
 hold on
 
 p = @(x) 0 + 0.958851077208406.* (x-0) -0.234760184801018.* (x-0).*(x-0.5) -0.118188469342704.* (x-0).*(x-0.5).*(x-1);
 f = p(x);
 
plot(x, sin(x), 'g', 'DisplayName', 'Sin(x)');
legend show;
hold off

true_error = abs(sin(0.75) - p(0.75))
true_error = abs(sin(0.2) - p(0.2))







