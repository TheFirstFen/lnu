 %Program 1.1 Bisection Method
 %Computes approximate solution of f(x)=0
 %Input: function handle f; a,b such that f(a)*f(b)<0,
 % and tolerance tol
 %Output: Approximate solution xc
 
clc
f = @(x) x-4*sin(2*x)-3-3/80;
opt = 1*10^-6;
bisect(f, 1, 2, opt)

function xc=bisect(f, a, b, tol)
   if sign(f(a))*sign(f(b)) >= 0
       error('f(a)f(b) <0 not satisfied!')
   end
   fa = f(a);
   fb = f(b);
   
   while ((b-a) / 2) > tol
       c = (a+b)/2;
       fc = f(c);
       if fc == 0
           break
       end
       if sign(fc)*sign(fa)<0
           b = c;
           fb = fc;
       else
           a= c;
           fa = fc;
       end
   end
   xc = (a+b)/2;
end
 