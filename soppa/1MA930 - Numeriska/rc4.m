

A = [
 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0
 0 0 1 0 1 0 2 0 0 0 0 0 0 0 0
 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0
 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0
 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0
 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
 0 0 0 0 0 0 2 1 0 0 1 0 0 0 0
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


[V, D] = eig(G);
[~, idx] = max(diag(D));
principalEigenvector = V(:, idx);
    
% Normalize
principalEigenvector = principalEigenvector / sum(principalEigenvector);



oldp = [0.0268
    0.0299
    0.0299
    0.0268
    0.0396
    0.0396
    0.0396
    0.0396
    0.0746
    0.1063
    0.1063
    0.0746
    0.1251
    0.1163
    0.1251];

differences = principalEigenvector - oldp;


nodes = (1:length(oldp))';


comparisonTable = table(nodes, principalEigenvector, oldp, differences, ...
    'VariableNames', {'Page', 'UpdatedPageRank', 'OldPageRank', 'Difference'});

disp(comparisonTable);

% Yes this succeeds we can see an increase of the probability for page 7 as
% intended. Meanwhile most of the other pages ranks decrease which is
% reasonable if one increases. 9, 10, 13, 14 also has a small increase in
% page rank. But all other ranks other than 7 only differs by less than
% 1 % which is a small percentage. 



