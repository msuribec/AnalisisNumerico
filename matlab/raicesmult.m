format long

f=input('Ingrese la función f(x), por ejemplo: @(x) exp(-x)-x  :');
x0=input('Ingrese el valor inicial x0:  ');
n=input ('Ingrese el número de iteraciones máximo:  ');
tol=input ('Ingrese la tolerancia:  ');

[x,e,i] = mroots(f,x0,n,tol);
function [x0,er,i] = mroots(f,x0,n,tol)

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
    disp([num2str(x0,sp) ' es raíz.']);
elseif er<tol
    disp([num2str(x1,sp) ' es aproximación a una raíz con tolerancia ' num2str(tol,sp)]);
elseif den==0
    disp('No se pudo desarrollar el método puesto que al calcular el xn, el denominador es 0');
else
    disp(['El método fracasó con ' num2str(i) ' iteraciones.']);
end
ejex = linspace(inicial, x0+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end