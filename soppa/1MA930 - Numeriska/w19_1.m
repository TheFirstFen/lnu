format short;

[t,y] = meshgrid(0:.1:1,0:.1:2);
f=t.*y+t.^3;
l=max(1,sqrt(f.^2)); % to give the arrows similar lengths
U=1./l;
V=f./l;
[t1, w] = euler([0,1], 1, 10);


ye = @(t) 3 * exp((t.^2)/2) - t^2 - 2;

xe = linspace(0, 1, 11);

quiver(t,y,U,V)
axis equal
axis([0 1.1 0 2.1])
hold on
plot(t1, w)

yvals = [0,0,0,0,0,0,0,0,0,0];
i = 1;
for xee = xe
    yvals(i) = ye(xee);
    i = i + 1;
end

steps = linspace(0, 10,11);

ei = abs(yvals(1, :) - w(1, :));


comparisonTable = table(steps', xe', w', yvals', ei', ...
    'VariableNames', {'Steps', 'ti', 'wi', 'yi', 'ei'});

disp(comparisonTable)








function [t,y]=euler(inter,y0,n)
t(1)=inter(1); y(1)=y0;
h=(inter(2)-inter(1))/n;
    for i=1:n
    t(i+1)=t(i)+h;
    y(i+1)=eulerstep(t(i),y(i),h);
    end
end


function y=eulerstep(t,y,h)
%one step of Euler’s Method
%Input: current time t, current value y, stepsize h
%Output: approximate solution value at time t+h
y=y+h*ydot(t,y);
end
function z=ydot(t,y)
%right-hand side of differential equation
z=t*y+t^3;
end

