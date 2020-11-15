
format long

fprintf('Enter the matrix A, example between brackets and separating rows with ;\n');
A=input('Ingresar matriz A = ');

fprintf('Enter the matrix A, example between brackets and separating rows with ;\n');
b=input('Ingresar el vector b = '); 

filename=input('Enter the path of the file where results will be saved  \n');
%%
gaussTot(A,b,filename)

function gaussTot(A,b,filename)
text=fopen(filename,'at');
[n,m]=size(A);
C=[A,b];
fprintf(text,'The augmented matrix \n');
writematrix(C,filename,'WriteMode','append','Delimiter','tab');
X=[];
if n==m 
    marca=1:n;
    for k=1:(n-1)
        fprintf(text,'\n PHASE %g=\n',k);
        aux=abs(C(k:n,k:n));
        [mayor]=max(aux,[],'all');
        [r,c]=find(aux==mayor);
        filaaux=r+k-1;
        columnaux=c+k-1;
        filam=filaaux(1);
        columnam=columnaux(1);
        if mayor ==0
            fprintf(text,'There are infinite solutions \n');
            break;
        else
            if filam ~= k
                C=swapRows(C,filam,k);
            end
            if columnam ~= k
                C=swapCols(C,columnam,k);
                marca=swapCols(marca,columnam,k);
            end
            
          
            
        end         
        writematrix(C,filename,'WriteMode','append','Delimiter','tab');
        fprintf(text,'\n The multipliers are: \n ');
        for i=(k+1):n
            M(i,k)=C(i,k)/C(k,k);
            fprintf(text,'\n m(%g,%g)= %g ',i,k,M(i,k));
            C(i,k:(n+1))= C(i,k:(n+1)) - M(i,k)*C(k,k:(n+1));
        end
         
        fprintf(text,'\n The matrix at this phase is :\n');
        writematrix(C,filename,'WriteMode','append','Delimiter','tab');
    end
    fprintf(text,'\n The final matrix is:\n');
    X= regSus(C,n);
    
    for i=1:n
        for j=1:n
            if marca(j)==i
                k=j;
            end
        end
        aux=X(k);
        X(k)=X(i);
        X(i)=aux;
        marca=swapCols(marca,i,k);
    end
else
    fprintf(text,'\n The matrix is not square\n');
end
writematrix(C,filename,'WriteMode','append','Delimiter','tab'); 
fprintf(text,'\n La solucion de los Xi es:\n');
writematrix(X(1,1:n)',filename,'WriteMode','append','Delimiter','tab');

end