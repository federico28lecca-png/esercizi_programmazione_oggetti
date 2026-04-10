"""
Create le classi per permettere ad un’azienda multinazionale di gestire gli
stipendi dei suoi programmatori.
Tutti i programmatori dell’azienda hanno uno stipendio pari a 1500 euro.
A dicembre però, gli viene data una premialità differente a seconda della loro
categoria; lo stipendio viene aumentato di:
- 500 euro, per i programmatori junior
- 1000 euro, per i programmatori senior
Definire prima il diagramma delle classi
"""

class CProgrammatore:
    stipendio_base = 1500
    premio_dicembre = 0

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def calcola_stipendio(self, mese):
        if mese == "dicembre":
            return self.stipendio_base + self.premio_dicembre
        return self.stipendio_base

class CJunior(CProgrammatore):
    premio_dicembre = 500

class CSenior(CProgrammatore):
    premio_dicembre = 1000

class CAzienda:
    def __init__(self):
        self._lista_programmatori = []

    def add_programmatore(self):
        tipo = input("Digita 'junior' / 'senior'")
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        if tipo == "junior":
            self._lista_programmatori.append(CJunior(nome, cognome))
        else:
            self._lista_programmatori.append(CSenior(nome, cognome))

    def stampa_stipendi(self, mese):
        for programmatore in self._lista_programmatori:
            print(f"{programmatore.nome} {programmatore.cognome} - {programmatore.calcola_stipendio(mese)}")

azienda1 = CAzienda()
azienda1.add_programmatore()
azienda1.add_programmatore()
azienda1.add_programmatore()
azienda1.stampa_stipendi("dicembre")