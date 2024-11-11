function [time1, time2, time3] = LUTimes(q)
   A = rand(q, q);
   b = rand(q,1);
   tic
   x = A\b;
   time1 = toc;
   tic
   [L, U] = lu(A);

   z = L\b;
   x1 = U\z;
   time2 = toc;
   
   tic
   inv(A);
   time3 = toc;

   
   