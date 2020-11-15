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

function [] = LUGaussParcial(A,b)
filename='LUGaussPartial.txt'; 
text=fopen(filename,'at');
[n, m] = size(A); 
L=eye(m); 
P=eye(m); 
U=A;
 if m==n
    for k=1:n-1
        
        largest=max(abs(U(k:n,k)));
        for j=k:n
            if(abs(U(j,k))==largest)
                i=j;
                break;
            end
        end
        
        if largest ==0 % if the max value is cero then all possible values are 0 
             fprintf(text,'\nThere is an infinite number of solutions\n');
             break 
         end
        
        if i ~= k% swap rows
             U([k,i],k:n)=U([i,k],k:n);
             L([k,i],1:k-1)=L([i,k],1:k-1);
             P([k,i],:)=P([i,k],:);
         end
               
        fprintf(text,'\n The matrix after row swapping is :\n\n');
        writematrix(U,filename,'WriteMode','append','Delimiter','tab');
        
        fprintf(text,'\n The P matrix after row swapping is :\n\n');
        writematrix(P,filename,'WriteMode','append','Delimiter','tab');
        
        fprintf(text,'\n The multipliers are:\n\n');
        
        for j=k+1:n
            L(j,k)=U(j,k)/U(k,k);
            fprintf(text,'\n m(%g,%g)= %g',j,k,L(j,k));
            U(j,k:n)=U(j,k:n)-L(j,k)*U(k,k:n);
        end
        fprintf(text,'\nThe U matrix at this phase is :\n' );
        writematrix(U,filename,'WriteMode','append','Delimiter','tab');
        
    end
 else
     fprintf(text,'Matrix is not square: \n');
 end
 
fprintf(text,'\nThe L matrix is :\n' );
writematrix(L,filename,'WriteMode','append','Delimiter','tab');
fprintf(text,'\nThe U matrix is :\n' );
writematrix(U,filename,'WriteMode','append','Delimiter','tab');

Pb=P*b;

Z=progSus(L,Pb);
X=[];
X= regSus([U Z],n);

fprintf(text,'\n The Z vector obtained from progressive substitution (LZ=b) is:\n');
writematrix(Z,filename,'WriteMode','append','Delimiter','tab');
fprintf(text,'\n The X vector obtained from regressive substitution (UX=Z) is:\n');
writematrix(X,filename,'WriteMode','append','Delimiter','tab');
end
