function [x,Error] = Jacobi(A,b,x0,tol,iter)
clc
text=fopen('Tabla_Jacobi','w');

t=('Iter        X1          X2         X3           X4          Error');
fprintf(text,'%s',t);
n=size(A,1);%TamaÃ±o de A
cond(A);%verificar si esta bien condicionada la matriz

D=diag(diag(A)); %el programa encuentra la diagonal de A
L=D-tril(A); %el programa encuentra la matriz trinagular inferiror	
U=D-triu(A); %el programa encuentra la matriz triangular superior

disp(D)
disp(L)
disp(U)
Tj=D^-1*(L+U); %Transitional matrix

disp(Tj);
rho=max(abs(eig(Tj))); %spectral radius

if rho>1	%si el re>1 el metodo no converge
    fprintf('radio espectral mayor que 1');
    fprintf('el metodo no converge');
end 

C=D^-1*b; %encunetre el valor de la constante Cj
i=0;
error=tol+1;
disp(C)

while error>tol && i<iter %mientras error>tol y i<iter ejecute la formula iterativa	
    xi=Tj*x0+C; %formula iterativa
    i=i+1;	%incrmente el valor del contador
    error=norm(xi-x0,Inf); 
    x0=xi; %se tiene un nuevo valor de x para continuar hastra que encuentre solucion
    p(i)=error;	%se crea un nuevo vector p, para cargar los valores del error
    fprintf(text,'\n %g\t\t',i);
    for j=1:n
        fprintf(text,'%f\t',(xi(j)));
    end
    fprintf(text,'\t %e \n',error); 
    disp([xi' error]);
end

fprintf(text,'\n \nRadio Espectral = %f',rho);%muestre el radio espectral

end