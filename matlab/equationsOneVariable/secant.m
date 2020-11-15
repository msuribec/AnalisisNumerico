
function [] = secant(f,x0,x1,n,tol)

syms x;
inicial=x0;
sp = '%.10f';
spa='%.10f %.10f %.10f %.10f\n';
disp (['i ' 'x ' 'fx ' 'errorabs ']);
fx0=double(subs(f,x0));
if fx0==0
    disp([num2str(x0,sp) ' is root.']);
else
    fx1=double(subs(f,x1));
    df=matlabFunction( diff(f(x)));
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
        disp([num2str(x1,sp) ' is root.']);
    elseif er<tol
        disp([num2str(x1,sp) 'is an approximation with tolerance ' num2str(tol,sp)]);

    elseif den==0
         disp('There might be a multiple root');
    else
        disp(['The method failed with ' num2str(i) ' iterations.']);
    end
end

ejex = linspace(inicial, x1+100*tol);
figure
plot(ejex, double(subs(f,ejex)))
grid
end
