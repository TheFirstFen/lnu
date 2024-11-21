function dydt = pendulum(t, y, A, f)
    g = 9.82;   
    l = 1;
    phi = y(1);
    phi_dot = y(2);
    
    phi_ddot = -(sin(phi) * (A * f^2 * cos(f*t) + g*l)) / l;
    
    dydt = [phi_dot; phi_ddot];
end
