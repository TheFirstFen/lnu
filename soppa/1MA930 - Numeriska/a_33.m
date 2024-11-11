narray = linspace(10,1000, 10);

t1 = zeros(1, length(narray));
t2 = zeros(1, length(narray));
t3 = zeros(1, length(narray));

for i = 1:length(narray)
    % Assume LUTimes is a function that returns three time measurements for a given n
    [t1(i), t2(i), t3(i)] = LUTimes(narray(i));
end

plot(narray, t1, 'b-o', 'LineWidth', 1);
hold on
plot(narray, t2, 'g-o', 'LineWidth', 1);
hold on
plot(narray, t3, 'r-o', 'LineWidth', 1);
hold off
xlabel('Array Size');
ylabel('Time (s)');
legend('Backslash', 'LU', 'inv');
title('Time Measurement for LUTimes');
