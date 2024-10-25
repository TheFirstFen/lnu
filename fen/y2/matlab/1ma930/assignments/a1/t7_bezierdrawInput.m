%Program 3.7 Freehand Draw Program Using Bezier Splines
%Click in Matlab figure window to locate first point, and click
% three more times to specify 2 control points and the next
% spline point. Continue with groups of 3 points to add more
% to the curve. Press return to terminate program.
function bezierdrawInput(points)
    % points is an n-by-8 matrix where each row represents one Bezier curve
    % with coordinates [x1, y1, x2, y2, x3, y3, x4, y4]

    % plot the axis lines
    plot([-1 1],[0,0],'k',[0 0],[-1 1],'k');
    hold on;
    t = 0:0.02:1; % parameter t for Bezier curve computation

    for i = 1:size(points, 1)
        % Extract points from the matrix
        x = points(i, 1:2:8);
        y = points(i, 2:2:8);

        % plot spline points and control pts
        plot([x(1) x(2)], [y(1) y(2)], 'r:', x(2), y(2), 'rs');
        plot([x(3) x(4)], [y(3) y(4)], 'r:', x(3), y(3), 'rs');
        plot(x(1), y(1), 'bo', x(4), y(4), 'bo');

        % Compute coefficients for the cubic Bezier curve
        bx = 3*(x(2) - x(1)); by = 3*(y(2) - y(1));
        cx = 3*(x(3) - x(2)) - bx; cy = 3*(y(3) - y(2)) - by;
        dx = x(4) - x(1) - bx - cx; dy = y(4) - y(1) - by - cy;
        xp = x(1) + t .* (bx + t .* (cx + t * dx));
        
        % Horner's method
        yp = y(1) + t .* (by + t .* (cy + t * dy));

        % plot the Bezier curve
        plot(xp, yp);
    end

    hold off;
end

A = [
289 452 289 452 166 452 166 452;
166 452 166 452 166 568 166 568;
166 568 166 627 185 657 223 657;
223 657 245 657 258 647 276 618;
276 618 292 589 304 580 321 580;
321 580 345 580 363 598 363 621;
363 621 363 657 319 683 259 683;
259 683 196 683 144 656 118 611;
118 611 92 566 84 530 83 450;
83 450 83 450 1 450 1 450;
1 450 1 450 1 418 1 418;
1 418 1 418 83 418 83 418;
83 418 83 418 83 104 83 104;
83 104 83 31 72 19 0 15;
0 15 0 15 0 0 0 0;
0   0 0   0 260 0  260 0;
260 0 260 0 260 15 260 15;
260 15 178 18 167 29 167 104;
167 104 167 104 167 418 167 418;
167 418 167 418 289 418 289 418;
289 418 289 418 289 452 289 452
];

bezierdrawInput(A);