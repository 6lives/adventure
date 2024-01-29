
class Enemy:

    def __init__(self, name, hp, strength, agility, intelligence, luck, money, exp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.agility = agility
        self.strength = strength
        self.intelligence = intelligence
        self.luck = luck
        self.money = money
        self.exp = exp

        self.melee_attack_damage: int = self.strength * 2
        self.ranged_attack_damage: int = self.agility * 2
        self.magic_attack_damage: int = self.intelligence * 2

        self.chance_to_block: float = (self.strength + (self.agility / 2)) / 100
        self.chance_to_dodge: float = (self.agility + self.luck) / 100

    def hit(self, player):
        if player.hp - self.melee_attack_damage < 0:
            player.hp = 0
            return player.hp
        player.hp -= self.melee_attack_damage
        return player.hp

    def reward(self, player):
        player.money += self.money
        player.exp += self.exp


ENEMIES: [Enemy] = [Enemy('Волк', 10, 2, 2, 1, 1, 10, 100),
                    Enemy('Медведь', 10, 2, 1, 1, 1, 50, 100),
                    Enemy('Лиса', 10, 1, 4, 2, 2, 15, 100),
                    Enemy('Белка', 9, 1, 6, 1, 1, 5, 100)]
