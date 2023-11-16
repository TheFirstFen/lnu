% Computes Riemann sums for the exponential function

a=1;                        % Left limit of integration
b=2;                        % Right limit of integration
n=3;                        % Antal delintervall/number of subintervals

dx=(b-a)/n;                 % width of subinterval
P=linspace(a,b,n+1);        % Partition P=[x_0 x_1 x_2 ... x_n]

% Evaluation of function e^x
fleft=exp(P(1:end-1));      % e^x in points x_{i-1}
fright=exp(P(2:end));       % e^x in points x_i

% Riemann sums (assumes increasing or decreasing function)
Rleft=sum(fleft)*dx;        % L if increasing function, U if decreasing         
Rright=sum(fright)*dx;      % U if increasing function, L if decreasing

L=min(Rleft,Rright);        % Lower Riemann sum
U=max(Rleft,Rright);        % Upper Riemann sum

disp(' ');
disp(['L(f,P)=' num2str(L)]);
disp(['U(f,P)=' num2str(U)]);
disp(' ');