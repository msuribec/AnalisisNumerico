
function [x0,er,i] = newton(f,x0,n,tol)
syms x;
inicial=x0;
sp = '%.10f';
spa='%.10f %.10f %.10f %.10f %.10f\n';
disp (['i ' 'x ' 'fx ' 'df' 'error abs ']);
fx=double(subs(f,x0));
df=matlabFunction( diff(f(x)));
dfx=double(subs(df,x0));
i=0;
er=tol+1;
while fx~=0 && er>tol && i<n && dfx~=0
    if i==0
        er=nan;
    end
    resp=[i double(x0) double(fx) double(dfx) double(er)];
    fprintf( spa, resp.' ) ;
    x1=x0-(fx/dfx);
    fx=double(subs(f,x1));
    dfx=double(subs(df,x1));
    er=abs(x1-x0);
    x0=x1;
    i=i+1;
end
resp=[i double(x0) double(fx) double(dfx) double(er)];
fprintf( spa, resp.' ) ;
if fx==0
    disp([num2str(x0,sp) ' is root.']);
elseif er<tol
    disp([num2str(x1,sp) ' is an approximation to a root with tolerance ' num2str(tol,sp)]);
elseif dfx==0
    disp([num2str(x1,sp) ' could be a multiple root']);
else
    disp(['The method failed with ' num2str(i) ' iterations.']);
end
ejex = linspace(inicial, x0+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end