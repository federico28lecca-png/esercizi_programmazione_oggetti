"""
Creare una classe per memorizzare i dati di uno studente delle superiori.
Questa classe deve avere un attributo di sola lettura chiamato numero_serie
che deve essere positivo e un attributo chiamato temperatura che deve essere
tra -100 e 100.
"""

class Studente:
    def __init__(self, numero_serie, temperatura):
        self._numero_serie = self._controlla_numero_serie(numero_serie)
        self.temperatura = temperatura

    def _controlla_numero_serie(self, numero_serie):
        while numero_serie < 0:
            numero_serie = int(input("Errore input. Inserisci numero serie > 0"))
        return numero_serie

    # numero_serie sola lettura
    @property
    def numero_serie(self):
        return self._numero_serie

    # temperatura lettura e scrittura
    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value):
        while value < -100 or value > 100:
            value = float(input("Inserisci temperatura compresa fra -100 e 100: "))
        self._temperatura = value

    def stampa_dati(self):
        print(f"Numero_serie: {self._numero_serie} - Temperatura: {self._temperatura}")

stud = Studente(3,3)
stud.stampa_dati()