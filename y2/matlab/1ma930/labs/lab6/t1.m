clc

[t,y] = meshgrid(0:.1:1,0:.1:2);
f=t.*y+t.^3;
l=max(1,sqrt(f.^2)); % to give the arrows similar lengths
U=1./l;
V=f./l;
quiver(t,y,U,V)
axis equal
axis([0 1.1 0 2.1])
