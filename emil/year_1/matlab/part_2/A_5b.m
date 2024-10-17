radius2 = sqrt(c(3) + c(2)^2 + c(1)^2)

hold on 
plot(A(:,1),A(:,2),'k.');
th = 0:pi/50:2*pi;
xunit = radius2 *cos(th) + c(1);
yunit = radius2 * sin(th) + c(2);
plot(xunit, yunit)
hold off