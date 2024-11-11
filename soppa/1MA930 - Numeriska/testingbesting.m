format short;

% Define the adjacency matrix A
A = [
 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0;
 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0;
 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0;
 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0;
 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0;
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0;
 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0;
 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0;
 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0;
 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0;
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1;
 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0;
 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0;
 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1;
 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0];

n = size(A, 1);


qs = [0, 0.15, 0.5];

vectors = zeros(n, length(qs));

c = 0;

for q = qs
    c = c + 1;
    G = zeros(n, n);
    for i = 1:n
        ni = sum(A(i, :));
        for j = 1:cols
            G(j, i) = q/15 + (((1 - q) * A(i, j)) / ni);
        end
    end
    
    % Finding dominant eigenvector using eig
    [V, D] = eig(G);
    [~, idx] = max(diag(D));
    principalEigenvector = V(:, idx);
    
    % Normalize
    principalEigenvector = principalEigenvector / sum(principalEigenvector);
    
    vectors(:, c) = principalEigenvector;
end

fprintf("Page ranks for q equals:\n    0         0.15         0.5\n");
fprintf("    --------------------------\n")
disp(vectors);



% Jump probability is the procentual chance of a surfer jumpoing to a
% random page instead of following a link on another page. 

% q = 0 means that the next jump is not random. The surfer strictly follows
% from one page to another via the link meaning some pages will not be 
% reached giving the page rank 0.

% q = 0.15 means that there is a 15 % probability of the surfer jumping to
% a random page instead of following a link. This distributes the
% probability of reaching pages more evenly.

% = 0.5 means that it is as likely that the surfer follows a link as it is
% going to a random page. This reduces the influence of the page links and
% pages with few or no in-bound links has a greatly higher rank that they
% have with a lower q value. 
