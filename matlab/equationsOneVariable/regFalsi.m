
[x,e,i] = rfalsi(f,a,b,n,tol);
function [xm,er,i] = rfalsi(f,a,b,n,tol)

sp = '%f';
fa = double(subs(f,a)); 
fb = double(subs(f,b));
if fa * fb > 0.0
    error ('The function has equal sign at a and at b, there is no root between a and b . ')
end
if fa==0
    disp(['The root is ' num2str(a)]);
else 
    disp (['i ' 'xi ' 'xm ' 'xf ' 'f(xi) ' 'f(xm) ' 'f(xf) eabs' ])
    i=1;
    xm =a-((fa*(b-a))/(fb-fa));
    fxm = double(subs(f,xm));
    er=tol+1;
    while i<n && er>tol && fxm~=0
        format long;
            resp=[i double(a) double(fa) double(xm) double(fxm) double(b) double(fb) double(er)];
            fprintf( '%f %f %f %f %f %f %f %f\n', resp.' ) ;
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
        xm = a-((fa*(b-a))/(fb-fa));
        fxm = double(subs(f,xm));
        er=abs(xm-xaux);
        i=i+1;
    end
    resp=[i double(a) double(fa) double(xm) double(fxm) double(b) double(fb) double(er)];
    fprintf( '%f %f %f %f %f %f %f %f\n', resp.' ) ;
    if fxm==0
        disp(['la raíz es ' num2str(xm)]);
    elseif er <tol
        disp([num2str(xm,sp) ' is an approximation to a root, with tolerance ' num2str(tol,sp)]);
    else
        disp(['The method failed with ' num2str(i) ' iterations.']);
    end
end

ejex = linspace(a,b);
figure
plot(ejex, double(subs(f,ejex)))
grid
end