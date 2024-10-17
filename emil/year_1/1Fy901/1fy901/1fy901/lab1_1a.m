load('lab1_acceleration(1000värden).mat');

ax = Acceleration.(1);
ay = Acceleration.(2);
az = Acceleration.(3);

time = linspace(0,10,1011);

plot(time, az, "LineWidth",3)
ylim([0 11])
xlabel('t[s]')
ylabel('g[m/s²]')
fontsize(gca,30,"pixels")
