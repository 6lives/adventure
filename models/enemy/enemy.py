
class Enemy:

    def __init__(self, name: str, hp: int, strength: int, agility: int, intelligence: int, luck: int, money: int, exp: int, level: int):
        self.level = level
        self.name = name
        self.max_hp = hp + (level * 10)
        self.hp = self.max_hp
        self.agility = agility
        self.strength = strength
        self.intelligence = intelligence
        self.luck = luck
        self.money_reward = money * level
        self.exp_reward = exp * level

        self.melee_attack_damage = lambda: self.strength * self.level
        self.ranged_attack_damage = lambda: self.agility * self.level
        self.magic_attack_damage = lambda: self.intelligence * self.level

        self.chance_to_dodge: float = (self.agility + self.luck) / 100

    def hit(self, player):
        if player.hp - self.melee_attack_damage() < 0:
            player.hp = 0
            return
        player.hp -= self.melee_attack_damage()

    def reward(self, player):
        player.money += self.money_reward
        coefficient = 1
        if player.level > self.level + 5:
            coefficient = 0.15
        player.exp += self.exp_reward * coefficient
