% Exempel 1
clear
clf

y0 = 0; % startvärde
[t,y] = ode45(@f,[0 5], y0);

figure(1)
plot(t,y)
