class Esame:
    def __init__(self, nome_esame, voto_primo_parziale, voto_secondo_parziale):
        self.nome_esame = nome_esame
        self.voto_primo_parziale = voto_primo_parziale
        self.voto_secondo_parziale = voto_secondo_parziale

    def _calcola_media(self):
        return (self.voto_primo_parziale + self.voto_secondo_parziale) // 2

    def stampa_voto_finale(self):
        print(f"Il voto finale è: {self._calcola_media()}")

analisi = Esame("Analisi", 32, 18)
analisi.stampa_voto_finale()