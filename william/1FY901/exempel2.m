% Exempel 2
clear
clf

x0 = [1 0]; % startvärde
[t,x] = ode45(@f2,[0 50], x0);

figure(2)
clf
plot(t,x(:,1))
hold on
plot(t,x(:,2))
xlabel('t (s)')
legend('x1 (m)','x2 (m/s)')



figure(3)
clf
plot(x(:,1),x(:,2))
xlabel('x1 (dvs x)') % dvs position
ylabel('x2 (dvs x-prim)') % dvs hastighet
% Det här kallas för ett fasdiagram. Systemet kommer att snurra runt i den
% här ovalen oavsett hur långt tidsintervall man väljer. Jämför detta med
% exempel 4: svängning med dämpning.
