function[x,Error]=GaussSeidel(A,b,x0,tol,iter)
text=fopen('Tabla_Gauss Seidel','w');
t=('Iter     X1               X2             X3               X4               Error');
fprintf(text,'%s\n',t);
[n,m]=size(A);

L=eye(m);
U=eye(m);
y=zeros(n,1);
x=zeros(n,1);

if n==m
  if det(A)~=0
    D=diag(diag(A));
    L=D-tril(A);
    U=D-triu(A);

   
    T=inv(D-L)*U;
    disp("Matriz transición");
    disp(T);
    

    C=inv(D-L)*b ;
    
    Lambda=eig(T);
    
    Radio=max(abs(eig(T)));

    if Radio>=1
       fprintf(text,'\n Como el radio espectral es mayor a 1, el metodo no asegura convergencia \n');
    
    else
       i=0;
       Error=tol+1;

       while Error>tol && i<iter
          i=i+1;
          x=T*(x0)+C;
       
          Error=norm((x-x0),'Inf');
          fprintf(text,' %g\t',i);
          for j=1:m
             fprintf(text,'  %f  \t',x(j));
          end
          fprintf(text,'\t %e \n',Error);
          disp([x' Error]);
          x0=x;
       end
       if Error<tol
             fprintf(text,'\nPrograma se detiene por ERROR < Tolerancia = %e \n',Error);
             
        else
            fprintf(text,'Programa se detiene por numero de iteraciones maxima= %g \n',iter);
            fprintf(text,'El error es= %g \n',Error);
       end
    end
    
  else
    fprintf(text,'\n El determinante de la matriz A es 0, entonces el sistema no tiene solucion unica\n');
  end
  
else
  fprintf(text,'\n\n Debe ingresar un sistema con igual numero de filas y columnas \n');
end
end