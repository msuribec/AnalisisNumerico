function LUCrout (A,b)
%Para ingresar los datos en la funci�n debe de realizarlo de la siguiente
%manera: inicie con el nombre de la funci�n que desea utilizar, seguido de
%los siguientes parametros entre parentesis y separados entre ellos con
%coma, matriz A entre corchetes separando los elementos de la fila con
%espacios y con un punto y coma(;) al terminar cada fila excepto en la
%�ltima, vector B entre corchetes y cada elemento separado con punto y coma(;).
%LUCrout([Matriz A],[Vector B])
%ejm LUCrout([2 -1 0 3;1 0.5 3 8;0 13 -2 11;14 5 -2 3],[1;1;1;1])
filename='Tabla_Croutt.txt';
text=fopen(filename,'w');
fprintf(text,'                     FACTORIZACION LU CROUTT\n\n\n');
%fprintf me permite ingresar comentarios de manera textual que pueden
%orientar al usuario en el uso del programa
[n,m]=size(A);
C=[A,b];
% la matriz C, representa la forma de la matriz aumentada [Ab]



if n==m 
    for k=1:n
      texto=['ETAPA: ' num2str(k)];      
      fprintf(text,texto);
      fprintf(text,'\n');
      %La instrucci�n iterativa for permite repetir estamentos a un
      %numero espec�fico de veces  
        u(k,k)=1; %princio del metodo
        suma=0;
        for p=1:k-1
            suma=suma+L(k,p)*u(p,k);
        end
        L(k,k)=(A(k,k)-suma);
        texto=['L(' num2str(k) ',' num2str(k) ')' num2str(L(k,k))];
        fprintf(text,texto);
        fprintf(text,'\n');
        for i=k+1:n
            suma=0;
            for r=1:k-1
                suma=suma+L(i,r)*u(r,k);
            end
            L(i,k)=(A(i,k)-suma); %obtencion de la matriz L
            fprintf(text,'\n Matriz L:\n' );
            
            writematrix(L,filename,'WriteMode','append','Delimiter','tab');
            texto=['L(' num2str(i) ',' num2str(k) ')' num2str(L(i,k))];
            fprintf(text,texto);
            fprintf(text,'\n');
        end
        for j=k+1:n
            suma=0;
            for s=1:k-1
                suma=suma+L(k,s)*u(s,j);
            end
            u(k,j)=(A(k,j)-suma)/L(k,k); %obtencion de la matriz U
            texto=['U(' num2str(k) ',' num2str(j) ')' num2str(u(k,j))];
            fprintf(text,texto);
            fprintf(text,'\n');
        end
    end
    memoriau=1; %calculo del determinante de u
    memoriaL=1; %calculo del determinante inicial de L
    for i=1:n
        memoriaL=memoriaL*L(i,i); 
    end
    producto=memoriaL*memoriau;  %calculo del determinante total
    
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
            for p=(i+1):n
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
    fprintf(text,'%1.4f\n',L(i,j));
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
    
fprintf(text,'\n\nLa solucion de X1 hasta Xn es:\n');  
%a continuacion de utiliza una instruccion for, para mostrar el usuario, 
%los resultados de una manera mas ordenada
for i=1:n
    xi=x(1,i);
    fprintf(text,'\nX%g=  %g',i,xi);
end

end