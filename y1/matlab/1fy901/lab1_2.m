load('lab1_acceleration(1000värden).mat');

ax = Acceleration.(1);
ay = Acceleration.(2);
az = Acceleration.(3);

N = 3;
syms i;
Az3 = 1/N * symsum(az(i,1), i, 1, N);
Sd3 = sqrt(1/(N-1) * symsum((Az3 - az(i,1)), i, 1, N)^2);
Sm3 = Sd3/sqrt(N);
Az3exakt = [Az3+Sm3 Az3-Sm3];

N = 5;
syms i;
Az5 = 1/N * symsum(az(i,1), i, 1, N);
Sd5 = sqrt(1/(N-1) * symsum((Az5 - az(i,1)), i, 1, N)^2);
Sm5 = Sd5/sqrt(N);
Az5exakt = [Az5+Sm5 Az5-Sm5];

N = 10;
syms i;
Az10 = 1/N * symsum(az(i,1), i, 1, N);
Sd10 = sqrt(1/(N-1) * symsum((Az10 - az(i,1)), i, 1, N)^2);
Sm10 = Sd10/sqrt(N);
Az10exakt = [Az10+Sm10 Az10-Sm10];

N = 20;
syms i;
Az20 = 1/N * symsum(az(i,1), i, 1, N);
Sd20 = sqrt(1/(N-1) * symsum((Az20 - az(i,1)), i, 1, N)^2);
Sm20 = Sd20/sqrt(N);
Az20exakt = [Az20+Sm20 Az20-Sm20];

N = 100;
syms i;
Az100 = 1/N * symsum(az(i,1), i, 1, N);
Sd100 = sqrt(1/(N-1) * symsum((Az100 - az(i,1)), i, 1, N)^2);
Sm100 = Sd100/sqrt(N);
Az100exakt = [Az100+Sm100 Az100-Sm100];

N = 1000;
syms i;
Az1000= 1/N * symsum(az(i,1), i, 1, N);
Sd1000 = sqrt(1/(N-1) * symsum((Az1000 - az(i,1)), i, 1, N)^2);
Sm1000 = Sd1000/sqrt(N);
Az1000exakt = [Az1000+Sm1000 Az1000-Sm1000];


histogram(Az100, 'Normalization', 'pdf')
