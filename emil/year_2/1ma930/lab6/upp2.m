clc
%% A

[t5,y5] = euler([0 1], 1, 5);
T5 = linspace(0, 1, 6);
g5 = 3*exp((T5.^2)/2) - T5.^2 - 2;
e5 = g5 - y5;
T5 = table(num2cell(t5'), num2cell(y5'), num2cell(g5'), num2cell(e5'), 'VariableNames', {'t5', 'y5', 'g5', 'e5'});
disp("Table for t5, y5:");
disp(T5);

[t10,y10] = euler([0 1], 1, 10);
T10 = linspace(0, 1, 11);
g10 = 3*exp((T10.^2)/2) - T10.^2 - 2;
e10 = g10 - y10;
T10 = table(num2cell(t10'), num2cell(y10'), num2cell(g10'), num2cell(e10'), 'VariableNames', {'t10', 'y10', 'g10', 'e10'});
disp("Table for t10, y10:");
disp(T10);


%% B
[t,y] = meshgrid(0:.1:1,0:.1:2);
f=t.*y+t.^3;
l=max(1,sqrt(f.^2)); % to give the arrows similar lengths
U=1./l;
V=f./l;

quiver(t,y,U,V)
hold on
axis equal
axis([0 1.1 0 2.1])

[t,y] = euler([0 1], 1, 100);
plot(t,y)


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