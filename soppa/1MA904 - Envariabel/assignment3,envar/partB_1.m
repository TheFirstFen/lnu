
a=-2;                        % Left limit of integration
b=2;                       % Right limit of integration
n=4;                        % Antal delintervall/number of subintervals



y = symsum(exp(-2+(i-1)),i,0,n)
x = symsum(exp(-2+(i)),i,0,n)
