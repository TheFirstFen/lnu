load('sensorlog_20230424_211327');

m = 90

ax = Acceleration.(1);
ay = Acceleration.(2);
az = Acceleration.(3);
time = (datenum(Acceleration.Timestamp)-datenum(Acceleration.Timestamp(1)))*86400

Fx = m * ax;
Fy = m * ay;
Fz = m * az;

hastighet_x = [NaN; diff(ax)./diff(time)];
hastighet_y = [NaN; diff(ay)./diff(time)];
hastighet_z = [NaN; diff(az)./diff(time)];



forflyttning_x = cumtrapz(time, ax);
forflyttning_y = cumtrapz(time, ay);
forflyttning_z = cumtrapz(time, az);

%%hastighet_z = cumtrapz(diff(time), diff(az));
%%forflyttning_z = cumtrapz(time, diff(hastighet_z));


hastighet_z = az * diff(time)

hold on
plot(time, hastighet_z, 'r');
plot(time, forflyttning_z, 'b');
plot(time, Fx, 'g');
xlabel('Tid (s)');
ylabel('m');
legend('hastighet', 'förflyttning', 'kraft');
hold off
