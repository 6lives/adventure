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
        self.exp: float = 0
        self.money = 0
        self.melee_attack_damage: int = self.strength * 2
        self.ranged_attack_damage: int = self.agility * 2
        self.magic_attack_damage: int = self.intelligence * 2

        self.chance_to_block: float = (self.strength + (self.agility / 2)) / 100
        self.chance_to_dodge: float = (self.agility + self.luck) / 100

        self.current_location = Forest

    def print_characteristics(self):
        return (f"Player info:\n"
                f"level = {self.level}\n"
                f"money = {self.money}\n"
                f"Hp = {self.hp}\n"
                f"Max hp = {self.max_hp}\n"
                f"Strength = {self.strength}\n"
                f"Agility = {self.agility}\n"
                f"Intelligence = {self.intelligence}\n"
                f"Luck = {self.luck}\n")

    def hit(self, enemy):
        enemy.hp -= self.melee_attack_damage
        return enemy.hp

    def level_up(self):
        self.level += 1
        self.strength += 1
        self.agility += 1
        self.max_hp += 20