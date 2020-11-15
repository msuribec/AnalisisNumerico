function C=swapRows(C,filam,k)
temp=C(k,:);
C(k,:)=C(filam,:);
C(filam,:)=temp;
end