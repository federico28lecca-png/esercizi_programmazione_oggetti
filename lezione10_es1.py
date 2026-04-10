"""Creare un decoratore che si comporta esattamente come il decoratore classmethod e verificarne il funzionamento"""

def fakeclassmethod(funzione):
    def wrapper(*varargs, **kwargs):
        print("stai usando il wrapper")
        classtype = type(varargs[0])
        funzione(classtype, *varargs[1:], **kwargs)
    return wrapper

class CProva:
    val = 1000

    def __init__(self):
        self.val = 9999

    @fakeclassmethod
    def stampa_val(cls):
        print(cls)  #
        print(cls.val)

prova = CProva()

prova.stampa_val() #stampa 1000 --> dimostrazione che sta usando l'attr di classe
print(prova.val)    #stampa 9999 --> dimostrazione che sta usando l'attr di istanza