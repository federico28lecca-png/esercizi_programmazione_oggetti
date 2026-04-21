from abc import ABC, abstractmethod
from math import pi

class CForma_Geometrica(ABC):
    @abstractmethod
    def calcola_area(self):
        pass

    @abstractmethod
    def calcola_perimetro(self):
        pass

    @abstractmethod
    def stampa_dati(self):
        pass

class CCerchio(CForma_Geometrica):
    def __init__(self, raggio):
        self.raggio = raggio

    def calcola_area(self):
        return pi * self.raggio ** 2

    def calcola_perimetro(self):
        return 2 * pi * self.raggio

    def stampa_dati(self):
        print(f"Area: {self.calcola_area():.2f} [m^2]")
        print(f"Perimetro: {self.calcola_perimetro():.2f} [m]ò652 ")

class CRettangolo(CForma_Geometrica):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def calcola_area(self):
        return self.base * self.altezza

    def calcola_perimetro(self):
        return 2 * self.base + 2 * self.altezza

    def stampa_dati(self):
        print(f"Area: {self.calcola_area():.2f} [m^2]")
        print(f"Perimetro: {self.calcola_perimetro():.2f} [m]")

print("Cerchio")
cerchio = CCerchio(4);
cerchio.stampa_dati();
print("\n---\n")
print("Rettangolo")
rettangolo = CRettangolo(4,2)
rettangolo.stampa_dati()





