function S =simps(f,a,b)
m=(a+b)/2;
fa=f(a);
fb=f(b);
fm=f(m);
h=(m-a);
fprintf('\n with h= %f\n',h);  
S = h/3 *(fa+4*fm+fb);
fprintf('Estimation with simpson 1/3 method = %.15f', S)

end
