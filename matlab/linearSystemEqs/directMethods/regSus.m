function [X]= regSus(C,n)
X=[];
for i=n:-1:1
    suma=0;
    for p=(i+1):n
        suma = suma + C(i,p)*X(p);
    end
    X(i)=(C(i,n+1)-suma)/C(i,i);        %formula de la susticion regresiva y solucion de las variables
end
end

