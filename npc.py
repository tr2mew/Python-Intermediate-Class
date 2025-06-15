class NPC:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
    
    def describe(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Mana: {self.mana}")
        print("-"*20)
        
    def damage(self, dmg):
        if self.mana <= 0:
            print("not enough mana")
            return
        self.hp -= dmg
        self.mana -= dmg
        print(f"{self.name} HP got -{dmg}")

n1 = NPC("Alice", 100, 200)
n2 = NPC("Mina", 200, 100)

n1.describe()
n1.damage(10)
n1.damage(10)
n1.describe()
n2.describe()