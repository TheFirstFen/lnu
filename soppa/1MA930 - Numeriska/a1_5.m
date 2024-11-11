format hex;

f = @(k) 19+2^(-k);
x = 19;

for k = linspace(0,49,1)
    if f(k) <= x
        disp("Ja k = " + (k - 1) + " är högsta heltalet då fl(19+2^-k) > fl(19)")
    end
end