clc
clear
f = @(x) 1 ./ (1 + x).^2;

result = integral(f, 0, 1);

disp(['The integral from 0 to 1 of 1/(1+x)^2 dx is: ', num2str(result)]);
