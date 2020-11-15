%  Example bisect(@(x) x^3 -7.51*x^2+18.4239*x-14.8331,3,4,1000,1e-7)
function [xm,er,i] = bisection(f,a,b,n,tol)
sp = '%.15f';
spa='%.1f %.15f %.15f %.15f %.15f %.15f %.15f %.15f\n';
fa =double(subs(f,a)); 
fb =double(subs(f,b));

if fa==0
    disp(['The root is ' num2str(a)]);
elseif fa * fb > 0.0
    error ('The function has equal sign at a and b, and therefore no root exists between a and b ')
else 
    disp (['i ' 'xi ' 'xm ' 'xf ' 'f(xi) ' 'f(xm) ' 'f(xf) eabs' ])
    i=1;
    xm = (a+b)/2;
    fxm = double(subs(f,xm));
    er=b-a;
    while i<n && er>tol && fxm~=0
        format long;
            resp=[i double(a) double(xm) double(b) double(fa) double(fxm) double(fb) double(er)];
            fprintf( spa,resp.' ) ;
        % find the middle and evaluate there
        if fxm == 0.0 % solved the equation exactly
            a = xm ;
            b = xm ;
            break % jumps out of the for loop
        end
        % decide which half to keep , so that the signs at the ends differ
        if fa * fxm < 0
            b = xm ;
            fb = fxm;
        else
            a = xm ;
            fa =fxm;
        end
        xaux=xm;
        xm = ( a + b )/2;
        fxm = double(subs(f,xm));
        er=abs(b-a);
        i=i+1;
    end
    resp=[i double(a) double(xm) double(b) double(fa) double(fxm) double(fb) double(er)];
    fprintf( spa, resp.' ) ;
    if fxm==0
        disp([num2str(xm,sp) ' is a root.']);
        
    elseif er <tol
        disp([num2str(xm,sp) ' is an approximation to a root, with tolerance ' num2str(tol,sp)]);
    else
        disp(['The method failed with' num2str(i) ' iterations.']);
    end
end

ejex = linspace(a,b);
figure
plot(ejex, double(subs(f,ejex)))
grid
end