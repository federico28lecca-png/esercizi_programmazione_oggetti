class CEnemy:
    def __init__(self, energy, damage, defense):
        self.energy = energy
        self.damage = damage
        self.defense = defense

class CReplicants(CEnemy):
    def __init__(self, energy, damage, defense, mechanical_systems, mechanical_systems_damage):
        self.mechanical_systems = mechanical_systems
        self.mechanical_systems_damage = mechanical_systems_damage
        super().__init__(energy, damage, defense)

class CyberHackers(CEnemy):
    def __init__(self, energy, damage, defense, ram, hacking_damage):
        self.ram = ram
        self.hacking_damage = hacking_damage
        super().__init__(energy, damage, defense)

