class CEsame:
    def __init__(self, nome_esame, voto_primo_parziale, voto_secondo_parziale):
        self.nome_esame = nome_esame
        self.voto_primo_parziale = voto_primo_parziale
        self.voto_secondo_parziale = voto_secondo_parziale

    def calcola_media(self):
        return (self.voto_primo_parziale + self.voto_secondo_parziale) / 2

    def stampa_voto_finale(self):
        print(f"Voto finale: {self.calcola_media()}")


class CLista_voti:
    def __init__(self):
        self._lista_esami = []

    def aggiungi_esame(self):
        nome_esame = input("Nome esame: ")
        voto_primo_parziale = float(input("Voto primo parziale: "))
        voto_secondo_parziale = float(input("Voto secondo parziale: "))
        nuovo_esame = CEsame(nome_esame, voto_primo_parziale, voto_secondo_parziale)
        self._lista_esami += [nuovo_esame]

    def mostra_nome_esame_piu_alto(self):
        max = self._lista_esami[0].calcola_media()
        for i in range(1, len(self._lista_esami)):
            if self._lista_esami[i].calcola_media() > max:
                max = self._lista_esami[i].calcola_media()
        print("Esami con voto più alto: ")
        for i in range(len(self._lista_esami)):
            if self._lista_esami[i].calcola_media() == max:
                print(self._lista_esami[i].nome_esame)


n_esami = int(input("Quanti esami vuoi inserire: "))
lista_voti = CLista_voti()
for i in range(n_esami):
    print(f"Dati esame {i+1}.")
    lista_voti.aggiungi_esame()

lista_voti.mostra_nome_esame_piu_alto()