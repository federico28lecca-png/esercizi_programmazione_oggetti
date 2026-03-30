class CEsame:
    def __init__(self, nome, voto_primo_parziale, voto_secondo_parziale):
        self.nome = nome
        self.voto_primo_parziale = voto_primo_parziale
        self.voto_secondo_parziale = voto_secondo_parziale

    def _calcola_media(self):
        return (self.voto_primo_parziale + self.voto_secondo_parziale)//2

    def mostra_media_voto(self):
        print(f"Il voto finale è: {self._calcola_media()}")

class CRegistroEsami:
    def __init__(self):
        self._lista_esami = []

    def add_esame(self):
        nome = input("Nome: ")
        voto_primo_parziale = float(input("Voto primo parziale: "))
        voto_secondo_parziale = float(input("Voto secondo parziale: "))
        new_esame = CEsame(nome, voto_primo_parziale, voto_secondo_parziale)
        self._lista_esami.append(new_esame)

    def print_voti(self):
        print("Elenco voti:")
        for esame in self._lista_esami:
            print(f"{esame.nome} - {esame._calcola_media()}")


registro = CRegistroEsami()
registro.add_esame()
registro.add_esame()
registro.print_voti()

