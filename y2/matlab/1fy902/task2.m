I = [ 1.36 1.42 1.49 1.56 1.64 1.73 1.83 1.94 2.07 2.21 2.38 2.57 2.79 3.05 3.38 3.78 4.28 4.58 4.94 5.09 5.26 5.44 5.62 5.83 6.05 6.29 6.54 6.82 7.12 ];
U = [ 13.72 13.61 13.50 13.37 13.23 13.07 12.90 12.70 12.48 12.23 11.94 11.61 11.22 10.76 10.20 9.50 8.62 8.09 7.47 7.20 6.91 6.60 6.27 5.91 5.52 5.11 4.66 4.18 3.65 ];

Rl = [ 10000 9500 9000 8500 8000 7500 7000 6500 6000 5500 5000 4500 4000 3500 3000 2500 2000 1750 1500 1400 1300 1200 1100 1000 900 800 700 600 500 ];
Pl = U .* I * 10^-3;

I2 = [ 3.78 4.28 4.58 4.94 5.09 5.26 5.44 5.62 5.83 6.05 6.29 ];
U2 = [ 9.50 8.62 8.09 7.47 7.20 6.91 6.60 6.27 5.91 5.52 5.11 ];

Rl2 = [ 2500 2000 1750 1500 1400 1300 1200 1100 1000 900 800 ];
Pl2 = U2 .* I2 * 10^-3;


plot(Rl, Pl, '.r')
hold on
plot(Rl2, Pl2, '*b')
xlabel("Rl(Ohm)")
ylabel("Pl(Watt)")