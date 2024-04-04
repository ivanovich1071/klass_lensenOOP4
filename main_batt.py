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
        return "стреляет стрелой из лука"


class Spear(Weapon):
    def attack(self):
        return "колет копьем"


class Ax(Weapon):
    def attack(self):
        return "рубит топором"


class Fighter:
    def __init__(self, strength):
        self.strength = strength
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self, monster):
        damage = 1 if self.weapon else 0
        if self.weapon:
            damage *= 2 if len(self.weapon) > 1 else 1
            monster.reduce_life(damage)
            self.strength += damage
            return f"Боец атакует с {', '.join(self.weapon)}. Монстр теряет {damage} жизнь. Сила бойца теперь {self.strength}."
        else:
            return "Боец наносит удары."


class Monster:
    def __init__(self, lives):
        self.lives = lives

    def reduce_life(self, damage):
        self.lives -= damage

    def is_alive(self):
        return self.lives > 0


# Ввод данных от пользователя
monster_lives = int(input("Введите количество жизней Монстра: "))
fighter_strength = int(input("Введите силу бойца: "))

# Создание бойца и монстра
fighter = Fighter(fighter_strength)
monster = Monster(monster_lives)

while monster.is_alive():
    weapon_choice = input("Выберите оружие (Меч, Лук, Копье, Топор): ").split()
    fighter.change_weapon(weapon_choice)
    print(fighter.attack(monster))
    if not monster.is_alive():
        print("Монстр побежден!")
        break
    continue_battle = input("Продолжить бой? (да/нет): ")
    if continue_battle.lower() != "да":
        break

print(f"Сила бойца: {fighter.strength}, количество жизней Монстра: {monster.lives}")