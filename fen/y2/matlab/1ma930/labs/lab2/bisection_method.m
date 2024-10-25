function [x,k,x_all] = bisection_method(f,a,b,opts)
    
    if (nargin < 4) || isempty(opts) || ~isfield(opts,'k_max')
        k_max = 200;
    else
        k_max = opts.k_max;
    end

    if (nargin < 4) || isempty(opts) || ~isfield(opts,'return_all')
        return_all = false;
    else
        return_all = opts.return_all;
    end

    if (nargin < 4) || isempty(opts) || ~isfield(opts,'TOL')
        TOL = 1e-10;
    else
        TOL = opts.TOL;
    end
   
    c = (a+b)/2;
    
   
    if f(c) == 0
        x = c;
        return
    end

    fa = f(a);
    fc = f(c);

    if return_all
        x_all = zeros(1,k_max+1);
    end

    for k = 1:k_max

        if return_all
            x_all(k) = c;
        end

        if fc == 0
            break;
        elseif (fa*fc > 0)
            a = c;
            fa = fc;
        else
            b = c;
        end

        c = (a+b)/2;

        if ((b-a) < TOL)
            break;
        end

        fc = f(c);
        
    end

    x = c;
    
    if return_all
        x_all(k+1) = x;
        x_all = x_all(1:(k+1));
    end
    
end