[t,y] = meshgrid(0:.1:1,0:.1:2);
f = @(t, y) t.*y+t.^3;

[t1, w] = explicit_trapezoid_method(f, [0 1], 1, 0.01);

steps = linspace(0, 10, 101);

ye = @(t) 3 * exp((t.^2)/2) - t^2 - 2;
xe = linspace(0, 1, 101);
yvals = zeros(101);
i = 1;
for xee = xe
    yvals(i) = ye(xee);
    i = i + 1;
end

ei = abs(yvals(1, :) - w(1, :));

comparisonTable = table(steps', xe', w', yvals', ei', ...
    'VariableNames', {'Steps', 'ti', 'wi', 'yi', 'ei'});

disp(comparisonTable)