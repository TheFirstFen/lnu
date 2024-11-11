rng(7)
n = 30;
center = [0 0];
radius = 1;
eps = 0.1;
r = eps * rand (n ,1) + radius - eps /2;

As = [center(1)+r.*cos(2*pi*(1: n )'/n) center(2)+r.*sin(2* pi *(1: n)'/n)];
b = As(:,1).^2 + As(:,2).^2;
plot(As(:,1), As(:,2), "b.");
hold on
A = As * 2;
A(:,3) = ones;
c = A\b

radius = sqrt(c(3)+(c(1))^2+(c(2)^2));

th = 0:pi/100:2*pi;
xunit = radius * cos(th) + c(1);
yunit = radius * sin(th) + c(2);
plot(xunit,yunit);
hold off
axis equal

MSE = sum((radius^2-((As(:,1)-c(1)).^2) - ((As(:,2)-c(2)).^2)).^2)/30





