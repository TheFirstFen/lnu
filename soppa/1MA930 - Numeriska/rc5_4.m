clear
clc
close all
for n=4:16:20
    for i = 1:n
        s(i+1) = i/n;
    end

    for i = 1:n
        t_starsN(i) = find_t_s_newton(s(i));
    end
    
    for i = 1:n
        t_stars(i) = find_t_s(s(i));
    end

    x = @(t) .5+.3*t+3.9*t^2-4.7*t^3;
    y = @(t) 1.5+.3*t+.9*t^2-2.7*t^3;
    figure
    hold on
    for i = 1:length(t_starsN)
        x_vecN(i) = x(t_starsN(i));
        y_vecN(i) = y(t_starsN(i));
    end
    
    plot(x_vecN,y_vecN,'bx','DisplayName', 'Newton')
    xlabel('x')
    ylabel('y')
    title(['Comparison of Newton and Bisection n = ', num2str(n)])
    axis([0 1.4 0 1.7])
    hold on
    
    for i = 1:length(t_stars)
        x_vec(i) = x(t_stars(i));
        y_vec(i) = y(t_stars(i));
    end
    
    plot(x_vec,y_vec,'ro','DisplayName', 'Bisection')
    xlabel('x')
    ylabel('y')
    title(['Comparison of Newton and Bisection n = ', num2str(n)])
    legend('show');
    axis([0 1.4 0 1.7])
end

