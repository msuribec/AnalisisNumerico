format long

f=input('Ingrese la función f(x), por ejemplo: @(x) exp(-x)-x  :');
x0=input('Ingrese el valor inicial x0:  ');
n=input ('Ingrese el número de iteraciones máximo:  ');
tol=input ('Ingrese la tolerancia:  ');

[x,e,i] = newtonraphson(f,x0,n,tol);
function [x0,er,i] = newtonraphson(f,x0,n,tol)
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
    disp([num2str(x0,sp) ' es raíz.']);
elseif er<tol
    disp([num2str(x1,sp) ' es aproximación a una raíz con tolerancia ' num2str(tol,sp)]);
elseif dfx==0
    disp([num2str(x1,sp) 'es una posible raíz multiple']);
else
    disp(['El método fracasó con ' num2str(i) ' iteraciones.']);
end
ejex = linspace(inicial, x0+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end