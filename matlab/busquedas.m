
f=input('Ingrese la función, por ejemplo: @(x) x^3 -7.51*x^2+18.4239*x-14.8331  :');
x0=input('Ingrese el x0:  ');
delta=input('Ingrese el delta deseado:  ');
n=input ('Ingrese el número de iteraciones máximo:  ');
busqincr(f,x0,delta,n);
function [] = busqincr(f,x0,delta,n)
sp = '%.10f';
spa='%.10f %.10f %.10f %.10f %.10f %.10f\n';
inicial=x0;
fx0=double(subs(f,x0));
if fx0==0.0
    disp([num2str(x0) ' es raíz.']);
else
    x1=x0+delta;
    fx1=double(subs(f,x1));
    i=1;
    disp(['i ' 'x0 ' ' x1' ' fx0' ' fx1' ' fx0*fx1' ]);
    while fx0*fx1~=0 && fx0*fx1>0 && i<n
        resp=[i double(x0) double(x1) double(fx0) double(fx1) double(fx0*fx1)];
        fprintf(spa, resp.' ) ;
        x0=x1;
        fx0=fx1;
        x1=x0+delta;
        fx1=double(subs(f,x1));
        i=i+1;
    end
    resp=[i double(x0) double(x1) double(fx0) double(fx1) double(fx0*fx1)];
    fprintf(spa, resp.' );
    if fx0*fx1==0
        if fx0==0
            disp([num2str(x0,sp) ' es raíz.']);
        else
            disp([num2str(x1,sp) ' es raíz.']);
        end
    elseif fx0*fx1<0
        resp=['Hay una raíz entre ' num2str(x0,sp) ' y ' num2str(x1,sp)];
        disp(resp);
    else
        disp(['El método fracasó con ' num2str(i,sp) ' iteraciones.']);
    end
    ejex = linspace(inicial, x1+100*delta);
    figure
    plot(ejex, double(subs(f,ejex)))
    grid
end

end
    
    
    

