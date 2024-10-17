function x = LUfactor(a,b)
[L,U] = lu(a);
Z = L\b;
x = U\Z;
end