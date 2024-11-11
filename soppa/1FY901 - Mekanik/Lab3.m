% Bredd mellersta måttet
a = 0.742;
% längd längsta måttet
b = 0.16;
% Höjd kortast måttet
c = 0.0087;

mass = 0.192;

time = (datenum(AngularVelocity.Timestamp)-datenum(AngularVelocity.Timestamp(1)))*86400;

max(AngularVelocity.Y);


angVelRad = AngularVelocity.Variables;



% Calculate height to mass centre
heightToMassCentre = sqrt(((a/2)^2)+((c/2)^2));
Ib = ((mass*9.81)*((2*heightToMassCentre) - c))/(max(angVelRad(:,2))^2);

% Parallell axis theorem ger:
Iy = abs(Ib - (mass*(heightToMassCentre^2)));

IyEst = (mass/12)*(a^2 + c^2);

IyDiff = Iy - IyEst;

IyProc = abs(IyDiff/(Iy)) * 100;

disp("Experimentell: " + Iy)
disp("Estimation: " + IyEst)
disp("Skillnad: " + abs(IyDiff))
disp("Procentuellskillnad: " + IyProc + " %")

% Plot angular velocity
figure;
plot(time, angVelRad(:,2));
title('Vinkelhastighet (y-axel)');
xlabel('Tid');
ylabel('Vinkel (rad)');
legend('Y');


