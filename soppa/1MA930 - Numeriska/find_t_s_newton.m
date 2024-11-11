function [t] = find_t_s_newton(s)

    dx_dt = @(t) 0.3 + 7.8*t - 14.1*t^2;
    dy_dt = @(t) 0.3 + 1.8*t - 8.1*t^2;

    integrand = @(t) sqrt((dx_dt(t)).^2 + (dy_dt(t)).^2);

    total_arc_length = adapquad(integrand, 0, 1, 1e-6);

    f = @(t) (adapquad(integrand, 0, t, 1e-6) / total_arc_length) - s;
    f_prime = @(t) integrand(t) / total_arc_length;
    


    t = newton_method(f,f_prime, s);
end

function t = newton_method(f, f_prime, s)
    t = s;
    TOL = 1e-3;
    max_iter = 100;
    for iter = 1:max_iter
        t_new = t - f(t) / f_prime(t);
        if abs(t_new - t) < TOL
            t = t_new;
            break;
        end
        t = t_new;
    end
end