function [t] = find_t_s(s)
    dx_dt = @(t) 0.3 + 7.8*t - 14.1*t^2;
    dy_dt = @(t) 0.3 + 1.8*t - 8.1*t^2;

    integrand = @(t) sqrt((dx_dt(t)).^2 + (dy_dt(t)).^2);


    total_arc_length = adapquad(integrand, 0, 1, 1e-3);
    f = @(t) (adapquad(integrand, 0, t, 1e-6) / total_arc_length) - s;
    
    TOL = 1e-3;
    t = bisection_method(f, 0, 1, TOL);
end