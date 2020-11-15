function [A,sol,text]= cambios(A,k,n)
if k==(n-1) && A(n,n)==0% en la última fila
        sol=0;
        text='There is no solution, Ann is 0 in the last phase';
else
    if A(k,k)~=0
        text='Switching rows was not necessary';
        sol=1;
    else% el akk es 0
        posibles=A(k+1:n,k);%posibles intercambios
        if sum(posibles~=zeros(n-k,1))==0% si todos los posibles son cero
            text='There is no solution, all possible row changes result in a division by zero';
            sol=0;
        else%hacer cambio de filas 
            for i=k+1:n
                if A(i,k)~=0% si no es cero
                    text=['Row ' num2str(i) ' and row ' num2str(k) ' were switched'];
                    temp=A(k,:);
                    A(k,:)=A(i,:);
                    A(i,:)=temp;
                    sol=1;
                    break;
                end
            end
        end
    end
end

end