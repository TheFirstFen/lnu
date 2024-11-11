load('fritt fall.mat')

ax = Acceleration.(1);
ay = Acceleration.(2);
az = Acceleration.(3);

time = linspace(0,10,65);

plot(time, az, "LineWidth",3)
ylim([-15 22])
xlabel('t[s]')
ylabel('g[m/s²]')
fontsize(gca,30,"pixels")

% x0 = 50 cm = 0.5 m
% teoretisk t = 0.32 s