# Liste comprehensive
# Exemple

#generarea unei liste care contine o progresie aritmetica 45...-34 cu ratia -5
L=[i for i in range(45,-34,-5)]
#selectarea elemetelor divizibile cu k din lista
k=3
LP=[x for x in L if x%k==0]
#calculu maximului din lista si determinarea pozitiei de aparitie
maxim=max(L)
index=L.index(maxim)
print(L)
print(LP)
print(maxim,"   ",index)


#generarea unei multimi de tipul -1, -1+eps, -1+2*eps, ..., 1
eps=0.1
L1=[-1+i*eps for i in range(10000) if -1+i*eps<=1]
print(L1)


import numpy
# alternativ, folosind numpy
L2=numpy.arange(-1,1+0.1,0.1)
print(L2)