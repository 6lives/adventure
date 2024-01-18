from aiogram.types import Message
from location import Forest


class Player:

    def __init__(self, message: Message):
        self.id = message.from_user.id
        self.level = 1
        self.hp: int = 100
        self.max_hp = 100
        self.strength: int = 1
        self.agility: int = 1
        self.intelligence: int = 1
        self.luck: int = 1

        self.exp: int = 0
        self.exp_to_lvl_up: int = 100

        self.money = 0
        self.melee_attack_damage: int = self.strength * 2
        self.ranged_attack_damage: int = self.agility * 2
        self.magic_attack_damage: int = self.intelligence * 2

        self.chance_to_block: float = (self.strength + (self.agility / 2)) / 100
        self.chance_to_dodge: float = (self.agility + self.luck) / 100

        self.current_location = Forest
        self.inAction: bool = False

    def print_characteristics(self):
        return (f"Информация игрока:\n"
                f"Уровень = {self.level}\n"
                f"Опыт = {self.exp}/{self.exp_to_lvl_up}\n"
                f"Золото = {self.money}\n"
                f"Хп = {self.hp}/{self.max_hp}\n"
                f"Сила = {self.strength}\n"
                f"Ловкость = {self.agility}\n"
                f"Интеллект = {self.intelligence}\n"
                f"Удача = {self.luck}\n")

    def hit(self, enemy):
        enemy.hp -= self.melee_attack_damage
        return enemy.hp

    def check_level_up(self):
        if self.exp >= self.exp_to_lvl_up:
            self.level += 1
            self.strength += 1
            self.agility += 1
            self.max_hp += 20
            self.exp_to_lvl_up += 100 * self.level
            self.exp = 0
            return True
        return False

    def dead(self):
        self.exp *= 0.8
        self.exp = round(self.exp)

    def heal(self, amount):
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount


