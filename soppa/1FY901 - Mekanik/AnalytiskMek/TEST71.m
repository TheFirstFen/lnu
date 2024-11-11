function dydt = TEST71(t, y, g, l, a, v)
    % y(1) är utslagsvinkeln p
    % y(2) är dp/dt

    % Beräkna d^2p/dt^2 enligt differentialekvationen
    dpdt = y(2);
    d2pdt2 = -(g + a * v^2 * cos(v * t)) * (sin(y(1)) / l);

    % Returnera derivatorna som en kolumnvektor
    dydt = [dpdt; d2pdt2];
end


