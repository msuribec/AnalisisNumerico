function [R,V] = Vandermonde(X,Y)

text=fopen('Proceso_Vandermonde.txt','w');
[m,n]=size(X);

fprintf(text,'\t\n\nLa matriz de Vandermonde es:\n');


for i=1:n
    for j=1:n
        V(i,j)= X(i)^(n-j);
        fprintf(text,'%g\t',V(i,j));
    end 
            fprintf(text,'\n');

end

b = Y';
R= V\b;
fprintf(text,'\nLa solucion del sistema es:\n');
for i=1:n
    fprintf(text,'a%d = %.8g\n',(n-i),R(i));
end
clear
clc
end