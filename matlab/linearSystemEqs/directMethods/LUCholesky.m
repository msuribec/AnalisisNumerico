function [xi,L,u] = LUCholesky(A,b)

clc
text=fopen('tabla_Cholesky.txt','w');
fprintf(text,'FACTORIZACION LU CHOLESKY\n\n\n');

[n,m]=size(A);
C=[A,b];
% la matriz C, representa la forma de la matriz aumentada [Ab]

if n==m
    for k=1:n
        disp(['ETAPA: ' num2str(k)]);
        %La instrucción iterativa for permite repetir estamentos a un
        %numero específico de veces
        suma1=0;
        for p=1:k-1
            suma1=suma1+L(k,p)*u(p,k);
        end
        L(k,k)=sqrt(A(k,k)-suma1);
        disp(['L(' num2str(k) ',' num2str(k) ')' num2str(L(k,k))]);
        u(k,k)=L(k,k); %principio del metodo
        disp(['U(' num2str(k) ',' num2str(k) ')' num2str(u(k,k))]);
        for i=k+1:n
            suma2=0;
            for q=1:k-1
                suma2=suma2+L(i,q)*u(q,k);
            end
            L(i,k)=(A(i,k)-suma2)/L(k,k); %obtencion de la matriz L
            disp(['L(' num2str(i) ',' num2str(k) ')' num2str(L(i,k))]);
        end
        for j=k+1:n
            suma3=0;
            for r=1:k-1
                suma3=suma3+L(k,r)*u(r,j);
            end
            u(k,j)=(A(k,j)-suma3)/L(k,k); %obtencion de la matriz U
            disp(['U(' num2str(k) ',' num2str(j) ')' num2str(u(k,j))]);
        end
    end
    producto=det(L)*det(u); %calculo del determinante
    if producto~=0
        for i=1:n
            suma=0;
            for p=1:i-1
                suma=suma+L(i,p)*z(p);
            end
            z(i)=(b(i)-suma)/L(i,i); %obtencion del vector Z
        end
        for i=n:-1:1
            suma=0;
            for p=i+1:n
                suma = suma+u(i,p)*x(p);
            end
            x(i)=(z(i)-suma)/u(i,i); % solcion, calculos de las variables
        end
    else
        fprintf(text,'\nEl determinante es igual a cero, por lo tanto el sistema tiene infinita o ninguna solucion\n');
    end
end


fprintf(text,'\n Matriz Ab:\n' );
for i=1:n
    for j=1:m+1
        if j<m+1
            fprintf(text,'%1.4f\t',C(i,j));
        end
        if j==m+1
            fprintf(text,'%1.4f \n',C(i,j));
        end
    end
end

fprintf(text,'\n Matriz L:\n' );
for i=1:n
    for j=1:m
        if j<m
            fprintf(text,'%1.4f\t',L(i,j));
        end
        if j==m
            fprintf(text,'%1.4f \n',L(i,j));
        end
    end
end

fprintf(text,'\n Matriz U:\n' );
for i=1:n
    for j=1:m
        if j<m
            fprintf(text,'%1.4f\t',u(i,j));
        end
        if j==m
            fprintf(text,'%1.4f \n',u(i,j));
        end
    end
end


fprintf(text,'\n El vector Z:\n');
for j=1:m
    fprintf(text,'%1.4f \n',z(1,j));
end

da


fprintf(text,'\n\nLa solucion de X1 hasta Xn es:\n');

for i=1:n
    xi=x(1,i);
    fprintf(text,'\nX%g=  %g',i,xi);
end
end