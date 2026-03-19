def min_max_lista(lista):
    minimo=lista
    massimo=lista
    minimo=min(lista)
    massimo=max(lista)
    return minimo,massimo

l=[5,3,2,4,6,7,89,0,-32]
minimo,massimo=min_max_lista(l)
print("Max: ",massimo,"\nMin: ",minimo)