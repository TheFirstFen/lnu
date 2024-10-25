 %Program2.2JacobiMethod
 %Inputs:fullorsparsematrixa,r.h.s.b,
 % numberofJacobiiterations,k
 %Output:solutionx
 function x = jacobi(a,b,k)
 n=length(b); %findn
 d=diag(a); %extractdiagonalofa
 r=a-diag(d); %ristheremainder
 x=zeros(n,1); %initializevectorx
 for j=1:k %loopforJacobiiteration
 x=(b-r*x)./d;
 end