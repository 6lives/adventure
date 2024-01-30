from .enemy import Enemy


class GoblinTeen(Enemy):
    def __init__(self, level: int):
        super().__init__('гоблин подросток', 20, 2, 2, 1, 1, 20, 40, level)


class GoblinTrapper(Enemy):
    def __init__(self, level: int):
        super().__init__('гоблин следопыт', 20, 2, 2, 1, 1, 20, 40, level)


class GoblinWarrior(Enemy):
    def __init__(self, level: int):
        super().__init__('гоблин воин', 20, 2, 2, 1, 1, 20, 40, level)


class GoblinShaman(Enemy):
    def __init__(self, level: int):
        super().__init__('гоблин шаман', 20, 2, 2, 1, 1, 20, 40, level)


class GoblinWarlord(Enemy):
    def __init__(self):
        super().__init__('предводитель гоблинов (БОСС)', 100, 5, 5, 5, 5, 100500, 10000, 25)