function dydt = TEST61(t, y, g, l, a, v)
    % y(1) är utslagsvinkeln p
    % y(2) är dp/dt
   

    % Beräkna d^2p/dt^2 enligt differentialekvationen
    dpdt = y(2);
    d2pdt2 = (m * g * l * sin(y(1)) + a * m * v^2 * sin(v * t)) / (m * l^2);

    % Returnera derivatorna som en kolumnvektor
    dydt = [dpdt; d2pdt2];
end


