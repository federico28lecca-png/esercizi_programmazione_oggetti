def min_max_lista(lista):
    minimo=min(lista)
    massimo=max(lista)
    return minimo,massimo

l=[]
n=int(input("Numero di elementi da inserire: "))
for i in range(n):
    num=(float(input("Numero "+str(i+1)+": ")))
    l+=[num]
minimo,massimo=min_max_lista(l)
print("Max: ",massimo,"\nMin: ",minimo)
