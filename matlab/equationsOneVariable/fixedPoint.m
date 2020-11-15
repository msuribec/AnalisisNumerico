
function [x0,er,i] = fixedPoint(f,g,x0,n,tol)
inicial=x0;
sp = '%.10f';
spa='%.10f %.10f %.10f %.10f\n';
disp (['i ' 'x ' 'fx ' 'error abs ']);
fx=double(subs(f,x0));
i=0;
er=tol+1;
while fx~=0 && er>tol && i<n
    if i==0
        er=nan;
    end
    resp=[i double(x0) double(fx) double(er)];
    fprintf( spa, resp.' ) ;
    xn=double(subs(g,x0));
    fx=double(subs(f,xn));
    er=abs(xn-x0);
    x0=xn;
    i=i+1;
end
resp=[i double(x0) double(fx) double(er)];
fprintf( spa, resp.' ) ;
if fx==0
    disp([num2str(x0,sp) ' is a root.']);
elseif er<tol
    disp([num2str(x0,sp) ' is an approximation to a root with tolerance ' num2str(tol,sp)]);
else
    disp(['The method failed with ' num2str(i) ' iterations.']);
end
ejex = linspace(inicial, x0+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end