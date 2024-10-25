format long;

x = 19;

k = 0;
y = x + 2^(-k);

while y > x
    k = k + 1;
    y = x + 2^(-k);
end

k = k-1
fprintf('The largest integer k such that fl(19 + 2^(-k)) > fl(19) is %d\n', k);
