function dydt = TEST74(t, y, g, l, a, v)
    % y(1) är utslagsvinkeln p
    % y(2) är dp/dt

    % Beräkna d^2p/dt^2 enligt differentialekvationen
    dpdt = y(2);
    d2pdt2 = -(g/l * sin(y(1))) - ((a * v) / l) * sin(v * t) * cos(y(1)) + 2 * y(2)^2 * sin(y(1));

    % Returnera derivatorna som en kolumnvektor
    dydt = [dpdt; d2pdt2];
end