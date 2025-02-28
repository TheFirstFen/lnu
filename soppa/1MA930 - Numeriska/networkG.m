

A = [
 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0
 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0
 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0
 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0
 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0
 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0
 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0
 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1
 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0];

q = 0.15;

[rows, cols] = size(A);

G = zeros(rows, cols);

for i = 1:rows
    % Get sum of row i
    ni = sum(A(i, :));
    for j = 1:cols
        G(j, i) = q/15 + (((1 - q) * A(i, j)) / ni);
    end
end

G;


p = [0.0268; 0.0299; 0.0299; 0.0268; 0.0396; 0.0396; 0.0396; 0.0396; 0.0746; 0.1063; 0.1063; 0.0746; 0.1251; 0.1163; 0.1251];

result = G * p;



tolerance = 1e-4;
if max(abs(result - p)) < tolerance
    disp("Verified p = G * p");
end


