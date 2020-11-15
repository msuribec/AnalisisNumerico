
function [] = incrementalSearch(f,x0,delta,n)
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
            disp([num2str(x0,sp) ' is root.']);
        else
            disp([num2str(x1,sp) ' is root.']);
        end
    elseif fx0*fx1<0
        resp=['There is a root between' num2str(x0,sp) ' and ' num2str(x1,sp)];
        disp(resp);
    else
        disp(['The method failed with ' num2str(i,sp) ' iterations.']);
    end
    ejex = linspace(inicial, x1+100*delta);
    figure
    plot(ejex, double(subs(f,ejex)))
    grid
end

end
    
    
    

