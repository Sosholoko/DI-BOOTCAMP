class Character():
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        self.other = other

    def get_info(self):
        print(f"{self.name}s'life is now {self.life}\n{self.name}s'attack is now {self.attack}")

    def get_infoo(self, other):
        print(f"{other.name}s'life is now {other.life}\n{other.name}s'attack is now {other.attack}")


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def medidate(self):
        self.life += 10
        self.attack -= 2
        print(f"You made {self.name} medidate")
        self.get_info()

    def animal_help(self):
        self.attack += 5
        self.get_info()

    def fight(self, other):
        other.life = other.life - (0.75*druid.life - 0.75*druid.attack)
        print(f"You made {self.name} attacks {other.name}")
        print(f"{other.name}'s life is now {other.life}")
        
        # print(other.life)
        # print(0.75*druid.life - 0.75*druid.attack)




class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def brawl(self, other):
        other.attack -= 2
        self.attack -= 0.5
        print(f"You made {self.name} brawl on {other.name}")
        self.get_info()
        other.get_info()

    def train(self):
        self.life += 2
        self.attack += 2
        print(f"You made {self.name} trained")
        self.get_info()

    def roar(self, other):
        other.attack -= 3
        print(f'You made {self.name} roar on {other.name}')
        other.get_info()



class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def curse(self, other):
        other.attack -= 2
        print(f'You made {self.name} cursing on {other.name}')
        other.get_info()

    def summon(self):
        self.attack += 3
        print(f'You made {self.name} summon')
        self.get_info()

    def cast_spell(self, other):
        force = self.life/self.attack
        print(force)
        other.life = other.life - force
        print(f"You made {self.name} cast a spell on {other.name}")
        print(f"{other.name}'s life is now {other.life}")
        




druid = Druid("Merlin")
druid2 = Druid("Elias")
warrior = Warrior("Wario")
warrior2 = Warrior("Legolas")
mage = Mage("Gandalf")
mage2 = Mage("Saruman")

# druid.fight(druid2)
# druid.fight(druid2)
# print(druid2.life)

# warrior.brawl(warrior2)
# warrior.roar(warrior2)

druid.fight(druid2)