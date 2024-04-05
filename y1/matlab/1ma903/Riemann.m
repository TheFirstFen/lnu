function Iapprox=Riemann(funk,a,b,tol)

n=ceil(abs(((b-a)*(funk(b)-funk(a)))/tol));          % Antal delintervall/number of subintervals

dx=(b-a)/n;                 % width of subinterval
P=linspace(a,b,n+1);        % Partition P=[x_0 x_1 x_2 ... x_n]

fleft=funk(P(1:end-1));      
fright=funk(P(2:end));       

% Riemann sums (assumes increasing or decreasing function)
Rleft=sum(fleft)*dx;        % L if increasing function, U if decreasing         
Rright=sum(fright)*dx;      % U if increasing function, L if decreasing

L=min(Rleft,Rright);        % Lower Riemann sum
U=max(Rleft,Rright);        % Upper Riemann sum

Iapprox=(U+L)/2;