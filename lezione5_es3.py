# Scrivere una funzione chiamata palindroma che retituisce True se una stringa è
# palindroma, False altrimenti

def isPalindroma(stringa):
    for i in range(0,len(stringa)//2):
        if stringa[i] != stringa[-(i+1)]:
            return False
    return True

stringa = input("Inserire stringa: ")
print(isPalindroma(stringa))