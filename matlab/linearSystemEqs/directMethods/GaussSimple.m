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
% text=fopen(filename,'at');

function [] = GaussSimple(A,b)
filename='GaussSimple.txt';
text=fopen(filename,'at');
                                                   
[n,m]=size(A); 
C=[A b];  
fprintf(text,'The augmented matrix \n');
writematrix(C,filename,'WriteMode','append','Delimiter','tab');
X=[];

if n==m 
     for k=1:(n-1)
         [C,sol,t]=cambios(C,k,n);
         fprintf(text,t);
         if sol==0
             break;
         end
         fprintf(text,'\nPHASE %g \n\n',k);
         writematrix(C,filename,'WriteMode','append','Delimiter','tab');
         fprintf(text,'\nThe multipliers of this phase are:\n');
         
         for i=(k+1):n
             M(i,k)= C(i,k)/C(k,k);
             fprintf(text,'\nm(%g,%g)= %g',i,k,M(i,k));
             for j=k:(n+1)
                C(i,j)= C(i,j)- M(i,k)*C(k,j);
             end
         end
         fprintf(text,'\n\n Applying multipliers we have:\n\n');
         writematrix(C,filename,'WriteMode','append','Delimiter','tab');
     end
     [X]= regSus(C,n);
else
    fprintf(text,'\nERROR: The matrix is nor square\n'); 
end
if sol~=0
    fprintf(text,'\n The final matrix is:\n\n');
    writematrix(C,filename,'WriteMode','append','Delimiter','tab');
    fprintf(text,'\n\nThe final solution is (in order):\n\n');
   writematrix(X(1,1:n)',filename,'WriteMode','append','Delimiter','tab');
end

