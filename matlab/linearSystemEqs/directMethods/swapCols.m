function C=swapCols(C,colm,k)
temp=C(:,k);
C(:,k)=C(:,colm);
C(:,colm)=temp;
end