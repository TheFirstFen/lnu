clc;
clear;

f = @(x) 1 ./ (1 + x).^2;


result = integral(f, 0, 1);

disp(['The value of the integral is :', num2str(result)])