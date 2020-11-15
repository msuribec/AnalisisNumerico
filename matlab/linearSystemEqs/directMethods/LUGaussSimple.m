
clc  
clear  
format long

fprintf('Enter the matrix A, example between brackets and separating rows with ;\n');
A=input('Ingresar matriz A = ');

fprintf('Enter the matrix A, example between brackets and separating rows with ;\n');
b=input('Ingresar el vector b = '); 
filename=input('Enter the path of the file where results will be saved  \n');
text=fopen(filename,'at');
                                   

[n,m]=size(A);
a=[A,b];
L=eye(n);% Identity matrix n x n 
Z=zeros(n,1);% vector of n zeros (vertical)
X=zeros(n,1);% vector of n zeros (vertical)

fprintf(text,'The augmented matrix \n');
writematrix(a,filename,'WriteMode','append','Delimiter','tab');

if n==m    
    for k=1:n-1 
        a=[A b];
        [a,sol,t]=cambios(a,k,n);
        A=a(:,1:n);
        b=a(:,n+1);
         if sol==0
             break;
         end
        writematrix(t,filename,'WriteMode','append','Delimiter','tab');
        fprintf(text,'\nThe multipliers of this phase are:\n');

        for i=(k+1):n
            M(i,k)=A(i,k)/A(k,k); 
            fprintf(text,'\nm(%g,%g)= %g \n',i,k,M(i,k));
            for j=k:n
                A(i,j)= A(i,j) - M(i,k)*A(k,j); 
                
                if i>j
                    L(i,j)= M(i,k);                    
                end
                if i==j
                    L(i,j)= 1;
                end
                if i<j
                    L(i,j)= 0;
                end
            end
        end
        fprintf(text,'\nThe U matrix at this phase is :\n' );
        writematrix(A,filename,'WriteMode','append','Delimiter','tab');
    end
else
    fprintf(text,'\nERROR: The matrix is nor square\n'); 
end
if sol~=0
    U=A;
    Z=progSus(L,b);
    X=[];
    X= regSus([U Z],n);
    fprintf(text,'\n The Z vector obtained from progressive substitution (LZ=b) is:\n');
    writematrix(Z,filename,'WriteMode','append','Delimiter','tab');
    fprintf(text,'\n The X vector obtained from regressive substitution (UX=Z) is:\n');
    writematrix(X,filename,'WriteMode','append','Delimiter','tab');
    
 
end
