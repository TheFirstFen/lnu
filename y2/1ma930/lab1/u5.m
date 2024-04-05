format long;

clc

y = 19;
k = 0;
f = 19 + 2^(-k);

while f > y
    k = k + 1;
    f = 19 + 2^(-k);
end

k = k - 1