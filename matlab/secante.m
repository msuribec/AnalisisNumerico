format long

f=input('Ingrese la función f(x), por ejemplo: @(x) exp(-x)-x  :');
x0=input('Ingrese el valor inicial x0:  ');
x1=input('Ingrese el valor inicial x1:  ');
n=input ('Ingrese el número de iteraciones máximo:  ');
tol=input ('Ingrese la tolerancia:  ');
secant(f,x0,x1,n,tol);
function [] = secant(f,x0,x1,n,tol)

syms x;
inicial=x0;
sp = '%.10f';
spa='%.10f %.10f %.10f %.10f\n';
disp (['i ' 'x ' 'fx ' 'errorabs ']);
fx0=double(subs(f,x0));
if fx0==0
    disp([num2str(x0,sp) ' es raíz.']);
else
    fx1=double(subs(f,x1));
    df=matlabFunction( diff(f(x)));
    dfx=double(subs(df,x0));
    i=0;
    er=tol+1;
    den=fx1-fx0;
    resp=[0 double(x0) double(fx0) nan];
    fprintf( spa, resp.' ) ;
    while er>tol && fx1~=0 && den~=0 && i<n
        if i==0
            er=nan;
        end
        resp=[i+1 double(x1) double(fx1) double(er)];
        fprintf( spa, resp.' ) ;
        x2=x1-fx1*(x1-x0)/den;
        er=abs(x2-x1);
        x0=x1;
        fx0=fx1;
        x1=x2;
        fx1=double(subs(f,x1));
        den=fx1-fx0;
        i=i+1;
    end
    resp=[i+1 double(x1) double(fx1) double(er)];
    fprintf( spa, resp.' ) ;
    if fx1==0
        disp([num2str(x1,sp) ' es raíz.']);
    elseif er<tol
        disp([num2str(x1,sp) ' es aproximación a una raíz con tolerancia ' num2str(tol,sp)]);

    elseif den==0
         disp('hay una posible raíz múltiple');
    else
        disp(['El método fracasó con ' num2str(i) ' iteraciones.']);
    end
end

ejex = linspace(inicial, x1+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end
