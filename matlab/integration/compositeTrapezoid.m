function answer = compositeTrapezoid(f,a,b,n)
 h=(b-a)/n;
 sum=0;
for k=1:1:n-1
  x(k)=a+k*h;
  y(k)=f(x(k));
  sum=sum+y(k);
end
% Formula:  (h/2)*[(y0+yn)+2*(y2+y3+..+yn-1)]
answer=h/2*(f(a)+f(b)+2*sum);
fprintf('\n The value of integration is %.15f\n',answer);  % exmple The value of integration is 0.410451
end