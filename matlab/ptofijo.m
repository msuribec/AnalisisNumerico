format long
f=input('Ingrese la función f(x), por ejemplo: @(x) x(1)^3 -7.51*x(1)^2+18.4239*x(1)-14.8331  :');
g=input('Ingrese la función, g(x) por ejemplo: @(x) x(1)^3 -7.51*x(1)^2+18.4239*x(1)-14.8331  :');
x0=input('Ingrese el valor inicial x0:  ');
n=input ('Ingrese el número de iteraciones máximo:  ');
tol=input ('Ingrese la tolerancia:  ');
[x,e,i] = fixedp(f,g,x0,n,tol);
function [x0,er,i] = fixedp(f,g,x0,n,tol)
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
    disp([num2str(x0,sp) ' es raíz.']);
elseif er<tol
    disp([num2str(x0,sp) ' es aproximación a una raíz con tolerancia ' num2str(tol,sp)]);
else
    disp(['El método fracasó con ' num2str(i) ' iteraciones.']);
end
ejex = linspace(inicial, x0+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end