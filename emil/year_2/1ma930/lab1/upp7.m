format long;

true_value = 1/3;
p = 0;

while true
    x = 10^(-p);
    
    result = (tan(x) - x) / x^3;
    digits = abs(log10(abs(result/true_value)));
    
    if digits < 16
        break;
    end
    
    p = p+1;
end
fprintf('The smallest integer p for witch the expression has no correct significant digits at x = 10^(-p) is: %d\n', p);