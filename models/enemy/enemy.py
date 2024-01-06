
class Enemy:

    def __init__(self, name: str, hp, strength: int, agility, intelligence, luck, money):
        self.name = name
        self.hp = hp
        self.agility = agility
        self.strength = strength
        self.intelligence = intelligence
        self.luck = luck
        self.money = money

        self.melee_attack_damage: int = self.strength * 2
        self.ranged_attack_damage: int = self.agility * 2
        self.magic_attack_damage: int = self.intelligence * 2

        self.chance_to_block: float = (self.strength + (self.agility / 2)) / 100
        self.chance_to_dodge: float = (self.agility + self.luck) / 100

    def hit(self, player):
        player.hp -= self.melee_attack_damage
        return player.hp


ENEMIES: [Enemy] = [Enemy('Wolf', 50, 2, 2, 1, 1, 10),
                    Enemy('Bear', 100, 4, 1, 1, 1, 50),
                    Enemy('Fox', 30, 1, 4, 2, 2, 15),
                    Enemy('Squirrel', 10, 1, 6, 1, 1, 5)]
