"""
Crea una classe chiamata formattatore che data una delle seguenti strutture
dati di python: lista e dizionario ne stampa i valori in modo user-friendly.
Data una lista, es [1,2,3] dovrà stampare:
Gli elementi della lista sono:
1
2
3
Dato un dizionario, es: {“a”:1, “b”:2} dovrà stampare:
Gli elementi del dizionario sono:
a=1
b=2
"""

from functools import singledispatchmethod

class CFormattatatore:
    @singledispatchmethod
    def formatta(self, dato):
        print("Tipo non supportato")

    @formatta.register
    def _(self, dato: list):
        print("Gli elementi della lista sono:")
        for idx, value in enumerate(dato):
            print(idx, value)

    @formatta.register
    def _(self, dato: dict):
        print("Gli elementi del dizionario sono:")
        for key, value in dato.items():
            print(f"{key}={value}")



formattatore = CFormattatatore()
print("--- Caso default ---")
formattatore.formatta(3)
print("\n--- Caso lista ---")
formattatore.formatta([1,2,3])
print("\n--- Caso dizionario ---")
formattatore.formatta({"a":1, "b":2})