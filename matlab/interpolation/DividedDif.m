
function [] = DividedDif(n,X,Y,r)
fprintf('The divided differences table is:\n');
fprintf('i\t');
for i=1:n+1
    fprintf('\t X%g\t\t',i);
end
fprintf('\n');
DD=zeros(n+1);
DD(:,1)=Y;
for k=2:n+1
    for J=k:n+1
        DD(J,k)=[DD(J,k-1)-DD(J-1,k-1)]/[X(J)-X(J-k+1)];
    end
end
for i=1:n+1
    fprintf('%g      ',i);
    for j=1:i
        if i<10
            if (DD(i,j))<0
            fprintf(' %.4f     ',DD(i,j));         
            else
            fprintf('  %.4f     ',DD(i,j));
            end
        else
            if j==1
                if (DD(i,j))<0
                fprintf('%.4f     ',DD(i,j));         
                else
                fprintf(' %.4f     ',DD(i,j));
                end 
            else
                if (DD(i,j))<0
                fprintf(' %.4f     ',DD(i,j));         
                else
                fprintf('  %.4f     ',DD(i,j));
                end
            end
        end        
    end
    fprintf('\n');
end
syms x;
fprintf('The polynomial is es: ');
formatSpec = '%.15f';
polnew=DD(1,1);
P=1;
polin=num2str(DD(1,1),formatSpec);
textoacum='';
for i=1:n
    P=P*(x-X(i));
    texto=['(x-' num2str(X(i)) ')'];
    co=num2str(DD(i+1,i+1));
    textoacum=[textoacum texto];
    polin=[polin co textoacum];
    polnew=polnew+P*DD(i+1,i+1);
end

fprintf(polin);
x=r;
vi=eval(polnew);
fprintf('\nel valor interpolado es %f\n',vi);
end