function x = LUfactor(a, b)
[L, U] = lu(a);
z = L\b;
x = U\z;
