f = pi+1;
A = 0.1; 


phi0 = pi;
phi_dot0 = 0;  
y0 = [phi0; phi_dot0];

    
tspan = [0 100];  


pendulum_with_params = @(t, y) pendulum(t, y, A, f);


[t, y] = ode45(pendulum_with_params, tspan, y0);

plot(t, y(:, 1));  
xlabel('Tid (s)');
ylabel('Vinkel (rad)');
title('Pendelrörelse');
