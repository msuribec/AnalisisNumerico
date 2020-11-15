% example 
%Lagrange([1,2,3,4],[1,4,9,16],2.1);
function [pn,y] = Lagrange(xpts,ypts,val)
format long;
yi=ypts';
n=length(xpts);
x=sym('x');
for j=1:n
    s=1;
    for i=1:j-1
        s=s*(x-xpts(i));
    end
    s2=1;
    for i=j+1:n
        s2=s2*(x-xpts(i));
    end
    s3=1;
    for i=1:j-1
        s3=s3*(xpts(j)-xpts(i));
    end
    s4=1;
    for i=j+1:n
        s4=s4*(xpts(j)-xpts(i));
    end
    L(j)=(s*s2)/(s3*s4); 
    fprintf('L%g :%s\n',(j-1),(L(j)));
  
end
pn=0;
for j=1:n
    pn=pn+L(j)*yi(j);
end
pn = simplify(pn);
fprintf('\n The polynomial is: %s',pn);
x=val;
y=eval(pn);
fprintf('\nThe approximation of a f(%.15f) is: %.15f',val,y);
end