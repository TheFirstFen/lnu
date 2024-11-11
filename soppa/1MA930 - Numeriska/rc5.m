

A = [
 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0;
 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0;
 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0;
 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0;
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0;
 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0;
 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0;
 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0;
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1;
 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0;
 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0;
 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1;
 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0];

q = 0.15;

[rows, cols] = size(A);

G = zeros(rows, cols);

for i = 1:n
    ni = sum(A(i, :));
    if ni == 0
        % If no outgoing links, distribute rank evenly across all nodes
        G(:, i) = q / n + (1 - q) / n;
    else
        for j = 1:n
            G(j, i) = q / n + ((1 - q) * A(i, j) / ni);
        end
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


% By removing all links to and from page 10 it decreases the chance of a
% surfer reching that page by approximately 9.5 % which is a lot. This also
% changes the other pages ranks increasing all pages except 9, 13, 14. By
% having the two results of 4 and 5 we can see that by adding more links
% it increases  for 9, 10, 13, 14 and if removing links it decreases the
% page ranks for the same. This can conclude to 9, 10, 13, 14 benefiting
% from more links while it doesnt benefit from removing links generally for
% the matrix. 





