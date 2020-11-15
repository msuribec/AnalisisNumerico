
function [x0,er,i] = multRoots(f,x0,n,tol)

syms x;
inicial=x0;
sp = '%.10f';
spa='%.10f %.10f %.10f %.10f %.10f %.10f\n';
disp (['i ' 'x ' 'fx ' ' f´(x)' ' f´´(x)' ' error abs ']);
fx=double(subs(f,x0));
df=matlabFunction( diff(f(x)));
d2f=matlabFunction( diff(df(x)));
dfx=double(subs(df,x0));
d2fx=double(subs(d2f,x0));
i=0;
den=dfx^2-(fx*d2fx);
er=tol+1;
while den~=0 && fx~=0 && er>tol && i<n
    if i==0
        er=nan;
    end
    resp=[i double(x0) double(fx) double(dfx) double(d2fx) double(er)];
    fprintf( spa, resp.' ) ;
    x1=x0-((fx*dfx)/den);
    fx=double(subs(f,x1));
    dfx=double(subs(df,x1));
    d2fx=double(subs(d2f,x1));
    den=dfx^2-(fx*d2fx);
    er=abs(x1-x0);
    x0=x1;
    i=i+1;
end
resp=[i double(x0) double(fx) double(dfx) double(d2fx) double(er)];
fprintf( spa, resp.' ) ;
if fx==0
    disp([num2str(x0,sp) ' is root.']);
elseif er<tol
    disp([num2str(x1,sp) ' is an approximation to a root, with tolerance ' num2str(tol,sp)]);
elseif den==0
    disp('The method could not continue since a division by zero ocurred when computing xn');
else
    disp(['The method failed with ' num2str(i) ' iterations.']);
end
ejex = linspace(inicial, x0+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end