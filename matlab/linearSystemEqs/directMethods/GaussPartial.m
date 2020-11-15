% 
% clc  
% clear  
% format long
% 
% fprintf('Enter the matrix A, example between brackets and separating rows with ;\n');
% A=input('Ingresar matriz A = ');
% 
% fprintf('Enter the matrix A, example between brackets and separating rows with ;\n');
% b=input('Ingresar el vector b = '); 
% filename=input('Enter the path of the file where results will be saved  \n');


function [] = GaussPartial(A,b)
filename='GaussPartial.txt';
text=fopen(filename,'at');
         
[n,m]=size(A);
C=[A,b];

fprintf(text,'\n The agumented matrix is = \n');
 writematrix(C,filename,'WriteMode','append','Delimiter','tab');

X=[];
if n==m 
     for k=1:(n-1)
         fprintf(text,'\n PHASE %g=\n\n',k);
         aux=abs(C(k:n,k));
         [mayor,filam]=max(aux);
         filam=filam+k-1;
         if mayor ==0 % if the max value is cero then all possible values are 0 
             fprintf(text,'\nThere is an infinite number of solutions\n');
             break 
         end
         if filam ~= k% swap rows
             C=swapRows(C,filam,k);
         end
         fprintf(text,'\n The matrix after row swapping:\n');
         writematrix(C,filename,'WriteMode','append','Delimiter','tab');
         fprintf(text,'\n The multipliers are:\n');
         
         for i=(k+1):n
             M(i,k)=C(i,k)/C(k,k); 
             fprintf(text,'\n m(%g,%g)= %g',i,k,M(i,k));
             C(i,k:n+1)=C(i,k:(n+1)) - M(i,k)*C(k,k:(n+1));
         end
         fprintf(text,'\n\n The matrix for this phase is :\n\n');    
         writematrix(C,filename,'WriteMode','append','Delimiter','tab');
    end
    X= regSus(C,n);
else
    fprintf(text,'\nERROR: The matrix is not square\n');
end
fprintf(text,'\n The final matrix is:\n\n');
    writematrix(C,filename,'WriteMode','append','Delimiter','tab');
    fprintf(text,'\n\nThe final solution is (in order):\n\n');
   writematrix(X(1,1:n)',filename,'WriteMode','append','Delimiter','tab');
end 