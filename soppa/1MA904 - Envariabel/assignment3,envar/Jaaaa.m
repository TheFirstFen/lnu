
ax = Acceleration.(1);
ay = Acceleration.(2);
az = Acceleration.(3);

sig3 = std(Acceleration.Z(1:3));
sig5 = std(Acceleration.Z(1:5));
sig10 = std(Acceleration.Z(1:10));
sig20 = std(Acceleration.Z(1:20));
sig100 = std(Acceleration.Z(1:100));
sig1000 = std(Acceleration.Z(1:1000));

sigm3 = sig3/sqrt(3);
sigm5 = sig5/sqrt(5);
sigm10 = sig10/sqrt(10);
sigm20 = sig20/sqrt(20);
sigm100 = sig100/sqrt(100);
sigm1000 = sig1000/sqrt(1000);

mea3 = mean(Acceleration.Z(1:3));
mea5 = mean(Acceleration.Z(1:5));
mea10 = mean(Acceleration.Z(1:10));
mea20 = mean(Acceleration.Z(1:20));
mea100 = mean(Acceleration.Z(1:100));
mea1000 = mean(Acceleration.Z(1:1000));

exac3 = [mea3+sigm3 mea3-sigm3];
exac5 = [mea5+sigm5 mea5-sigm5];
exac10 = [mea10+sigm10 mea10-sigm10];
exac20 = [mea20+sigm20 mea20-sigm20];
exac100 = [mea100+sigm100 mea100-sigm100];
exac1000 = [mea1000+sigm1000 mea1000-sigm1000];

histogram(az,'Normalization','pdf')
pd = fitdist(az, 'Normal')

x = linspace(min(az), max(az), 1000);
y = pdf(pd, x);
hold on
plot(x, y, 'r', 'LineWidth', 2)
hold off






