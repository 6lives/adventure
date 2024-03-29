from aiogram.types import Message
from location.forest import Forest
import random


class Player:

    def __init__(self, message: Message):
        self.id: int = message.from_user.id
        self.fullName: str = message.from_user.full_name
        self.level: int = 1
        self.hp: int = 100
        self.max_hp = lambda: 100 + (self.strength + self.level) * 5

        self.strength: int = 1
        self.agility: int = 1
        self.intelligence: int = 1
        self.luck: int = 1

        self.exp: int = 0
        self.exp_to_lvl_up: int = 100
        self.available_attr_pts: int = 0

        self.money = 0
        self.melee_attack_damage = lambda: (self.strength * 1.5)
        self.ranged_attack_damage: int = self.agility * 2
        self.magic_attack_damage: int = self.intelligence * 2

        self.chance_to_evade = lambda: 0.5 if ((self.agility * 1.5) + (self.luck * 0.5)) / 100 > 0.5 else ((self.agility * 1.5) + (self.luck * 0.5)) / 100

        self.current_location = Forest
        self.inAction: bool = False
        self.isDead: bool = False

    def print_characteristics(self) -> str:
        return (f"Информация игрока:\n"
                f"Уровень = {self.level}\n"
                f"Опыт = {self.exp}/{self.exp_to_lvl_up}\n"
                f"Золото = {self.money}\n"
                f"Хп = {self.hp}/{self.max_hp()}\n"
                f"Сила = {self.strength}\n"
                f"Ловкость = {self.agility}\n"
                f"Интеллект = {self.intelligence}\n"
                f"Удача = {self.luck}\n"
                f"Доступных очков характеристик = {self.available_attr_pts}")

    def hit(self, enemy) -> None:
        if enemy.hp - self.melee_attack_damage() < 0:
            enemy.hp = 0
            return
        enemy.hp -= self.melee_attack_damage()

    def check_evade(self) -> bool:
        return 0 < round(random.uniform(0.01, 1), 2) <= self.chance_to_evade()

    def check_level_up(self) -> bool:
        if self.exp >= self.exp_to_lvl_up:
            while self.exp >= self.exp_to_lvl_up:
                exceed_exp = self.exp - self.exp_to_lvl_up
                self.level += 1
                self.available_attr_pts += 1
                self.exp_to_lvl_up = 100 * self.level
                self.exp = exceed_exp
            return True
        return False

    def dead(self) -> None:
        self.isDead = True
        self.exp *= 0.8
        self.exp = round(self.exp)

    def heal(self, amount) -> None:
        if self.hp + amount > self.max_hp():
            self.hp = self.max_hp()
        else:
            self.hp += amount


