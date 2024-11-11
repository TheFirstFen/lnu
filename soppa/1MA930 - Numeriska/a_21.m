format long

H = hilb(7);
b=10*ones(7,1);

x=(H\b);
xexact=invhilb(7)*b;

norm(b,'inf')
max(b)

cond(H,'inf')

