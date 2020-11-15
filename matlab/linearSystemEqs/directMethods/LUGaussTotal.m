function [L, U, P, Q,X,Z] = LUGaussTotal(A,b)
[n, n] = size(A);
p = 1:n; 
q = 1:n;
for k = 1:n-1
    %find max of submatrix
    submatrix=abs(A(k:n,k:n));
    [largest]=max(submatrix,[],'all');
    [r,c]=find(submatrix==largest);
    r=r+k-1;
    c=c+k-1;
    % row and column swap
    A( [k, r], : ) = A( [r, k], : );% swap kth row and 
    A( :, [k, c] ) = A( :, [c, k] );
    p( [k, r] ) = p( [r, k] ); q( [k, c] ) = q( [c, k] );
    if A(k,k) == 0
      break
    end
    A(k+1:n,k) = A(k+1:n,k)/A(k,k);
    i = k+1:n;
    A(i,i) = A(i,i) - A(i,k) * A(k,i);
end
L = tril(A,-1) + eye(n);
U = triu(A);

P = eye(n);
P = P(p,:);
Q = eye(n);
Q = Q(:,q);
Pb=P*b;
[Z]=progSus(L,Pb);
X=[];
[X]= regSus([U Z],n);
X=X*Q;
end