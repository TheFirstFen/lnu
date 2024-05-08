t2
clc
format default

f = @(t, y) t.*y+t.^3;

[t, w] = explicit_trapezoid_method(f, [0 1], 1, 0.1);

ei = w - yi10;