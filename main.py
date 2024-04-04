from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "рубит мечом"


class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} {self.weapon.attack()}"
        else:
            return f"{self.name} боец бьет"


class Monster:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return f"{self.name} побежден"
fighter = Fighter("Боец")
sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
print(fighter.attack())

fighter.change_weapon(bow)
print(fighter.attack())

monster = Monster("Монстр")
print(monster.attack())