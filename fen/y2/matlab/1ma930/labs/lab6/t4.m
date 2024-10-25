t3
clc

K = 8;

err = zeros(1,K);

for k = 1:K
    n = 10^k;
    h = 1/n;
    w = y0;
    for i = 1:n
        w = w+ h/2*(f((i-1)/n,w) + f((i-1)/n+h,w+h*f((i-1)/n,w)));
    end

end

