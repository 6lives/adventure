from models.enemy.enemy import Enemy


class Wolf(Enemy):
    def __init__(self, level: int):
        super().__init__('волк', 20, 1, 1, 1, 1, 10, 20, level)


class Bear(Enemy):
    def __init__(self, level: int):
        super().__init__('медведь', 20, 2, 1, 1, 1, 15, 30, level)


class Squirrel(Enemy):
    def __init__(self, level: int):
        super().__init__('белка', 5, 1, 1, 1, 2, 1, 5, level)


class Badger(Enemy):
    def __init__(self, level: int):
        super().__init__('барсук', 10, 1, 1, 0, 1, 15, 15, level)


class Fox(Enemy):
    def __init__(self, level: int):
        super().__init__('лиса', 10, 1, 3, 1, 2, 15, 15, level)
