def caratteri_duplicati(stringa):
    for i in range(0,len(stringa)):
        for j in range(i+1,len(stringa)):
            if stringa[i]==stringa[j]:
                return True
    return False

stringa=input("Inserisci stringa: ")
print(caratteri_duplicati(stringa))
