function [x] = bisection_method2(f, a, b, TOL)
    k_max = 200;
    return_all = false;
    
    if nargout > 2
        return_all = true;
    end
    
    c = (a + b) / 2;

    if f(c) == 0
        x = c;
        iterations = 0;
        x_all = c;
        return
    end

    fa = f(a);
    fc = f(c);

    if return_all
        x_all = zeros(1, k_max + 1);
    end

    for iterations = 1:k_max
        if return_all
            x_all(iterations) = c;
        end

        if fc == 0
            break;
        elseif (fa * fc > 0)
            a = c;
            fa = fc;
        else
            b = c;
        end

        c = (a + b) / 2;

        if ((b - a) / 2 < TOL)
            break;
        end

        fc = f(c);
    end

    x = c;

    if return_all
        x_all(iterations + 1) = x;
        x_all = x_all(1:(iterations + 1));
    end
end
