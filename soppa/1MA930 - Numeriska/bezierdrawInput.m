%Program 3.7 Freehand Draw Program Using Bezier Splines
%Click in Matlab figure window to locate first point, and click
% three more times to specify 2 control points and the next
% spline point. Continue with groups of 3 points to add more
% to the curve. Press return to terminate program.
function bezierdrawInput(points)
    % points is an n-by-8 matrix where each row represents one Bezier curve
    plot([-1 1],[0,0],'k',[0 0],[-1 1],'k');
    hold on;

    t = 0:0.02:1;

    for i = 1:size(points, 1)
        % Extract points from the matrix
        x = points(i, 1:2:8);
        y = points(i, 2:2:8);

        % plot spline points and control pts
        plot([x(1) x(2)], [y(1) y(2)], 'r:', x(2), y(2), 'rs');
        plot([x(3) x(4)], [y(3) y(4)], 'r:', x(3), y(3), 'rs');
        plot(x(1), y(1), 'bo', x(4), y(4), 'bo');

        % Compute coefficients for the cubic Bezier curve
        bx = 3*(x(2) - x(1));
        by = 3*(y(2) - y(1));
        cx = 3*(x(3) - x(2)) - bx;
        cy = 3*(y(3) - y(2)) - by;
        dx = x(4) - x(1) - bx - cx;
        dy = y(4) - y(1) - by - cy;

        % Compute the Bezier curve
        xp = x(1) + t .* (bx + t .* (cx + t * dx));
        yp = y(1) + t .* (by + t .* (cy + t * dy));

        % plot the Bezier curve
        plot(xp, yp);
    end

    hold off;
end

