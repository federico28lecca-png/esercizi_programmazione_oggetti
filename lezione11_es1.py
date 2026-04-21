class CStringa:
    def __init__(self, stringa_nuova):
        self._stringa = stringa_nuova
        self._lunghezza_stringa = self._calcola_lunghezza(stringa_nuova)

    def _calcola_lunghezza(self, stringa):
        return len(stringa)

    @property
    def stringa(self):
        return self._stringa

    @stringa.setter
    def stringa(self, stringa_nuova):
        self._stringa = stringa_nuova
        self._lunghezza_stringa = self._calcola_lunghezza(stringa_nuova)

    @property
    def lunghezza_stringa(self):
        return self._lunghezza_stringa

    def stampa_dati(self):
        print(self._stringa)
        print(self._lunghezza_stringa)


stringa1 = CStringa("Ciaggggo")
stringa1.stampa_dati()

stringa1.stringa = "Ciao a tuttiiiiiiiiiiiiiiiiiiiiii"
stringa1.stampa_dati()
