class CPersona:
    def __init__(self, codice_fiscale):
        self.codice_fiscale = codice_fiscale

class CStudente(CPersona):
    def __init__(self, codice_fiscale, classe_frequentata):
        self.classe_frequentata = classe_frequentata
        super().__init__(codice_fiscale)

    def stampa_dati(self):
        print("classe frequentata ", self.classe_frequentata)


class CInsegnante(CPersona):
    def __init__(self, codice_fiscale, materia_insegnata):
        self.materia_insegnata = materia_insegnata
        super().__init__(codice_fiscale)

    def stampa_dati(self):
        print("materia insegnata ", self.materia_insegnata)


class CAnagrafica():
    def __init__(self):
        self._persone = []

    def _crea_insegnante( self):
        codice_fiscale = input ("inserisci il codice_fiscale ")
        materia_insegnata = input("inserisci il nome della materia ")
        return CInsegnante(codice_fiscale, materia_insegnata)

    def _crea_studente( self):
        codice_fiscale = input("inserisci il codice_fiscale ")
        classe_frequentata = input("inserisci la classe frequentata ")
        return CStudente(codice_fiscale, classe_frequentata)

    def aggiungi_persona(self):
        tipo = input("vuoi inserire un insegnante o uno studente? digita 'insegnante' o 'studente' ")
        if tipo == 'insegnante':
            persona = self._crea_insegnante()
        else:
            if tipo == 'studente':
                persona = self._crea_studente()
            else:
                print("tipo errato")
                return
        self._persone.append(persona)

    def cerca_persona(self):
        codice_fiscale = input("inserisci il codice fiscale della persona che vuoi cercare ")
        for persona in self._persone:
            if persona.codice_fiscale == codice_fiscale:
                persona.stampa_dati()
                return
        print("Persona non trovata")


anagrafica = CAnagrafica()
anagrafica.aggiungi_persona()
anagrafica.aggiungi_persona()
anagrafica.cerca_persona()

print(anagrafica._persone)